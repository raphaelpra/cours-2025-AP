# FAQ - Problemes d'installation courants

Ce document recense les problemes les plus frequents lors de l'installation et leurs solutions.

---

## Checklist de validation

Avant de continuer, verifiez que tout fonctionne :

```bash
# 1. Git Bash (Windows) ou Terminal (Mac/Linux)
echo $BASH_VERSION  # Doit afficher 5.x.x ou plus

# 2. Git
git --version       # Doit afficher git version 2.x.x

# 3. VS Code
code --version      # Doit afficher un numero de version

# 4. UV
uv --version        # Doit afficher uv 0.x.x

# 5. Python via UV
uv run python --version  # Doit afficher Python 3.x.x

# 6. Conda desactive (important !)
which conda         # Doit dire "not found" ou ne rien afficher
echo $CONDA_PREFIX  # Doit etre vide
```

Si toutes ces commandes fonctionnent, votre setup est correct !

---

## Problemes Git Bash / Terminal

### "bash: command not found" pour n'importe quelle commande

**Cause** : Le terminal n'est pas bash ou le PATH est corrompu.

**Solution Windows** :
1. Verifiez que vous utilisez **Git Bash** et pas PowerShell ou CMD
2. Cherchez "Git Bash" dans le menu demarrer
3. Si Git Bash n'existe pas, reinstallez Git for Windows

**Solution Mac/Linux** :
```bash
# Verifier votre shell
echo $SHELL

# Si ce n'est pas bash ou zsh, changez :
chsh -s /bin/bash
# puis ouvrez un nouveau terminal
```

### Le terminal demarre dans un dossier bizarre (pas le home)

**Cause** : Raccourci mal configure (Windows) ou config corrompue.

**Solution Windows** :
1. Supprimez le raccourci Git Bash de la barre des taches
2. Cherchez "Git Bash" dans le menu demarrer
3. Clic droit -> "Epingler a la barre des taches"

**Solution tous OS** :
Ajoutez en debut de `~/.bashrc` :
```bash
cd ~
```

### "pwd" affiche un chemin avec des espaces et ca pose probleme

**Cause** : Votre nom d'utilisateur contient des espaces ou accents.

**Solution** : Evitez d'avoir des projets dans des chemins avec espaces.
```bash
# Creer un dossier de travail sans espaces
mkdir -p /c/dev  # Windows
mkdir -p ~/dev   # Mac/Linux

# Travailler depuis ce dossier
cd /c/dev  # ou ~/dev
```

---

## Problemes VS Code

### "code: command not found"

**Cause** : L'installation de VS Code ne s'est pas bien passee.

La commande `code` est configuree **automatiquement** lors de l'installation. Si elle ne fonctionne pas → **reinstallez VS Code**.

