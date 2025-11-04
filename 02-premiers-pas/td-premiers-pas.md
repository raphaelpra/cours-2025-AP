# TD - Premiers pas en Python

Exercices pratiques pour mettre en application les concepts de base.

➜ Créez vos fichiers dans le dossier `perso/` pour travailler librement sans conflit git.

---

## Exercice 1 : Variables et types

**Objectif** : Manipuler variables et types de base

Créez un fichier `perso/ex1.py` qui :

1. Crée des variables de différents types :
   - Votre prénom (string)
   - Votre âge (int)
   - Votre taille en mètres (float)
   - Si vous aimez Python (bool)

2. Affiche chaque variable avec son type en utilisant `type()`

3. Effectue des conversions :
   - Convertit l'âge en string
   - Convertit la taille en int (troncature)

**Exemple de sortie attendue :**
```
Prénom: Alice, type: <class 'str'>
Âge: 20, type: <class 'int'>
...
```

---

## Exercice 2 : Cryptographie - Chiffre de César

**Objectif** : Manipulation avancée de strings et algorithmes

Créez un fichier `perso/ex2.py` qui implémente le chiffre de César :

1. **Fonction d'encodage** : Crée une fonction qui décale chaque lettre de l'alphabet
   - Exemple : avec un décalage de 3, "A" devient "D", "X" devient "A"
   - Garde les espaces et ponctuation inchangés
   - Gère majuscules et minuscules séparément

2. **Fonction de décodage** : Inverse le processus

3. **Interface utilisateur** :
   - Demande le message à chiffrer/déchiffrer
   - Demande la clé (décalage entre 1 et 25)
   - Propose les deux modes (chiffrer/déchiffrer)

4. **Défi bonus** : Casseur de code automatique
   - Teste tous les décalages possibles (1-25)
   - Affiche tous les résultats pour que l'utilisateur choisisse le bon

**Exemple d'exécution :**
```
=== CHIFFRE DE CÉSAR ===
Message : Hello World!
Clé (1-25) : 3
Mode (c)hiffrer ou (d)échiffrer : c
Résultat : Khoor Zruog!

Mode cassage automatique (o/n) : o
Clé 1 : Gdkkn Vnqkc!
Clé 2 : Fcjjm Umpjb!
Clé 3 : Ebiil Tloia!
...
```

---

## Exercice 3 : Calculatrice avancée avec parsing

**Objectif** : Parsing et évaluation d'expressions mathématiques

Créez un fichier `perso/ex3.py` qui implémente une calculatrice capable de parser des expressions.

### Partie A : Calculatrice simple (pour commencer)

1. Demande à l'utilisateur deux nombres (`input()`)
   - **Attention** : `input()` retourne toujours un string !

2. Convertit les entrées en `float`

3. Calcule et affiche toutes les opérations de base

### Partie B : Parser d'expressions (plus avancé)

4. Demande à l'utilisateur une expression mathématique sous forme de string
   - Exemple : `"14 + 42"`, `"100 / 5"`, `"3 * 7"`

5. Parse l'expression pour extraire :
   - Le premier nombre
   - L'opérateur (+, -, *, /, %, **)
   - Le deuxième nombre

6. Effectue le calcul et affiche le résultat

**Conseils pour le parsing :**
- Utilisez la méthode `.split()` pour séparer l'expression
- Gérez les espaces avec `.strip()`
- Pensez aux cas d'erreur (division par zéro, opérateur invalide)

### Partie C : Améliorations (bonus)

7. **Gestion des erreurs** : Affiche des messages d'erreur appropriés
8. **Boucle interactive** : Permet plusieurs calculs successifs
9. **Opérations avancées** : Ajoutez racine carrée, puissance, etc.

**Exemple d'exécution :**
```
=== CALCULATRICE PYTHON ===
Entrez une expression (ex: 14 + 42) : 25 * 4
Résultat : 25.0 * 4.0 = 100.0

Nouvelle expression (q pour quitter) : 100 / 3
Résultat : 100.0 / 3.0 = 33.333...

Nouvelle expression (q pour quitter) : q
Au revoir !
```

---

