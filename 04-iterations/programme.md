# Programme du Cours 04 - Itérations

**Date :** 16/12/2025

---

## Déroulé de la séance

- [ ] rappels + questions discord + questions sur le pendu ?
- [ ] Appel des présences
- [ ] Récupération du cours depuis GitHub - comme d'hab
- [ ] ["parse_graph" - un exercice de parsing de fichier pour construire une
  structure de données évoluée](https://python-exos.info-mines.paris/tps/graph-shortest-path/readme-graph-shortest-path-nb/)  
      cet exercice permet de travailler sur
  - dictionnaire - liste - tuples - set
  - références partagées
  - fichiers - vite fait
- [ ] Cours "Itérations" 
  - [ ] 1/3 boucle `for` et basics itertools: <https://python.info-mines.paris/iterations-1-nb/>
  - [ ] 2/3 compréhensions et expressions génératrices: <https://python.info-mines.paris/iterations-2-nb/>
  - [ ] 3/3 en fonction de l'avancement: fonctions génératrices <https://python.info-mines.paris/generateurs-nb/> (si le temps le permet)
- [ ] TP: [code de Vigenere](vigenere-tp.md)
- [ ] TP: [énumérer les solutions d'un problème combinatoire: le problème des reines](https://python-exos.info-mines.paris/tps/queens/readme-queens-nb/)
- [ ] Devoirs
  - Lire et apprendre le cours, dans le chapitre "syntaxe et instructions", sur les notebooks suivants qui ont été vus en séance mais à 1000 km/h:
    - [ ] syntaxe
    - [ ] présentation du code
    - [ ] affectations
    - [ ] opérateurs
    - [ ] instructions
  - **Préparer 2 questions par personne** → Discord #questions

---

## Récupération du cours - groupe 9

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

## exo `parse_graph`

[seulement première partie `parse_graph`](https://python-exos.info-mines.paris/tps/graph-shortest-path/readme-graph-shortest-path-nb/)



---

## Les slides du cours en ligne

### Version HTML pour navigateur

pour rappel: <https://python.info-mines.paris>

### Récupération des slides (si pas déjà fait)

```bash
git clone https://github.com/flotpython/slides.git
cd slides/notebooks

# et pareil que plus haut pour les mises à jour:
git pull
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

## Cours en ligne - Sections du jour

Rendez-vous sur [python.info-mines.paris](https://python.info-mines.paris) :


### Itérations (1/3)

**Lien :** <https://python.info-mines.paris/iterations-1-nb/>

**Concepts clés :**

- **Boucle for** : itération sur séquences et itérables
- module `itertools` : outils pour combiner itérables, création d'itérateurs complexes

### Itérations (2/3)

**Lien :** <https://python.info-mines.paris/iterations-2-nb/>

**Concepts clés :**

- **Compréhensions** : listes, ensembles, dictionnaires
- **Expressions génératrices** : syntaxe et usage

### Générateurs (itérations 3/3)

**Lien :** <https://python.info-mines.paris/generateurs-nb/>

**Concepts clés :**

- **Fonctions génératrices** : `yield`, état interne, itération paresseuse

---

## TP - Le code de Vigenere

il s'agit d'écrire une fonction de chiffrement et déchiffrement selon le code de Vigenere, qui est une amélioration du code de César.

Voyez l'énoncé dans le fichier [vigenere-tp.md](vigenere-tp.md).

---

## TP - Les reines sur un échiquier

<https://python-exos.info-mines.paris/tps/queens/readme-queens-nb/>

conseils de mise en œuvre:

- télécharger le zip depuis la page du TP
- dézipper localement dans ce dossier - sans doute le mieux est quelque part dans `perso`/
- ouvrir le notebook `reines.ipynb` avec Jupyter Lab

ça peut rester aussi simple que cela; mais si vous voulez faire des choses plus avancées:

- ensuite, comme expliqué dans le notebook, vous pouvez au fur et à mesure déplacer votre code depuis le notebook vers des fichiers `.py` dans le même dossier (et les importer dans le notebook)
- de cette façon vous pouvez à la fois
  - faire tourner votre code dans le notebook
  - et aussi faire tourner les tests depuis le terminal

---

## Notes

_(Espace pour notes pendant le cours)_
