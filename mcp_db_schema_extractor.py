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

# Diccionario de traducción de los tipos de datos de ADO a texto legible
# para ser usado en la salida Markdown.
# Los valores son constantes de ADO.DataTypeEnum.
ADO_DATA_TYPES = {
    0: "Empty", 2: "SmallInt", 3: "Integer", 4: "Single", 5: "Double",
    6: "Currency", 7: "Date", 8: "String (OLE)", 11: "Boolean", 13: "Variant",
    17: "TinyInt", 20: "BigInt", 64: "FileTime", 72: "GUID", 128: "Binary",
    129: "Text (Ansi)", 130: "Text (Unicode)", 131: "Decimal", 132: "Numeric",
    133: "Date", 134: "Time", 135: "DateTime", 200: "Text", 201: "Text (Long)",
    202: "Text", 203: "Text (Long)", 204: "Binary (Long)", 205: "Stream"
}

# === Funciones de Extracción de Esquema ===

def get_database_schema(db_path, password):
    """
    Se conecta a una base de datos de Access y extrae su esquema, incluyendo columnas y
    su tipo de dato. Este método utiliza ADO (ActiveX Data Objects).
    
    Ahora también incluye tablas vinculadas, pero excluye las tablas de sistema
    cuyo nombre comienza con "MSys".

    Args:
        db_path (str): La ruta completa al archivo .accdb.
        password (str): La contraseña de la base de datos.

    Returns:
        tuple: Un diccionario con el esquema y un booleano de éxito.
               El esquema es {nombre_tabla: [(nombre_columna, tipo_dato_id), ...]}.
    """
    if not os.path.exists(db_path):
        print(f"Error: El archivo de base de datos no se encontró en '{db_path}'.")
        return None, False

    conn = None
    tables_rs = None
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

        # Obtener una lista de tablas
        tables_rs = conn.OpenSchema(adSchemaTables)

        table_names = []
        linked_tables = []  # Lista para almacenar información de tablas vinculadas
        
        while not tables_rs.EOF:
            table_name = tables_rs.Fields("TABLE_NAME").Value
            table_type = tables_rs.Fields("TABLE_TYPE").Value
            
            # Procesar tablas de usuario y vinculadas, excluyendo tablas de sistema
            if table_type in ("TABLE", "LINK") and not table_name.startswith("MSys"):
                if table_type == "LINK":
                    # Es una tabla vinculada
                    linked_tables.append(table_name)
                    print(f"🔗 Tabla vinculada detectada: '{table_name}' - Verificando accesibilidad...")
                else:
                    table_names.append(table_name)
            
            tables_rs.MoveNext()

        tables_rs.Close()
        tables_rs = None

        # Procesar primero las tablas normales (no vinculadas)
        for table_name in table_names:
            # Verificar nuevamente que no sea tabla de sistema
            if table_name.startswith("MSys"):
                continue
                
            columns = []
            recordset = None
            try:
                # Abrir un Recordset para la tabla, de forma que se puedan leer sus Fields
                recordset = win32com.client.Dispatch('ADODB.Recordset')
                recordset.Open(f"SELECT TOP 1 * FROM [{table_name}]", conn)
                
                for field in recordset.Fields:
                    # Almacenar el nombre y el tipo de dato como una tupla
                    columns.append((field.Name, field.Type))
                
                db_schema[table_name] = columns
                
            except Exception as e:
                print(f"Advertencia: Error al procesar la tabla '{table_name}': {str(e)}")
                # Continuar con la siguiente tabla
                continue
            finally:
                try:
                    if recordset and recordset.State == 1:
                        recordset.Close()
                except:
                    pass
                recordset = None

        # Procesar tablas vinculadas de manera especial
        for table_name in linked_tables:
            # Verificar nuevamente que no sea tabla de sistema
            if table_name.startswith("MSys"):
                continue
                
            columns = []
            recordset = None
            linked_path = "ruta no disponible"
            
            # Intentar obtener la ruta usando DAO (Data Access Objects)
            try:
                # Crear una instancia de DAO
                dao_engine = win32com.client.Dispatch("DAO.DBEngine.120")  # Access 2013+
                dao_db = dao_engine.OpenDatabase(db_path, False, False, f"MS Access;PWD={password}" if password else "")
                
                # Buscar la tabla vinculada en la colección TableDefs
                for tbl in dao_db.TableDefs:
                    if tbl.Name == table_name and tbl.Connect:
                        # Es una tabla vinculada, extraer la ruta del Connect string
                        import re
                        connect_str = str(tbl.Connect)
                        db_match = re.search(r'DATABASE=([^;]+)', connect_str)
                        if db_match:
                            linked_path = db_match.group(1)
                        break
                
                # Cerrar la base de datos DAO
                dao_db.Close()
                dao_engine = None
                
            except Exception:
                # Si falla DAO, intentar con Access COM
                try:
                    # Crear una instancia de Access COM sin mostrar la interfaz
                    access_app = win32com.client.Dispatch("Access.Application")
                    access_app.Visible = False  # No mostrar la interfaz de Access
                    
                    # Abrir la base de datos
                    access_app.OpenCurrentDatabase(db_path, False, password if password else "")
                    
                    # Buscar la tabla vinculada en la colección TableDefs
                    for tbl in access_app.CurrentDb().TableDefs:
                        if tbl.Name == table_name and tbl.Connect:
                            # Es una tabla vinculada, extraer la ruta del Connect string
                            import re
                            connect_str = str(tbl.Connect)
                            db_match = re.search(r'DATABASE=([^;]+)', connect_str)
                            if db_match:
                                linked_path = db_match.group(1)
                            break
                    
                    # Cerrar Access
                    access_app.CloseCurrentDatabase()
                    access_app.Quit()
                    access_app = None
                    
                except Exception:
                    # Si fallan ambos métodos, continuar con la lógica normal
                    pass
            
            try:
                # Intentar acceder a la tabla vinculada con una consulta mínima
                recordset = win32com.client.Dispatch('ADODB.Recordset')
                recordset.Open(f"SELECT TOP 1 * FROM [{table_name}]", conn)
                
                # Si llega aquí, la tabla vinculada es accesible
                print(f"✅ Tabla vinculada '{table_name}' - Accesible")
                print(f"    Ruta: {linked_path}")
                
                for field in recordset.Fields:
                    columns.append((field.Name, field.Type))
                
                # Almacenar con información de tabla vinculada accesible
                db_schema[f"{table_name} (VINCULADA ACCESIBLE - {linked_path})"] = columns
                
            except Exception as e:
                # La tabla vinculada no es accesible
                error_msg = str(e)
                
                # Si no tenemos la ruta de COM, intentar extraerla del error
                if linked_path == "ruta no disponible":
                    import re
                    path_patterns = [
                        r"'([^']+\.accdb)'",  # 'archivo.accdb'
                        r'"([^"]+\.accdb)"',  # "archivo.accdb"
                        r"'([^']+)'",         # cualquier cosa entre comillas simples
                        r'"([^"]+)"'          # cualquier cosa entre comillas dobles
                    ]
                    
                    for pattern in path_patterns:
                        path_match = re.search(pattern, error_msg)
                        if path_match:
                            linked_path = path_match.group(1)
                            break
                
                print(f"⚠️  Tabla vinculada '{table_name}' - NO ACCESIBLE")
                print(f"    Ruta esperada: {linked_path}")
                
                # Agregar información básica de la tabla vinculada al esquema
                columns.append(("Tabla_Vinculada", "LINK"))
                columns.append(("Ruta_Esperada", f"TEXT: {linked_path}"))
                columns.append(("Estado", "TEXT: NO ACCESIBLE"))
                
                # Almacenar con información de tabla vinculada no accesible
                db_schema[f"{table_name} (VINCULADA NO ACCESIBLE - {linked_path})"] = columns
                
            finally:
                try:
                    if recordset and recordset.State == 1:
                        recordset.Close()
                except:
                    pass
                recordset = None
            
        return db_schema, True
    except Exception as e:
        print(f"Ocurrió un error inesperado al usar ADO para obtener el esquema: {e}")
        return None, False
    finally:
        try:
            if tables_rs and tables_rs.State == 1:
                tables_rs.Close()
        except:
            pass
        try:
            if conn and conn.State == 1:
                conn.Close()
        except:
            pass

