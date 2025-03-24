import os

def opcion1(cabecera,diccionario):
# Listado de películas ganadoras, tanto de USA como extrajeras
    os.system('cls')
    print(cabecera)
    for anyo in diccionario["Oscars"]:
        for categoria, detalle in anyo["categorias"].items():
            if categoria.lower() == "mejor película":  # Filtrar solo ganadores de "Mejor Película"
                # Extraer nombre de la película y nacionalidad
                pelicula = detalle["titulo"] if isinstance(detalle, dict) else detalle
                nacionalidad = detalle.get("nacionalidad", "Desconocida") if isinstance(detalle, dict) else "Desconocida"
                
                # Determinar si es de EE.UU. o extranjera
                origen = "EE.UU." if "EE.UU." in nacionalidad else "Extranjera"

                print(f"Año {anyo['año']}: {pelicula} - {origen}")

# def opcion1(cabecera,diccionario):
# # Listado de películas ganadoras de USA y extrajeras, ordenadas por años
#     os.system('cls')
#     print(cabecera)
#     for anio in diccionario["Oscars"]:
#         for categoria, detalle in anio["categorias"].items():
#             if categoria.lower() == "mejor película":  # Filtrar solo ganadores de "Mejor Película"
#                 # Extraer nombre de la película y nacionalidad
#                 pelicula = detalle["titulo"] if isinstance(detalle, dict) else detalle
#                 nacionalidad = detalle.get("nacionalidad", "Desconocida") if isinstance(detalle, dict) else "Desconocida"
                
#                 # Determinar si es de EE.UU. o extranjera
#                 origen = "EE.UU." if "EE.UU." in nacionalidad else "Extranjera"

#                 print(f"Año {anio['año']}: {pelicula} - {origen}")



def opcion3():
    import json
 
    # Opening JSON file
    f = open('/media/usuario/SanDisk/A S I R/LENGUAJES/JSON/proyecto/oscars.json','r')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for i in data:
        print(i)
    
    # Closing file
    f.close()

def opcion4(diccionario):
   for año in diccionario["Oscars"]["años"]:
    print(f"\n🏆 Año {año['año']}")
    print("=" * 40)
    
    for categoria, detalle in año["categorias"].items():
        print(f"{categoria} →", end=" ")
        if isinstance(detalle, dict):
            if "ganador" in detalle:
                print(detalle["ganador"], "-", detalle["pelicula"])
            elif "ganadora" in detalle:
                print(detalle["ganadora"], "-", detalle["pelicula"])
            elif "titulo" in detalle:
                print(detalle["titulo"])
        else:
            print(detalle)