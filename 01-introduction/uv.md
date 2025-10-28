# UV

---

## 🧩 Pourquoi un gestionnaire d’environnement ?

* Éviter les conflits entre versions de dépendances
* Gérer plusieurs projets Python indépendants
* Simplifier la création et la reproduction d’environnements
* Faciliter l’installation et la mise à jour des paquets
* Fournir une alternative rapide et intégrée à `pip + venv`

👉 **Objectif :** rendre le travail sur plusieurs projets Python *propre, isolé et reproductible*.

---

## ⚡ Présentation rapide de **uv**

* **uv** est un gestionnaire d’environnement et de dépendances Python moderne
* Compatible avec les outils existants (`pip`, `virtualenv`, `pyproject.toml`)
* Écrit en **Rust** → très rapide
* Permet de gérer les environnements, dépendances et exécutions en une seule commande

🔗 [Documentation officielle : https://docs.astral.sh/uv](https://docs.astral.sh/uv)

---

## 🛠️ Installation

### Sur macOS / Linux / WSL

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Sur Windows (PowerShell)

```powershell
iwr https://astral.sh/uv/install.ps1 -useb | iex
```

Vérifier l’installation :

```bash
uv --version
```

🧭 En cas de souci, voir la doc :
👉 [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)

---

## 💡 Quelques commandes utiles

Créer un nouveau projet Python :

```bash
uv init mon-projet
```

Créer un environnement virtuel :

```bash
uv venv
```

Installer une dépendance :

```bash
uv add requests
```

Lancer le projet :

```bash
uv run python main.py
```

Mettre à jour les dépendances :

```bash
uv sync
```

---

## 🧰 Intégration avec VS Code

### Étape 1 : Ouvrir ton projet dans VS Code

### Étape 2 : Sélectionner l’interpréteur Python de `uv`

* Ouvre la palette de commandes (`Ctrl+Shift+P` ou `Cmd+Shift+P`)
* Recherche : `Python: Select Interpreter`
* Choisis celui créé par `uv` (dans `.venv`)

### Étape 3 : (optionnel)

Configurer le `.vscode/settings.json` :

```json
{
  "python.defaultInterpreterPath": ".venv/bin/python"
}
```

---

## 🚀 En résumé

✅ Environnements isolés
✅ Gestion simple des dépendances
✅ Compatible VS Code
✅ Ultra rapide

🧠 **Essaye :**

```bash
uv init demo
cd demo
uv add rich
uv run python -m rich
```
