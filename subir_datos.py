import pandas as pd
from sqlalchemy import create_engine

# Cargar CSVs
datos = pd.read_csv('datos.csv')
empleados = pd.read_csv('empleados.csv')
paises = pd.read_csv('paises.csv')

# Conexión a MySQL
usuario = 'root'
clave = 'Dragon2307*'
host = 'localhost'
puerto = '3306'
base_datos = 'consolidado'

conexion = create_engine(f'mysql+pymysql://{usuario}:{clave}@{host}:{puerto}/{base_datos}')

# Subir tablas
empleados.to_sql('empleados', con=conexion, if_exists='replace', index=False)
paises.to_sql('paises', con=conexion, if_exists='replace', index=False)
datos.to_sql('datos', con=conexion, if_exists='replace', index=False)

print("✅ Tablas cargadas correctamente en MySQL.")

