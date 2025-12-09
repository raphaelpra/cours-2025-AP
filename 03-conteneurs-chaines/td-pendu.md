# TD - Jeu du pendu en TUI (Text User Interface)

Projet pratique pour appliquer les concepts de conteneurs et manipulation de chaînes.

➜ Créez vos fichiers dans le dossier `perso/` pour travailler librement sans conflit git.

---

## 🎯 Objectifs pédagogiques

Ce TD met l'accent sur :
- **Choix des conteneurs appropriés** : Quand utiliser `list`, `set`, `tuple`, ou `dict` ?
- **Itérations efficaces** : Parcourir les structures de manière pythonique
- **Manipulation de chaînes** : Slicing, méthodes, formatage
- **Logique de jeu** : Conditions, états, boucles

---

## 📝 Version 1 : Pendu simplifié (Débutant)

**Fichier :** `perso/pendu_v1.py`

### Spécifications

**Mot à deviner :** Prédéfini dans le code (ex: `"PYTHON"`)

**Règles :**
1. L'utilisateur a **8 tentatives** maximum
2. À chaque tour, afficher :
   - L'état actuel du mot (lettres trouvées + underscores pour lettres manquantes)
   - Nombre de tentatives restantes
   - Lettres déjà proposées
3. L'utilisateur propose une lettre
4. Si la lettre est dans le mot → révéler toutes ses occurrences
5. Sinon → perdre une tentative
6. Victoire si le mot est complet avant 0 tentatives

### Structures de données à utiliser

**Réfléchissez aux choix suivants :**

```python
# Pour stocker le mot à deviner ?
# → str (immuable, indexable)

# Pour stocker les lettres trouvées ?
# → set (recherche rapide, pas de doublons)

# Pour stocker les lettres proposées ?
# → set (évite les doublons automatiquement)

# Pour construire l'affichage du mot ?
# → list (mutable, construction progressive puis join)
```

### Exemple d'exécution

```
=== JEU DU PENDU ===
Mot à deviner : _ _ _ _ _ _
Tentatives restantes : 8
Lettres déjà proposées : []

Proposez une lettre : P
✓ Bonne lettre !

Mot à deviner : P _ _ _ _ _
Tentatives restantes : 8
Lettres déjà proposées : ['P']

Proposez une lettre : Z
✗ Mauvaise lettre !

Mot à deviner : P _ _ _ _ _
Tentatives restantes : 7
Lettres déjà proposées : ['P', 'Z']

...

🎉 GAGNÉ ! Le mot était PYTHON
```

### Conseils d'implémentation

1. **Normalisation** : Convertir tout en majuscules avec `.upper()`
2. **Validation** : Vérifier que l'entrée est bien une seule lettre
3. **Test d'appartenance** : Utiliser `lettre in lettres_proposees` (set rapide !)
4. **Affichage du mot** : Créer une liste puis utiliser `" ".join(liste)`

### Squelette de code

```python
# Données du jeu
mot_secret = "PYTHON"
lettres_trouvees = set()
lettres_proposees = set()
tentatives_restantes = 8

# Boucle principale
while tentatives_restantes > 0:
    # Construire l'affichage du mot
    affichage = []
    for lettre in mot_secret:
        if lettre in lettres_trouvees:
            affichage.append(lettre)
        else:
            affichage.append("_")

    mot_affiche = " ".join(affichage)

    # Afficher l'état du jeu
    print(f"\nMot à deviner : {mot_affiche}")
    print(f"Tentatives restantes : {tentatives_restantes}")
    print(f"Lettres proposées : {sorted(lettres_proposees)}")

    # Vérifier victoire
    if "_" not in affichage:
        print(f"\n🎉 GAGNÉ ! Le mot était {mot_secret}")
        break

    # Demander une lettre
    # ... (à compléter)
```

---

## 🚀 Version 2 : Pendu avancé (Intermédiaire/Avancé)

**Fichier :** `perso/pendu_v2.py`

### Améliorations par rapport à la version 1

1. **Dictionnaire de mots** : Sélection aléatoire parmi une liste
2. **Dessin ASCII du pendu** : Représentation visuelle de l'état
3. **Catégories de mots** : Thématiques (animaux, pays, objets, etc.)
4. **Système de score** : Points basés sur difficulté et tentatives restantes
5. **Rejouer** : Possibilité de lancer plusieurs parties

### Structures de données à utiliser

**Dictionnaire pour les catégories :**