## Exercice 4 : Système de recommandation de films

**Objectif** : Structures de données et logique complexe

Créez un fichier `perso/ex4.py` qui simule un système de recommandation :

1. **Base de données de films** (utiliser des dictionnaires) :
```python
films = {
    "Inception": {"genre": "sci-fi", "note": 8.8, "annee": 2010},
    "Parasite": {"genre": "thriller", "note": 8.6, "annee": 2019},
    "Wall-E": {"genre": "animation", "note": 8.4, "annee": 2008},
    # Ajoutez au moins 10 films variés
}
```

2. **Fonctions de recherche** :
   - `films_par_genre(genre)` : retourne tous les films d'un genre
   - `films_par_note_min(note_min)` : films avec note >= note_min
   - `films_recents(annee_min)` : films sortis après une année

3. **Système de recommandation** :
   - Demande les préférences utilisateur (genres aimés, note minimale)
   - Calcule un score de compatibilité pour chaque film
   - Affiche le top 3 des recommandations

4. **Interface interactive** :
   - Menu avec différentes options de recherche
   - Possibilité d'ajouter de nouveaux films
   - Affichage formaté des résultats

**Défi bonus** : Système de notation utilisateur
- L'utilisateur peut noter des films (1-10)
- Le système apprend ses goûts et améliore les recommandations
- Sauvegarde les préférences dans un fichier texte

---

## Exercice 5 : Mini-projet - Générateur de profil avancé

**Objectif** : Synthèse des concepts avec validation

Créez un fichier `perso/ex5.py` qui :

1. Demande à l'utilisateur ses informations avec **validation** :
   - Prénom (au moins 2 caractères)
   - Nom (au moins 2 caractères)
   - Âge (entre 0 et 120)
   - Ville
   - Email (doit contenir @ et un point)

2. Génère un profil formaté avec calculs :
```
=== PROFIL UTILISATEUR ===
Nom complet : DUPONT Jean
Âge : 25 ans (né(e) en 2000)
Ville : Paris (6 lettres)
Email : jean.dupont@email.com
Initiales : J.D.
Statut : Majeur(e)
==========================
```

3. **Fonctionnalités avancées** :
   - Détecte si la personne est majeure/mineure
   - Demande s'il s'agit d'un homme ou d'une femme et adapte le profil en conséquence
   - Valide le format email basique
   - Formate le nom en majuscules et prénom avec première lettre majuscule

4. **Gestion d'erreurs** : Redemande les informations si elles sont invalides

**Exemple d'interaction :**
```
Prénom : a
❌ Le prénom doit contenir au moins 2 caractères
Prénom : Jean
✅ Prénom valide

Âge : 150
❌ L'âge doit être entre 0 et 120
Âge : 25
✅ Âge valide
```

---

## Pour aller plus loin

Si vous avez terminé, voici des exercices plus challengeants (au choix) :

### Exercice 6 : Simulateur de bataille de cartes

**Objectif** : Logique de jeu et algorithmes

Créez un jeu de bataille simplifié :

1. **Deck de cartes** : 52 cartes (As=1, Roi=13, couleurs ignorées)
2. **Distribution** : 26 cartes par joueur
3. **Règles de bataille** :
   - Chaque joueur pose sa carte du dessus
   - La plus haute gagne les deux cartes
   - En cas d'égalité : "bataille" (3 cartes cachées + 1 visible)
   - Le jeu continue jusqu'à ce qu'un joueur n'ait plus de cartes

4. **Fonctionnalités** :
   - Simulation automatique complète
   - Mode pas-à-pas (appuyer sur Entrée pour continuer)
   - Statistiques : nombre de tours, batailles, cartes gagnées
   - Détection des boucles infinies (arrêt après 1000 tours)

**Défi bonus** : Analyse statistique
- Jouez 100 parties automatiquement
- Calculez la durée moyenne, min, max
- Histogramme des durées de partie

### Exercice 7 : Bot conversationnel simple

**Objectif** : Intelligence artificielle basique et amusante

Créez un chatbot qui simule une conversation :

