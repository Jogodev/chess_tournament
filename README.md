# Projet gestion de tournoi d'échecs

## Cloner le projet


````bash
$ git clone https://github.com/Jogodev/chess_tournament.git
$ cd chess_tournament
````

### Créer l'environnement virtuel

````bash
$ python -m venv env
````

### Activater l'environnement virtuel

#### Windows
````bash
$ . env\scripts\activate 
````
#### Mac
````bash
$ source env\scripts\activate 
````
#### linux
````bash
$ source env\scripts\activate 
````

### Installer les paquets

````bash
$ pip install -r requirements.txt
````

### Lancer le programme

Dans le dossier du programme éxecuter :
````bash
$ python main.py
````

### Rapports flake 8

Se positionner dans le dossier du projet dans le terminal et executer :
````bash
$ flake8 --format=html --htmldir=flake8-report
````