**Solution Windows** :
1. Desinstallez VS Code (Parametres > Applications)
2. Reinstallez depuis [code.visualstudio.com](https://code.visualstudio.com/)
3. **Cochez ces options** pendant l'installation :
   - [x] Add "Open with Code" action to file context menu
   - [x] Add "Open with Code" action to directory context menu
   - [x] **Add to PATH** (crucial !)
4. Ouvrez un **nouveau** terminal Git Bash
5. Testez : `code --version`

**Solution macOS** :
1. Verifiez que VS Code est dans `/Applications/` (pas dans Downloads !)
2. Ouvrez VS Code
3. `Cmd+Shift+P` -> "Shell Command: Install 'code' command in PATH"
4. Ouvrez un **nouveau** terminal

### VS Code ne trouve pas Python / "Python not found"

**Cause** : L'interpreteur Python n'est pas selectionne.

**Solution** :
1. Ouvrez votre projet : `code .`
2. `Ctrl+Shift+P` -> "Python: Select Interpreter"
3. Choisissez l'interpreteur dans `.venv` si disponible
4. Sinon, installez l'extension Python de Microsoft

### "Import could not be resolved" (erreurs Pylance)

**Cause** : Mauvais interpreteur ou package non installe.

**Solution** :
1. Verifiez l'interpreteur (voir ci-dessus)
2. Installez le package : `uv add nom_du_package`
3. Rechargez VS Code : `Ctrl+Shift+P` -> "Developer: Reload Window"

### Le terminal de VS Code utilise PowerShell au lieu de Bash (Windows)

**Cause** : Configuration par defaut de VS Code.

**Solution** :
1. `Ctrl+Shift+P` -> "Terminal: Select Default Profile"
2. Choisissez "Git Bash"
3. Fermez et rouvrez le terminal

---

## Problemes UV

### "uv: command not found"

**Cause** : UV n'est pas installe ou pas dans le PATH.

**Solution** :
```bash
# Reinstaller UV
curl -LsSf https://astral.sh/uv/install.sh | sh

# Recharger le PATH
source ~/.bashrc  # ou ~/.zshrc sur Mac

# Ou ouvrir un nouveau terminal
```

### "error: No `pyproject.toml` found"

**Cause** : Vous n'etes pas dans un projet UV ou le projet n'est pas initialise.

**Solution** :
```bash
# Verifier que vous etes dans le bon dossier
pwd
ls  # Doit montrer les fichiers de votre projet

# Initialiser le projet si necessaire
uv init
```

### "error: Failed to download Python"

**Cause** : Probleme de connexion ou de permissions.

**Solution** :
```bash
# Verifier la connexion internet
curl -I https://astral.sh

# Si probleme de certificat (entreprise/proxy) :
curl -k -LsSf https://astral.sh/uv/install.sh | sh

# Si probleme de permissions :
chmod +x ~/.local/bin/uv
```

### Les packages ne s'installent pas / "No solution found"

**Cause** : Conflit de versions ou package inexistant.

**Solution** :
```bash
# Verifier le nom exact du package
uv search nom_package  # ou chercher sur pypi.org

# Forcer une version specifique
uv add "requests>=2.25,<3.0"

# Supprimer le cache et recommencer
rm -rf ~/.cache/uv
uv sync
```

---

## Problemes Conda / Python

### "(base)" apparait toujours dans le prompt

**Cause** : Conda est encore actif malgre vos efforts.

**Solution complete** :
```bash
# 1. Desactiver
conda deactivate

# 2. Empecher l'activation automatique
conda config --set auto_activate_base false

# 3. Ouvrir le fichier de config
code ~/.bashrc  # ou ~/.zshrc

# 4. Supprimer TOUS les blocs conda (peut apparaitre plusieurs fois !)
# >>> conda initialize >>>
# ... tout ce bloc ...
# <<< conda initialize <<<

# 5. Sauvegarder et ouvrir un nouveau terminal
```

### "python: command not found" apres avoir desactive Conda

**Cause** : Python etait fourni par Conda, maintenant il n'y a plus de Python.

**Solution** :
```bash
# Utiliser UV pour gerer Python
uv venv  # Cree un venv avec Python

# Ou lancer Python via UV
uv run python --version
```

### Plusieurs versions de Python se melangent

**Cause** : PATH mal configure avec plusieurs sources Python.

**Diagnostic** :
```bash
# Voir tous les Python disponibles
which -a python
which -a python3

# Voir le PATH complet
echo $PATH | tr ':' '\n'
```

**Solution** :
Nettoyer le PATH dans `~/.bashrc` en ne gardant qu'une seule source Python (UV).

### "ModuleNotFoundError: No module named 'xxx'"

**Cause** : Le module n'est pas installe dans le bon environnement.

**Solution** :
```bash
# Verifier quel Python est utilise
which python

# S'assurer d'etre dans le bon venv
source .venv/bin/activate

# Installer le module
uv add xxx

# Ou avec pip si necessaire
uv pip install xxx
```

---

## Problemes de configuration (.bashrc / .zshrc)

### Je ne trouve pas mon fichier .bashrc

**Rappel des emplacements** :
- **Linux** : `~/.bashrc` (toujours bash)
- **macOS** : `~/.zshrc` (zsh par defaut depuis Catalina) ou `~/.bashrc` (si bash)
- **Windows Git Bash** : `~/.bashrc` (dans `/c/Users/VotreNom/`)

**Pour voir les fichiers caches** :
```bash
ls -la ~  # Le -a montre les fichiers caches (commencant par .)
```

**Si le fichier n'existe pas** :
```bash
touch ~/.bashrc  # Cree un fichier vide
```

### Windows/Git Bash : .bashrc existe mais n'est pas charge !

**Cause** : Sur Git Bash, le fichier `.bash_profile` est lu EN PREMIER. Si `.bash_profile` existe mais ne charge pas `.bashrc`, vos configurations sont ignorees.

**Diagnostic** :
```bash
# Verifier quels fichiers existent
ls -la ~ | grep bash

# Verifier si .bash_profile charge .bashrc
cat ~/.bash_profile | grep bashrc
```

**Solution** :
```bash
# Creer les fichiers s'ils n'existent pas
touch ~/.bashrc
touch ~/.bash_profile

# Ajouter le chargement de .bashrc dans .bash_profile
# (seulement si pas deja present)
grep -q "source ~/.bashrc" ~/.bash_profile || echo 'source ~/.bashrc' >> ~/.bash_profile

# Recharger
source ~/.bash_profile
```

**Ordre de chargement sur Git Bash** :
```
1. ~/.bash_profile  (lu en premier, s'il existe)
2. ~/.bashrc        (lu seulement si .bash_profile le charge !)
```

C'est pourquoi on ajoute `source ~/.bashrc` dans `.bash_profile`.

### Les modifications du .bashrc ne prennent pas effet

**Cause** : Le terminal n'a pas recharge le fichier.

**Solution** :
```bash
# Option 1 : Recharger manuellement
source ~/.bashrc

# Option 2 : Ouvrir un nouveau terminal

# Option 3 (Mac avec zsh) : Mauvais fichier
source ~/.zshrc  # Utilisez zshrc, pas bashrc !
```

### Mon .bashrc est corrompu / plein d'erreurs

**Solution** : Creer une sauvegarde et repartir proprement.
```bash
# Sauvegarder l'ancien
cp ~/.bashrc ~/.bashrc.backup

# Creer un nouveau fichier minimal
cat > ~/.bashrc << 'EOF'
# Configuration minimale

# PATH pour les programmes locaux
export PATH="$HOME/.local/bin:$PATH"

# Alias utiles
alias ll='ls -la'
alias gs='git status'

# Prompt simple
PS1='\u@\h:\w\$ '
EOF

# Ouvrir un nouveau terminal pour tester
```

### J'ai lance "conda init" plusieurs fois et c'est le chaos

**Diagnostic** :
```bash
# Compter les blocs conda
grep -c "conda initialize" ~/.bashrc

# Si > 1, il y a des doublons !
```

**Solution** :
```bash
# Ouvrir le fichier
code ~/.bashrc

# Supprimer TOUS les blocs entre :
# >>> conda initialize >>>
# et
# <<< conda initialize <<<

# Ne garder AUCUN bloc conda !
```

---

## Problemes specifiques Windows

### Git Bash ne reconnait pas les accents dans les noms de fichiers

**Solution** :
```bash
# Ajouter dans ~/.bashrc
export LANG=fr_FR.UTF-8
export LC_ALL=fr_FR.UTF-8
```

### Les chemins Windows vs Unix

**Correspondances** :
| Windows | Git Bash |
|---------|----------|
| `C:\Users\Jean` | `/c/Users/Jean` |
| `D:\projets` | `/d/projets` |
| `\\serveur\partage` | `/mnt/serveur/partage` |

### "Permission denied" lors de l'installation

**Cause** : Tentative d'ecrire dans un dossier systeme.

**Solution** : Utilisez les options "User Install" (pas de droits admin necessaires).

---

## Problemes specifiques macOS

### "xcrun: error: invalid active developer path"

**Cause** : Xcode Command Line Tools pas installe.

**Solution** :
```bash
xcode-select --install
```

### "zsh: command not found" apres installation

**Cause** : Sur Mac recent, le shell par defaut est zsh, pas bash.

**Solution** :
Ajoutez vos configurations dans `~/.zshrc` au lieu de `~/.bashrc`.

### Problemes avec les cles SSH

**Si `ssh-keygen` demande une passphrase** : Vous pouvez la laisser vide pour simplifier.

**Pour ajouter la cle a GitHub** :
```bash
# Copier la cle publique
cat ~/.ssh/id_ed25519.pub | pbcopy

# Puis coller sur github.com/settings/keys
```

---

## Script de diagnostic complet

Executez ce script pour un diagnostic complet de votre installation :

```bash
#!/bin/bash
echo "=========================================="
echo "   DIAGNOSTIC ENVIRONNEMENT PYTHON"
echo "=========================================="
echo ""

echo "--- Systeme ---"
echo "OS: $(uname -s)"
echo "Shell: $SHELL"
echo "Home: $HOME"
echo ""

echo "--- Git ---"
if command -v git &> /dev/null; then
    echo "Git: $(git --version)"
else
    echo "Git: NON INSTALLE !"
fi
echo ""

echo "--- VS Code ---"
if command -v code &> /dev/null; then
    echo "VS Code: $(code --version | head -1)"
else
    echo "VS Code: NON DANS LE PATH !"
fi
echo ""

echo "--- UV ---"
if command -v uv &> /dev/null; then
    echo "UV: $(uv --version)"
else
    echo "UV: NON INSTALLE !"
fi
echo ""

echo "--- Python ---"
if command -v python &> /dev/null; then
    echo "Python: $(python --version)"
    echo "Emplacement: $(which python)"
else
    echo "Python: NON DANS LE PATH"
fi
echo ""

echo "--- Conda (devrait etre desactive) ---"
if command -v conda &> /dev/null; then
    echo "ATTENTION: Conda est encore actif !"
    echo "Emplacement: $(which conda)"
    echo "Environnement: $CONDA_PREFIX"
else
    echo "Conda: Desactive (OK)"
fi
echo ""

echo "--- PATH ---"
echo "Premiers elements du PATH :"
echo $PATH | tr ':' '\n' | head -5
echo ""

echo "--- Fichiers de config ---"
[ -f ~/.bashrc ] && echo ".bashrc: existe" || echo ".bashrc: n'existe pas"
[ -f ~/.zshrc ] && echo ".zshrc: existe" || echo ".zshrc: n'existe pas"
echo ""

echo "--- Blocs conda dans les configs ---"
bashrc_conda=$(grep -c "conda initialize" ~/.bashrc 2>/dev/null || echo "0")
zshrc_conda=$(grep -c "conda initialize" ~/.zshrc 2>/dev/null || echo "0")
echo "Blocs conda dans .bashrc: $bashrc_conda"
echo "Blocs conda dans .zshrc: $zshrc_conda"
[ "$bashrc_conda" -gt "0" ] && echo "ATTENTION: Conda toujours configure dans .bashrc !"
[ "$zshrc_conda" -gt "0" ] && echo "ATTENTION: Conda toujours configure dans .zshrc !"
echo ""

echo "=========================================="
echo "   FIN DU DIAGNOSTIC"
echo "=========================================="
```

**Pour l'executer** :
```bash
# Copiez le script dans un fichier
code diagnostic.sh
# Collez, sauvegardez, puis :
bash diagnostic.sh
```

---

## Obtenir de l'aide

Si aucune solution ne fonctionne :

1. **Notez l'erreur exacte** (copiez-collez le message)
2. **Executez le script de diagnostic** et copiez le resultat
3. **Demandez de l'aide** sur Discord ou en cours

**Informations utiles a fournir** :
- Votre OS (Windows 10/11, macOS version, Linux distribution)
- Le message d'erreur exact
- Les commandes que vous avez tapees
- Le resultat du script de diagnostic

---

*Document cree pour le cours Python - Mines Paris*
