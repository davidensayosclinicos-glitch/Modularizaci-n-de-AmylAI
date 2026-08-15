import reflex as rx

from app.components.clinical_shell import clinical_shell
from app.components.risk_diagram import risk_diagram


def panel_title(title: str, description: str) -> rx.Component:
    return rx.el.div(
        rx.el.h2(title, class_name="text-lg font-semibold text-[#173f46]"),
        rx.el.p(
            description, class_name="mt-1 text-sm leading-6 text-[#71807a]"
        ),
        class_name="mb-5",
    )


def field(
    label: str, placeholder: str, input_type: str = "text"
) -> rx.Component:
    return rx.el.label(
        rx.el.span(
            label, class_name="mb-2 block text-xs font-semibold text-[#526761]"
        ),
        rx.el.input(
            type=input_type,
            placeholder=placeholder,
            class_name="w-full rounded-xl border border-[#cedbd0] bg-[#fbfaf6] px-3.5 py-2.5 text-sm text-[#173f46] outline-hidden transition-colors placeholder:text-[#a1aaa4] focus:border-[#3d9678] focus:ring-2 focus:ring-[#dcefe0]",
        ),
        class_name="block",
    )


def individual_page() -> rx.Component:
    return clinical_shell(
        "Evaluación individual",
        "01 · Captura clínica",
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    panel_title(
                        "Nuevo expediente",
                        "Registra la información mínima para iniciar una lectura clínica trazable.",
                    ),
                    rx.el.div(
                        field("Referencia del caso", "Ej. AMY-2026-001"),
                        field(
                            "Referencia del paciente", "Identificador interno"
                        ),
                        field("Edad", "Años", "number"),
                        rx.el.label(
                            rx.el.span(
                                "Sexo",
                                class_name="mb-2 block text-xs font-semibold text-[#526761]",
                            ),
                            rx.el.select(
                                rx.el.option("Seleccionar", value=""),
                                rx.el.option("Femenino", value="female"),
                                rx.el.option("Masculino", value="male"),
                                rx.el.option(
                                    "No especificado", value="unspecified"
                                ),
                                class_name="w-full appearance-none rounded-xl border border-[#cedbd0] bg-[#fbfaf6] px-3.5 py-2.5 text-sm text-[#173f46] outline-hidden focus:border-[#3d9678] focus:ring-2 focus:ring-[#dcefe0]",
                            ),
                            class_name="block",
                        ),
                        class_name="grid grid-cols-1 gap-4 sm:grid-cols-2",
                    ),
                    rx.el.div(
                        rx.el.label(
                            rx.el.span(
                                "Motivo de consulta",
                                class_name="mb-2 block text-xs font-semibold text-[#526761]",
                            ),
                            rx.el.textarea(
                                placeholder="Describe el motivo principal de la evaluación...",
                                class_name="min-h-28 w-full resize-y rounded-xl border border-[#cedbd0] bg-[#fbfaf6] px-3.5 py-3 text-sm text-[#173f46] outline-hidden placeholder:text-[#a1aaa4] focus:border-[#3d9678] focus:ring-2 focus:ring-[#dcefe0]",
                            ),
                            class_name="block",
                        ),
                        class_name="mt-5",
                    ),
                    class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5 sm:p-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "shield-check", class_name="h-5 w-5 text-[#2d7a68]"
                        ),
                        rx.el.p(
                            "Captura responsable",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "Usa referencias internas y evita incluir datos identificables que no sean necesarios para el análisis.",
                        class_name="mt-3 text-sm leading-6 text-[#66756f]",
                    ),
                    rx.el.a(
                        "Consultar guía clínica",
                        rx.icon("arrow-up-right", class_name="h-4 w-4"),
                        href="/guide",
                        class_name="mt-4 flex items-center gap-1 text-sm font-semibold text-[#2d7a68]",
                    ),
                    class_name="rounded-2xl border border-[#d8e4d9] bg-[#edf5ed] p-5 sm:p-6",
                ),
                class_name="flex flex-col gap-4",
            ),
            rx.el.div(
                panel_title(
                    "Contexto clínico",
                    "Añade señales y antecedentes para enriquecer la posterior interpretación.",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "heart-pulse", class_name="h-5 w-5 text-[#2d7a68]"
                        ),
                        rx.el.p(
                            "Síntomas y señales",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        rx.el.p(
                            "Pendiente",
                            class_name="ml-auto rounded-full bg-[#f0f2ed] px-2.5 py-1 text-[11px] font-medium text-[#738079]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "La selección estructurada de síntomas aparecerá en el flujo de evaluación.",
                        class_name="mt-3 text-sm leading-6 text-[#71807a]",
                    ),
                    class_name="rounded-xl border border-dashed border-[#cddbcf] bg-[#f6faf5] p-4",
                ),
                rx.el.div(
                    rx.icon(
                        "notebook-tabs", class_name="h-5 w-5 text-[#ad7619]"
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Antecedentes relevantes",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        rx.el.p(
                            "Alergias, medicación e historia clínica organizada.",
                            class_name="mt-1 text-xs leading-5 text-[#71807a]",
                        ),
                    ),
                    class_name="mt-4 flex items-start gap-3 rounded-xl border border-[#eadbb8] bg-[#fbf6e9] p-4",
                ),
                rx.el.div(
                    rx.el.p(
                        "Siguiente paso",
                        class_name="text-xs font-semibold uppercase tracking-[0.14em] text-[#936518]",
                    ),
                    rx.el.p(
                        "Completa los campos esenciales para habilitar el análisis del caso.",
                        class_name="mt-2 text-sm leading-6 text-[#66756f]",
                    ),
                    rx.el.a(
                        "Ir a diagnóstico",
                        rx.icon("chevron-right", class_name="h-4 w-4"),
                        href="/diagnosis",
                        class_name="mt-4 flex w-fit items-center gap-1 rounded-xl bg-[#174e50] px-3.5 py-2.5 text-sm font-semibold text-[#fbfaf6] hover:bg-[#123f41]",
                    ),
                    class_name="mt-5 border-t border-[#e5e9e3] pt-5",
                ),
                class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5 sm:p-6",
            ),
            class_name="grid grid-cols-1 gap-5 xl:grid-cols-[minmax(0,1.35fr)_minmax(20rem,0.65fr)]",
        ),
    )


