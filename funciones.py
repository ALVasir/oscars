import os
import sys
import json


def opcion1(cabecera,diccionario):
    os.system('clear')
    print(cabecera)
    margen = 15*" "
    regleta = 50*"-"
    print(f'\n{margen}LISTADO DE AÑOS / CATEGORIAS Y PELÍCULAS GANADORAS')
    print(f'{margen}{regleta}\n')
    # sólo las categorías con película
    for anio, categorias in diccionario["Ganadores"].items():
        print(f'{margen}{anio}\n{margen}{regleta}')
        for nombre_categoria, detalles in categorias.items():
            if "Pelicula" in nombre_categoria or "Titulo" in detalles:
                titulo = detalles.get("Titulo", detalles.get("Pelicula", "Desconocido"))
                print(f'{margen}{nombre_categoria}: {titulo}\n')
    # vuelta al menú
    input(f'\n{margen}< presiona ENTER para volver al menú >')


def opcion2(cabecera, diccionario):
    os.system('clear')
    print(cabecera)
    margen = 15*" "
    regleta = 50*"-"
    print(f'\n{margen}PELÍCULAS DE REINO UNIDO GANADORAS DE OSCARS')
    print(f'{margen}{regleta}\n')
    # json incompleto, la nacionalidad la tomo a partir de la del director
    # debo usar una lista para almacenar las películas inglesas, contarlas y listarlas
    contador = 0
    peliculas_uk = []
    # necesito encontrar qué películas son inglesas
    for anio, categorias in diccionario["Ganadores"].items():
        if "Mejor Pelicula" in categorias:
            pelicula = categorias["Mejor Pelicula"]
            director = pelicula.get("Director", {})
            if director.get("Nacionalidad") == "Reino Unido":
                titulo = pelicula.get("Titulo", "Desconocido")
                peliculas_uk.append((anio, titulo))
                contador = contador+1
    # listado de películas inglesas
    for anio, titulo in peliculas_uk:
        print(f'{margen}{anio}: {titulo}')
    # total de películas
    print(f'\n{margen}{regleta}')
    print(f'{margen}TOTAL DE PELÍCULAS: {contador}')
    # vuelta al menú
    input(f'\n{margen}< presiona ENTER para volver al menú >')


def opcion3(cabecera, diccionario):
    os.system('clear')
    print(cabecera)
    margen = 15*" "
    regleta = 50*"-"
    print(f'\n{margen}GANADORES POR AÑO')
    print(f'{margen}{regleta}')
    # entrada de año y control de error
    # si no existe el año vuelve al menú principal
    anio = input(f'{margen}Elige un año para listar (2010-2023): ')
    if anio not in diccionario["Ganadores"]:
        print(f'\n{margen}< no hay datos para el año {anio} >')
        input(f'\n{margen}< presiona ENTER para volver al menú >')
        return
    # listado 
    print(f'\n{margen}GANADORES DEL AÑO {anio}')
    print(f'{margen}{regleta}')
    for categoria, detalles in diccionario["Ganadores"][anio].items():
    # listado según categorías
        if "Ganador" in detalles:
            print(f'{margen}{categoria}: {detalles["Ganador"]} - {detalles.get("Pelicula", "")}')
    # listado según mejor película
        elif "Titulo" in detalles:
            print(f'{margen}{categoria}: {detalles["Titulo"]}')
            print(f'{margen}Director: {detalles["Director"]["Nombre"]}')
    # vuelta al menú
    input(f'\n{margen}< presiona ENTER para volver al menú >')


