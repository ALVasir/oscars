# Oscars
Base de datos con los Ganadores, Nominados, Presentadores y Anecdotario de los Oscars de Hollywood

Este proyecto va sobre un diccionario que contiene datos sobre los Oscars. El diccionario está formado a su vez por 4 diccionarios:

- Ganadores de los Oscars, que será una lista de los años de 2010 a 2024, y cada año será un diccionario con las categorías.
- Nominados a os Oscars, donde lógicamente se incluirá el ganador, pero lo importante es ver todos los que se presentaron, así que seguirá la misma estructura aunque sin los apartados de premios como es obvio.
- Presentadores, que incluirá los maestros de ceremonias y actores que presentaron cada nominación.
- Anecdotario, que como su propio nombre indica será un breve diccionario repasando el evento.

El objetivo de este proyecto es el primer diccionario, o sea, los Ganadores de los Oscars.

La organización se podría plantear de otra forma, pero he elegido esta porque así podría ser un proyecto modular donde cada sección la podría hacer otra persona, o simplemente desarrollar cada una en diferentes etapas.

Estructura del diccionario de diccionarios:

Oscars = {"Ganadores": [lista de años 2010-2024], "Nominados": [lista de años 2010-2024], "Presentadores": [lista de años 2010-2024], "Anécdotas": [lista de años 2010-2024]} 
Años = {"Mejor Película": {diccionario con datos}, "Mejor Dirección": {diccionario con datos}, "Mejor Actor": {diccionario con datos}, "Mejor Actriz": {diccionario con datos}

Ejemplo del diccionario con un año:

```python
{
	"Ganadores": [
		2010: {
			"Mejor Película": {
				"Título": "The Hurt Locker",
				"Director": {
					"Nombre": "Kathryn Bigelow",
					"Nacionalidad": "EE.UU."
				},
				"Productores": ["Kathryn Bigelow", "Mark Boal"],
				"Actores Principales": [
					{"Nombre": "Jeremy Renner", "Personaje": "Sargento William James"},
					{"Nombre": "Anthony Mackie", "Personaje": "Sargento J.T. Sanborn"}
				],
				"Premios Ganados": ["Mejor Película", "Mejor Dirección", "Mejor Guión Original"]
			},
			"Mejor Dirección": {
				"Ganador": "Kathryn Bigelow",
				"Película": "The Hurt Locker",
				"Nacionalidad": "EE.UU."
			},
			"Mejor Actor": {
				"Ganador": "Jeff Bridges",
				"Película": "Crazy Heart",
				"Personaje": "Bad Blake"
			},
			"Mejor Actriz": {
				"Ganador": "Sandra Bullock",
				"Película": "The Blind Side",
				"Personaje": "Leigh Anne Tuohy"
			}
		},
		2024: {
		.
		.
		.
		}
	]
}
```
