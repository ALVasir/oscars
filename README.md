# Oscars
Base de datos con los Ganadores, Nominados, Presentadores y Anecdotario de los Oscars de Hollywood

Este proyecto va sobre un diccionario que contiene datos sobre los Oscars. El diccionario está formado a su vez por 4 diccionarios:

- Ganadores de los Oscars, que será una lista de los años de 2010 a 2023, y cada año será un diccionario con las categorías.
- Nominados a os Oscars, donde lógicamente se incluirá el ganador, pero lo importante es ver todos los que se presentaron, así que seguirá la misma estructura aunque sin los apartados de premios como es obvio.
- Presentadores, que incluirá los maestros de ceremonias y actores que presentaron cada nominación.
- Anecdotario, que como su propio nombre indica será un breve diccionario repasando el evento.

El objetivo de este proyecto es el primer diccionario, o sea, los Ganadores de los Oscars.

La organización se podría plantear de otra forma, pero he elegido esta porque así podría ser un proyecto modular donde cada sección la podría hacer otra persona, o simplemente desarrollar cada una en diferentes etapas.

La nacionalidad de la película la cogerá de la nacionalidad del director, cuando lo correcto sería la de los productores, pero no se incluía este dato en mi json.

Ejemplo del diccionario con el primer y último año:

```python

{
    "Ganadores": {
        "2010": {
            "Mejor Pelicula": {
                "Titulo": "The Hurt Locker",
                "Director": {
                    "Nombre": "Kathryn Bigelow",
                    "Nacionalidad": "EE.UU."
                },
                "Productores": ["Kathryn Bigelow", "Mark Boal"],
                "Actores Principales": [
                    {"Nombre": "Jeremy Renner", "Personaje": "Sargento William James"},
                    {"Nombre": "Anthony Mackie", "Personaje": "Sargento J.T. Sanborn"}
                ],
                "Premios Ganados": ["Mejor Pelicula", "Mejor Director", "Mejor Guion Original"]
            },
            "Mejor Director": {
                "Ganador": "Kathryn Bigelow",
                "Pelicula": "The Hurt Locker",
                "Nacionalidad": "EE.UU."
            },
            "Mejor Actor": {
                "Ganador": "Jeff Bridges",
                "Pelicula": "Crazy Heart",
                "Personaje": "Bad Blake"
            },
            "Mejor Actriz": {
                "Ganador": "Sandra Bullock",
                "Pelicula": "The Blind Side",
                "Personaje": "Leigh Anne Tuohy"
            }
        },
...
...
...
        "2023": {
            "Mejor Pelicula": {
                "Titulo": "Oppenheimer",
                "Director": {
                    "Nombre": "Christopher Nolan",
                    "Nacionalidad": "Reino Unido"
                },
                "Productores": ["Emma Thomas", "Charles Roven"],
                "Actores Principales": [
                    { "Nombre": "Cillian Murphy", "Personaje": "J. Robert Oppenheimer" },
                    { "Nombre": "Robert Downey Jr.", "Personaje": "Lewis Strauss" }
                ],
                "Premios Ganados": ["Mejor Pelicula", "Mejor Director", "Mejor Actor (Cillian Murphy)", "Mejor Actor de Reparto (Robert Downey Jr.)"]
            },
            "Mejor Director": {
                "Ganador": "Christopher Nolan",
                "Pelicula": "Oppenheimer",
                "Nacionalidad": "Reino Unido"
            },
            "Mejor Actor": {
                "Ganador": "Cillian Murphy",
                "Pelicula": "Oppenheimer",
                "Personaje": "J. Robert Oppenheimer"
            },
            "Mejor Actriz": {
                "Ganador": "Emma Stone",
                "Pelicula": "Poor Things",
                "Personaje": "Bella Baxter"
            }
        }
    }
}

```
