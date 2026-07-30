"""Genera Javier_Retamero_CV.pdf a partir de los mismos datos que index.html,
ya filtrados (sin telefono/direccion/fecha de nacimiento) para un repo publico.
Uso: python scripts/generate_pdf.py (desde la raiz del repo).
"""

from pathlib import Path

from fpdf import FPDF

ROOT = Path(__file__).resolve().parent.parent
ACCENT = (14, 165, 174)  # teal, coherente con --accent del sitio
TEXT_DIM = (90, 98, 122)
TEXT = (16, 21, 42)

EXPERIENCIA = [
    (
        "QA Automation & Performance Engineer",
        "ITI (Instituto Tecnologico de la Informatica)",
        "06.2021 - actualidad",
        [
            "Responsable de la estrategia de automatizacion de pruebas con Playwright: arquitectura, "
            "estandares y buenas practicas.",
            "Diseno y evolucion de suites end-to-end, API y regresion integradas en pipelines de CI/CD.",
            "Responsable de pruebas de rendimiento y carga: planificacion, ejecucion y analisis de resultados.",
            "Coordinacion y seguimiento de un equipo de 3 QA Engineers.",
            "Mentoring en Playwright, Agile Testing, Jira y Xray a equipos internos y clientes.",
            "Investigacion y aplicacion de IA para optimizar analisis de requisitos y generacion de casos de prueba.",
        ],
    ),
    (
        "Responsable Depto. QA",
        "Health in Code / IMEGEN (Instituto de Medicina Genomica)",
        "06.2020 - 06.2021",
        [
            "Diseno y ejecucion de pruebas manuales y automatizadas para garantizar la calidad de las entregas.",
            "Implantacion y promocion de practicas de Agile Testing dentro del equipo.",
            "Coordinacion y planificacion de Sprints; supervision de despliegues y releases a produccion.",
        ],
    ),
    (
        "Quality Assurance (QA)",
        "PFS",
        "05.2018 - 06.2020",
        [
            "Diseno y mantenimiento de pruebas automatizadas con Selenium WebDriver.",
            "Administracion y configuracion de Jenkins para ejecucion continua de pruebas.",
            "Primeras experiencias en pruebas de rendimiento con Apache JMeter.",
        ],
    ),
    (
        "Administrador de Sistemas",
        "Grupo Antolin",
        "12.2017 - 05.2018",
        [
            "Administracion de sistemas, soporte a usuarios y gestion de infraestructura IT.",
            "Colaboracion en desarrollo y mantenimiento de aplicaciones y bases de datos.",
        ],
    ),
    (
        "Tecnico Informatico",
        "Lopez Vello Telecomunicaciones",
        "04.2012 - 09.2012",
        [
            "Soporte tecnico, instalacion y mantenimiento de sistemas informaticos y equipos de seguridad.",
        ],
    ),
]

FORMACION = [
    ("2026", "ISTQB (R) Certified Tester Foundation Level - Agile Tester (CTFL-AT)"),
    ("2025", "ISTQB (R) Certified Tester Foundation Level (CTFL)"),
    ("2013 - actualidad", "Grado en Informatica - Universidad Politecnica de Valencia"),
    ("2011 - 2013", "CFGS Administracion de Sistemas Informaticos y Redes - IES Rodrigo Botet"),
    ("2009 - 2011", "CFGM Sistemas Microinformaticos y Redes - Colegio Esclavas de Maria"),
]

TECNOLOGIAS = [
    ("Automatizacion", "Playwright, Selenium WebDriver, Gherkin"),
    ("Performance", "k6, Apache JMeter"),
    ("APIs & CI/CD", "REST, Postman, Jenkins, Git"),
    ("Gestion & agilidad", "Agile Testing, JIRA, Xray"),
    ("Lenguajes", "TypeScript, SQL, Python"),
    ("IA aplicada a QA", "Generacion de casos de prueba, analisis de requisitos"),
    ("Idiomas", "Espanol (nativo), Ingles tecnico"),
]

