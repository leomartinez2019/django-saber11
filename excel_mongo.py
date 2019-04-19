import xlrd
from saber2017.models import Colegio
from saber2016.models import Colegio16

#archivo1 = "/home/lowenhard/resultados_saber2017b.xlsx"
archivo2 = "/home/lowenhard/resultadosSaber2016a.xlsx"
archivo3 = "/home/lowenhard/resultadosSaber2016b.xls"

def proc(archivo):
    book = xlrd.open_workbook(archivo)
    sheet = book.sheet_by_index(0)
    encabezado = [elem.lower() for elem in sheet.row_values(5)[:14]]
    lista_colegios = []
    inicio = 6
    while True:
        try:
            colegio = sheet.row_values(inicio)[:14]
            diccio = {x: y for x, y in zip(encabezado, colegio)}
            diccio['periodo'] = 2017
            lista_colegios.append(diccio)
            inicio += 1
        except IndexError:
            #print("Se ingresaron {0} datos".format(inicio - 6))
            #print("Último colegio: {0}".format(colegio[1]))
            break
    return lista_colegios
    #print(lista_colegios)

def poblardb(archivo, modelo):
    """
    Ingresa los valores de la hoja de excel a la base
    de datos django
    """
    conteo = 0
    datos = test_proc(archivo)
    for dato in datos[1:]:
        colegio = modelo(**dato)
        colegio.save()
        conteo += 1
    print("Se ingresaron {0} datos".format(conteo))

def test_error(archivo):
    """
    revisa si el archivo se puede abrir y el número de
    filas de la hoja de excel
    """
    book = xlrd.open_workbook(archivo)
    sheet = book.sheet_by_index(0)
    last_row = sheet.nrows
    print("Número de filas: {0}".format(last_row))
    print(sheet.row_values(last_row - 2))

def test_proc(archivo):
    """
    test de correcta lectura y proceso de los datos de excel
    """
    book = xlrd.open_workbook(archivo)
    sheet = book.sheet_by_index(0)
    year_str = sheet.cell(6, 19).value
    if isinstance(year_str, float): # para archivo excel de 2016b
        year_str = sheet.cell(6, 23).value
    year = int(year_str[:-1])
    encabezado = [elem.lower() for elem in sheet.row_values(5)[:14]]
    lista_colegios = []
    inicio = 6
    while True:
        try:
            colegio = sheet.row_values(inicio)[:14]
            diccio = {x: y for x, y in zip(encabezado, colegio)}
            diccio['periodo'] = year
            diccio['evaluados'] = int(diccio['evaluados'])
            lista_colegios.append(diccio)
            inicio += 1
        except IndexError:
            print("Se ingresaron {0} datos".format(inicio - 6))
            print("Último colegio: {0}".format(colegio[1]))
            break
    return lista_colegios
    #print(lista_colegios)
