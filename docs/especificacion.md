# Especificación activa

Requisitos verificables del sitio. Deriva del alcance descrito en `README.md` y
de la `docs/constitucion.md`. La columna **Estado** refleja la realidad
comprobada del repositorio, no la intención.

Leyenda de estado: `OK` funciona y es verificable · `HUECO` área prevista sin
contenido · `ROTO` existe pero falla · `PENDIENTE` aún no iniciado.

## Requisitos funcionales

| ID | Requisito | Verificación | Estado |
|---|---|---|---|
| RF-01 | **Sobre mí**: resumen profesional e intereses. | Sección visible en la portada con texto real. | OK |
| RF-02 | **Stack y habilidades**: tecnologías y competencias. | Sección "Mi stack tecnológico" con chips e icono de cada herramienta en la portada. | OK |
| RF-03 | **Experiencia y logros**: logros verificables. | Tarjetas en la portada. | OK |
| RF-04 | **Galería**: fotografías ampliables. | Galería con lightbox navegable (abrir, flechas, Esc/clic fuera) en la portada. | OK |
| RF-05 | **Contacto**: medios de comunicación. | Email, LinkedIn, GitHub y enlace a CV en la portada. | ROTO (el enlace a `cv-guillermo-pineda.pdf` apunta a un archivo inexistente) |
| RF-06 | **Blog**: publicaciones breves. | Listing en `/blog/` con entradas. | HUECO (el listing apunta a `posts/`, que no existe) |
| RF-07 | **Proyectos**: notebooks y proyectos recientes. | Listing en `/proyectos/` con tarjetas. | HUECO (no hay archivos de proyecto; el grid sale vacío) |
| RF-08 | **Notebooks de experimentos**: hipótesis y resultados de ML/ciencia de datos. | Página y carpeta `notebooks/` con experimentos. | PENDIENTE |
| RF-09 | **Navegación** entre todas las áreas del sitio. | Navbar con enlaces a cada sección. | HUECO (solo Inicio/Proyectos/Blog; faltan Notebooks y un acceso a Contacto) |

## Requisitos no funcionales

| ID | Requisito | Verificación | Estado |
|---|---|---|---|
| RNF-01 | **Responsive / mobile-first**: funciona en móvil y escritorio. | Revisión visual a varios anchos sin desbordes. | OK (por revisar en móvil real) |
| RNF-02 | **Accesibilidad**: semántica, teclado, contraste. | Recorrido por teclado y contraste suficiente. | PENDIENTE de auditoría formal |
| RNF-03 | **Dependencias mínimas**: sin dependencias innecesarias. | `pyproject.toml` sin dependencias salvo justificación documentada. | OK (`dependencies = []`) |
| RNF-04 | **Publicación**: el sitio se genera y se puede desplegar. | `quarto render` sin errores y `site-url` válido. | ROTO (`site-url` es el placeholder `https://tuusuario.github.io/mi_pagina`) |
| RNF-05 | **Tema claro/oscuro** conmutable por el usuario, con tokens de color mantenibles. | El botón de Quarto alterna `quarto-light`/`quarto-dark` en `<body>`; los tokens de `assets/styles.css` cambian con él. | OK |
| RNF-06 | **Fondo decorativo** (red neuronal) interactivo, sutil y adaptado a ambos temas. | Los nodos se activan al pasar el cursor y emiten un pulso al presionar; no bloquea clics (`pointer-events:none`) ni la lectura, respeta `prefers-reduced-motion`. | OK |

## Documentación del repositorio

| Documento | Estado |
|---|---|
| `README.md` | Desactualizado: afirma que existe `main.py`, que no existe y que se usa como validación en `AGENTS.md`. |
| `AGENTS.md` | Vigente. |
| `docs/constitucion.md` | Creado en este cambio. |
| `docs/especificacion.md` | Creado en este cambio. |
| `partials/stack-icons.html` | Iconos del stack como SVG inline (simple-icons). Generado por `scripts/gen_stack_icons.py`. |
| `assets/lightbox.html` | Visor de la galería; se incluye con `include-after-body` desde `_quarto.yml`. |
| `assets/neural-bg.html` | Fondo de red neuronal interactivo; se incluye con `include-after-body` desde `_quarto.yml`. |

## Decisiones pendientes (requieren aprobación)

1. **RF-05 / CV**: o se incorpora el PDF `cv-guillermo-pineda.pdf`, o se retira
   el enlace "CV en PDF" de la portada.
2. **RNF-05 / site-url**: valor real (usuario y nombre de repositorio en GitHub
   Pages) para reemplazar el placeholder.
3. **RF-06 / blog**: confirmar la carpeta de posts (`posts/`) y su primer
   contenido.
4. **RF-07 / proyectos**: confirmar la estructura de cada proyecto para que el
   listing tenga contenido.

## Siguientes etapas (SDD)

Clarificación de las decisiones pendientes → planificación (estructura de
carpetas `posts/`, `proyectos/`, `notebooks/`, `src/`) → tareas → implementación
→ validación por requisito → publicación.
