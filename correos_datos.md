# Estructura de la Base de Datos y Relaciones

Este documento detalla la estructura de la base de datos de Access, incluyendo sus tablas, columnas y relaciones. Las relaciones se obtuvieron directamente del esquema de la base de datos.

## Estructura de Tablas

### Tabla: `TbConfigCorreos`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Activo` | `Boolean` |
| `ID` | `Integer` |
| `Password` | `Text` |
| `Puerto` | `Integer` |
| `SSL` | `Boolean` |
| `ServidorSMTP` | `Text` |
| `Timeout` | `Integer` |
| `Usuario` | `Text` |

### Tabla: `TbCorreos`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Aplicacion` | `Text` |
| `Asunto` | `Text` |
| `Cuerpo` | `Text (Long)` |
| `Destinatarios` | `Text` |
| `DestinatariosConCopia` | `Text` |
| `DestinatariosConCopiaOculta` | `Text` |
| `FechaEnvio` | `Date` |
| `FechaGrabacion` | `Date` |
| `IDCorreo` | `Integer` |
| `URLAdjunto` | `Text` |

### Tabla: `TbCorreosEnviados`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Aplicacion` | `Text` |
| `Asunto` | `Text` |
| `Cuerpo` | `Text (Long)` |
| `Destinatarios` | `Text` |
| `DestinatariosConCopia` | `Text` |
| `DestinatariosConCopiaOculta` | `Text` |
| `FechaEnvio` | `Date` |
| `FechaGrabacion` | `Date` |
| `IDCorreo` | `Integer` |
| `URLAdjunto` | `Text` |

### Tabla: `TbPlantillasCorreo`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `Activa` | `Boolean` |
| `Aplicacion` | `Text` |
| `Asunto` | `Text` |
| `Cuerpo` | `Text (Long)` |
| `ID` | `Integer` |
| `Nombre` | `Text` |

## Relaciones entre Tablas

No se encontraron relaciones definidas en la base de datos o hubo un error al obtenerlas.