1. **Base de réponses** :
   - Dictionnaire de patterns → réponses
   - Exemple : "comment ça va" → ["Ça va bien !", "Super et toi ?", "Plutôt bien merci"]
   - Au moins 15-20 patterns différents

2. **Fonctionnalités amusantes** :
   - Réponses aléatoires pour éviter la répétition
   - Détection de l'humeur (mots positifs/négatifs)
   - Mémorisation du nom de l'utilisateur
   - Blagues intégrées (commande "raconte une blague")

3. **Intelligence basique** :
   - Détection de mots-clés dans les phrases
   - Réponses par défaut pour les messages non compris
   - Mode "perroquet" : répète la phrase en la modifiant

**Exemple de conversation :**
```
🤖 Bot: Salut ! Comment tu t'appelles ?
👤 Toi: Je m'appelle Alice
🤖 Bot: Enchanté Alice ! Comment ça va ?
👤 Toi: Je suis triste
🤖 Bot: Oh non Alice... Veux-tu que je te raconte une blague ?
👤 Toi: blague
🤖 Bot: Pourquoi les plongeurs plongent-ils toujours en arrière ? 
      Parce que sinon, ils tombent dans le bateau ! 😄
```

### Exercice 8 : Analyseur de code Python basique

**Objectif** : Parsing et analyse textuelle avancée

Créez un analyseur qui examine un fichier Python et affiche :

1. **Statistiques de base** :
   - Nombre de lignes, lignes vides, commentaires
   - Ratio code/commentaires
   - Longueur moyenne des lignes

2. **Analyse syntaxique** :
   - Détection des fonctions (def)
   - Comptage des variables (assignations avec =)
   - Structures de contrôle (if, for, while)
   - Imports utilisés

3. **Métriques de qualité** :
   - Fonctions trop longues (>20 lignes)
   - Lignes trop longues (>80 caractères)
   - Niveau d'indentation maximal
   - Noms de variables d'une seule lettre

4. **Rapport formaté** :
```
=== ANALYSE DU FICHIER moncode.py ===
📊 Statistiques générales :
   - 150 lignes total (120 code, 20 commentaires, 10 vides)
   - Ratio code/commentaires : 6:1
   
🔍 Éléments détectés :
   - 8 fonctions définies
   - 25 variables assignées
   - 12 structures de contrôle
   
⚠️  Problèmes potentiels :
   - 3 fonctions trop longues
   - 5 lignes dépassent 80 caractères
```

### Exercice 9 : Générateur de mots de passe intelligent

**Objectif** : Algorithmes et sécurité informatique

Créez un générateur qui produit des mots de passe mémorables ET sécurisés :

1. **Générateur basique** :
   - Longueur personnalisable (8-50 caractères)
   - Choix des types : majuscules, minuscules, chiffres, symboles
   - Évite les caractères ambigus (0/O, 1/l/I)

2. **Mode "passphrase"** (plus amusant) :
   - Combine des mots aléatoires : "Cheval-Bleu-42-Rocket"
   - Liste de 200+ mots courants en français
   - Séparateurs variés (-, _, ., !)
   - Nombres aléatoires intégrés

3. **Évaluateur de force** :
   - Calcule un score de sécurité (0-100)
   - Détecte les patterns faibles (123, abc, azerty)
   - Suggestions d'amélioration
   - Estimation du temps de crack

4. **Interface amusante** :
   - Génération en lot (10 mots de passe d'un coup)
   - Mode "défi" : génère jusqu'à avoir un score > 90
   - Phrases mnémotechniques pour retenir le mot de passe

**Exemple de sortie :**
```
🔐 GÉNÉRATEUR DE MOTS DE PASSE

Mode choisi: Passphrase amusante
Résultat: Licorne-Violette-73-Rocket!

📊 Analyse de sécurité:
   Force: ████████████████░░░░ 85/100 (Très fort)
   Temps de crack estimé: 2.5 millions d'années
   
💡 Phrase mnémotechnique:
   "La Licorne Violette court vers la Rocket numéro 73!"
```

---

## Ressources

- [python.info-mines.paris](https://python.info-mines.paris) - Section "Premiers pas"
- [Documentation Python](https://docs.python.org/fr/3/)
