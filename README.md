# Binary-Search-Catalog-Python

# 🛒 Recherche de Code-Produit dans un Catalogue 🔍

## 📌 Description

Ce projet consiste à développer un programme Python permettant à une grande surface de rechercher rapidement un **code-produit** dans un catalogue informatisé.

Le catalogue contient les **codes-produits des articles** sous forme d'entiers et il est toujours maintenu **trié par ordre croissant** afin d'optimiser les recherches.

Pour vérifier l'existence d'un produit, le programme utilise la méthode de **recherche dichotomique** (Binary Search) qui permet une recherche rapide et efficace. ⚡

---

## 🎯 Objectif du projet

L'objectif est de :

✅ Saisir le nombre de codes-produits du catalogue  
✅ Remplir le catalogue avec des codes entiers triés dans l'ordre croissant  
✅ Vérifier qu'un nouveau code respecte l'ordre du catalogue  
✅ Rechercher un code-produit donné par l'utilisateur  
✅ Afficher si le produit existe ou non dans le catalogue  

---

## 🧠 Algorithme utilisé

### 🔎 Recherche dichotomique

La recherche dichotomique fonctionne en divisant le catalogue en deux parties à chaque étape :

1. 📌 Comparer le code recherché avec le code situé au milieu
2. ⬅️ Chercher dans la partie gauche si le code est plus petit
3. ➡️ Chercher dans la partie droite si le code est plus grand
4. ✅ Arrêter lorsque le code est trouvé

Cette méthode est plus rapide qu'une recherche séquentielle pour un grand catalogue.

---

## 🛠️ Technologies utilisées

- 🐍 Python
- 🔢 NumPy
- 📚 Structures utilisées :
  - Tableaux
  - Boucles
  - Conditions
  - Recherche dichotomique

---
