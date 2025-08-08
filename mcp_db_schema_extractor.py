# -*- coding: utf-8 -*-
"""
Programa principal (MCP) para la gestión automatizada del esquema de la base de datos.

Este script utiliza las funciones de un extractor de esquemas de base de datos
para generar un archivo Markdown con la estructura de tablas y relaciones de
una base de datos de Microsoft Access (.accdb).

Uso:
  python mcp_db_schema_extractor.py -db <ruta_a_db.accdb> [-p <password>] [-o <ruta_a_archivo.md>]

Argumentos:
  -db, --db_path       Ruta completa al archivo .accdb (obligatorio).
  -p, --password       Contraseña de la base de datos (opcional).
  -o, --output_path    Ruta completa para el archivo de salida Markdown (opcional).
                       Si no se especifica, se creará 'db_schema_analisis.md' en el mismo directorio.

NOTA: Este script asume que las funciones de extracción de esquema (get_database_schema,
      get_relationships_from_adox, create_markdown_output) están disponibles.
      Para que sea un script único, las he incluido aquí directamente.
"""
import os
import argparse

# Asegúrate de instalar esta librería con 'pip install pypiwin32'
try:
    import win32com.client
except ImportError:
    print("Error: La librería 'pywin32' no está instalada.")
    print("Por favor, instálala usando: pip install pypiwin32")
    exit()


# === Funciones de Extracción de Esquema (Tomadas del Canvas anterior) ===

def get_database_schema(db_path, password):
    """
    Se conecta a una base de datos de Access y extrae su esquema, incluyendo columnas,
    iterando tabla por tabla. Este método utiliza ADO (ActiveX Data Objects).

    Args:
        db_path (str): La ruta completa al archivo .accdb.
        password (str): La contraseña de la base de datos.

    Returns:
        tuple: Un diccionario con el esquema y un booleano de éxito.
               El esquema es {nombre_tabla: [nombre_columna_1, nombre_columna_2, ...]}.
    """
    if not os.path.exists(db_path):
        print(f"Error: El archivo de base de datos no se encontró en '{db_path}'.")
        return None, False

    conn = None
    try:
        # Cadena de conexión OLEDB para archivos .accdb
        conn_str = f"Provider=Microsoft.ACE.OLEDB.12.0;Data Source={db_path};"
        if password:
            conn_str += f"Jet OLEDB:Database Password={password};"
        
        # Crear la conexión COM
        conn = win32com.client.Dispatch('ADODB.Connection')
        conn.Open(conn_str)
        
        db_schema = {}
        adSchemaTables = 20

        # Obtener una lista de tablas de usuario
        tables_rs = conn.OpenSchema(adSchemaTables)

        table_names = []
        while not tables_rs.EOF:
            table_name = tables_rs.Fields("TABLE_NAME").Value
            table_type = tables_rs.Fields("TABLE_TYPE").Value
            
            # Solo procesar tablas de usuario
            if table_type == "TABLE":
                table_names.append(table_name)
            
            tables_rs.MoveNext()

        # Recorrer cada tabla para obtener sus campos
        for table_name in table_names:
            columns = []
            # Abrir un Recordset para la tabla, de forma que se puedan leer sus Fields
            recordset = win32com.client.Dispatch('ADODB.Recordset')
            recordset.Open(f"SELECT * FROM `{table_name}`", conn)
            
            for field in recordset.Fields:
                columns.append(field.Name)
            
            db_schema[table_name] = columns
            recordset.Close()
            
        return db_schema, True
    except Exception as e:
        print(f"Ocurrió un error inesperado al usar ADO para obtener el esquema: {e}")
        return None, False
    finally:
        if conn and conn.State == 1:
            conn.Close()

