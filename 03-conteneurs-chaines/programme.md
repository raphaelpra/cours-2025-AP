# Programme du Cours 03 - Conteneurs et chaînes

**Date :** 09/12/2025

---

## Déroulé de la séance

- [ ] Rappel + questions
- [ ] Appel des présences → `presences.csv`
- [ ] Récupération du cours depuis GitHub
- [ ] **Correction Ex2 - Chiffre de César** → Au tableau (~20 min)
- [ ] Cours "Conteneurs" - Listes, tuples, dictionnaires, sets (~30 min)
- [ ] Cours "Chaînes de caractères" - Slicing, méthodes, formatage (~20 min)
- [ ] TD pratique → [td-pendu.md](./td-pendu.md) (~60 min)
- [ ] Devoirs
  - Lire et apprendre le cours sur les fichiers → <https://python.info-mines.paris/files-nb/>
  - Lire et apprendre le cours sur les références → <https://python.info-mines.paris/references-nb/>
  - **Préparer 2 questions par personne** → Discord #questions

---

## Récupération du cours

### Mise à jour avant chaque cours

```bash
cd cours-2025-AP

# Pour voir s'il y a des changements
git status

# Si le git status renvoie des modifs que vous souhaitez `mettre de coté`
git stash

git pull
```

➜ Vos fichiers `perso*` sont automatiquement ignorés par git (pas de conflits)

---

## Slides du cours

### Récupération des slides (si pas déjà fait)

```bash
git clone https://github.com/flotpython/slides.git
cd slides/notebooks
```

### Lancement avec Jupyter Lab

```bash
cd slides/notebooks
jupyter lab
```

➜ Une fenêtre de navigateur s'ouvrira automatiquement
➜ Clic droit sur un fichier → "Open with → Notebook"
➜ Terminez avec `File -> Shut Down` pour libérer le terminal

---

## Correction Ex2 - Chiffre de César

**Format :** Correction au tableau (live coding)

**Durée :** ~20 min

**Objectif :** Transition depuis cours 02 vers conteneurs/chaînes

**Points abordés :**
- Itération sur strings (caractère par caractère)
- Construction progressive : liste temporaire + `.join()`
- Méthodes de strings : `.isupper()`, `.islower()`, `.isalpha()`
- Conversions ASCII : `ord()` / `chr()`
- Opérateur modulo `%` pour décalage circulaire

**Questions de discussion :**
- Pourquoi liste + join plutôt que concaténation directe ?
- String immuable vs liste mutable
- Complexité O(n) vs O(n²)

➜ Cette correction introduit naturellement les concepts de manipulation de chaînes et construction de conteneurs

---

## Cours en ligne - Sections du jour

Rendez-vous sur [python.info-mines.paris](https://python.info-mines.paris) :

### 1. Conteneurs (1/2)

**Lien :** <https://python.info-mines.paris/containers-1-nb/>

**Concepts clés :**

- **Listes** : Structures dynamiques, taille variable, modification en place
- **Tuples** : Séquences immuables, hashables (utilisables comme clés de dictionnaires)
- **Range** : Génération efficace de séquences numériques

**Opérations importantes :**

- Indexation et slicing avec modification
- Méthodes : `append()`, `pop()`, `extend()`, `insert()`, `sort()`, `reverse()`
- Affectation par slices : `L[i:j] = L2`

### 2. Séquences et chaînes

**Lien :** <https://python.info-mines.paris/sequences-str-nb/>

**Concepts clés :**

- **Slicing avancé** : `S[i:j:k]`, indices négatifs, comportement permissif
- **Méthodes de manipulation** : `strip()`, `split()`, `join()`, `replace()`, `find()`
- **Formatage** : f-strings, insertion dynamique de valeurs
- **Littéraux** : Quotes multiples, raw strings, escape sequences

---

## TD - Jeu du pendu en TUI

Mise en pratique des conteneurs et chaînes via un projet ludique :

- Version facile : Mot prédéfini, affichage ASCII basique
- Version avancée : Dictionnaire de mots aléatoires, scoring, interface améliorée

**Focus pédagogique :** Choix des structures de données (list vs set vs dict) et itérations appropriées

➜ Voir [td-pendu.md](./td-pendu.md) pour les détails

---

## Notes

_(Espace pour notes pendant le cours)_