def get_relationships_from_adox(db_path: str, password: str):
    """
    Se conecta a una base de datos de Access y extrae las relaciones
    utilizando la biblioteca ADOX (ActiveX Data Objects Extensions).

    Args:
        db_path (str): La ruta completa al archivo .accdb.
        password (str): La contraseña de la base de datos.

    Returns:
        list: Una lista de tuplas que describen las relaciones, incluyendo las columnas.
    """
    if not os.path.exists(db_path):
        print(f"Error: El archivo de base de datos no se encontró en '{db_path}'.")
        return []

    relaciones = []
    cat = None
    conn = None

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
                table_name = str(table.Name)
                
                # Evitar tablas de sistema
                if table_name.startswith("MSys"):
                    continue
                    
                try:
                    if table.Keys.Count > 0:
                        for key in table.Keys:
                            try:
                                if key.Type == AD_KEY_FOREIGN and key.RelatedTable:
                                    # Se detecta una clave foránea, lo que indica una relación
                                    foreign_table = table_name
                                    primary_table = str(key.RelatedTable)
                                    
                                    # Recorrer las columnas de la clave para obtener los campos de la relación
                                    for col_idx in range(key.Columns.Count):
                                        try:
                                            foreign_column = str(key.Columns[col_idx].Name)
                                            # Comprobar si RelatedColumn es un objeto o una cadena de texto
                                            related_column_obj = key.Columns[col_idx].RelatedColumn
                                            if isinstance(related_column_obj, str):
                                                primary_column = related_column_obj
                                            else:
                                                primary_column = str(related_column_obj.Name)
                                            relaciones.append((primary_table, foreign_table, primary_column, foreign_column))
                                        except (AttributeError, Exception) as e:
                                            # En caso de que haya un error con los objetos COM,
                                            # se añade la relación sin los nombres de las columnas
                                            print(f"Advertencia: No se pudieron obtener los campos de la relación entre '{foreign_table}' y '{primary_table}'.")
                                            relaciones.append((primary_table, foreign_table, 'N/A', 'N/A'))
                            except Exception as e:
                                # Error específico de clave, continuar con la siguiente
                                continue
                except Exception as e:
                    # Error al acceder a las claves de la tabla, continuar con la siguiente tabla
                    continue
        else:
            print("No se encontraron tablas en la base de datos.")

    except Exception as e:
        error_msg = str(e)
        if "no puede ejecutar la operación solicitada" in error_msg or "cannot perform the requested operation" in error_msg:
            print("Advertencia: No se pudieron extraer relaciones debido a limitaciones del proveedor ADOX.")
            print("Esto puede ocurrir con ciertas versiones de Access o configuraciones de seguridad.")
        else:
            print(f"Advertencia: Ocurrió un error al obtener las relaciones.")
            print(f"Error detallado: {error_msg}")
    finally:
        try:
            if cat:
                cat.ActiveConnection = None
                cat = None
        except:
            pass
        try:
            if conn:
                conn = None
        except:
            pass

    return relaciones