def get_relationships_from_adox(db_path: str, password: str):
    """
    Se conecta a una base de datos de Access y extrae las relaciones
    utilizando la biblioteca ADOX (ActiveX Data Objects Extensions).

    Args:
        db_path (str): La ruta completa al archivo .accdb.
        password (str): La contraseña de la base de datos.

    Returns:
        list: Una lista de cadenas de texto que describen las relaciones.
    """
    if not os.path.exists(db_path):
        return []

    relaciones = []
    cat = None

    try:
        # Cadena de conexión para ADOX
        conn_str = f"Provider=Microsoft.ACE.OLEDB.12.0;Data Source={db_path};"
        if password:
            conn_str += f"Jet OLEDB:Database Password={password};"

        cat = win32com.client.Dispatch('ADOX.Catalog')
        cat.ActiveConnection = conn_str

        # ADOX.KeyTypeEnum.adKeyForeign tiene un valor de 2
        AD_KEY_FOREIGN = 2
        if cat.Tables.Count > 0:
            for table in cat.Tables:
                # Se obtienen las claves (Key) de la tabla, que pueden ser primarias o foráneas
                if table.Keys.Count > 0:
                    for key in table.Keys:
                        if key.Type == AD_KEY_FOREIGN and key.RelatedTable:
                            # Se detecta una clave foránea, lo que indica una relación
                            foreign_table = table.Name
                            primary_table = key.RelatedTable
                            relaciones.append((primary_table, foreign_table))
        else:
            print("No se encontraron relaciones en la base de datos.")

    except Exception as e:
        print(f"Advertencia: Ocurrió un error al obtener las relaciones. ¿Está Access instalado?")
        print(f"Error detallado: {e}")
    finally:
        if cat:
            cat = None

    return relaciones

def create_markdown_output(schema, relationships):
    """
    Crea el contenido en formato Markdown para el esquema de la base de datos.
    """
    markdown_content = "# Estructura de la Base de Datos y Relaciones\n\n"
    markdown_content += "Este documento detalla la estructura de la base de datos de Access, incluyendo "
    markdown_content += "sus tablas, columnas y relaciones. Las relaciones se obtuvieron directamente "
    markdown_content += "del esquema de la base de datos.\n\n"

    markdown_content += "## Estructura de Tablas\n\n"
    for table, columns in sorted(schema.items()):
        markdown_content += f"### Tabla: `{table}`\n"
        markdown_content += "| Nombre de Columna |\n"
        markdown_content += "|-------------------|\n"
        for column in sorted(columns):
            markdown_content += f"| `{column}` |\n"
        markdown_content += "\n"
    
    markdown_content += "## Relaciones entre Tablas\n\n"
    if relationships:
        markdown_content += "Las siguientes relaciones fueron encontradas en el esquema de la base de datos:\n\n"
        for tabla_principal, tabla_relacionada in relationships:
            markdown_content += f"- La tabla `{tabla_relacionada}` se relaciona con `{tabla_principal}`.\n"
    else:
        markdown_content += "No se encontraron relaciones definidas en la base de datos o hubo un error al obtenerlas.\n"
        
    return markdown_content


# === Lógica principal del MCP ===

def main():
    """Función principal del script."""
    parser = argparse.ArgumentParser(description='Extrae el esquema de una base de datos de Access y las relaciones a un archivo Markdown.')
    parser.add_argument('-db', '--db_path', required=True, help='Ruta completa al archivo .accdb.')
    parser.add_argument('-p', '--password', default='', help='Contraseña de la base de datos (opcional).')
    parser.add_argument('-o', '--output_path', default='db_schema_analisis.md', help='Ruta para el archivo de salida Markdown (opcional).')
    
    args = parser.parse_args()

    # Obtiene el esquema de la base de datos (tablas y columnas) usando ADO
    db_schema, schema_success = get_database_schema(args.db_path, args.password)
    
    # Obtiene las relaciones directamente del esquema usando ADOX
    relationships = get_relationships_from_adox(args.db_path, args.password)

    if schema_success and db_schema:
        # Crea el contenido Markdown
        markdown_output = create_markdown_output(db_schema, relationships)
        
        # Escribe el contenido en el archivo de salida
        try:
            with open(args.output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_output)
            print(f"¡Éxito! El esquema de la base de datos y las relaciones han sido exportadas a '{args.output_path}'.")
        except IOError as e:
            print(f"Error al escribir el archivo de salida: {e}")

if __name__ == '__main__':
    main()
