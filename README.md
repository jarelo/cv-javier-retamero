# Javier Retamero — CV

Web personal de una sola página: QA Automation & Performance Engineer.

**🔗 Ver online**: https://jarelo.github.io/cv-javier-retamero/

## Qué es esto

Un CV en formato web, sin frameworks ni build — HTML, CSS y JavaScript vanilla,
pensado para publicarse tal cual en GitHub Pages. Incluye:

- Modo claro/oscuro (persistente, con detección de preferencia del sistema).
- Animaciones de aparición al hacer scroll.
- Descarga del CV en PDF (`Javier_Retamero_CV.pdf`, generado con
  [`scripts/generate_pdf.py`](scripts/generate_pdf.py) a partir de los mismos
  datos que la web).

## Estructura

```
├── index.html          # contenido y estructura
├── style.css           # diseño (tema oscuro por defecto)
├── script.js           # toggle de tema + scroll reveal
├── assets/profile.jpg  # foto de perfil
├── scripts/
│   └── generate_pdf.py # regenera Javier_Retamero_CV.pdf
└── Javier_Retamero_CV.pdf
```

## Desarrollo local

No hace falta build ni dependencias — basta con abrir `index.html` en el
navegador, o servirlo con cualquier servidor estático:

```bash
python -m http.server 8000
```

Para regenerar el PDF tras cambiar el contenido (requiere `fpdf2`):

```bash
python -m pip install fpdf2
python scripts/generate_pdf.py
```

## Nota sobre los datos de contacto

A propósito, ni el sitio ni el PDF incluyen teléfono, dirección postal ni
fecha de nacimiento — solo email y ciudad, para minimizar lo expuesto en un
repositorio público.
