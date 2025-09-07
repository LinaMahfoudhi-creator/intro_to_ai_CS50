### Projet 2 : Degrees of Separation


# Degrees of Separation

## Description
Ce projet permet de trouver le chemin le plus court entre deux acteurs 
dans une base de données de films, en utilisant l'algorithme de recherche en largeur (BFS). 
Il calcule les "degrés de séparation" entre deux personnes.

## Fonctionnalités
- Chargement des données à partir de fichiers CSV.
- Recherche du chemin le plus court entre deux acteurs via leurs collaborations dans des films.
- Affichage des films et des acteurs impliqués dans le chemin trouvé.

## Fichiers
- `degrees.py` : Contient l'implémentation principale.
- `util.py` : Fournit des structures de données pour la recherche (pile, file).
- `small/` et `large/` : Contiennent des exemples de bases de données.

## Instructions
1. Assurez-vous d'avoir Python installé.
2. Placez les fichiers CSV dans le répertoire approprié (`small` ou `large`).
3. Exécutez le fichier `degrees.py` :
   ```bash
   python degrees.py [directory]