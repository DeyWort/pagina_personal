# Página personal

Sitio web personal para presentar mi experiencia en ciencia de datos, desarrollo
de software y proyectos propios. Funcionará como un CV digital con información
de contacto, publicaciones y demostraciones técnicas.

## Propósito y contenido

La página tendrá las siguientes áreas:

- **Sobre mí:** resumen profesional y principales intereses.
- **Notebooks:** experimentos, hipótesis y resultados relacionados con
  aprendizaje automático y ciencia de datos.
- **Stack y habilidades:** tecnologías, herramientas y competencias.
- **Blog:** publicaciones breves sobre ideas, aprendizajes y proyectos.
- **Contacto:** medios para comunicarse y enlaces profesionales.

## Tecnología

- **Quarto** para la estructura, publicación y presentación del sitio.
- **HTML y CSS** para la interfaz y el diseño responsive.
- **Python** para notebooks, experimentos y lógica de datos.
- JavaScript u otras tecnologías podrán incorporarse únicamente cuando sean
  necesarias para una funcionalidad concreta.

El proyecto requiere Python 3.12 o superior. La implementación de Quarto,
la estructura final de carpetas y las dependencias se definirán durante la
planificación técnica.

## Estado actual

El sitio Quarto ya existe y es previsualizable. La portada (rediseñada) incluye:
"Sobre mí" orientado a resultados, sección "Mi stack tecnológico" con iconos,
tarjetas de experiencia ligadas a sus fotografías y una galería con visor
navegable. Soporta tema claro y oscuro conmutables. Están pendientes de
contenido las secciones de Blog y Proyectos (sus listings apuntan a carpetas aún
vacías) y la sección de Notebooks. El requisito a nivel de Python (`main.py`)
aún no existe.

El estado detallado, requisito por requisito, vive en
[`docs/especificacion.md`](docs/especificacion.md); los principios y límites del
proyecto, en [`docs/constitucion.md`](docs/constitucion.md).

## Desarrollo basado en especificaciones

Se seguirá **Spec-Driven Development (SDD)** para reducir ambigüedades y
mantener trazabilidad entre necesidades, implementación y validación:

| Etapa | Resultado esperado |
|---|---|
| Constitución | Principios y límites innegociables del proyecto |
| Especificación | Requisitos funcionales y no funcionales verificables |
| Clarificación | Revisión de ambigüedades, dependencias y casos límite |
| Planificación | Arquitectura, módulos, datos y decisiones técnicas |
| Tareas | Trabajo dividido en unidades pequeñas con criterios de terminado |
| Implementación | Desarrollo en `src/`, notebooks y recursos del sitio |
| Validación | Pruebas, revisión visual y recorrido requisito por requisito |
| Publicación | Generación y despliegue del sitio Quarto |

Antes de modificar código, se deben revisar la constitución y la
especificación activa cuando estén disponibles.

## Uso local

El sitio se previsualiza y se genera con Quarto (requiere `quarto` instalado):

```bash
quarto preview        # servidor en vivo con recarga automática
quarto render         # genera la salida del sitio en _site/
```

La salida `_site/` es un artefacto generado y no se versiona.

## Alcance y prioridades

La prioridad es construir primero una base accesible, responsive y fácil de
mantener; después se añadirán los notebooks, las publicaciones y la
demostración interactiva. No se añadirán servicios externos, analítica,
autenticación ni dependencias nuevas sin una necesidad documentada y una
decisión técnica explícita.
