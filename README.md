# Cours Python - Mines Paris

Bienvenue dans le repository du cours Python !

---

## Première installation

### 1. Cloner le repository

```bash
git clone https://github.com/raphaelpra/cours-2025-AP.git
cd cours-2025-AP
```

### 2. Installer les outils

**UV (gestionnaire d'environnement Python)** → [Guide complet](./01-introduction/uv.md)

**Discord (communication et support)** → [Instructions](./01-introduction/Discord.md)

---

## Travailler avec vos fichiers personnels

Vous pouvez créer vos propres fichiers et dossiers directement dans ce repository pour :
- Prendre des notes
- Faire vos exercices et TPs
- Tester du code

### Comment faire ?

**Créez des fichiers ou dossiers qui commencent par `perso` :**

```bash
# Fichiers de notes
01-introduction/perso-notes.md
01-introduction/perso-idees.txt

# Fichiers Python pour vos exercices
01-introduction/perso-exercice1.py
02-*/perso-tp.py

# Dossiers pour organiser vos TPs
01-introduction/perso/
01-introduction/perso/exercice1.py
01-introduction/perso/exercice2.py
01-introduction/perso/data.json

# Ou un dossier perso à la racine
perso/
perso/tests.py
perso/notes.md
```

**Tous ces fichiers et dossiers sont automatiquement ignorés par git**, ce qui signifie :
- Vos fichiers restent privés et locaux sur votre machine
- Ils ne seront jamais partagés ou envoyés sur GitHub
- Vous ne risquez pas de créer des conflits lors des mises à jour
- Vous pouvez travailler librement sans vous soucier de git

---

## Récupérer les nouveaux cours

Avant chaque cours, récupérez les nouveaux contenus :

```bash
cd cours-2025-AP
git pull
```

**C'est tout !** Le système ignore automatiquement vos fichiers `perso*`, donc :
- Pas de conflit avec vos fichiers personnels
- Pas besoin de faire de commit
- Vous récupérez juste les nouveaux cours

### En cas de problème

Si `git pull` affiche une erreur, vous pouvez forcer la mise à jour :

```bash
git fetch --all
git reset --hard origin/master
```

⚠️ **Attention** : cette commande écrase TOUS les fichiers sauf vos fichiers/dossiers `perso*`

---

## Structure du Repository

```
.
├── README.md              # Ce fichier
├── 01-introduction/       # Cours 1
│   ├── programme.md       # Déroulé du cours
│   ├── Discord.md         # Configuration Discord
│   └── uv.md              # Configuration UV
├── 02-*/                  # Cours 2 (à venir)
└── ...
```

---

## Ressources

* **[Site du cours](https://python.info-mines.paris)** - Présentation générale
* **[Discord](./01-introduction/Discord.md)** - Rejoindre le serveur
* **[Guide UV](./01-introduction/uv.md)** - Gestionnaire d'environnement Python

---

Bon cours ! 🐍
