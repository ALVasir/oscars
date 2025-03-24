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





def opcion3():
    import json
 

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
