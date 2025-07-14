import pandas as pd
from sqlalchemy import create_engine

# Cargar datos desde Excel
datos = pd.read_excel('BD_Consolidado.xls')

# Crear tabla empleados únicos
empleados = datos[['id_agente', 'agente']].drop_duplicates().reset_index(drop=True)

# Crear tabla países únicos
paises = datos[['pais']].drop_duplicates().reset_index(drop=True)
paises['id_pais'] = paises.index + 1
paises = paises[['id_pais', 'pais']]

# Asociar el id del país en el DataFrame principal
datos = datos.merge(paises, on='pais', how='left')

# Conexión a la base de datos MySQL
usuario = 'root'
clave = 'Dragon2307*'
host = 'localhost'
puerto = '3306'
base_datos = 'consolidado'

# Crear conexión
conexion = create_engine(f'mysql+pymysql://{usuario}:{clave}@{host}:{puerto}/{base_datos}')

# Subir tablas
empleados.to_sql('empleados', con=conexion, if_exists='replace', index=False)
paises.to_sql('paises', con=conexion, if_exists='replace', index=False)
datos.to_sql('datos', con=conexion, if_exists='replace', index=False)

print("✅ Tablas 'empleados', 'paises' y 'datos' subidas con éxito a MySQL.")
