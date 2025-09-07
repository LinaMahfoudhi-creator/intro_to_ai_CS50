# Crossword

## Description
Ce projet implémente un solveur de mots croisés utilisant des techniques d'optimisation. 
Le programme génère un puzzle de mots croisés basé sur une structure donnée et un ensemble de mots, 
en respectant les contraintes d'intersection.

## Fonctionnalités
- Lecture de la structure du puzzle et de la liste de mots à partir de fichiers.
- Représentation des variables (mots) avec leurs positions, directions et longueurs.
- Détection des chevauchements entre les mots.
- Résolution du puzzle en assignant des mots aux variables tout en respectant les contraintes.

## Fichiers
- `crossword.py` : Contient l'implémentation principale.

## Instructions
1. Assurez-vous d'avoir Python installé.
2. Préparez un fichier pour la structure du puzzle (ex. `structure.txt`) et un fichier contenant les mots (ex. `words.txt`).
3. Exécutez le fichier `generate.py` :
   ```bash
   python crossword.py structure.txt words.txt