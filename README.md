# Projet Refuge
## Installation
1 - Installer les dépendances 
    
    poetry install

2 - Créer un une configuration PyCharm avec Python pointant sur le module refuge_esn81.main

## Base de donnée

1 - Créer une base de donnée nommée "animals"

2 - Modifier l'utilisateur et le mot de passe dans le fichier database/database.py

3 - Modifier l'utilisateur et le mot de passe dans le fichier alembic.ini

4 - Jouer les migrations en lançant la commande

    poetry run alembic upgrade head

## Lancement
1 - Démarrer le serveur de développement FastAPI

    poetry run uvicorn refuge_esn81.main:app --reload --port 9000

2 - La documentation interactive Swagger est disponible à l'adresse suivante : http://localhost:9000/docs