def diagnosis_page() -> rx.Component:
    return clinical_shell(
        "Revisión diagnóstica",
        "02 · Interpretación clínica",
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.icon(
                                "scan-search",
                                class_name="h-5 w-5 text-[#174e50]",
                            ),
                            rx.el.p(
                                "Resultado del caso",
                                class_name="text-base font-semibold text-[#173f46]",
                            ),
                            class_name="flex items-center gap-2",
                        ),
                        rx.el.span(
                            "Sin caso seleccionado",
                            class_name="rounded-full bg-[#f0f2ed] px-2.5 py-1 text-[11px] font-medium text-[#738079]",
                        ),
                        class_name="flex items-center justify-between gap-4",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Diagnóstico orientativo",
                            class_name="text-xs font-semibold uppercase tracking-[0.14em] text-[#9aa39c]",
                        ),
                        rx.el.p(
                            "Pendiente de evaluación",
                            class_name="mt-2 text-2xl font-semibold text-[#173f46]",
                        ),
                        rx.el.p(
                            "Selecciona o crea un expediente para generar una lectura clínica explicable.",
                            class_name="mt-2 max-w-xl text-sm leading-6 text-[#71807a]",
                        ),
                        class_name="mt-8 border-l-2 border-[#dfe9df] pl-4",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "Confianza", class_name="text-xs text-[#71807a]"
                            ),
                            rx.el.p(
                                "—",
                                class_name="mt-1 text-xl font-semibold text-[#174e50]",
                            ),
                        ),
                        rx.el.div(
                            rx.el.p(
                                "Nivel de riesgo",
                                class_name="text-xs text-[#71807a]",
                            ),
                            rx.el.p(
                                "No calculado",
                                class_name="mt-1 text-xl font-semibold text-[#936518]",
                            ),
                        ),
                        class_name="mt-8 grid grid-cols-2 gap-4 border-t border-[#e5e9e3] pt-5",
                    ),
                    class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5 sm:p-6",
                ),
                rx.el.div(
                    risk_diagram(),
                    class_name="min-w-0",
                ),
                class_name="grid grid-cols-1 gap-5 xl:grid-cols-2",
            ),
            rx.el.div(
                panel_title(
                    "Explicación clínica",
                    "La salida se organizará por hallazgos, señales de alerta y recomendaciones.",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "file-text", class_name="h-4 w-4 text-[#607c84]"
                        ),
                        rx.el.p(
                            "Narrativa clínica",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "Aún no hay una narrativa disponible. Inicia una evaluación individual para construir el contexto del caso.",
                        class_name="mt-3 text-sm leading-6 text-[#71807a]",
                    ),
                    class_name="rounded-xl border border-dashed border-[#cddbcf] bg-[#f6faf5] p-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "circle-alert", class_name="h-4 w-4 text-[#c96b54]"
                        ),
                        rx.el.p(
                            "Señales de alerta",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "Las red flags se mostrarán cuando existan datos clínicos suficientes.",
                        class_name="mt-3 text-sm leading-6 text-[#71807a]",
                    ),
                    class_name="rounded-xl border border-[#ecd5cd] bg-[#fdf3ef] p-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "circle_check", class_name="h-4 w-4 text-[#2d7a68]"
                        ),
                        rx.el.p(
                            "Recomendaciones",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "La revisión mantendrá separadas las sugerencias del diagnóstico y del criterio clínico.",
                        class_name="mt-3 text-sm leading-6 text-[#71807a]",
                    ),
                    class_name="rounded-xl border border-[#d8e4d9] bg-[#edf5ed] p-4",
                ),
                class_name="grid grid-cols-1 gap-4 md:grid-cols-3 rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5 sm:p-6",
            ),
            class_name="flex flex-col gap-5",
        ),
    )


