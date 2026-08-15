"""Enriquecimiento narrativo con Gemini real (google-genai).

No existe modo simulado: si la clave falla o el modelo no responde, se
propaga `GeminiError` para mostrar el error en la interfaz.
"""

import json
import logging
import os
from typing import TypedDict

from google import genai

# Lista breve de modelos reales verificados con la misma GOOGLE_API_KEY.
# Se prueban en orden para tolerar saturación temporal (503) o
# indisponibilidad puntual (404/429) de un modelo concreto.
MODEL_CANDIDATES: list[str] = [
    "gemini-flash-latest",
    "gemini-flash-lite-latest",
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-pro-latest",
]

MODEL_NAME = MODEL_CANDIDATES[0]


class GeminiError(Exception):
    pass


class NarrativeOutput(TypedDict):
    narrative: str
    considerations: list[str]
    differentials: list[str]
    model: str


def _build_prompt(
    age: int | None,
    sex: str,
    chief_complaint: str,
    summary: str,
    symptoms: list[str],
    red_flags: list[str],
    risk_factors: list[str],
    risk_label: str,
    risk_score: float,
    confidence: float,
) -> str:
    age_text = str(age) if age is not None else "no informada"
    return (
        "Actúas como apoyo documental para un equipo clínico que evalúa sospecha de "
        "amiloidosis. Recibes el resultado de un algoritmo experto local y debes "
        "redactar una narrativa clínica prudente en español, sin emitir diagnóstico "
        "definitivo ni indicar tratamiento farmacológico concreto.\n\n"
        f"Edad: {age_text}\n"
        f"Sexo: {sex or 'no especificado'}\n"
        f"Motivo de consulta: {chief_complaint or 'no informado'}\n"
        f"Resumen clínico: {summary or 'no informado'}\n"
        f"Síntomas estructurados: {', '.join(symptoms) or 'ninguno'}\n"
        f"Señales de alerta: {', '.join(red_flags) or 'ninguna'}\n"
        f"Factores de riesgo: {', '.join(risk_factors) or 'ninguno'}\n"
        f"Resultado local: {risk_label} ({risk_score:.0f}/100), "
        f"confianza {confidence:.0f}%\n\n"
        "Responde EXCLUSIVAMENTE con JSON válido con esta forma:\n"
        '{"narrative": "3 a 5 frases integrando el caso", '
        '"considerations": ["2 a 4 consideraciones clínicas"], '
        '"differentials": ["2 a 4 diagnósticos diferenciales a descartar"]}'
    )


def _short_error(exc: Exception) -> str:
    message = str(exc).replace("\n", " ").strip()
    if len(message) > 180:
        message = f"{message[:177]}..."
    return message or exc.__class__.__name__


def _parse_response(text: str) -> tuple[str, list[str], list[str]]:
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.strip("`")
        if cleaned.lower().startswith("json"):
            cleaned = cleaned[4:]
        cleaned = cleaned.strip()
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start != -1 and end != -1:
        cleaned = cleaned[start : end + 1]
    try:
        data = json.loads(cleaned)
    except json.JSONDecodeError as exc:
        logging.exception(f"Error: {exc}")
        raise GeminiError(
            "Gemini respondió en un formato inesperado y no pudo interpretarse."
        ) from exc
    narrative = str(data.get("narrative", "")).strip()
    considerations = [
        str(item).strip()
        for item in data.get("considerations", [])
        if str(item).strip()
    ]
    differentials = [
        str(item).strip()
        for item in data.get("differentials", [])
        if str(item).strip()
    ]
    if not narrative:
        raise GeminiError("Gemini no devolvió narrativa clínica utilizable.")
    return narrative, considerations, differentials


def generate_clinical_narrative(
    age: int | None,
    sex: str,
    chief_complaint: str,
    summary: str,
    symptoms: list[str],
    red_flags: list[str],
    risk_factors: list[str],
    risk_label: str,
    risk_score: float,
    confidence: float,
) -> NarrativeOutput:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise GeminiError(
            "GOOGLE_API_KEY no está configurada: no se puede enriquecer la narrativa."
        )
    prompt = _build_prompt(
        age,
        sex,
        chief_complaint,
        summary,
        symptoms,
        red_flags,
        risk_factors,
        risk_label,
        risk_score,
        confidence,
    )
    try:
        client = genai.Client(api_key=api_key)
    except Exception as exc:
        logging.exception(f"Error: {exc}")
        raise GeminiError(
            f"No se pudo inicializar el cliente de Gemini: {exc}"
        ) from exc

    failures: list[str] = []
    for model_name in MODEL_CANDIDATES:
        try:
            chat = client.chats.create(model=model_name)
            response = chat.send_message(prompt)
            text = response.text or ""
            narrative, considerations, differentials = _parse_response(text)
        except GeminiError as exc:
            logging.exception(f"Error: {exc}")
            failures.append(f"{model_name}: {exc}")
            continue
        except Exception as exc:
            logging.exception(f"Error: {exc}")
            failures.append(f"{model_name}: {_short_error(exc)}")
            continue
        return {
            "narrative": narrative,
            "considerations": considerations,
            "differentials": differentials,
            "model": model_name,
        }

    detail = " | ".join(failures) if failures else "sin detalle disponible"
    raise GeminiError(
        "Ningún modelo Gemini disponible respondió correctamente "
        f"({len(MODEL_CANDIDATES)} intentos). Detalle: {detail}"
    )