def get_relationships_from_system_tables(db_path: str, password: str):
    """
    Método alternativo para obtener relaciones usando las tablas del sistema de Access.
    Se usa como respaldo cuando ADOX falla.
    
    Args:
        db_path (str): La ruta completa al archivo .accdb.
        password (str): La contraseña de la base de datos.
        
    Returns:
        list: Una lista de tuplas que describen las relaciones.
    """
    if not os.path.exists(db_path):
        return []

    relaciones = []
    conn = None
    
    try:
        # Cadena de conexión OLEDB para archivos .accdb
        conn_str = f"Provider=Microsoft.ACE.OLEDB.12.0;Data Source={db_path};"
        if password:
            conn_str += f"Jet OLEDB:Database Password={password};"
        
        # Crear la conexión COM
        conn = win32com.client.Dispatch('ADODB.Connection')
        conn.Open(conn_str)
        
        # Intentar consultar las tablas del sistema para obtener relaciones
        try:
            recordset = win32com.client.Dispatch('ADODB.Recordset')
            # Esta consulta busca información de relaciones en las tablas del sistema
            query = """
            SELECT MSysRelationships.szRelationship, MSysRelationships.szReferencedObject, 
                   MSysRelationships.szObject, MSysRelationships.szReferencedColumn, 
                   MSysRelationships.szColumn
            FROM MSysRelationships
            WHERE MSysRelationships.szObject IS NOT NULL
            """
            recordset.Open(query, conn)
            
            while not recordset.EOF:
                try:
                    relationship_name = recordset.Fields("szRelationship").Value or "N/A"
                    primary_table = recordset.Fields("szReferencedObject").Value or "N/A"
                    foreign_table = recordset.Fields("szObject").Value or "N/A"
                    primary_column = recordset.Fields("szReferencedColumn").Value or "N/A"
                    foreign_column = recordset.Fields("szColumn").Value or "N/A"
                    
                    if primary_table != "N/A" and foreign_table != "N/A":
                        relaciones.append((primary_table, foreign_table, primary_column, foreign_column))
                except:
                    pass
                recordset.MoveNext()
            
            recordset.Close()
            
        except Exception:
            # Si las tablas del sistema no están disponibles, no es crítico
            pass
            
    except Exception:
        # Falló el método alternativo, retornar lista vacía
        pass
    finally:
        try:
            if conn and conn.State == 1:
                conn.Close()
        except:
            pass
    
    return relaciones

