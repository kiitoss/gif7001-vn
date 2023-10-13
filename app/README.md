# FastAPI

## Introduction

Ce document vous montre comment utiliser **FastAPI** pour créer une API RESTful.

## Présentation

**FastAPI** est un framework Web moderne, rapide (hautes performances) et rapide à créer avec Python 3.6+ basé sur des types (par exemple, il sait que `name` ci-dessus est une chaîne de caractères et que `age` est un entier).

Les performances sont si élevées que FastAPI est utilisé par des sociétés telles que Microsoft, Netflix, Uber, etc.

FastAPI est également livré avec un système de documentation automatique interactif, qui vous permet de tester vos points de terminaison à partir du navigateur.

FastAPI est basé sur Starlette et Pydantic.

## Prérequis

La première étape consiste à installer FastAPI. Dans votre terminal, exécutez :

```bash
$ pip install fastapi
```

Installez également `uvicorn` pour qu'il fonctionne comme serveur :

```bash
$ pip install uvicorn
```

Et la même chose pour chacune des dépendances du projet (exemple: ZBar) :
```bash
$ pip install pyzbar
```

---

## Bien débuter

Pour démarrer le serveur, exécutez la commande suivante :

```bash
$ python3 main.py
```

Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
Started reloader process [28720]
Started server process [28722]
Waiting for application startup.
Application startup complete.
```

---

## En savoir plus

Pour en apprendre davantage, consultez [la documentation officielle de FastAPI](https://fastapi.tiangolo.com/fr/).

---