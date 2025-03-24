import os


def opcion1(cabecera, diccionario):
# 1. Listado de todas las películas ganadoras indicando su categoría y el año
    os.system('cls')
    print(cabecera)
    print("\nLISTADO COMPLETO DE PELÍCULAS GANADORAS DE LOS OSCARS\n")
    print(f"{'Año':<5} | {'Categoría':<20} | {'Película Ganadora':<45} | {'Ganador/a'}")
    print("-" * 100)
    
    categoriasl_premiadas = ['Mejor Pelicula','Mejor Director','Mejor Actor','Mejor Actriz','Mejor Actor de Reparto','Mejor Actriz de Reparto']
    
    for anyodicc in diccionario["Ganadores"]:
        for anyo, categorias in anyodicc.items():
            for categoria, datos in categorias.items():
                if categoria in categoriasl_premiadas:
                    if categoria == 'Mejor Pelicula':
                        pelicula = datos.get('Titulo', 'Desconocido')
                        ganador = datos.get('Director', {}).get('Nombre', 'Desconocido')
                    else:
                        pelicula = datos.get('Pelicula', 'Desconocido')
                        ganador = datos.get('Ganador', datos.get('Ganadora', 'Desconocido'))
                    
                    print(f"{anyo:<5} | {categoria:<20} | {pelicula:<45} | {ganador}")
    
    input("\n< presione ENTER para volver al MENÚ >")

def opcion2(cabecera, diccionario):
# 2. Lista las películas de Reino Unido e indica cuántas son
    os.system('cls')
    print(cabecera)
    print("\nPELÍCULAS DEL REINO UNIDO GANADORAS DE OSCARS\n")
    
    peliculas_uk = []
    
    for anyodicc in diccionario["Ganadores"]:
        for anyo, categorias in anyodicc.items():
            if "Mejor Pelicula" in categorias:
                pelicula = categorias["Mejor Pelicula"]
                nacionalidad = pelicula["Director"].get("Nacionalidad", "")
                
                if nacionalidad == "Reino Unido":
                    info = {
                        'año': anyo,
                        'titulo': pelicula["Titulo"],
                        'director': pelicula["Director"]["Nombre"],
                        'premios': ", ".join(pelicula.get("Premios Ganados", []))
                    }
                    peliculas_uk.append(info)
    
    if peliculas_uk:
        print(f"{'Año':<5} | {'Película':<35} | {'Director':<25} | {'Premios'}")
        print("-" * 90)
        for pelicula in peliculas_uk:
            print(f"{pelicula['año']:<5} | {pelicula['titulo']:<35} | {pelicula['director']:<25} | {pelicula['premios']}")
        
        print(f"\nTotal de películas del Reino Unido: {len(peliculas_uk)}")
    else:
        print("No se encontraron películas del Reino Unido.")
    
    input("\n< presione ENTER para volver al MENÚ >")