def create_markdown_output(schema, relationships):
    """
    Crea el contenido en formato Markdown para el esquema de la base de datos.
    """
    markdown_content = "# Estructura de la Base de Datos y Relaciones\n\n"
    markdown_content += "Este documento detalla la estructura de la base de datos de Access, incluyendo "
    markdown_content += "sus tablas, columnas y relaciones. Las relaciones se obtuvieron directamente "
    markdown_content += "del esquema de la base de datos.\n\n"

    # Separar tablas normales de tablas vinculadas
    normal_tables = {}
    linked_accessible_tables = {}
    linked_non_accessible_tables = {}
    
    for table_name, columns in schema.items():
        if "(VINCULADA ACCESIBLE" in table_name:
            linked_accessible_tables[table_name] = columns
        elif "(VINCULADA NO ACCESIBLE" in table_name:
            linked_non_accessible_tables[table_name] = columns
        else:
            normal_tables[table_name] = columns

    markdown_content += "## Estructura de Tablas\n\n"
    
    # Primero mostrar las tablas normales
    if normal_tables:
        markdown_content += "### Tablas Locales\n\n"
        for table, columns in sorted(normal_tables.items()):
            markdown_content += f"#### Tabla: `{table}`\n"
            markdown_content += "| Nombre de Columna | Tipo de Dato |\n"
            markdown_content += "|-------------------|--------------|\n"
            for column_name, column_type in sorted(columns):
                # Obtener el nombre del tipo de dato de nuestro diccionario de mapeo
                data_type_str = ADO_DATA_TYPES.get(column_type, f"Tipo_{column_type}")
                markdown_content += f"| `{column_name}` | `{data_type_str}` |\n"
            markdown_content += "\n"
    
    # Mostrar tablas vinculadas accesibles
    if linked_accessible_tables:
        markdown_content += "### Tablas Vinculadas (Accesibles)\n\n"
        markdown_content += "✅ **Las siguientes tablas están vinculadas a bases de datos externas y son accesibles:**\n\n"
        
        for table_full_name, columns in sorted(linked_accessible_tables.items()):
            markdown_content += f"#### Tabla: `{table_full_name}`\n"
            markdown_content += "| Nombre de Columna | Tipo de Dato |\n"
            markdown_content += "|-------------------|--------------|\n"
            for column_name, column_type in sorted(columns):
                data_type_str = ADO_DATA_TYPES.get(column_type, f"Tipo_{column_type}")
                markdown_content += f"| `{column_name}` | `{data_type_str}` |\n"
            markdown_content += "\n"
    
    # Mostrar tablas vinculadas no accesibles
    if linked_non_accessible_tables:
        markdown_content += "### Tablas Vinculadas (No Accesibles)\n\n"
        markdown_content += "⚠️ **Las siguientes tablas están vinculadas a bases de datos externas que no están disponibles:**\n\n"
        
        for table_full_name, columns in sorted(linked_non_accessible_tables.items()):
            markdown_content += f"#### Tabla: `{table_full_name}`\n"
            markdown_content += "| Información | Detalle |\n"
            markdown_content += "|-------------|----------|\n"
            
            for column_name, column_type in columns:
                if column_name == "Tabla_Vinculada":
                    markdown_content += f"| Tipo | Tabla Vinculada |\n"
                elif column_name == "Ruta_Esperada":
                    path_info = str(column_type).replace("TEXT: ", "")
                    markdown_content += f"| Ruta Esperada | `{path_info}` |\n"
                elif column_name == "Estado":
                    estado = str(column_type).replace("TEXT: ", "")
                    markdown_content += f"| Estado | {estado} |\n"
                elif column_name == "Descripcion":
                    desc = str(column_type).replace("TEXT: ", "")
                    markdown_content += f"| Descripción | {desc} |\n"
            markdown_content += "\n"
    
    markdown_content += "## Relaciones entre Tablas\n\n"
    if relationships:
        markdown_content += "Las siguientes relaciones fueron encontradas en el esquema de la base de datos:\n\n"
        for tabla_principal, tabla_relacionada, col_principal, col_relacionada in relationships:
            markdown_content += f"- La tabla `{tabla_relacionada}.{col_relacionada}` se relaciona con `{tabla_principal}.{col_principal}`.\n"
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

    print(f"Procesando base de datos: {args.db_path}")
    
    # Verificar que el archivo existe
    if not os.path.exists(args.db_path):
        print(f"Error: No se encontró el archivo de base de datos en '{args.db_path}'")
        return

    # Obtiene el esquema de la base de datos (tablas y columnas) usando ADO
    print("Extrayendo esquema de tablas...")
    db_schema, schema_success = get_database_schema(args.db_path, args.password)
    
    if not schema_success or not db_schema:
        print("Error: No se pudo obtener el esquema de la base de datos.")
        return

    print(f"Se encontraron {len(db_schema)} tablas en la base de datos.")
    
    # Obtiene las relaciones directamente del esquema usando ADOX
    print("Extrayendo relaciones...")
    relationships = get_relationships_from_adox(args.db_path, args.password)
    
    # Si ADOX falló o no encontró relaciones, intentar método alternativo
    if len(relationships) == 0:
        print("Intentando método alternativo para extraer relaciones...")
        relationships = get_relationships_from_system_tables(args.db_path, args.password)
    
    print(f"Se encontraron {len(relationships)} relaciones en la base de datos.")

    # Crea el contenido Markdown
    print("Generando archivo Markdown...")
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
