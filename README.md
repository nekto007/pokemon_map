# Pokémon map

![screenshot](https://dvmn.org/filer/canonical/1563275070/172/)

### Subject Area

A site to help with the game [Pokemon GO](https://www.pokemongo.com/en-us/). This is a game about catching [Pokemon](https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%BA%D0%B5%D0%BC%D0%BE%D0%BD).

The essence of the game is that pokemons periodically appear on the map, for a certain period of time. Each player can catch a pokemon, and add to his personal collection.

There can be several individuals of the same pokémon on the map at once: for example, 3 Bulbasaurus. Each individual can be caught by several players at once. If a player catches a pokémon specimen, it disappears for him, but remains for others.

The game has an evolution mechanic. Pokémon of one species can "evolve" into another. For example, Bulbasaurus evolves into Ivesaurus, which evolves into Venusaurus.

![bulba evolution](https://dvmn.org/filer/canonical/1562265973/167/)

Translated with www.DeepL.com/Translator (free version)

## Setup

1. Clone project
```bash
git clone https://github.com/nekto007/pokemon_map.git
cd pokemon_map
```
2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install requirements

```bash
pip install -r requirements.txt
```

4. Create database

```bash
python manage.py migrate
```

5. Create Django superuser

```bash
python manage.py createsuperuser
```

6. Run local server

```bash
python manage.py runserver
```

## Work

1. Open `Pokemon map` at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

2. Open `admin` panel if needed at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Project Objectives

The code is written for educational purposes - it is a lesson in a course on Python and web development at [Devman](https://dvmn.org).
