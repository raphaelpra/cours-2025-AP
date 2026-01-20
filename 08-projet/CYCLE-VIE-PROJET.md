# Cycle de vie d'un projet Python

Guide complet : de l'initialisation au partage d'un projet Python avec UV et Git.

---

## 1. Initialisation

### Creer le projet

```bash
# Creer un nouveau projet UV
uv init mon-projet
cd mon-projet

# Structure generee :
# mon-projet/
# ├── pyproject.toml
# ├── README.md
# └── src/
#     └── mon_projet/
#         └── __init__.py
```

### Initialiser Git

```bash
git init
git add .
git commit -m "Init projet"
```

---

## 2. Developpement

### Ajouter des dependances

```bash
# Ajouter une dependance
uv add requests

# Ajouter une dependance de dev (tests, linting...)
uv add --dev pytest ruff

# Voir les dependances installees
uv tree
```

Les dependances sont ajoutees dans `pyproject.toml` et verrouillees dans `uv.lock`.

### Lancer du code

```bash
# Executer un fichier
uv run python main.py

# Executer un module
uv run python -m mon_projet

# Lancer les tests
uv run pytest
```

### Synchroniser l'environnement

```bash
# Apres un git pull ou modification manuelle de pyproject.toml
uv sync
```

---

## 3. Creer une commande CLI

### Structure du projet

```
mon-projet/
├── pyproject.toml
└── src/
    └── mon_projet/
        ├── __init__.py
        └── cli.py
```

### Definir le point d'entree

Dans `src/mon_projet/cli.py` :

```python
def main():
    print("Hello depuis mon-projet!")
```

Dans `pyproject.toml`, ajouter :

```toml
[project.scripts]
mon-cli = "mon_projet.cli:main"
```

### Installer en mode editable

```bash
uv pip install -e .
```

La commande `mon-cli` est maintenant disponible :

```bash
mon-cli
# → Hello depuis mon-projet!
```

**Mode editable** : les modifications du code sont prises en compte immediatement, sans reinstallation.

---

## 4. Partage sur GitHub

### Creer le repository

```bash
# Avec GitHub CLI
gh repo create mon-projet --public --source=. --push

# Ou manuellement :
# 1. Creer le repo sur github.com
# 2. Ajouter le remote
git remote add origin git@github.com:username/mon-projet.git
git push -u origin main
```

### Fichiers a ignorer

Creer/completer `.gitignore` :

```gitignore
# Environnement virtuel
.venv/

# Cache Python
__pycache__/
*.pyc

# Build
dist/
*.egg-info/

# IDE
.vscode/
.idea/
```

**Note** : `uv.lock` doit etre commite (garantit la reproductibilite).

### Push des modifications

```bash
git add .
git commit -m "Add feature X"
git push
```

---

## 5. Installation par d'autres

### Depuis GitHub

```bash
# Cloner et installer
git clone https://github.com/username/mon-projet.git
cd mon-projet
uv sync
uv pip install -e .

# Ou directement sans cloner
uv pip install git+https://github.com/username/mon-projet.git
```

### Executer sans installer (uvx)

```bash
# Execute la CLI dans un environnement temporaire
uvx --from git+https://github.com/username/mon-projet.git mon-cli
```

### Depuis un fichier wheel

```bash
# Cote developpeur : construire le package
uv build
# → Genere dist/mon_projet-0.1.0-py3-none-any.whl

# Cote utilisateur : installer le wheel recu
uv pip install mon_projet-0.1.0-py3-none-any.whl
```

---

## 6. Resume des commandes

| Etape | Commande |
|-------|----------|
| Creer projet | `uv init mon-projet` |
| Init git | `git init && git add . && git commit -m "Init"` |
| Ajouter dependance | `uv add <package>` |
| Lancer code | `uv run python <fichier>` |
| Installer CLI locale | `uv pip install -e .` |
| Creer repo GitHub | `gh repo create mon-projet --public --source=. --push` |
| Push | `git add . && git commit -m "msg" && git push` |
| Installer depuis git | `uv pip install git+https://github.com/user/repo.git` |
| Build wheel | `uv build` |

---

## 7. Workflow typique

```bash
# Jour 1 : Creation
uv init mon-projet && cd mon-projet
git init
uv add rich click
# ... developper ...
uv pip install -e .  # tester la CLI
git add . && git commit -m "Init projet"
gh repo create mon-projet --public --source=. --push

# Jours suivants : Developpement
# ... modifier le code ...
uv run python main.py  # tester
git add . && git commit -m "Add feature" && git push

# Partage
# Envoyer le lien GitHub ou le fichier .whl
```