def batches_page() -> rx.Component:
    return clinical_shell(
        "Procesamiento por lotes",
        "03 · Ingesta clínica",
        rx.el.div(
            rx.el.div(
                panel_title(
                    "Entrada de datos",
                    "Prepara archivos clínicos para revisión, normalización y procesamiento controlado.",
                ),
                rx.el.div(
                    rx.icon("upload", class_name="h-7 w-7 text-[#2d7a68]"),
                    rx.el.p(
                        "Suelta aquí un CSV o PDF clínico",
                        class_name="mt-4 text-base font-semibold text-[#36544e]",
                    ),
                    rx.el.p(
                        "La carga por lotes se habilitará en el siguiente paso de integración.",
                        class_name="mt-2 max-w-md text-center text-sm leading-6 text-[#71807a]",
                    ),
                    rx.el.div(
                        rx.el.span(
                            "CSV",
                            class_name="rounded-full bg-[#e6f0e7] px-2.5 py-1 text-[11px] font-semibold text-[#2d7a68]",
                        ),
                        rx.el.span(
                            "PDF",
                            class_name="rounded-full bg-[#f4ead1] px-2.5 py-1 text-[11px] font-semibold text-[#936518]",
                        ),
                        class_name="mt-5 flex gap-2",
                    ),
                    class_name="flex min-h-64 flex-col items-center justify-center rounded-2xl border-2 border-dashed border-[#cddbcf] bg-[#f6faf5] px-5 py-8 text-center",
                ),
                class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5 sm:p-6",
            ),
            rx.el.div(
                panel_title(
                    "Estado de importaciones",
                    "Cada archivo conservará su estado, conteo de registros y trazabilidad.",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "layers-3", class_name="h-5 w-5 text-[#607c84]"
                        ),
                        rx.el.p(
                            "Sin importaciones recientes",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "Cuando se reciba un archivo, aquí podrás revisar registros procesados, errores y casos vinculados.",
                        class_name="mt-3 text-sm leading-6 text-[#71807a]",
                    ),
                    class_name="rounded-xl border border-dashed border-[#cddbcf] bg-[#f6faf5] p-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Recibidos", class_name="text-xs text-[#71807a]"
                        ),
                        rx.el.p(
                            "0",
                            class_name="mt-1 text-2xl font-semibold text-[#174e50]",
                        ),
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Con errores", class_name="text-xs text-[#71807a]"
                        ),
                        rx.el.p(
                            "0",
                            class_name="mt-1 text-2xl font-semibold text-[#9b5545]",
                        ),
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Procesados", class_name="text-xs text-[#71807a]"
                        ),
                        rx.el.p(
                            "0",
                            class_name="mt-1 text-2xl font-semibold text-[#2d7a68]",
                        ),
                    ),
                    class_name="mt-6 grid grid-cols-3 gap-3 border-t border-[#e5e9e3] pt-5",
                ),
                class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5 sm:p-6",
            ),
            rx.el.div(
                rx.el.p(
                    "Flujo recomendado",
                    class_name="text-xs font-semibold uppercase tracking-[0.14em] text-[#936518]",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "1",
                            class_name="flex h-7 w-7 items-center justify-center rounded-full bg-[#174e50] text-xs font-semibold text-[#fbfaf6]",
                        ),
                        rx.el.p(
                            "Recibir",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.div(
                        class_name="hidden h-px flex-1 bg-[#d8e4d9] sm:block"
                    ),
                    rx.el.div(
                        rx.el.span(
                            "2",
                            class_name="flex h-7 w-7 items-center justify-center rounded-full bg-[#dfe9df] text-xs font-semibold text-[#587069]",
                        ),
                        rx.el.p(
                            "Validar",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.div(
                        class_name="hidden h-px flex-1 bg-[#d8e4d9] sm:block"
                    ),
                    rx.el.div(
                        rx.el.span(
                            "3",
                            class_name="flex h-7 w-7 items-center justify-center rounded-full bg-[#dfe9df] text-xs font-semibold text-[#587069]",
                        ),
                        rx.el.p(
                            "Procesar",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    class_name="mt-4 flex flex-col gap-3 sm:flex-row sm:items-center sm:gap-4",
                ),
                class_name="rounded-2xl border border-[#eadbb8] bg-[#fbf6e9] p-5 sm:p-6",
            ),
            class_name="grid grid-cols-1 gap-5 xl:grid-cols-[minmax(0,1.2fr)_minmax(20rem,0.8fr)]",
        ),
    )


def database_page() -> rx.Component:
    return clinical_shell(
        "Base de datos clínica",
        "04 · Trazabilidad",
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "database", class_name="h-5 w-5 text-[#174e50]"
                        ),
                        rx.el.p(
                            "Catálogo de entidades",
                            class_name="text-base font-semibold text-[#173f46]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "La estructura persistente de AmylAI está preparada para conservar el expediente completo.",
                        class_name="mt-2 text-sm leading-6 text-[#71807a]",
                    ),
                    class_name="mb-5",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Entidad",
                            class_name="text-[11px] font-semibold uppercase tracking-[0.13em] text-[#8a9791]",
                        ),
                        rx.el.p(
                            "Propósito",
                            class_name="text-[11px] font-semibold uppercase tracking-[0.13em] text-[#8a9791]",
                        ),
                        class_name="grid grid-cols-[minmax(10rem,0.7fr)_minmax(0,1.3fr)] gap-4 border-b border-[#dce4dc] pb-3",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "ClinicalCase",
                            class_name="font-mono text-sm font-medium text-[#174e50]",
                        ),
                        rx.el.p(
                            "Expediente clínico y contexto principal",
                            class_name="text-sm text-[#66756f]",
                        ),
                        class_name="grid grid-cols-[minmax(10rem,0.7fr)_minmax(0,1.3fr)] gap-4 border-b border-[#e5e9e3] py-4",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "ClinicalMetadata",
                            class_name="font-mono text-sm font-medium text-[#174e50]",
                        ),
                        rx.el.p(
                            "Antecedentes, signos vitales y metadatos",
                            class_name="text-sm text-[#66756f]",
                        ),
                        class_name="grid grid-cols-[minmax(10rem,0.7fr)_minmax(0,1.3fr)] gap-4 border-b border-[#e5e9e3] py-4",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "ClinicalImport",
                            class_name="font-mono text-sm font-medium text-[#174e50]",
                        ),
                        rx.el.p(
                            "Archivos recibidos y estado de importación",
                            class_name="text-sm text-[#66756f]",
                        ),
                        class_name="grid grid-cols-[minmax(10rem,0.7fr)_minmax(0,1.3fr)] gap-4 border-b border-[#e5e9e3] py-4",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "ProcessingExecution",
                            class_name="font-mono text-sm font-medium text-[#174e50]",
                        ),
                        rx.el.p(
                            "Ejecuciones, parámetros y métricas",
                            class_name="text-sm text-[#66756f]",
                        ),
                        class_name="grid grid-cols-[minmax(10rem,0.7fr)_minmax(0,1.3fr)] gap-4 border-b border-[#e5e9e3] py-4",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "DiagnosticResult",
                            class_name="font-mono text-sm font-medium text-[#174e50]",
                        ),
                        rx.el.p(
                            "Resultado, riesgo, narrativa y recomendaciones",
                            class_name="text-sm text-[#66756f]",
                        ),
                        class_name="grid grid-cols-[minmax(10rem,0.7fr)_minmax(0,1.3fr)] gap-4 pt-4",
                    ),
                    class_name="overflow-x-auto",
                ),
                class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5 sm:p-6",
            ),
            rx.el.div(
                rx.el.div(
                    rx.icon(
                        "lock-keyhole", class_name="h-5 w-5 text-[#2d7a68]"
                    ),
                    rx.el.p(
                        "Persistencia preparada",
                        class_name="text-sm font-semibold text-[#36544e]",
                    ),
                    class_name="flex items-center gap-2",
                ),
                rx.el.p(
                    "Los datos clínicos se mantendrán separados de la interfaz y vinculados por relaciones trazables.",
                    class_name="mt-3 text-sm leading-6 text-[#66756f]",
                ),
                rx.el.a(
                    "Ir a importaciones",
                    rx.icon("arrow-up-right", class_name="h-4 w-4"),
                    href="/batches",
                    class_name="mt-4 flex items-center gap-1 text-sm font-semibold text-[#2d7a68]",
                ),
                class_name="rounded-2xl border border-[#d8e4d9] bg-[#edf5ed] p-5 sm:p-6",
            ),
            class_name="grid grid-cols-1 gap-5 xl:grid-cols-[minmax(0,1.4fr)_minmax(18rem,0.6fr)]",
        ),
    )


