import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Cargar los datos
datos = pd.read_csv("NoFetal2019.csv", header=0, sep=";")

# Verificar duplicados y generar reporte
duplicados = datos[datos.duplicated()]
print("Valores duplicados encontrados:")
print(duplicados)
# Eliminar duplicados
datos = datos.drop_duplicates()

# Verificar y eliminar filas con valores nulos o faltantes
datos = datos.dropna(subset=["MANERA_MUERTE","COD_MUERTE"])

# Reemplazar valores nulos o faltantes de la columna COD_DANE
datos['COD_DANE'] = datos['COD_DANE'].astype(str)
# Realizar la operación de fillna sin usar inplace
datos['COD_DANE'] = datos['COD_DANE'].fillna(datos['COD_DEPARTAMENTO'].astype(str) + datos['COD_MUNICIPIO'].astype(str))
print (datos)

# Estandarizar la variable Sexo
datos['SEXO'] = datos['SEXO'].replace({'M': 1, 'F': 2})

# Convertir FECHA_DEFUNCION al formato especificado
datos['FECHA_DEFUNCION2'] = pd.to_datetime(datos['FECHA_DEFUNCION2'], format='%d/%m/%y').dt.strftime('%Y-%m-%d')

# Guardar el conjunto de datos limpio en un nuevo archivo de Excel
datos.to_csv("NoFetal2019_limpio.csv", index=False)

# Crear un Histograma con la cantidad de muertes por mes
datos['MES_DEFUNCION'] = pd.to_datetime(datos['FECHA_DEFUNCION2']).dt.month
meses = datos['MES_DEFUNCION'].value_counts().sort_index()
plt.bar(meses.index, meses.values)
plt.xlabel('Mes')
plt.ylabel('Cantidad de muertes')
plt.title('Cantidad de muertes por mes en 2019')
plt.xticks(np.arange(1, 13), ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])
plt.show()