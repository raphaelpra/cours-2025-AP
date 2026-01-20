# Guide Complet de Setup Python

Ce guide explique comment configurer un environnement de developpement Python propre et moderne.

**Important** : Ce cours utilise **UV** comme gestionnaire d'environnement Python, **pas Conda**.
Si vous avez Conda installe, vous devrez le desactiver completement (voir section dediee).

---

## Table des matieres

1. [Comprendre les concepts cles](#partie-1--comprendre-les-concepts-cles)
   - [Le PATH](#-le-path---la-variable-magique)
   - [PYTHONPATH](#-pythonpath---importer-ses-modules)
   - [bashrc / zshrc](#-bashrc--zshrc---le-fichier-de-demarrage)
2. [Installations](#partie-2--installations)
   - [Git Bash (Windows)](#-git-bash-windows)
   - [Visual Studio Code](#-visual-studio-code)
   - [UV](#-uv---gestionnaire-python-moderne)
3. [Desactiver Conda](#partie-3--desactiver-completement-conda)
4. [Environnements virtuels](#partie-4--environnements-virtuels-venv)
5. [Configuration VS Code](#partie-5--configuration-vs-code-avec-venv)
6. [Desinstallation](#partie-6--desinstallation)

---

# Partie 1 : Comprendre les concepts cles

## Le PATH - La variable magique

### Qu'est-ce que le PATH ?

Le `PATH` est une **variable d'environnement** qui indique au systeme **ou chercher les programmes**.

Quand vous tapez une commande comme `python` ou `code` dans le terminal, le systeme :
1. Regarde la liste des dossiers dans le PATH
2. Cherche un executable du meme nom dans chaque dossier
3. Execute le premier trouve

### Visualiser le PATH

```bash
# Afficher le PATH (les : separent les dossiers)
echo $PATH

# Exemple de sortie :
# /home/user/.local/bin:/usr/local/bin:/usr/bin:/bin
```

### Schema : Comment le PATH fonctionne

```
 Vous tapez: python
       |
       v
+------------------+
|  Le systeme      |
|  cherche dans    |
|  l'ordre :       |
+------------------+
       |
       v
  PATH = /home/user/.local/bin : /usr/local/bin : /usr/bin
              |                        |              |
              v                        v              v
        [cherche ici]          [puis ici]      [puis ici]
        python trouve?         python trouve?  python trouve?
              |
              v
      Premier trouve = execute !
```

### Pourquoi c'est important ?

Si vous avez **plusieurs versions de Python** installees :
- Une dans `/usr/bin/python` (systeme)
- Une dans `/home/user/miniconda/bin/python` (conda)
- Une dans `/home/user/.local/bin/python` (uv)

**Celle qui sera utilisee depend de l'ordre dans le PATH !**

### Modifier le PATH

```bash
# Ajouter un dossier AU DEBUT du PATH (prioritaire)
export PATH="/mon/nouveau/dossier:$PATH"

# Ajouter un dossier A LA FIN du PATH (moins prioritaire)
export PATH="$PATH:/mon/nouveau/dossier"
```

> **Attention** : Les modifications avec `export` ne durent que pour la session en cours.
> Pour les rendre permanentes, il faut les mettre dans `~/.bashrc` (voir section suivante).

### Verifier quel programme est utilise

```bash
# Quel python est utilise ?
which python
# ou
type python

# Exemple de sortie :
# /home/user/.local/bin/python
```

---

## PYTHONPATH - Importer ses modules

### Qu'est-ce que le PYTHONPATH ?

Le `PYTHONPATH` est une variable d'environnement qui indique a Python **ou chercher les modules a importer**.

> **Difference avec PATH** :
> - `PATH` = ou trouver les **programmes executables** (comme `python`)
> - `PYTHONPATH` = ou trouver les **modules Python** (pour `import mon_module`)

### Quand l'utiliser ?

**Dans 99% des cas, vous n'avez PAS besoin de modifier PYTHONPATH.**

Utilisez-le seulement si :
- Vous avez un module dans un dossier non-standard
- Vous developpez une librairie et voulez la tester sans l'installer

### Comment Python trouve les modules ?

Quand vous faites `import mon_module`, Python cherche dans cet ordre :

```
1. Le dossier du script en cours d'execution
2. Les dossiers dans PYTHONPATH
3. Les dossiers d'installation (site-packages)
```

### Verifier ou Python cherche

```python
import sys
print(sys.path)

# Sortie typique :
# ['',                                    # dossier courant
#  '/home/user/mon_projet',               # PYTHONPATH si defini
#  '/home/user/.local/lib/python3.12/site-packages',  # pip install --user
#  '/usr/lib/python3.12/site-packages']   # pip install global
```

### Exemple d'utilisation

```bash
# Structure du projet :
# mon_projet/
#   src/
#     mon_module.py
#   scripts/
#     main.py

# Pour que main.py puisse faire "import mon_module" :
export PYTHONPATH="/chemin/vers/mon_projet/src:$PYTHONPATH"
python scripts/main.py
```

### La bonne pratique : utiliser un venv

Plutot que de modifier `PYTHONPATH`, utilisez un **environnement virtuel** :

```bash
# Creer un venv
uv venv

# Activer le venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Installer votre module en mode "editable"
uv pip install -e .
```

---

## bashrc / zshrc - Le fichier de demarrage

### Qu'est-ce que c'est ?

Quand vous ouvrez un terminal, il execute automatiquement un **fichier de configuration**.

| Shell | Fichier de config | Emplacement |
|-------|-------------------|-------------|
| **bash** | `.bashrc` | `~/.bashrc` |
| **zsh** | `.zshrc` | `~/.zshrc` |

> **Note** : Le `~` represente votre dossier personnel (home directory).
> - Windows (Git Bash) : `/c/Users/VotreNom/`
> - macOS : `/Users/VotreNom/`
> - Linux : `/home/VotreNom/`

### Windows/Git Bash : Le fichier n'existe pas par defaut !

Sur **Git Bash (Windows)**, le fichier `~/.bashrc` **n'est pas cree automatiquement**.
De plus, Git Bash utilise d'abord `~/.bash_profile` avant `~/.bashrc`.

**Verifier si les fichiers existent :**
```bash
ls -la ~ | grep bash
```

**Configurer correctement (a faire une seule fois si le fichier .bashrc n'est pas present/charge) :**
```bash
# 1. Creer .bashrc s'il n'existe pas
touch ~/.bashrc

# 2. Creer .bash_profile s'il n'existe pas
touch ~/.bash_profile

# 3. Faire en sorte que .bash_profile charge .bashrc
# (Verifie d'abord si la ligne existe deja pour eviter les doublons)
grep -q "source ~/.bashrc" ~/.bash_profile || echo 'source ~/.bashrc' >> ~/.bash_profile
```

**Script tout-en-un (copier-coller dans Git Bash) :**
```bash
touch ~/.bashrc
touch ~/.bash_profile
grep -q "source ~/.bashrc" ~/.bash_profile 2>/dev/null || echo 'source ~/.bashrc' >> ~/.bash_profile
echo "Configuration OK ! Ouvrez un nouveau terminal pour appliquer."
```

Apres cette configuration, vous pouvez editer `~/.bashrc` normalement et les modifications seront appliquees a chaque nouveau terminal.

### Quel shell utilisez-vous ?

```bash
# Afficher votre shell actuel
echo $SHELL

# Sortie possible :
# /bin/bash   -> vous utilisez bash -> fichier ~/.bashrc
# /bin/zsh   -> vous utilisez zsh  -> fichier ~/.zshrc
```

### A quoi sert ce fichier ?

Le fichier de config permet de :
- Definir des **variables d'environnement** (PATH, PYTHONPATH)
- Creer des **alias** (raccourcis de commandes)
- Configurer le **prompt** (apparence du terminal)
- Executer des **scripts au demarrage**

### Exemple de contenu .bashrc

```bash
# ~/.bashrc

# Ajouter un dossier au PATH
export PATH="$HOME/.local/bin:$PATH"

# Definir l'editeur par defaut
export EDITOR="code --wait"

# Alias pratiques
alias ll="ls -la"
alias py="python3"
alias gs="git status"

# Message de bienvenue
echo "Bienvenue dans le terminal !"
```

### Voir et editer le fichier

```bash
# Voir le contenu
cat ~/.bashrc

# Editer avec VS Code
code ~/.bashrc

# Editer avec nano (si VS Code pas disponible)
nano ~/.bashrc
```

### Appliquer les modifications

Apres avoir modifie `.bashrc`, vous devez soit :

```bash
# Option 1 : Recharger le fichier
source ~/.bashrc

# Option 2 : Ouvrir un nouveau terminal
```

### Schema : Le cycle de vie du terminal

```
   Ouverture du terminal
          |
          v
   +------------------+
   | Execute ~/.bashrc|  <-- Vos configs sont chargees ici
   +------------------+
          |
          v
   +------------------+
   | Terminal pret    |
   | PATH configure   |
   | Alias disponibles|
   +------------------+
          |
          v
   Vous tapez vos commandes...
```

### Attention aux modifications multiples !

**Probleme courant** : Certains installateurs (comme `conda init`) ajoutent des lignes a votre `.bashrc`. Si vous lancez l'installation plusieurs fois, vous pouvez vous retrouver avec des **configurations en double** qui causent des problemes.

Voir la section [Desactiver Conda](#partie-3--desactiver-completement-conda) pour diagnostiquer et corriger cela.

---

# Partie 2 : Installations

## Git Bash (Windows)

> **Cette section concerne uniquement Windows.** Sur macOS et Linux, le terminal bash est deja installe.

### Pourquoi Git Bash ?

Git Bash fournit :
- Un terminal **bash** (comme sur Linux/macOS)
- La commande **git** pour le controle de version
- Des outils Unix (`ls`, `cat`, `grep`, etc.)

### Installation

1. Telechargez sur [https://gitforwindows.org/](https://gitforwindows.org/)

2. Lancez l'installateur et gardez les options par defaut, **sauf** :

   **Ecran "Adjusting your PATH environment"** :
   Choisissez l'option **recommandee** (option 2) :
   > "Git from the command line and also from 3rd-party software"

   ```
   +----------------------------------------------------------+
   |  Adjusting your PATH environment                         |
   |                                                          |
   |  ( ) Use Git from Git Bash only                          |
   |  (*) Git from the command line and 3rd-party software    |  <-- Choisir celle-ci
   |  ( ) Use Git and optional Unix tools from the Command    |
   +----------------------------------------------------------+
   ```

3. Terminez l'installation

### Verifier l'installation

Ouvrez **Git Bash** (pas PowerShell, pas cmd) :

```bash
# Verifier bash
echo $BASH_VERSION
# Doit afficher : 5.x.x(1)-release

# Verifier git
git --version
# Doit afficher : git version 2.x.x
```

### Epingler Git Bash a la barre des taches

1. Cherchez "Git Bash" dans le menu demarrer
2. Clic droit -> "Epingler a la barre des taches"

> **Important** : Utilisez toujours Git Bash pour ce cours, jamais PowerShell ou CMD.

---

## Visual Studio Code

### Installation

1. Telechargez sur [https://code.visualstudio.com/](https://code.visualstudio.com/)

2. **Windows** : Choisissez "User Installer" (pas besoin de droits admin)

3. **macOS** : **Glissez l'application dans le dossier Applications !**
   > C'est crucial, sinon la commande `code` ne fonctionnera pas correctement.

4. Gardez les options par defaut

### Verifier l'installation

```bash
# Dans un NOUVEAU terminal (important !)
code --version
# Doit afficher quelque chose comme : 1.85.0

# Tester l'ouverture du dossier courant
code .
```

### Si `code` ne fonctionne pas

La commande `code` est configuree **automatiquement** lors de l'installation de VS Code.

Si elle ne fonctionne pas, c'est que l'installation ne s'est pas bien passee → **reinstallez VS Code**.

**Windows** : Lors de la reinstallation, verifiez que ces options sont cochees :

```
+----------------------------------------------------------+
|  Select Additional Tasks                                  |
|                                                          |
|  [x] Add "Open with Code" action to file context menu    |
|  [x] Add "Open with Code" action to directory context    |
|  [x] Register Code as an editor for supported file types |
|  [x] Add to PATH (requires shell restart)  <-- IMPORTANT |
+----------------------------------------------------------+
```

Puis ouvrez un **nouveau** terminal Git Bash et retestez `code --version`.

**macOS** : 
1. Verifiez que VS Code est bien dans `/Applications/` (pas dans Downloads !)
2. Si besoin, ouvrez VS Code puis : `Cmd+Shift+P` -> `Shell Command: Install 'code' command in PATH`
3. Ouvrez un **nouveau** terminal

### Configuration recommandee

Activez l'**Auto Save** :
- Menu File -> Auto Save (cochez)

Installez l'extension **Python** :
- Cliquez sur l'icone Extensions (ou `Ctrl+Shift+X`)
- Cherchez "Python" (par Microsoft)
- Installez

---

## UV - Gestionnaire Python moderne

### Pourquoi UV ?

| Caracteristique | Conda | UV |
|----------------|-------|-----|
| Vitesse | Lent (minutes) | Ultra-rapide (secondes) |
| Taille | Lourd | Leger |
| Conflits | Frequents | Rares |
| Simplicite | Complexe | Simple |

UV est ecrit en Rust et remplace avantageusement `pip` et `conda` pour la gestion des packages Python.

### Installation

**macOS / Linux / WSL :**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (Git Bash)** :
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell)** :
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

> **Note Windows** : Les deux methodes (Git Bash et PowerShell) installent UV au meme endroit (`~/.local/bin` ou `%USERPROFILE%\.local\bin`). Vous pouvez utiliser l'une ou l'autre, elles coexistent sans probleme.
> **Note macOS** : Le shell par defaut est souvent **zsh**. Ajoutez bien `.local/bin` dans **~/.zshrc** (voir ci-dessous) et evitez de melanger `.bashrc` et `.zshrc`.

### Etape importante : Ajouter `.local/bin` au PATH

Apres l'installation, UV affiche un message comme :

```
uv installed successfully to /home/user/.local/bin/uv
To add $HOME/.local/bin to your PATH, run:
  export PATH="$HOME/.local/bin:$PATH"
```

**Vous DEVEZ ajouter ce dossier au PATH de facon permanente.**

**Linux / macOS (bash) / Git Bash :**
```bash
# Ajouter a la fin de ~/.bashrc (ou ~/.zshrc sur macOS)
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

# Recharger
source ~/.bashrc
```

**macOS (zsh par defaut)** :
```bash
# Ajouter a la fin de ~/.zshrc
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc

# Recharger
source ~/.zshrc
```

**Verification :**
```bash
echo $PATH | grep -q ".local/bin" && echo "OK: .local/bin est dans le PATH" || echo "ERREUR: .local/bin manque"
```

### Verifier l'installation

```bash
# Dans un NOUVEAU terminal (important !)
uv --version
# Doit afficher : uv 0.x.x
```

Si vous obtenez `uv: command not found`, c'est que `.local/bin` n'est pas dans votre PATH. Refaites l'etape precedente.

### Commandes essentielles

```bash
# Creer un nouveau projet Python
uv init mon-projet
cd mon-projet

# Creer un environnement virtuel
uv venv

# Installer une dependance
uv add requests
uv add numpy pandas matplotlib

# Lancer un script Python
uv run python mon_script.py

# Synchroniser les dependances (apres un git pull par exemple)
uv sync
```

### UV vs pip - Correspondances

| pip | uv |
|-----|-----|
| `pip install requests` | `uv add requests` |
| `pip install -r requirements.txt` | `uv sync` |
| `python -m venv .venv` | `uv venv` |
| `pip list` | `uv pip list` |

---

# Partie 3 : Desactiver completement Conda

## Pourquoi desactiver Conda ?

Avoir Conda **et** UV sur le meme systeme cause souvent des problemes :
- Conflits de PATH (quelle version de Python est utilisee ?)
- Conflits de packages
- Configurations corrompues apres plusieurs `conda init`

## Diagnostic : Est-ce que Conda pose probleme ?

### Test 1 : Conda est-il actif ?

```bash
# Verifier si conda est dans le PATH
which conda
# ou
type conda

# Si ca affiche un chemin, conda est actif
# Si ca dit "not found", conda n'est pas actif
```

### Test 2 : Le prompt montre-t-il "(base)" ?

```bash
# Si votre prompt ressemble a :
(base) user@machine:~$

# Alors conda est actif et vous etes dans l'environnement "base"
```

### Test 3 : Regarder le .bashrc

```bash
# Ouvrir le fichier
code ~/.bashrc
# ou sur macOS avec zsh :
code ~/.zshrc
```

Cherchez des blocs comme :

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/user/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    # ...
fi
unset __conda_setup
# <<< conda initialize <<<
```

**Si vous voyez ce bloc PLUSIEURS FOIS** = probleme de configuration multiple !

## Procedure de desactivation complete

### Etape 1 : Desactiver conda temporairement

```bash
# Desactiver l'environnement courant
conda deactivate

# Desactiver completement pour cette session
conda config --set auto_activate_base false
```

### Etape 2 : Retirer conda init du .bashrc

1. Ouvrez votre fichier de config :
   ```bash
   code ~/.bashrc   # Linux/Windows
   code ~/.zshrc    # macOS
   ```

2. Trouvez et **supprimez** ou commentez tous les blocs `conda initialize` :
   ```bash
   # >>> conda initialize >>>
   # ... tout ce bloc ...
   # <<< conda initialize <<<
   ```

3. **Important** : Si le bloc apparait plusieurs fois, supprimez TOUTES les occurrences.

4. Sauvegardez le fichier

### Etape 3 : Nettoyer le PATH

Dans le meme fichier, cherchez des lignes qui ajoutent conda au PATH :

```bash
# Lignes a supprimer si presentes :
export PATH="/home/user/miniconda3/bin:$PATH"
export PATH="/home/user/anaconda3/bin:$PATH"
export PATH="$HOME/miniconda3/condabin:$PATH"
```

### Etape 4 : Verifier

Fermez le terminal et ouvrez-en un nouveau :

```bash
# Verifier que conda n'est plus actif
which conda
# Doit dire "not found" ou ne rien afficher

# Verifier que le prompt n'a plus "(base)"
# Votre prompt doit ressembler a :
user@machine:~$
# Et PAS a :
(base) user@machine:~$
```

### Etape 5 (optionnelle) : Supprimer completement Conda

Si vous etes sur de ne plus avoir besoin de Conda :

```bash
# Supprimer le dossier conda (ATTENTION : irreversible !)
rm -rf ~/miniconda3
# ou
rm -rf ~/anaconda3

# Supprimer les fichiers de config conda
rm -rf ~/.conda
rm -rf ~/.condarc
```

## Script de diagnostic automatique

Copiez-collez ce script pour diagnostiquer votre configuration :

```bash
echo "=== DIAGNOSTIC CONDA ==="
echo ""
echo "1. Conda dans PATH ?"
which conda 2>/dev/null && echo "   -> OUI, conda est dans le PATH" || echo "   -> NON, conda n'est pas dans le PATH"
echo ""
echo "2. Python utilise ?"
which python
python --version 2>/dev/null
echo ""
echo "3. Blocs conda init dans .bashrc ?"
grep -c "conda initialize" ~/.bashrc 2>/dev/null && echo "   -> Blocs trouves dans .bashrc" || echo "   -> Aucun bloc dans .bashrc"
grep -c "conda initialize" ~/.zshrc 2>/dev/null && echo "   -> Blocs trouves dans .zshrc" || echo "   -> Aucun bloc dans .zshrc"
echo ""
echo "4. Variable CONDA_PREFIX ?"
echo "   CONDA_PREFIX = $CONDA_PREFIX"
[ -z "$CONDA_PREFIX" ] && echo "   -> Non defini (OK)" || echo "   -> Defini (conda actif !)"
echo ""
echo "=== FIN DIAGNOSTIC ==="
```

---

# Partie 4 : Environnements virtuels (venv)

## Pourquoi des environnements virtuels ?

**Probleme** : Tous vos projets partagent le meme Python et les memes packages.

```
Projet A : necessite requests==2.25
Projet B : necessite requests==2.31
           ^
           Conflit !
```

**Solution** : Chaque projet a son propre **environnement virtuel** avec ses propres packages.

## Schema : Sans vs Avec venv

```
SANS environnement virtuel :
+------------------+
| Python global    |
| numpy 1.20       |   <-- Partage par TOUS les projets
| requests 2.25    |   <-- Un seul peut gagner !
+------------------+
     ^      ^
     |      |
Projet A  Projet B


AVEC environnements virtuels :
+------------------+     +------------------+
| Projet A/.venv   |     | Projet B/.venv   |
| numpy 1.20       |     | numpy 1.26       |  <-- Versions differentes OK !
| requests 2.25    |     | requests 2.31    |
+------------------+     +------------------+
```

## Creer un environnement virtuel avec UV

```bash
# Dans votre projet
cd mon-projet

# Creer le venv
uv venv

# Cette commande cree un dossier .venv/ contenant :
# - Une copie de Python
# - pip
# - Un espace pour installer des packages
```

## Activer l'environnement

**Linux / macOS / Git Bash :**
```bash
source .venv/bin/activate
```

**Windows (PowerShell)** :
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (CMD)** :
```cmd
.venv\Scripts\activate.bat
```

### Comment savoir si le venv est actif ?

Le prompt change pour montrer le nom du venv :

```bash
# Avant activation :
user@machine:~/mon-projet$

# Apres activation :
(.venv) user@machine:~/mon-projet$
```

## Desactiver l'environnement

```bash
deactivate
```

## Workflow typique avec UV

```bash
# 1. Creer un projet
uv init mon-projet
cd mon-projet

# 2. Le venv est cree automatiquement par uv init
#    mais vous pouvez aussi faire : uv venv

# 3. Installer des dependances
uv add requests numpy

# 4. Lancer votre code
uv run python main.py
```

## Eviter de taper `uv run` a chaque fois

Taper `uv run python ...` a chaque fois peut etre fastidieux.

**Solution : activer le venv une fois, puis utiliser `python` directement.**

```bash
# Activer le venv (a faire une fois par session terminal)
source .venv/bin/activate   # Linux/macOS/Git Bash

# Maintenant vous pouvez utiliser python directement !
python main.py              # au lieu de: uv run python main.py
python                      # lance l'interpreteur
pip list                    # voir les packages installes
```

### Comment savoir si le venv est actif ?

Regardez votre prompt :

```bash
# AVANT activation :
user@machine:~/projet$

# APRES activation :
(.venv) user@machine:~/projet$
#  ^
#  Le nom du venv apparait !
```

### Desactiver le venv

```bash
deactivate
```

### Recapitulatif

| Methode | Commande | Quand l'utiliser |
|---------|----------|------------------|
| Avec `uv run` | `uv run python main.py` | Commande ponctuelle, pas besoin d'activer |
| Avec activation | `source .venv/bin/activate` puis `python main.py` | Session de travail prolongee |

**Conseil** : Pour une session de travail, activez le venv au debut. Vous pourrez ensuite utiliser `python` normalement sans prefixe.

## Bonne pratique : .gitignore

Ne commitez **jamais** le dossier `.venv` dans git !

```bash
# Ajouter au .gitignore
echo ".venv/" >> .gitignore
```

---

# Partie 5 : Configuration VS Code avec venv

## Selectionner l'interpreteur Python

VS Code doit savoir quel Python utiliser parmi ceux installes sur votre machine.

### Methode 1 : Palette de commandes

1. Ouvrez votre projet dans VS Code : `code .`
2. Appuyez sur `Ctrl+Shift+P` (ou `Cmd+Shift+P` sur Mac)
3. Tapez : `Python: Select Interpreter`
4. Choisissez celui dans `.venv` :
   ```
   Python 3.12.0 ('.venv': venv)
   ./venv/bin/python
   ```

### Methode 2 : Barre de status

1. Regardez en bas a droite de VS Code
2. Cliquez sur la version Python affichee
3. Selectionnez l'interpreteur du venv

## Configuration permanente (settings.json)

Pour que VS Code utilise toujours le venv du projet :

1. Creez le dossier `.vscode` dans votre projet
2. Creez le fichier `.vscode/settings.json` :

```json
{
    "python.defaultInterpreterPath": ".venv/bin/python",
    "python.terminal.activateEnvironment": true
}
```

**Sur Windows**, le chemin est different :
```json
{
    "python.defaultInterpreterPath": ".venv\\Scripts\\python.exe",
    "python.terminal.activateEnvironment": true
}
```

## Configuration globale (tous les projets)

Pour appliquer ces reglages a tous vos projets :

1. `Ctrl+Shift+P` -> `Preferences: Open User Settings (JSON)`
2. Ajoutez :

```json
{
    "python.terminal.activateEnvironment": true,
    "python.defaultInterpreterPath": ".venv/bin/python"
}
```

## Verifier que VS Code utilise le bon Python

1. Ouvrez un terminal dans VS Code : `Ctrl+`` (backtick)
2. Verifiez :
   ```bash
   which python
   # Doit afficher : /chemin/vers/votre-projet/.venv/bin/python
   
   python --version
   # Doit afficher la version de votre venv
   ```

## Schema : VS Code + venv

```
+----------------------------------+
|  VS Code                         |
|                                  |
|  +----------------------------+  |
|  | Terminal integre           |  |
|  | (.venv) user:~/projet$     |  |  <-- venv active !
|  +----------------------------+  |
|                                  |
|  Barre de status :               |
|  [Python 3.12.0 ('.venv': venv)] |  <-- Bon interpreteur
|                                  |
+----------------------------------+
```

## Problemes courants

### "Python n'est pas reconnu"

1. Verifiez que le venv existe : `ls .venv`
2. Recreez-le si necessaire : `uv venv`
3. Rechargez VS Code : `Ctrl+Shift+P` -> `Developer: Reload Window`

### "Import could not be resolved"

VS Code ne trouve pas les modules installes :

1. Verifiez l'interpreteur selectionne (barre de status)
2. Installez les modules : `uv add nom_du_module`
3. Rechargez VS Code

### Le terminal n'active pas le venv automatiquement

Ajoutez dans `.vscode/settings.json` :

```json
{
    "python.terminal.activateEnvironment": true
}
```

---

# Partie 6 : Desinstallation

## Desinstaller UV

Si vous souhaitez supprimer UV de votre systeme :

### Etape 1 : Supprimer l'executable

**Linux / macOS / Git Bash :**
```bash
rm -rf ~/.local/bin/uv
rm -rf ~/.local/bin/uvx
```

**Windows (PowerShell)** :
```powershell
Remove-Item "$env:USERPROFILE\.local\bin\uv.exe" -Force
Remove-Item "$env:USERPROFILE\.local\bin\uvx.exe" -Force
```

### Etape 2 : Supprimer le cache UV (optionnel)

```bash
rm -rf ~/.cache/uv
```

### Etape 3 : Nettoyer le PATH (optionnel)

Si vous aviez ajoute `.local/bin` au PATH uniquement pour UV, vous pouvez le retirer de votre `~/.bashrc` :

```bash
# Editez le fichier et supprimez la ligne :
# export PATH="$HOME/.local/bin:$PATH"
code ~/.bashrc
```

## Desinstaller VS Code

**Windows** :
- Parametres > Applications > Visual Studio Code > Desinstaller

**macOS** :
- Glissez `/Applications/Visual Studio Code.app` vers la corbeille
- Supprimez les donnees : `rm -rf ~/Library/Application\ Support/Code`

**Linux** :
```bash
sudo apt remove code  # Debian/Ubuntu
# ou
sudo dnf remove code  # Fedora
```

## Desinstaller Git (Windows)

- Parametres > Applications > Git > Desinstaller

---

## Ressources supplementaires

- [Documentation UV](https://docs.astral.sh/uv/)
- [Documentation VS Code Python](https://code.visualstudio.com/docs/python/environments)
- [Site du cours](https://python.info-mines.paris)

---

*Document cree pour le cours Python - Mines Paris*