def guide_page() -> rx.Component:
    return clinical_shell(
        "Guía clínica",
        "05 · Referencia de trabajo",
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "Marco de uso",
                        class_name="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#ad7619]",
                    ),
                    rx.el.h2(
                        "Una lectura estructurada, no una caja negra.",
                        class_name="mt-3 max-w-2xl text-2xl font-semibold leading-tight text-[#173f46] sm:text-3xl",
                    ),
                    rx.el.p(
                        "AmylAI organiza el razonamiento alrededor del contexto, las señales de alerta y la explicación del resultado.",
                        class_name="mt-3 max-w-2xl text-sm leading-6 text-[#66756f] sm:text-base",
                    ),
                    class_name="rounded-2xl border border-[#dce4dc] bg-[#e7efe7] p-6 sm:p-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.span(
                            "01",
                            class_name="text-xs font-semibold text-[#ad7619]",
                        ),
                        rx.el.h3(
                            "Captura el contexto",
                            class_name="mt-3 text-base font-semibold text-[#173f46]",
                        ),
                        rx.el.p(
                            "Registra únicamente la información clínica necesaria para comprender el caso.",
                            class_name="mt-2 text-sm leading-6 text-[#71807a]",
                        ),
                        class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5",
                    ),
                    rx.el.div(
                        rx.el.span(
                            "02",
                            class_name="text-xs font-semibold text-[#ad7619]",
                        ),
                        rx.el.h3(
                            "Revisa las señales",
                            class_name="mt-3 text-base font-semibold text-[#173f46]",
                        ),
                        rx.el.p(
                            "Distingue síntomas, factores de riesgo y red flags antes de interpretar.",
                            class_name="mt-2 text-sm leading-6 text-[#71807a]",
                        ),
                        class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5",
                    ),
                    rx.el.div(
                        rx.el.span(
                            "03",
                            class_name="text-xs font-semibold text-[#ad7619]",
                        ),
                        rx.el.h3(
                            "Explica el resultado",
                            class_name="mt-3 text-base font-semibold text-[#173f46]",
                        ),
                        rx.el.p(
                            "Separa narrativa, confianza y recomendaciones para facilitar la revisión humana.",
                            class_name="mt-2 text-sm leading-6 text-[#71807a]",
                        ),
                        class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5",
                    ),
                    class_name="grid grid-cols-1 gap-4 md:grid-cols-3",
                ),
                class_name="flex flex-col gap-5",
            ),
            rx.el.div(
                panel_title(
                    "Principios de interpretación",
                    "Pautas visibles para mantener una práctica prudente y reproducible.",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon("scale", class_name="h-5 w-5 text-[#2d7a68]"),
                        rx.el.p(
                            "El contexto importa",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        rx.el.p(
                            "Un mismo hallazgo puede tener significados distintos según antecedentes y presentación.",
                            class_name="mt-2 text-sm leading-6 text-[#71807a]",
                        ),
                        class_name="rounded-xl border border-[#d8e4d9] bg-[#edf5ed] p-4",
                    ),
                    rx.el.div(
                        rx.icon(
                            "message-circle-warning",
                            class_name="h-5 w-5 text-[#ad7619]",
                        ),
                        rx.el.p(
                            "La incertidumbre se comunica",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        rx.el.p(
                            "Una ausencia de datos también debe quedar visible para quien revisa el expediente.",
                            class_name="mt-2 text-sm leading-6 text-[#71807a]",
                        ),
                        class_name="rounded-xl border border-[#eadbb8] bg-[#fbf6e9] p-4",
                    ),
                    class_name="grid grid-cols-1 gap-4 md:grid-cols-2",
                ),
                rx.el.a(
                    "Abrir evaluación individual",
                    rx.icon("arrow-up-right", class_name="h-4 w-4"),
                    href="/individual",
                    class_name="mt-5 flex w-fit items-center gap-1 rounded-xl bg-[#174e50] px-3.5 py-2.5 text-sm font-semibold text-[#fbfaf6] hover:bg-[#123f41]",
                ),
                class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5 sm:p-6",
            ),
            class_name="grid grid-cols-1 gap-5 xl:grid-cols-[minmax(0,1.35fr)_minmax(20rem,0.65fr)]",
        ),
    )


