# Constitución del proyecto

Principios y límites innegociables de la página personal. Todo cambio
(especificación, plan, tarea, implementación) debe ser compatible con este
documento. Si un requisito entra en conflicto con la constitución, prevalece la
constitución y el requisito se reformula.

## 1. Propósito

El sitio es un **CV digital y portafolio técnico** de Guillermo Pineda Ramírez.
Su función es presentar, de forma clara y verificable: el resumen profesional,
los experimentos de ciencia de datos y aprendizaje automático, el stack y las
habilidades, las publicaciones tipo blog y la información de contacto.

## 2. Tecnología

- **Quarto** es el framework principal del sitio.
- **HTML y CSS** definen la estructura y la presentación; el diseño es
  *responsive* y *mobile-first*.
- **Python** se usa para notebooks, experimentos y procesamiento de datos.
- **JavaScript** u otras tecnologías se incorporan solo cuando aportan una
  funcionalidad necesaria que HTML/CSS no pueden resolver.

## 3. Separación de responsabilidades

El contenido, la presentación y la lógica interactiva se mantienen en capas
separadas. Un cambio de estilo no debe exigir tocar la lógica; un cambio de
lógica no debe duplicar estilos ni contenido.

## 4. Accesibilidad y responsive

Son requisitos, no mejoras opcionales:

- estructura semántica correcta;
- navegación completa por teclado;
- contraste suficiente;
- diseño *mobile-first* que funcione en escritorio y móvil.

## 5. Dependencias

Se mantienen al mínimo. Toda dependencia nueva se justifica por una necesidad
concreta y se documenta en el mismo cambio que la introduce. No se añade una
dependencia cuando la funcionalidad puede resolverse con lo ya existente.

## 6. Privacidad

- No se crean servicios externos, autenticación, analítica ni almacenamiento de
  datos sin una especificación y aprobación explícitas.

## 7. Higiene del repositorio

- No se incluyen credenciales, claves, datos personales sensibles ni archivos
  generados (por ejemplo, la salida `_site/`).
- No se modifica trabajo ajeno al objetivo de la tarea; los cambios existentes
  se integran con cuidado.

## 8. Idioma y estilo de código

- El código, los nombres de archivos y los nombres de variables se escriben en
  **inglés**.
- Los comentarios de código se escriben en **español** y solo cuando aclaran una
  decisión o una parte no obvia.
- El contenido del sitio puede estar en español (idioma del sitio: `es`).

## 9. Trazabilidad (Spec-Driven Development)

Ninguna implementación ocurre sin un requisito o tarea verificable previa. El
flujo es: constitución → especificación → clarificación → planificación →
tareas → implementación → validación → publicación. Cada etapa deja un
resultado escrito y comprobable.

## 10. Criterio de terminado

Una tarea termina cuando: cumple el requisito sin alterar funciones no
relacionadas; conserva el comportamiento responsive y las convenciones; deja la
documentación relacionada actualizada; ejecuta la validación apropiada e
informa su resultado; y no deja archivos temporales ni cambios fuera de
alcance.
