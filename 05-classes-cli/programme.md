# Programme du Cours 05 - Classes et CLI

**Date :** 06/01/2026

---

## Déroulé de la séance

- [x] Rappel + questions (+ questions discord)
- [x] Appel des présences → `presences.csv`
- [x] Récupération du cours depuis GitHub
- [x] Cours "Classes" - Introduction à la POO (~40 min)
- [x] Cours "argparse/CLI" - Écrire un lanceur (~20 min)
- [x] TP pratique → [tp-cli-api.md](./tp-cli-api.md) (~60 min)
- [ ] Devoirs
  - Terminer le TP si non fini
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

## Cours en ligne - Sections du jour

Rendez-vous sur [python.info-mines.paris](https://python.info-mines.paris) :

### 1. Classes : exemples

**Lien :** <https://python.info-mines.paris/classes-exemples-nb/>

**Concepts clés :**

- **Définir un nouveau type** avec `class`
- **Constructeur** `__init__(self, ...)` : initialise les attributs
- **Afficheur** `__repr__(self)` : représentation textuelle de l'objet
- **Méthodes** : fonctions qui s'appliquent sur un objet (`self`)
- **Attributs** : données stockées dans l'objet (`self.name`, `self.age`)

**Exemples du cours :**

- `User` : classe simple avec nom et âge
- `Stack` : pile FILO avec push/pop
- `Point` : coordonnées x, y avec méthode distance
- `Circle` : cercle avec centre et rayon
- `Student` : données étudiant avec calcul d'âge

**Points importants :**

```python
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}, {self.age} ans"

# Utilisation
user1 = User("Lambert", 25)
print(user1)  # Lambert, 25 ans
```

### 2. Écrire un lanceur (argparse)

**Lien :** <https://python.info-mines.paris/argparse-nb/>

**Concepts clés :**

- **`sys.argv`** : accès direct aux arguments (déconseillé sauf cas trivial)
- **`argparse`** : module standard pour parser les arguments proprement
- **Arguments positionnels** : obligatoires, dans l'ordre
- **Options** : commencent par `-` ou `--`, facultatives

**Pourquoi argparse ?**

- Génération automatique de l'aide (`--help`)
- Validation des arguments
- Gestion propre des options courtes (`-v`) et longues (`--verbose`)
- Code lisible et maintenable

**Exemple minimal :**

```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Mon programme")
    parser.add_argument("nombre", type=int, help="un entier")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="mode bavard")

    args = parser.parse_args()

    if args.verbose:
        print(f"Le nombre est {args.nombre}")
    else:
        print(args.nombre)

if __name__ == "__main__":
    main()
```

**Utilisation :**

```bash
python mon_script.py 42           # Affiche: 42
python mon_script.py -v 42        # Affiche: Le nombre est 42
python mon_script.py --help       # Affiche l'aide
```

---

## TP - CLI avec appel API

Mise en pratique combinée des classes et argparse :

- Créer une CLI qui interroge une API REST
- Utiliser des classes pour modéliser les données
- Gérer les erreurs réseau proprement

**Focus pédagogique :**

- Combinaison classes + argparse + requests
- Séparation des responsabilités (parsing, API, affichage)
- Gestion d'erreurs

➜ Voir [tp-cli-api.md](./tp-cli-api.md) pour les détails

---

## Ressources complémentaires

- **Classes** : <https://python.info-mines.paris/classes-exemples-nb/>
- **Méthodes spéciales** : <https://python.info-mines.paris/dunder-specials-nb/>
- **argparse tutorial** : <https://docs.python.org/3/howto/argparse.html>
- **Module requests** : <https://requests.readthedocs.io/>

---

## Notes

_(Espace pour notes pendant le cours)_
