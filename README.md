# Javier Retamero — CV

Web personal de una sola página: QA Automation & Performance Engineer.

**🔗 Ver online**: https://jarelo.github.io/cv-javier-retamero/

## Qué es esto

Un CV en formato web, sin frameworks ni build — HTML, CSS y JavaScript vanilla,
pensado para publicarse tal cual en GitHub Pages. Incluye:

- Tema oscuro por defecto, con toggle a claro (persistente vía `localStorage`).
- Animaciones de aparición al hacer scroll (con contenido visible por defecto
  si JavaScript falla, ver `script.js`).
- Descarga del CV en PDF (`Javier_Retamero_CV.pdf`).

## Estructura

```
├── index.html          # contenido y estructura
├── style.css           # diseño (tema oscuro por defecto)
├── script.js           # toggle de tema + scroll reveal
├── assets/profile.jpg  # foto de perfil
├── scripts/
│   └── generate_pdf.py # generador alternativo de PDF a partir de los
│                        # mismos datos que la web (sin usar actualmente:
│                        # Javier_Retamero_CV.pdf es hoy el PDF original)
└── Javier_Retamero_CV.pdf
```

## Desarrollo local

No hace falta build ni dependencias — basta con abrir `index.html` en el
navegador, o servirlo con cualquier servidor estático:

```bash
python -m http.server 8000
```