INTERESES = "Tecnologia - Naturaleza - Deporte - Formacion continua - Viajar"


class CV(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", size=8)
        self.set_text_color(*TEXT_DIM)
        self.cell(0, 10, "javier-retamero.github.io - CV generado automaticamente", align="C")


def section_title(pdf: CV, text: str) -> None:
    pdf.ln(4)
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(*ACCENT)
    pdf.cell(0, 8, text.upper())
    pdf.ln(7)
    pdf.set_draw_color(*ACCENT)
    pdf.set_line_width(0.4)
    pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
    pdf.ln(4)


def main() -> None:
    pdf = CV(format="A4", unit="mm")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()
    pdf.set_margins(18, 16, 18)

    photo = ROOT / "assets" / "profile.jpg"
    if photo.exists():
        pdf.image(str(photo), x=pdf.w - pdf.r_margin - 28, y=16, w=28, h=28)

    pdf.set_font("Helvetica", "B", 22)
    pdf.set_text_color(*TEXT)
    pdf.cell(120, 10, "Javier Retamero")
    pdf.ln(9)
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(*ACCENT)
    pdf.cell(120, 7, "QA Automation & Performance Engineer")
    pdf.ln(7)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(*TEXT_DIM)
    pdf.cell(120, 6, "javirelo@hotmail.com  -  Valencia, Espana")
    pdf.ln(14)

    section_title(pdf, "Objetivo profesional")
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(
        0,
        5,
        "Profesional de QA especializado en automatizacion de pruebas y rendimiento, orientado a la "
        "mejora continua y la calidad del software. Mi objetivo es aportar valor mediante la "
        "optimizacion de procesos de testing, la deteccion temprana de incidencias y la colaboracion "
        "con equipos multidisciplinares, contribuyendo al crecimiento de la empresa y a mi desarrollo "
        "profesional.",
    )

    section_title(pdf, "Experiencia")
    for puesto, empresa, fechas, bullets in EXPERIENCIA:
        pdf.set_font("Helvetica", "B", 10.5)
        pdf.set_text_color(*TEXT)
        pdf.cell(0, 5.5, puesto)
        pdf.ln(5.5)
        pdf.set_font("Helvetica", "I", 9)
        pdf.set_text_color(*TEXT_DIM)
        pdf.cell(0, 5, f"{empresa}  |  {fechas}")
        pdf.ln(5.5)
        pdf.set_font("Helvetica", "", 9)
        pdf.set_text_color(*TEXT)
        for b in bullets:
            pdf.set_x(pdf.l_margin + 3)
            pdf.multi_cell(0, 4.6, f"-  {b}", new_x="LMARGIN", new_y="NEXT")
        pdf.ln(2)

    section_title(pdf, "Formacion")
    for anio, titulo in FORMACION:
        pdf.set_font("Helvetica", "B", 9)
        pdf.set_text_color(*ACCENT)
        pdf.multi_cell(0, 5, anio, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9.5)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(0, 5.5, titulo, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)

    section_title(pdf, "Competencias y tecnologias")
    for categoria, valores in TECNOLOGIAS:
        pdf.set_font("Helvetica", "B", 9.5)
        pdf.set_text_color(*TEXT)
        pdf.multi_cell(0, 5, categoria, new_x="LMARGIN", new_y="NEXT")
        pdf.set_font("Helvetica", "", 9.5)
        pdf.set_text_color(*TEXT_DIM)
        pdf.multi_cell(0, 5.5, valores, new_x="LMARGIN", new_y="NEXT")
        pdf.ln(1)

    section_title(pdf, "Fuera del trabajo")
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(*TEXT_DIM)
    pdf.multi_cell(0, 5, INTERESES, new_x="LMARGIN", new_y="NEXT")

    output_path = ROOT / "Javier_Retamero_CV.pdf"
    pdf.output(str(output_path))
    print(f"PDF generado en {output_path}")


if __name__ == "__main__":
    main()