def stress_page() -> rx.Component:
    return clinical_shell(
        "Estrés y validación",
        "06 · Calidad clínica",
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        "Módulo de validación",
                        class_name="text-[11px] font-semibold uppercase tracking-[0.16em] text-[#ad7619]",
                    ),
                    rx.el.h2(
                        "Conoce cómo responde el sistema antes de confiar en él.",
                        class_name="mt-3 max-w-2xl text-2xl font-semibold leading-tight text-[#173f46] sm:text-3xl",
                    ),
                    rx.el.p(
                        "Este espacio está preparado para escenarios sintéticos, pruebas de sensibilidad y revisión de rendimiento clínico.",
                        class_name="mt-3 max-w-2xl text-sm leading-6 text-[#66756f] sm:text-base",
                    ),
                    class_name="rounded-2xl border border-[#dce4dc] bg-[#e7efe7] p-6 sm:p-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Escenarios",
                            class_name="text-xs font-semibold uppercase tracking-[0.13em] text-[#8a9791]",
                        ),
                        rx.el.p(
                            "0",
                            class_name="mt-3 text-3xl font-semibold text-[#174e50]",
                        ),
                        rx.el.p(
                            "Pendientes de cargar",
                            class_name="mt-1 text-xs text-[#71807a]",
                        ),
                        class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Corridas",
                            class_name="text-xs font-semibold uppercase tracking-[0.13em] text-[#8a9791]",
                        ),
                        rx.el.p(
                            "—",
                            class_name="mt-3 text-3xl font-semibold text-[#936518]",
                        ),
                        rx.el.p(
                            "Sin validaciones ejecutadas",
                            class_name="mt-1 text-xs text-[#71807a]",
                        ),
                        class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5",
                    ),
                    rx.el.div(
                        rx.el.p(
                            "Estado",
                            class_name="text-xs font-semibold uppercase tracking-[0.13em] text-[#8a9791]",
                        ),
                        rx.el.p(
                            "Listo",
                            class_name="mt-3 text-3xl font-semibold text-[#2d7a68]",
                        ),
                        rx.el.p(
                            "Entorno preparado",
                            class_name="mt-1 text-xs text-[#71807a]",
                        ),
                        class_name="rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5",
                    ),
                    class_name="grid grid-cols-1 gap-4 sm:grid-cols-3",
                ),
                class_name="flex flex-col gap-5",
            ),
            rx.el.div(
                panel_title(
                    "Qué se podrá validar",
                    "Las métricas se incorporarán cuando exista un conjunto de escenarios clínicos.",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "sliders-horizontal",
                            class_name="h-5 w-5 text-[#174e50]",
                        ),
                        rx.el.p(
                            "Sensibilidad a red flags",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "Comprobar que una señal crítica modifique el nivel de riesgo de forma visible y consistente.",
                        class_name="mt-3 text-sm leading-6 text-[#71807a]",
                    ),
                    class_name="rounded-xl border border-[#dce4dc] bg-[#fbfaf6] p-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "chart-column", class_name="h-5 w-5 text-[#2d7a68]"
                        ),
                        rx.el.p(
                            "Calibración y confianza",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "Comparar confianza declarada con resultados de referencia y revisar zonas de incertidumbre.",
                        class_name="mt-3 text-sm leading-6 text-[#71807a]",
                    ),
                    class_name="rounded-xl border border-[#d8e4d9] bg-[#edf5ed] p-4",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.icon(
                            "repeat-2", class_name="h-5 w-5 text-[#ad7619]"
                        ),
                        rx.el.p(
                            "Reproducibilidad",
                            class_name="text-sm font-semibold text-[#36544e]",
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    rx.el.p(
                        "Registrar versión, parámetros y métricas para poder explicar cada corrida clínica.",
                        class_name="mt-3 text-sm leading-6 text-[#71807a]",
                    ),
                    class_name="rounded-xl border border-[#eadbb8] bg-[#fbf6e9] p-4",
                ),
                class_name="grid grid-cols-1 gap-4 md:grid-cols-3 rounded-2xl border border-[#dce4dc] bg-[#fbfaf6] p-5 sm:p-6",
            ),
            class_name="flex flex-col gap-5",
        ),
    )
