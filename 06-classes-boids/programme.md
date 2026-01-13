# Programme du Cours 06 - Classes : héritage & boids

**Date :** 13/01/2026

---

## Déroulé de la séance

- [ ] Rappel + questions (+ questions discord)
- [ ] Appel des présences → `presences.csv`
- [ ] Récupération du cours depuis GitHub
- [ ] Cours "Attributs & Héritage" (~30 min)
- [ ] TP pratique Boids (~90 min) → [tp-boids/README-boids-nb.md](./tp-boids/README-boids-nb.md)
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

### 1. Attributs & Héritage (obligatoire)

**Lien :** <https://python.info-mines.paris/attributes-inheritance-nb/>

**Concepts clés :**

- **Espaces de noms** : modules, classes et instances sont chacun un espace de nom
- **Variables vs attributs** : liaison lexicale (code) vs liaison dynamique (runtime)
- **Résolution d'attributs** :
  - Écriture : directement dans l'espace de nom de l'objet
  - Lecture : recherche de bas en haut (instance → classe → super-classes)
- **Héritage** : `class B(A):` - B hérite des attributs de A
- **`super()`** : appeler la méthode de la classe parente
- **`isinstance()`** et **`issubclass()`** : vérifier les types

**Exemple clé - Héritage :**

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Appelle Animal.__init__
        self.breed = breed

    def speak(self):  # Redéfinition (override)
        return "Woof!"

dog = Dog("Rex", "Berger")
print(dog.name)   # Rex (hérité de Animal)
print(dog.speak()) # Woof! (redéfini dans Dog)
```

**Points importants :**

- Les classes ont généralement des **méthodes** comme attributs
- Les instances ont généralement des **données** comme attributs
- `super()` évite de coder en dur le nom de la classe parente

### 2. Cours optionnels (si temps disponible)

Ces sections seront vues en fonction du temps restant :

#### Le modèle est flexible

**Lien :** <https://python.info-mines.paris/flexible-model-nb/>

- Attributs de classe vs attributs d'instance
- Méthodes de classe (`@classmethod`)
- Méthodes statiques (`@staticmethod`)

#### Properties

**Lien :** <https://python.info-mines.paris/properties-nb/>

- Le décorateur `@property`
- Créer des getters/setters pythoniques

#### Enums et Dataclasses

**Lien :** <https://python.info-mines.paris/enums-dataclasses-nb/>

- `Enum` : définir des constantes nommées
- `@dataclass` : simplifier la création de classes de données

---

## TP - Simulation des Boids

### Objectif

Créer une simulation de "boids" (oiseaux artificiels) avec la librairie `arcade`.

Ce TP illustre la **programmation par spécialisation de classes** : on hérite des classes fournies par `arcade` pour créer notre propre logique de jeu.

### Préparation

**Important : Travaillez dans un dossier `perso` !**

```bash
cd 06-classes-boids/tp-boids
mkdir perso
cd perso
```

#### 1. Installer la librairie arcade

```bash
uv add arcade
```

#### 2. Copier les fichiers nécessaires

```bash
# Copier le starter code
cp ../boids-01.py .

# Copier le dossier media
cp -r ../media .
```

Ou téléchargez directement le zip : [ARTEFACTS-boids.zip](./tp-boids/ARTEFACTS-boids.zip)

### Instructions du TP

➜ Voir [tp-boids/README-boids-nb.md](./tp-boids/README-boids-nb.md) pour les détails complets

### Résumé des étapes

| Version | Objectif |
|---------|----------|
| v01 | Starter code - un boid immobile |
| v02 | Utiliser `SpriteList` pour plusieurs boids |
| v03 | Faire avancer le boid (hériter de `Sprite`) |
| v04 | Circuit fermé (wrapping) |
| v05 | Ajouter du bruit sur la direction |
| v06 | Contrôle clavier (← →) |
| v07 | Ajouter un obstacle |
| v08 | Grille d'obstacles |
| v09 | Détecter les voisins |
| v10 | **Règle de séparation** (objectif principal) |
| v11+ | Améliorations optionnelles |

### Focus pédagogique

- **Héritage** : créer `class Boid(Sprite)` et `class Obstacle(Sprite)`
- **`super().__init__()`** : initialiser correctement les classes parentes
- **Redéfinition de méthodes** : override de `update()` pour le comportement
- **Programmation par acteurs** : chaque entité adapte son comportement localement

---

## Ressources complémentaires

- **Attributs & héritage** : <https://python.info-mines.paris/attributes-inheritance-nb/>
- **Modèle flexible** : <https://python.info-mines.paris/flexible-model-nb/>
- **Properties** : <https://python.info-mines.paris/properties-nb/>
- **Enums & dataclasses** : <https://python.info-mines.paris/enums-dataclasses-nb/>
- **Librairie arcade** : <https://api.arcade.academy/>
- **Tutoriel arcade** : <https://realpython.com/arcade-python-game-framework/>
- **Vidéo du TP** : <https://www.youtube.com/watch?v=d4789cBD3Ek>

---

## Notes

_(Espace pour notes pendant le cours)_
