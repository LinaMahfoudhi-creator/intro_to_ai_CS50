# Attention

## Description
Ce projet implémente un outil pour visualiser les scores d'attention dans les modèles de langage basés sur des transformateurs. Il utilise un modèle pré-entraîné (BERT) pour générer des prédictions et produit des diagrammes représentant les scores d'attention.

## Fonctionnalités
- Tokenisation des entrées textuelles avec un modèle BERT pré-entraîné.
- Génération de prédictions pour les tokens masqués.
- Visualisation des scores d'attention sous forme de diagrammes graphiques.

## Fichiers
- `mask.py` : Contient l'implémentation principale.

## Instructions
1. Assurez-vous d'avoir Python installé.
2. Installez les dépendances nécessaires :
   ```bash
   pip install tensorflow transformers pillow