# Oscars
Base de datos con los Ganadores, Nominados, Presentadores y Anecdotario de los Oscars de Hollywood

Este proyecto va sobre un diccionario que contiene datos sobre los Oscars.

La organización se podría plantear de otra forma, pero he elegido esta porque así podría ser un proyecto modular donde cada sección la podría hacer otra persona, o simplemente desarrollar cada una en diferentes etapas.

Este diccionario contendrá los Ganadores de los Oscars, los Nominados, los Presentadores, y por último el Anecdotario de la ceremonia. Al final es todo un diccionario que contendrá las 4 secciones, y cada sección será un diccionario con su propia estructura.

El objeto de este proyecto es comenzar por los Ganadores.

El de Nominados es parecido pero cada categoria sería una lista para contener cada uno de los nominados, cosa que no ocurre con el de ganadores.

Estructura del diccionario de diccionarios:

Oscars = {"Ganadores": "Años", "Nominados": "Años", "Presentadores: "Años", "Anecdotas": "Años"}

"Ganadores": "Años" <-- este es el objetivo de este proyecto inicial
- Dentro de este diccionario, los años son una lista con los años.
- Cada uno de los años de la lista es un diccionario, que contiene las claves del año y las categorias de ese año.
- Las categorías son un diccionario dividiendo los diferentes premios por categoría, algunas de ellas serían nuevamente un diccionario.

Ejemplo de cómo sería el json para el año 2010:

```python
{
  "Ganadores": [
    "Años" {
        "año": 2010,
        "categorias": {
          "Mejor Película": {
            "titulo": "The Hurt Locker",
            "director": {
              "nombre": "Kathryn Bigelow",
              "nacionalidad": "EE.UU."
            },
            "productores": ["Kathryn Bigelow", "Mark Boal"],
            "actores_principales": [
              { "nombre": "Jeremy Renner", "personaje": "Sargento William James" },
              { "nombre": "Anthony Mackie", "personaje": "Sargento J.T. Sanborn" }
            ],
            "premios_ganados": ["Mejor Película", "Mejor Dirección", "Mejor Guion Original"]
          },
          "Mejor Dirección": {
            "ganador": "Kathryn Bigelow",
            "pelicula": "The Hurt Locker",
            "nacionalidad": "EE.UU."
          },
          "Mejor Actor": {
            "ganador": "Jeff Bridges",
            "pelicula": "Crazy Heart",
            "personaje": "Bad Blake"
          },
          "Mejor Actriz": {
            "ganadora": "Sandra Bullock",
            "pelicula": "The Blind Side",
            "personaje": "Leigh Anne Tuohy"
          }
        }
      }
    ]
  ]
}
```
