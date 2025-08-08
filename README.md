# Extractor de Esquema de Base de Datos Access

Un script de Python que extrae automáticamente el esquema de una base de datos de Microsoft Access (.accdb) y genera un archivo Markdown con la estructura de tablas, columnas y relaciones.

## 🚀 Características

- **Extracción completa del esquema**: Obtiene todas las tablas y sus columnas
- **Detección de relaciones**: Identifica las relaciones entre tablas usando ADOX
- **Salida en Markdown**: Genera documentación legible y bien estructurada
- **Soporte para contraseñas**: Maneja bases de datos protegidas con contraseña
- **Interfaz de línea de comandos**: Fácil de usar desde la terminal

## 📋 Requisitos del Sistema

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
| Nombre de Columna |
|-------------------|
| `ID_Cliente`      |
| `Nombre`          |
| `Email`           |

### Tabla: `Pedidos`
| Nombre de Columna |
|-------------------|
| `ID_Pedido`       |
| `ID_Cliente`      |
| `Fecha`           |

## Relaciones entre Tablas

- La tabla `Pedidos` se relaciona con `Clientes`.
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

## 🙏 Agradecimientos

- Microsoft por las librerías COM de Access
- La comunidad de Python por las excelentes herramientas de desarrollo

---

⭐ Si este proyecto te ha sido útil, ¡no olvides darle una estrella!