```python
MOTS_PAR_CATEGORIE = {
    "animaux": ["ELEPHANT", "GIRAFE", "CROCODILE", "PAPILLON", "RENARD"],
    "pays": ["FRANCE", "BRESIL", "JAPON", "AUSTRALIE", "EGYPTE"],
    "objets": ["ORDINATEUR", "TELEPHONE", "BUREAU", "STYLO", "LAMPE"],
    "metiers": ["INGENIEUR", "MEDECIN", "PROFESSEUR", "ARCHITECTE", "POMPIER"]
}
```

**Pourquoi un dictionnaire ?**
- Accès rapide par clé (catégorie)
- Structure claire et extensible
- Facilite l'ajout de nouvelles catégories

### Dessin ASCII du pendu

```python
ETAPES_PENDU = [
    """
       ------
       |    |
       |
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    PERDU !
    """
]
```

**Structure :** Liste de strings (accès par index = nombre d'erreurs)

### Système de score

```python
def calculer_score(mot, tentatives_restantes, nb_tentatives_max=8):
    """
    Score basé sur :
    - Longueur du mot (difficulté)
    - Tentatives restantes (performance)
    """
    score_base = len(mot) * 10
    bonus_performance = tentatives_restantes * 5
    return score_base + bonus_performance
```

### Exemple d'exécution

```
╔══════════════════════════════════════╗
║       JEU DU PENDU - VERSION 2       ║
╚══════════════════════════════════════╝

Catégories disponibles :
1. Animaux
2. Pays
3. Objets
4. Métiers

Choisissez une catégorie (1-4) : 1

       ------
       |    |
       |
       |
       |
       |
    --------

Mot à deviner : _ _ _ _ _ _ _ _  (8 lettres)
Catégorie : Animaux
Tentatives restantes : 8
Lettres proposées : []

Proposez une lettre : E

✓ Bonne lettre ! Il y a 2 'E' dans le mot

       ------
       |    |
       |
       |
       |
       |
    --------

Mot à deviner : E _ E _ _ _ _ _
Catégorie : Animaux
Tentatives restantes : 8
Lettres proposées : ['E']

...

🎉 GAGNÉ ! Le mot était ELEPHANT
🏆 Score : 120 points

Voulez-vous rejouer ? (o/n) :
```

### Fonctionnalités à implémenter

#### 1. Sélection aléatoire du mot

```python
import random

def choisir_mot(categorie):
    """Retourne un mot aléatoire de la catégorie donnée"""
    return random.choice(MOTS_PAR_CATEGORIE[categorie])
```

**Pourquoi `random.choice()` ?**
- Sélection uniforme dans une liste/séquence
- Alternative : `random.randint()` + indexation manuelle (moins pythonique)

#### 2. Affichage du pendu

```python
def afficher_pendu(nb_erreurs):
    """Affiche l'étape correspondante du dessin"""
    if nb_erreurs < len(ETAPES_PENDU):
        print(ETAPES_PENDU[nb_erreurs])
```

#### 3. Validation des entrées

```python
def demander_lettre(lettres_deja_proposees):
    """
    Demande une lettre à l'utilisateur avec validation :
    - Une seule lettre
    - Pas déjà proposée
    - Alphabétique
    """
    while True:
        entree = input("Proposez une lettre : ").upper().strip()

        if len(entree) != 1:
            print("❌ Entrez une seule lettre")
            continue

        if not entree.isalpha():
            print("❌ Entrez uniquement des lettres")
            continue

        if entree in lettres_deja_proposees:
            print("❌ Lettre déjà proposée")
            continue

        return entree
```

**Méthodes de string utilisées :**
- `.upper()` : Normalisation
- `.strip()` : Supprimer espaces
- `.isalpha()` : Vérifier caractère alphabétique

#### 4. Boucle de jeu complète

```python
def jouer_partie():
    # Choix de la catégorie
    categorie = choisir_categorie()
    mot_secret = choisir_mot(categorie)

    # Initialisation
    lettres_trouvees = set()
    lettres_proposees = set()
    nb_erreurs = 0
    nb_tentatives_max = len(ETAPES_PENDU) - 1

    # Boucle principale
    while nb_erreurs < nb_tentatives_max:
        afficher_etat_jeu(mot_secret, lettres_trouvees, lettres_proposees, nb_erreurs)

        # Vérifier victoire
        if all(lettre in lettres_trouvees for lettre in mot_secret):
            print(f"\n🎉 GAGNÉ ! Le mot était {mot_secret}")
            score = calculer_score(mot_secret, nb_tentatives_max - nb_erreurs)
            print(f"🏆 Score : {score} points")
            return True

        # Demander une lettre
        lettre = demander_lettre(lettres_proposees)
        lettres_proposees.add(lettre)

        # Vérifier si la lettre est dans le mot
        if lettre in mot_secret:
            lettres_trouvees.add(lettre)
            nb_occurrences = mot_secret.count(lettre)
            print(f"\n✓ Bonne lettre ! Il y a {nb_occurrences} '{lettre}' dans le mot")
        else:
            nb_erreurs += 1
            print(f"\n✗ Mauvaise lettre !")

    # Défaite
    afficher_pendu(nb_erreurs)
    print(f"\n💀 PERDU ! Le mot était {mot_secret}")
    return False
```

**Compréhension de liste utilisée :**
```python
all(lettre in lettres_trouvees for lettre in mot_secret)
```
- Expression génératrice pour vérifier toutes les lettres
- Plus efficace que construire une liste complète

---

## 🎓 Points d'attention pédagogiques

### Choix des conteneurs : Comparaison

| Conteneur | Cas d'usage dans le pendu | Avantage |
|-----------|---------------------------|----------|
| `set` | Lettres trouvées/proposées | Recherche O(1), pas de doublons |
| `list` | Construction affichage mot | Mutable, ordre préservé, indexable |
| `tuple` | Mot secret (v1) | Immuable, hashable |
| `str` | Mot secret (v2) | Immuable, iterable, méthodes riches |
| `dict` | Catégories de mots | Accès par clé, structure logique |

### Opérations sur les sets

```python
# Ajout
lettres_proposees.add("A")

# Test d'appartenance (très rapide !)
if "A" in lettres_proposees:
    ...

# Différence (lettres non encore proposées)
alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lettres_restantes = alphabet - lettres_proposees
```

### Itération sur les strings

```python
# Parcours simple
for lettre in mot_secret:
    print(lettre)

# Parcours avec index (enumerate)
for i, lettre in enumerate(mot_secret):
    print(f"Position {i}: {lettre}")

# Compréhension de liste
affichage = [lettre if lettre in lettres_trouvees else "_"
             for lettre in mot_secret]
```

### Méthodes de string utiles

```python
# Comptage
nb_e = mot_secret.count("E")

# Test d'appartenance
if "A" in mot_secret:
    ...

# Joindre une liste
mot_affiche = " ".join(["P", "Y", "T", "H", "O", "N"])  # "P Y T H O N"

# Formatage
print(f"Il reste {tentatives} tentatives")
```

---

## 🏆 Extensions possibles (Bonus)

### 1. Mode multijoueur local
- Joueur 1 entre un mot secret
- Joueur 2 devine (écran effacé entre les deux)

### 2. Statistiques de session
```python
stats = {
    "parties_jouees": 0,
    "victoires": 0,
    "score_total": 0,
    "mots_trouves": []
}
```

### 3. Système de difficulté
- Facile : 10 tentatives, mots courts
- Moyen : 8 tentatives, mots moyens
- Difficile : 6 tentatives, mots longs

### 4. Indices
- Révéler une lettre aléatoire (coût : -1 tentative)
- Afficher la première/dernière lettre

### 5. Sauvegarde de partie
- Utiliser un fichier texte pour sauvegarder l'état
- Reprendre une partie interrompue
- *(Nécessite le cours suivant sur les fichiers)*

---

## 📚 Ressources

- **Conteneurs** : https://python.info-mines.paris/containers-1-nb/
- **Séquences et strings** : https://python.info-mines.paris/sequences-str-nb/
- **Documentation Python** :
  - `str` methods : https://docs.python.org/3/library/stdtypes.html#string-methods
  - `set` operations : https://docs.python.org/3/library/stdtypes.html#set
  - `random` module : https://docs.python.org/3/library/random.html

---

## ✅ Checklist de progression

### Version 1 (Simplifié)
- [ ] Affichage du mot avec underscores
- [ ] Input et validation de lettre
- [ ] Test si lettre dans mot
- [ ] Mise à jour lettres trouvées (set)
- [ ] Compteur de tentatives
- [ ] Détection victoire/défaite
- [ ] Gestion des lettres déjà proposées

### Version 2 (Avancé)
- [ ] Dictionnaire de mots par catégorie
- [ ] Sélection aléatoire avec `random.choice()`
- [ ] Dessin ASCII du pendu (liste d'étapes)
- [ ] Menu de choix de catégorie
- [ ] Calcul du score
- [ ] Option rejouer
- [ ] Interface améliorée (bordures, emojis)

### Bonus
- [ ] Mode multijoueur
- [ ] Statistiques de session
- [ ] Système d'indices
- [ ] Niveaux de difficulté
