# 🔍 Extractor de Esquema de Base de Datos Access (MCP)

Herramienta para extraer y documentar automáticamente la estructura de bases de datos Microsoft Access (.accdb), generando documentación en formato Markdown.

## ✨ Características

- **Extracción automática** de tablas y sus columnas
- **Detección de relaciones** entre tablas
- **Documentación en Markdown** fácil de leer y compartir
- **Soporte para bases de datos protegidas** con contraseña
- **Módulo portable** para sistemas de IA que necesiten analizar bases de datos Access

## 🖥️ Requisitos del Sistema

- **Windows**: Este script requiere Windows ya que utiliza COM objects de Microsoft
- **Microsoft Access**: Debe estar instalado en el sistema (o al menos el motor de base de datos ACE)
- **Python 3.6+**: Versión recomendada de Python

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/ardelperal/MCP_access_schema.git
cd MCP_access_schema
```

### 2. Crear un entorno virtual

```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate

# En PowerShell:
venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install pypiwin32
```

### 4. Verificar la instalación

```bash
python mcp_db_schema_extractor.py --help
```

## 📖 Uso

### Sintaxis básica

```bash
python mcp_db_schema_extractor.py -db <ruta_a_db.accdb> [-p <password>] [-o <archivo_salida.md>]
```

### Parámetros

- `-db, --db_path` (obligatorio): Ruta completa al archivo .accdb
- `-p, --password` (opcional): Contraseña de la base de datos
- `-o, --output_path` (opcional): Ruta para el archivo de salida Markdown (por defecto: `db_schema_analisis.md`)

### Ejemplos de uso

#### Ejemplo básico (sin contraseña)
```bash
python mcp_db_schema_extractor.py -db "C:\MiBaseDatos\empresa.accdb"
```

#### Con contraseña
```bash
python mcp_db_schema_extractor.py -db "C:\MiBaseDatos\empresa.accdb" -p "micontraseña"
```

#### Especificando archivo de salida
```bash
python mcp_db_schema_extractor.py -db "C:\MiBaseDatos\empresa.accdb" -o "esquema_empresa.md"
```

#### Ejemplo completo
```bash
python mcp_db_schema_extractor.py -db "C:\Datos\gestion_riesgos.accdb" -p "secreto123" -o "documentacion_bd.md"
```

## 📄 Formato de salida

El script genera un archivo Markdown con la siguiente estructura:

```markdown
# Estructura de la Base de Datos y Relaciones

## Estructura de Tablas

### Tabla: `Clientes`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `ID_Cliente`      | `Integer`    |
| `Nombre`          | `Text`       |
| `Email`           | `Text`       |

### Tabla: `Pedidos`
| Nombre de Columna | Tipo de Dato |
|-------------------|--------------|
| `ID_Pedido`       | `Integer`    |
| `ID_Cliente`      | `Integer`    |
| `Fecha`           | `Date`       |

## Relaciones entre Tablas

- La tabla `Pedidos` se relaciona con `Clientes` (Columnas: `ID_Cliente` -> `ID_Cliente`).
```

## 🔧 Solución de problemas

### Error: "La librería 'pywin32' no está instalada"
```bash
pip install pypiwin32
```

### Error: "No se encuentra el proveedor Microsoft.ACE.OLEDB.12.0"
- Instala Microsoft Access Database Engine 2016 Redistributable
- O instala Microsoft Office/Access

### Error de permisos
- Ejecuta la terminal como administrador
- Verifica que el archivo .accdb no esté abierto en Access

### No se detectan relaciones
- Verifica que las relaciones estén definidas correctamente en Access
- Algunas bases de datos pueden no tener relaciones formales definidas

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**ardelperal** - [GitHub](https://github.com/ardelperal)

## 🤖 Uso como MCP para Inteligencias Artificiales

Este repositorio está diseñado para funcionar como un Módulo de Código Portable (MCP) para sistemas de Inteligencia Artificial. A continuación, se detallan los pasos para implementarlo como un MCP:

### Configuración del MCP en formato JSON

Para instalar este MCP en un sistema de IA compatible, debes incluir la siguiente configuración en el archivo JSON de definición de MCPs:

```json
{
  "name": "mcp_GitHub_access_schema",
  "description": "Extractor de esquema de bases de datos Access que genera documentación en formato Markdown",
  "parameters": {
    "properties": {
      "db_path": {
        "type": "string",
        "description": "Ruta completa al archivo .accdb que se desea analizar"
      },
      "password": {
        "type": "string",
        "description": "Contraseña de la base de datos (opcional)"
      },
      "output_path": {
        "type": "string",
        "description": "Ruta para el archivo de salida Markdown (opcional, por defecto: db_schema_analisis.md)"
      }
    },
    "required": ["db_path"]
  },
  "repository": {
    "url": "https://github.com/ardelperal/MCP_access_schema.git",
    "branch": "main"
  },
  "requirements": {
    "os": "windows",
    "dependencies": ["pypiwin32==306"],
    "external_dependencies": ["Microsoft Access o Microsoft Access Database Engine 2016+ Redistributable"]
  },
  "entry_point": "mcp_db_schema_extractor.py",
  "version": "1.0.0",
  "author": "ardelperal"
}
```

### Ejemplo de llamada al MCP desde una IA

Una vez configurado el MCP, la IA puede invocarlo de la siguiente manera:

```javascript
// Ejemplo de invocación del MCP desde una IA
<function_calls>
<invoke name="mcp_GitHub_access_schema">
<parameter name="db_path">C:\MiBaseDatos\empresa.accdb</parameter>
<parameter name="password">micontraseña</parameter>
<parameter name="output_path">esquema_empresa.md</parameter>
</invoke>
</function_calls>
```

## 🙏 Agradecimientos

- Microsoft por las librerías COM de Access
- La comunidad de Python por las excelentes herramientas de desarrollo
- Los sistemas de IA que utilizan este MCP para mejorar sus capacidades

---

⭐ Si este proyecto te ha sido útil, ¡no olvides darle una estrella!