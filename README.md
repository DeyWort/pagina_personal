# Página personal · Guillermo Pineda Ramírez

CV digital y portafolio técnico de ciencia de datos y aprendizaje automático.

**Sitio en vivo:** https://deywort.github.io/pagina_personal/

## Qué contiene

- **Sobre mí** y **stack tecnológico** con las herramientas que uso a diario.
- **Experiencia y logros**: hackathons, visitas técnicas y formación.
- **Galería** de proyectos y actividades con visor navegable.
- **Contacto** y enlaces profesionales.

Las secciones de **Blog** y **notebooks** de experimentos están en desarrollo.

## Cómo está hecho

- **Quarto** como framework del sitio (estructura, publicación y notebooks).
- **HTML y CSS** para la interfaz, con diseño responsive y tema claro/oscuro.
- **JavaScript mínimo** y sin dependencias externas, solo para funciones concretas:
  el visor de la galería y el fondo interactivo.
- **GitHub Actions → GitHub Pages** para publicar (`_site/` se genera en CI).

## Ver el sitio en local

Requiere [Quarto](https://quarto.org) instalado.

```bash
quarto preview    # servidor en vivo con recarga automática
quarto render     # genera el sitio en _site/
```

`_site/` es un artefacto generado y no se versiona.

## Contacto

- **Email:** pinedaramirezmemo@gmail.com
- **LinkedIn:** https://www.linkedin.com/in/guillermo-pineda-ramirez/
- **GitHub:** https://github.com/DeyWort
