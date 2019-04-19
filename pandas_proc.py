import pandas as pd

archivo = "/home/lowenhard/Clasificaci_n_De_Planteles_2016-2_Grado_11.csv"

# Para cambiar nombres de columnas en pandas:
columns={
    'Tipo': 'tipo',
    'Municipio': 'municipio',
    'Sector': 'sector',
    'Evaluados (últimos 3 años)': 'evaluados',
    'Matriculados (últimos 3 años)': 'matriculados',
    'Índice de Matemática': 'matematicas',
    'Índice de Lectura Crítica': 'lectura',
    'Índice de Ciencias Naturales': 'ciencias',
    'Índice de Sociales y Ciudadanas': 'sociales',
    'Índice de Inglés': 'ingles',
    'Índice Total': 'total',
    'Código Dane': 'codigo_dane',
    'Nombre del Establecimiento': 'nombre',
    'Clasificación': 'clasificacion'
}

def test1():
    'convierte csv en dataframe y luego en lista de diccionarios'
    data = pd.read_csv(archivo, dtype={'Código Dane': object})
    data = data.rename(columns=columns)
    data.evaluados.fillna(0, inplace=True)
    data.matriculados.fillna(0, inplace=True)
    data.evaluados = data.evaluados.astype(int)
    data.matriculados = data.matriculados.astype(int)
    # Esta es la lista que luego valos a ingresar a la base de datos
    lista = data.to_dict(orient='records')
    print(lista[203])
    print(len(lista))
    print(lista[23].keys())
    assert len(lista) == 11105


def get_data():
    'get data ready to populate database'
    data = pd.read_csv(archivo, dtype={'Código Dane': object})
    data = data.rename(columns=columns)
    data.evaluados.fillna(0, inplace=True)
    data.matriculados.fillna(0, inplace=True)
    data.evaluados = data.evaluados.astype(int)
    data.matriculados = data.matriculados.astype(int)
    # Esta es la lista que luego valos a ingresar a la base de datos
    lista = data.to_dict(orient='records')
    return lista

#print(get_data()[1830])
#print(get_data()[9537])
#print(len(get_data()))