def opcion4(cabecera, diccionario):
    os.system('clear')
    print(cabecera)
    margen = 15*" "
    regleta = 50*"-"
    print(f'\n{margen}OSCARS DE UN ACTOR/DIRECTOR')
    print(f'{margen}{regleta}')
    # entrada del actor o director
    nombre = input(f'{margen}Dime el nombre del actor o director: ').strip()
    # almacenar las búsquedas en una lista para luego listarla    
    encontrado = False
    resultados = []
    # buscar en todos los años y categorías
    for anio, categorias in diccionario["Ganadores"].items():
        for categoria, detalles in categorias.items():
    # ganador = actor o director > lista
            if "Ganador" in detalles and nombre in detalles["Ganador"]:
                resultados.append({
                    "año": anio,
                    "categoria": categoria,
                    "pelicula": detalles.get("Pelicula", "N/A")
                })
                encontrado = True
    # ganador director en mejor película > lista
            if categoria == "Mejor Pelicula" and "Director" in detalles:
                if nombre in detalles["Director"]["Nombre"]:
                    resultados.append({
                        "año": anio,
                        "categoria": "Director de " + categoria,
                        "pelicula": detalles["Titulo"]
                    })
                    encontrado = True
    # mostrar la lista y control de errores
    if not encontrado:
        print(f'\n{margen}< no hay Oscars para {nombre}')
    else:
        print(f'\n{margen}{nombre} ganó {len(resultados)} Oscar:')
        print(f'{margen}{regleta}')
        for premio in resultados:
            print(f'{margen}{premio["año"]}: {premio["categoria"]} por {premio["pelicula"]}')
    # vuelta al menú
    input(f'\n{margen}< presiona ENTER para volver al menú >')


def opcion5(cabecera, diccionario):
    os.system('clear')
    print(cabecera)
    margen = 15*" "
    regleta = 50*"-"
    print(f'\n{margen}RANKING DE MÁXIMOS GANADORES DE OSCARS')
    print(f'{margen}{regleta}\n')
    # almacenar las búsquedas listas para cada categoría    
    actores = {}
    directores = {}
    peliculas = {}
    # buscar por todos los años y categorías
    for anio, categorias in diccionario["Ganadores"].items():
        for categoria, detalles in categorias.items():
    # contador de actores
            if "Ganador" in detalles and ("Actor" in categoria or "Actriz" in categoria):
                nombre = detalles["Ganador"]
                actores[nombre] = actores.get(nombre,0)+1
    # contador de directores
            if "Ganador" in detalles and "Director" in categoria:
                nombre = detalles["Ganador"]
                directores[nombre] = directores.get(nombre,0)+1
            elif categoria == "Mejor Pelicula" and "Director" in detalles:
                nombre = detalles["Director"]["Nombre"]
                directores[nombre] = directores.get(nombre,0)+1
    # contador de películas
            if "Titulo" in detalles:
                titulo = detalles["Titulo"]
                peliculas[titulo] = peliculas.get(titulo,0)+1
            elif "Pelicula" in detalles:
                titulo = detalles["Pelicula"]
                peliculas[titulo] = peliculas.get(titulo,0)+1
    # actor ganador
    max_actor = ""
    max_actor_premios = 0
    for actor, premios in actores.items():
        if premios > max_actor_premios:
            max_actor = actor
            max_actor_premios = premios
   # director ganador
    max_director = ""
    max_director_premios = 0
    for director, premios in directores.items():
        if premios > max_director_premios:
            max_director = director
            max_director_premios = premios
   # película ganadora
    max_pelicula = ""
    max_pelicula_premios = 0
    for pelicula, premios in peliculas.items():
        if premios > max_pelicula_premios:
            max_pelicula = pelicula
            max_pelicula_premios = premios
    # listado de ganadores
    print(f'{margen}ACTOR CON MÁS OSCARS:')
    print(f'{margen}{max_actor} > {max_actor_premios} premios')
    print(f'{margen}{regleta}')
    print(f'{margen}DIRECTOR CON MÁS OSCARS:')
    print(f'{margen}{max_director} > {max_director_premios} premios')
    print(f'{margen}{regleta}')
    print(f'{margen}PELÍCULA CON MÁS OSCARS:')
    print(f'{margen}{max_pelicula} > {max_pelicula_premios} premios')
    print(f'{margen}{regleta}')
    # vuelta al menú
    input(f'\n{margen}< presiona ENTER para volver al menú >')

