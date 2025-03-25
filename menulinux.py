# Bibliografia
#   https://docs.python.org/3/library/index.html
#   https://www.codigopiton.com/como-hacer-un-menu-de-usuario-en-python/
#   https://ellibrodepython.com/for-python

# librerias cosmeticas
#   time.sleep(3) segundos de pausa
#   os.system('cls') para Windows ('clear') para Linux
#   os.rename(old,new) para renombrar

import time, os
import json

# importar mis funciones y el fichero de datos

from foscarslinux import *

with open('/home/usuario/Documentos/json/oscars.json','r') as archivo:
    diccionario = json.load(archivo)


# menu principal

# 1. Listado de todas las películas ganadoras indicando su categoría y el año
# 2. Lista las películas de Reino Unido e indica cuántas son
# 3. Pide un año e indica los ganadores por categoria
# 4. Listar los Oscars de un actor/director. Ej: Steven Spielberg ganó x Oscars los años: 2020 con la peli X, 2021 con la peli X
# 5. Listar qué actor o director o película tienen más Oscars y cuantos tienen

cabecera = (f'''
 ░▒▓██████▓▒░ ░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓███████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓████████▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░  \n''')

menuprincipal = (f'''
{42*" "}MENÚ PRINCIPAL
{18*" "}{38*"-"}
{29*" "}Mostrar películas ganadoras [1]
{33*" "}Mostrar películas de UK [2]
{29*" "}Mostrar ganadores según año [3]
{21*" "}Mostrar Oscars de un actor/director [4]
{18*" "}Ranking de Oscars según actor/director [5]
{51*" "}Salir [6]
{18*" "}{38*"-"}''')

os.system('clear')
print(f'{cabecera}\n{menuprincipal}')

# menú de opciones, que se ejecutan en la función foscars.py

salir = False
while not salir:
    os.system('clear')
    print(f'{cabecera}{menuprincipal}')
    opcion=int(input(f'{38*" "}Teclee una opción:  '))
    if opcion == 1:
        opcion1(cabecera,diccionario)
    elif opcion == 2:
        opcion2(cabecera,diccionario)
    elif opcion == 3:
        opcion3(cabecera,diccionario)
    elif opcion == 4:
        opcion4(cabecera,diccionario)
    elif opcion == 5:
        opcion5(cabecera,diccionario)
    elif opcion == 6:
        os.system('clear')
        print(f'{cabecera}{menuprincipal}')
        print(f'{30*" "}> Ha salido del programa <\n')
        salir = True
    else:
        os.system('clear')
        print(f'{cabecera}{menuprincipal}')
        print(f'{35*" "}> opción incorrecta <')
        time.sleep(3)
        os.system('clear')
