# TP Agar.io - Développement progressif d'un jeu

Le but de ce TP est de réaliser un petit jeu en Python inspiré de [agar.io](https://agar.io).

L'objectif pédagogique est de vous apprendre à **concevoir et réaliser un programme complet**, pas de créer le nouveau best-seller. Gardez en tête que votre but est de réaliser un **programme qui marche** et non un programme parfait.

Ce TP vous guidera à travers plusieurs versions successives du jeu, de la fenêtre de base jusqu'à un jeu fonctionnel avec déplacement et carte scrollable.

---

## 📚 Ressources Pygame essentielles

Avant de commencer, prenez connaissance de ces ressources que vous utiliserez tout au long du TP :

**Documentation officielle :**
- [Guide de démarrage Pygame](https://www.pygame.org/wiki/GettingStarted)
- [pygame.display - Gestion de la fenêtre](https://www.pygame.org/docs/ref/display.html)
- [pygame.draw - Dessiner des formes](https://www.pygame.org/docs/ref/draw.html)
- [pygame.event - Gestion des événements](https://www.pygame.org/docs/ref/event.html)
- [pygame.mouse - Gestion de la souris](https://www.pygame.org/docs/ref/mouse.html)
- [pygame.math.Vector2 - Calculs vectoriels](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2)
- [pygame.color - Couleurs prédéfinies](https://www.pygame.org/docs/ref/color_list.html)

**Tutoriels recommandés :**
- [Real Python - PyGame: A Primer](https://realpython.com/pygame-a-primer/)

---

## Philosophie du TP

- **Progression par étapes** : chaque version ajoute une fonctionnalité
- **Commits réguliers** : faites un commit git après chaque version fonctionnelle
- **Code qui marche** : privilégiez la fonctionnalité à la perfection
- **Apprentissage itératif** : vous améliorerez votre code au fur et à mesure

**Important** : Tout au long du TP, nous allons travailler sur un **fichier unique** `agario.py`, que vous allez modifier au fur et à mesure.

---

## Prérequis

### Installation de `uv`

Ce TP utilise **uv**, un gestionnaire d'environnement Python moderne et rapide. Si vous ne l'avez pas encore installé, référez-vous au fichier [uv.md](../uv.md) dans le cours.

Vérifiez votre installation :

```bash
uv --version
```

### Configuration du projet

Créez et configurez un nouveau projet avec `uv` :

```bash
# Créer un nouveau projet
uv init tp-agario
cd tp-agario

# Ajouter pygame comme dépendance
uv add pygame
```

Cette commande va :
- Créer un environnement virtuel `.venv`
- Installer `pygame` et ses dépendances
- Créer/mettre à jour le fichier `pyproject.toml`

### Test de l'installation

Pour vérifier que pygame fonctionne correctement :

```bash
uv run python -m pygame.examples.aliens
```

Soyez patient lors du premier lancement, la librairie initialise de nombreux composants.

---

## Configuration VS Code

### Extension Python

Il est **fortement recommandé** d'installer l'extension Python pour VS Code.

### Sélectionner l'interpréteur

Indiquez à VS Code d'utiliser l'environnement virtuel créé par `uv` :

1. Cliquez dans la barre de statut (en bas) sur la zone indiquant le Python courant
2. Sélectionnez l'interpréteur dans `.venv`

![](media/vscode-which-python.png)

### Terminal intégré

Pour lancer votre programme directement depuis VS Code :

1. Ouvrir la palette de commandes : `⇧ ⌘ P` (Mac) ou `⇧ ⌃ P` (Windows/Linux)
2. Chercher **"Python: Create Terminal"**
3. Dans ce terminal : `uv run python agario.py`

### Qualité du code

VS Code indique en temps réel les problèmes dans votre code. Regardez la zone en bas à gauche.

![](media/vscode-problems.png)

---

## ⚠️ Note importante

**NE PAS exécuter ce code depuis un notebook Jupyter** (ni nbhosting, ni Colab, ni local).

Utilisez toujours un terminal classique avec `uv run python agario.py`.

---

## Version 0 : Code de démarrage

Créez un fichier `agario.py` avec le code suivant :

```python
# v0 : on repeint l'écran à une période de 1 seconde

#!/usr/bin/env python
import pygame as pg
from random import randint


def main():
    clock = pg.time.Clock()

    # on initialise pygame et on crée une fenêtre de 640x640 pixels
    pg.init()
    screen = pg.display.set_mode((640, 640))

    # On donne un titre à la fenetre
    pg.display.set_caption("agario")

    # La boucle du jeu
    done = False
    while not done:
        clock.tick(1)

        # on génère une couleur (Rouge, Vert, Bleu) au hasard
        random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
        screen.fill(random_color)

        # enfin on met à jour la fenêtre avec tous les changements
        pg.display.update()

        # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
        # ici donc tous les évènements survenus durant la seconde précédente
        for event in pg.event.get():
            continue

    pg.quit()


# if python says run, then we should run
if __name__ == "__main__":
    main()
```

### Lancer le programme

```bash
uv run python agario.py
```

Vous devriez voir une fenêtre qui change de couleur chaque seconde. **Problème** : vous ne pouvez pas fermer la fenêtre normalement !

### 💡 Point technique : `pg.display.update()`

C'est l'appel à `pg.display.update()` qui produit réellement l'affichage à l'écran.

Tous les autres calculs (dessiner des formes, remplir l'écran) se produisent en mémoire (très rapide), mais parler à la carte graphique est beaucoup plus lent (plusieurs centaines de fois).

**Règle importante** : Pour une bonne fluidité, n'appelez `update()` qu'**une seule fois par itération** de la boucle.

📖 **Doc** : [pygame.display.update()](https://www.pygame.org/docs/ref/display.html#pygame.display.update)

### Premier commit

```bash
git add agario.py
git commit -m "v0: fenêtre avec couleur aléatoire"
```

---

## Version 1 : Gestion des événements

Améliorons notre programme pour pouvoir le quitter proprement.

### 🎯 Objectif

Gérer deux types d'événements :
- Fermeture de la fenêtre (clic sur la croix)
- Appui sur la touche `Q`

### 📝 À faire

Modifiez la boucle `for event in pg.event.get():` pour :

1. Détecter l'événement `pg.QUIT` (fermeture fenêtre) → mettre `done = True`
2. Détecter l'événement `pg.KEYDOWN` avec la touche `pg.K_q` → mettre `done = True`

**Code squelette** :

```python
for event in pg.event.get():
    # A compléter : vérifier si event.type == pg.QUIT
    #   si oui : done = True

    # A compléter : vérifier si event.type == pg.KEYDOWN
    #   si oui : vérifier si event.key == pg.K_q
    #       si oui : done = True
```

### 📖 Documentation

- [pygame.event - Types d'événements](https://www.pygame.org/docs/ref/event.html)
- Liste des constantes : `pg.QUIT`, `pg.KEYDOWN`
- Liste des touches : [pygame.key](https://www.pygame.org/docs/ref/key.html)

### ✅ Test

Lancez le programme. Vous devez pouvoir :
- Fermer la fenêtre avec la croix
- Quitter avec la touche `Q`

### Commit

```bash
git add agario.py
git commit -m "v1: gestion événements (fermeture fenêtre + touche q)"
```

---

## Version 2 : Dessiner un blob

Créons notre premier élément de jeu : un cercle coloré (blob) au centre de l'écran.

### 🎯 Objectif

- Importer les couleurs prédéfinies de Pygame
- Dessiner un cercle bleu de rayon 20 au centre de l'écran
- Augmenter le framerate à 60 FPS

### 📝 À faire

1. **Imports** : Ajoutez `from pygame.color import THECOLORS as COLORS`

2. **Avant la boucle** : Définissez les variables du blob
   ```python
   blob_color = COLORS["blue"]
   blob_size = 20
   ```

3. **Dans la boucle** :
   - Changez `clock.tick(1)` en `clock.tick(60)` (60 FPS)
   - Remplacez la couleur aléatoire par un fond noir : `screen.fill(COLORS["black"])`
   - Dessinez un cercle au centre :
     ```python
     center = (640 // 2, 640 // 2)
     # A compléter : utiliser pg.draw.circle(screen, couleur, position, rayon)
     ```

### 📖 Documentation

- [pygame.draw.circle()](https://www.pygame.org/docs/ref/draw.html#pygame.draw.circle)
- [Liste des couleurs Pygame](https://www.pygame.org/docs/ref/color_list.html)
- [pygame.time.Clock.tick()](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick)

### ✅ Test

Vous devriez voir un cercle bleu fixe au centre d'un écran noir.

### Commit

```bash
git add agario.py
git commit -m "v2: affichage d'un blob fixe au centre"
```

---

## Version 3 : Déplacement avec la souris

Faisons bouger notre blob en suivant la position de la souris !

### 🎯 Objectif

Utiliser les vecteurs 2D pour calculer le déplacement du blob vers la souris.

### 📝 À faire

1. **Import** : Ajoutez `from pygame.math import Vector2 as V2`

2. **Avant la boucle** : Remplacez les constantes par des vecteurs
   ```python
   SCREEN = V2(640, 640)
   WIDTH, HEIGHT = SCREEN
   SCREEN_CENTER = SCREEN / 2

   blob_position = SCREEN_CENTER.copy()  # Position initiale
   blob_speed = 3
   ```

3. **Dans la boucle** (avant l'affichage) : Calculez le mouvement
   ```python
   # A compléter : récupérer la position de la souris
   # mouse_pos = V2(pg.mouse.get_pos())

   # A compléter : calculer le vecteur direction
   # direction = mouse_pos - blob_position

   # A compléter : si la distance est > 5 (évite les tremblements)
   #   normaliser le vecteur direction avec .normalize()
   #   ajouter direction * blob_speed à blob_position
   ```

4. **Affichage** : Utilisez `blob_position` pour dessiner le cercle
   ```python
   pg.draw.circle(screen, blob_color, (int(blob_position.x), int(blob_position.y)), blob_size)
   ```

### 💡 Aide

- `direction.length()` donne la longueur du vecteur
- `direction.normalize()` retourne un vecteur de longueur 1 dans la même direction
- Multiplier un vecteur par un nombre : `vecteur * vitesse`

### 📖 Documentation

- [pygame.mouse.get_pos()](https://www.pygame.org/docs/ref/mouse.html#pygame.mouse.get_pos)
- [pygame.math.Vector2](https://www.pygame.org/docs/ref/math.html#pygame.math.Vector2)
- Méthodes Vector2 : `.length()`, `.normalize()`, `.copy()`

### ✅ Test

Déplacez votre souris : le blob doit la suivre en douceur.

### Commit

```bash
git add agario.py
git commit -m "v3: déplacement du blob vers la souris"
```

---

## Version 4 : Ajouter une grille

Pour donner une impression d'espace, ajoutons une grille de fond.

### 🎯 Objectif

Créer une fonction qui dessine des lignes espacées de 50 pixels.

### 📝 À faire

1. **Constante** : Ajoutez `TILE_SIZE = 50` après vos autres constantes

2. **Nouvelle fonction** (avant `main()`) :
   ```python
   def draw_grid(screen):
       """Dessine une grille sur tout l'écran"""
       # A compléter : boucle for pour dessiner les lignes verticales
       #   pour x de 0 à WIDTH (pas de TILE_SIZE)
       #       pg.draw.line(screen, COLORS["grey"], (x, 0), (x, HEIGHT))

       # A compléter : boucle for pour dessiner les lignes horizontales
       #   pour y de 0 à HEIGHT (pas de TILE_SIZE)
       #       pg.draw.line(screen, COLORS["grey"], (0, y), (WIDTH, y))
   ```

3. **Dans la boucle** : Appelez `draw_grid(screen)` après `screen.fill()` et avant le blob

### 📖 Documentation

- [pygame.draw.line()](https://www.pygame.org/docs/ref/draw.html#pygame.draw.line)
- [range() avec un pas](https://docs.python.org/3/library/functions.html#func-range)

### ✅ Test

Vous devriez voir une grille grise. Le blob peut maintenant sortir de l'écran !

### Commit

```bash
git add agario.py
git commit -m "v4: ajout d'une grille de fond"
```

---

## Version 5 : Grande carte avec scrolling

La vraie magie d'agar.io : une grande carte ! Au lieu de déplacer le blob, on va déplacer la **caméra**.

### 🎯 Objectif

- Créer une carte 10× plus grande que l'écran
- Le blob reste visuellement au centre
- La grille "défile" pour donner l'impression de mouvement

### 📝 Concepts clés

**Changement de paradigme** :
- Avant : le blob bouge, la grille est fixe
- Maintenant : le blob est fixe à l'écran, la grille défile

**Principe** :
- `blob_position` = position dans la grande carte
- On dessine uniquement la portion de grille visible
- Le blob est toujours dessiné au centre de l'écran

### À faire

1. **Nouvelles constantes** :
   ```python
   MAP = 10 * SCREEN  # Carte 10× plus grande
   M_WIDTH, M_HEIGHT = MAP
   MAX_SPEED = 100
   ```

2. **Fonction utile** (avant `main()`) :
   ```python
   from math import floor

   def round_to(n, div):
       """Arrondit n au multiple inférieur de div"""
       return floor(n / div) * div
   ```

3. **Modifier `draw_grid()`** pour accepter `camera_position` :
   ```python
   def draw_grid(screen, camera_position):
       """Dessine uniquement la portion de grille visible"""
       # A compléter : calculer display_rect (rectangle de la zone visible)
       # display_rect = pg.Rect(
       #     camera_position.x - SCREEN_CENTER.x,
       #     camera_position.y - SCREEN_CENTER.y,
       #     WIDTH, HEIGHT
       # )

       # A compléter : calculer les limites de la grille à dessiner
       # first_vertical = int(max(0, round_to(display_rect.left, TILE_SIZE)))
       # last_vertical = int(min(M_WIDTH, first_vertical + WIDTH + TILE_SIZE))
       # (même chose pour horizontal)

       # A compléter : dessiner les lignes visibles
       # Pour chaque ligne, soustraire display_rect.x ou .y pour convertir
       # les coordonnées de la carte en coordonnées écran
       # Exemple : screen_x = x - display_rect.x
   ```

4. **Dans `main()`** :
   - Changer `blob_position = V2(MAP) / 2` (centre de la carte)
   - Modifier le calcul de direction :
     ```python
     mouse_pos = V2(pg.mouse.get_pos())
     direction = mouse_pos - SCREEN_CENTER  # Direction par rapport au centre

     # A compléter : limiter la vitesse
     # Si direction.length() >= MAX_SPEED : normaliser
     # Sinon : diviser par MAX_SPEED (vitesse proportionnelle)
     ```
   - Appeler `draw_grid(screen, blob_position)`
   - Dessiner le blob **toujours au centre** : `(int(SCREEN_CENTER.x), int(SCREEN_CENTER.y))`

5. **Debug** : Affichez la position dans le titre
   ```python
   pg.display.set_caption(f"agario - x={blob_position.x:.0f} y={blob_position.y:.0f}")
   ```

### 💡 Indices

- `display_rect` représente la zone de la carte actuellement visible
- Pour convertir coordonnées carte → écran : `screen_x = carte_x - display_rect.x`
- On ne dessine que les lignes dans l'intervalle visible
- Pensez à ajouter `pg.K_ESCAPE` pour quitter aussi avec Echap

### 📖 Documentation

- [pygame.Rect](https://www.pygame.org/docs/ref/rect.html)
- [max() et min()](https://docs.python.org/3/library/functions.html#max)

### ✅ Test

Bougez la souris : la grille doit défiler, donnant l'impression de se déplacer sur une grande carte.

### Commit

```bash
git add agario.py
git commit -m "v5: grande carte avec scrolling de la caméra"
```

---

## Version 6 : Limites de la carte

Actuellement, vous pouvez sortir de la carte indéfiniment. Ajoutons des limites !

### 🎯 Objectif

- Empêcher le blob de sortir de la carte
- Afficher des zones blanches pour matérialiser les bords

### 📝 À faire

1. **Fonction utile** :
   ```python
   def clamp(value, min_value, max_value):
       """Limite value entre min_value et max_value"""
       # A compléter : retourner min(max_value, max(value, min_value))
   ```

2. **Nouvelle fonction `draw_overmap()`** :
   ```python
   def draw_overmap(screen, camera_position):
       """Dessine des rectangles blancs pour les zones hors carte"""
       # A compléter : calculer display_rect (comme dans draw_grid)

       # A compléter : si display_rect.left < 0
       #   dessiner un rectangle blanc à gauche
       #   mask = pg.Rect(0, 0, -display_rect.left, HEIGHT)
       #   pg.draw.rect(screen, COLORS["white"], mask)

       # A compléter : faire de même pour top, right, bottom
       # Indices :
       #   - top < 0 : rectangle en haut
       #   - right >= M_WIDTH : rectangle à droite (attention au calcul de position)
       #   - bottom >= M_HEIGHT : rectangle en bas
   ```

3. **Dans la boucle** (après mise à jour de `blob_position`) :
   ```python
   # A compléter : limiter la position avec clamp()
   # blob_position.x = clamp(blob_position.x, 0, M_WIDTH)
   # blob_position.y = clamp(blob_position.y, 0, M_HEIGHT)
   ```

4. **Affichage** : Appelez `draw_overmap(screen, blob_position)` après `draw_grid()`

### 📖 Documentation

- [pygame.Rect - Attributs](https://www.pygame.org/docs/ref/rect.html) : `.left`, `.top`, `.right`, `.bottom`
- [pygame.draw.rect()](https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect)

### ✅ Test

- Allez dans les coins : vous devez voir des zones blanches
- Essayez de sortir : le blob est bloqué aux limites

### Commit

```bash
git add agario.py
git commit -m "v6: limites de la carte et affichage des zones hors-carte"
```

---

## 🎉 Bravo !

Vous avez maintenant un jeu fonctionnel avec :
- ✅ Une fenêtre pygame
- ✅ Un blob contrôlable à la souris
- ✅ Une grande carte avec scrolling fluide
- ✅ Des limites de carte propres
- ✅ Une gestion correcte des événements

---

## 🚀 Extensions possibles (optionnel)

Si vous voulez aller plus loin :

### 1. Ajouter de la nourriture

Créez une classe `Food` avec position aléatoire et couleur :

```python
from random import randint

class Food:
    def __init__(self):
        self.position = V2(randint(0, M_WIDTH), randint(0, M_HEIGHT))
        self.color = (randint(100, 255), randint(100, 255), randint(100, 255))
        self.size = 5

    def draw(self, screen, camera_position):
        # A compléter : convertir position carte → écran et dessiner
        # screen_pos = self.position - (camera_position - SCREEN_CENTER)
        # pg.draw.circle(...)
```

📖 **Doc** : Consultez les exemples de classes dans [Real Python - Python Classes](https://realpython.com/python3-object-oriented-programming/)

### 2. Système de collision

Détectez quand le blob mange de la nourriture :

```python
def check_collision(blob_pos, blob_size, food):
    distance = (blob_pos - food.position).length()
    return distance < blob_size + food.size
```

### 3. Croissance du blob

Quand le blob mange, augmentez sa taille :

```python
blob_size += 0.5
blob_speed = max(2, blob_speed - 0.01)  # Plus gros = plus lent
```

### 4. Score et affichage texte

Affichez un score avec `pygame.font` :

```python
font = pg.font.Font(None, 36)
score_text = font.render(f"Score: {score}", True, COLORS["white"])
screen.blit(score_text, (10, 10))
```

📖 **Doc** : [pygame.font](https://www.pygame.org/docs/ref/font.html)

### 5. Plusieurs aliments à la fois

Créez une liste et gérez-la :

```python
foods = [Food() for _ in range(50)]

# Dans la boucle
for food in foods:
    food.draw(screen, blob_position)
    if check_collision(blob_position, blob_size, food):
        score += 1
        foods.remove(food)
        foods.append(Food())  # Nouvelle nourriture
```

### 6. Mini-map

Affichez une mini-carte dans un coin montrant votre position globale.

**Indice** : Dessinez un petit rectangle avec les proportions de la carte, et un point pour le blob.

---

## 🆘 Aide et dépannage

### Erreurs courantes

**"NameError: name 'pg' is not defined"**
→ Vérifiez `import pygame as pg` en haut du fichier

**"AttributeError: 'tuple' object has no attribute 'x'"**
→ Vous utilisez un tuple `(x, y)` au lieu d'un `V2(x, y)`

**Le blob tremble**
→ Vérifiez la condition `if direction.length() > 5` dans v3

**La grille ne défile pas**
→ Vérifiez que vous passez `blob_position` à `draw_grid()` et que vous dessinez le blob au `SCREEN_CENTER`

**"NameError: name 'WIDTH' is not defined"**
→ Vérifiez que vous avez bien défini les constantes globales avant les fonctions

### Où trouver de l'aide

1. **Relisez les messages d'erreur** : ils indiquent souvent la ligne et le problème
2. **Consultez la documentation Pygame** (liens ci-dessus)
3. **Discord du cours** : canal `#questions`
4. **Comparez avec les versions précédentes** : si v4 ne marche pas, vérifiez que v3 fonctionnait

### Astuce de debug

Utilisez `print()` pour afficher les valeurs :

```python
print(f"Position: {blob_position}, Direction: {direction}, Length: {direction.length()}")
```

---

## 📚 Ressources supplémentaires

- [Documentation officielle Pygame](https://www.pygame.org/docs/)
- [Pygame tutorials](https://www.pygame.org/wiki/tutorials)
- [Real Python - PyGame: A Primer](https://realpython.com/pygame-a-primer/)
- [Pygame examples](https://github.com/pygame/pygame/tree/main/examples) - Code source des exemples

---

## 💡 Conseils pour progresser

1. **Commits réguliers** : chaque version qui marche = un commit
2. **Testez souvent** : lancez après chaque petite modification
3. **Lisez les erreurs** : ne les ignorez pas, elles sont là pour aider
4. **Expérimentez** : changez les constantes (vitesse, couleurs, tailles)
5. **Commentez** : votre futur vous remerciera
6. **Demandez de l'aide** : se bloquer 30min sans demander n'est pas productif

Bon codage ! 🐍🎮
