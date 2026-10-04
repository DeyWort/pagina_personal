# AGENTS.md — Página personal

## Contexto del proyecto

Este repositorio contiene una página personal que funcionará como CV digital
y portafolio técnico. Debe presentar:

- un resumen **Sobre mí**;
- notebooks con experimentos e hipótesis de ciencia de datos y aprendizaje
  automático;
- stack tecnológico, habilidades e información de contacto;
- publicaciones tipo blog;
- el miniproyecto **Genera música con baile y movimiento**, una demostración
  de visión por computadora que usa la cámara web para transformar el
  movimiento de la persona en música.

La demostración debe contemplar escritorio y móvil, además de comunicar de
forma clara los permisos de cámara, los estados de carga y los errores.

## Tecnologías y convenciones

- Usar **Quarto** como framework principal del sitio.
- Usar Python para notebooks, experimentos y procesamiento de datos.
- Usar HTML y CSS para la estructura y la presentación responsive.
- Usar JavaScript u otras tecnologías solo cuando aporten una funcionalidad
  necesaria, especialmente para cámara, interacción o audio.
- Mantener el código, nombres de archivos y nombres de variables en inglés.
- Escribir los comentarios de código en español y añadirlos solo cuando
  aclaren una decisión o una parte no obvia.
- Preferir accesibilidad semántica, navegación por teclado, contraste
  suficiente y diseño mobile-first.
- Mantener las dependencias al mínimo y documentar cualquier dependencia nueva.

## Flujo de trabajo obligatorio

1. Tener claro el requisito antes de modificar código. Si existe una
   especificación activa, revisarla; si no, no inventar requisitos: trabajar con
   el alcance descrito en `README.md`.
2. Convertir cada cambio en un requisito o tarea verificable antes de
   implementarlo.
3. Reutilizar componentes, estilos y utilidades existentes antes de crear
   duplicados.
4. Mantener separados el contenido, la presentación y la lógica interactiva.
5. Validar cada cambio con las pruebas, el render de Quarto o la comprobación
   más pequeña que cubra el comportamiento modificado.
6. Revisar especialmente responsive design, accesibilidad y permisos de
   cámara cuando el cambio afecte al miniproyecto.

## Comandos del repositorio

El repositorio todavía no define scripts de ejecución, pruebas o formato en
`pyproject.toml`. Mientras se incorpora la aplicación Quarto, la entrada
Python mínima puede comprobarse con:

```bash
python main.py
```

Cuando se agreguen comandos oficiales, actualizar esta sección y `README.md`
en el mismo cambio. No asumir comandos de Quarto o herramientas de formato
que no estén instalados o documentados en el proyecto.

## Límites

- No modificar archivos ajenos al objetivo de la tarea.
- No crear servicios externos, autenticación, analítica ni almacenamiento de
  datos sin una especificación y aprobación explícitas.
- No solicitar permisos de cámara hasta que el usuario active la experiencia.
- No incluir credenciales, claves, datos personales sensibles ni archivos
  generados en el repositorio.
- No introducir una dependencia cuando la funcionalidad pueda resolverse con
  las herramientas existentes.
- No reemplazar cambios realizados por otra persona; integrar los cambios
  existentes cuidadosamente.

## Criterios de terminado

Una tarea está terminada cuando:

- cumple el requisito solicitado sin alterar funcionalidades no relacionadas;
- conserva el comportamiento responsive y las convenciones del proyecto;
- la documentación relacionada queda actualizada;
- la validación apropiada se ejecuta y su resultado se informa;
- no quedan archivos temporales ni cambios generados fuera del alcance.
