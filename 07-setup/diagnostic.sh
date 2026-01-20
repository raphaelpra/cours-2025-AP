#!/bin/bash
# Script de diagnostic pour l'environnement Python
# Usage: bash diagnostic.sh

echo "=========================================="
echo "   DIAGNOSTIC ENVIRONNEMENT PYTHON"
echo "   Cours Python - Mines Paris"
echo "=========================================="
echo ""

# Couleurs (si le terminal les supporte)
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

ok() {
    echo -e "${GREEN}[OK]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[ATTENTION]${NC} $1"
}

fail() {
    echo -e "${RED}[ERREUR]${NC} $1"
}

# --- Systeme ---
echo "=== SYSTEME ==="
echo "OS: $(uname -s)"
echo "Shell: $SHELL"
echo "Home: $HOME"
echo ""

# --- Git ---
echo "=== GIT ==="
if command -v git &> /dev/null; then
    ok "Git installe: $(git --version)"
else
    fail "Git NON INSTALLE !"
    echo "    -> Installer Git: https://git-scm.com/downloads"
fi
echo ""

# --- VS Code ---
echo "=== VS CODE ==="
if command -v code &> /dev/null; then
    ok "VS Code dans le PATH: $(code --version | head -1)"
else
    fail "VS Code NON DANS LE PATH !"
    echo "    -> Sur Mac: Cmd+Shift+P > 'Shell Command: Install code command in PATH'"
    echo "    -> Sur Windows: Reinstaller avec l'option 'Add to PATH'"
fi
echo ""

# --- UV ---
echo "=== UV ==="
if command -v uv &> /dev/null; then
    ok "UV installe: $(uv --version)"
else
    fail "UV NON INSTALLE !"
    echo "    -> Installer: curl -LsSf https://astral.sh/uv/install.sh | sh"
fi
echo ""

# --- Python ---
echo "=== PYTHON ==="
if command -v python &> /dev/null; then
    ok "Python: $(python --version)"
    echo "    Emplacement: $(which python)"
    
    # Verifier si c'est le Python de conda
    python_path=$(which python)
    if [[ "$python_path" == *"conda"* ]] || [[ "$python_path" == *"miniconda"* ]] || [[ "$python_path" == *"anaconda"* ]]; then
        warn "Python vient de Conda ! Voir section desactivation Conda."
    fi
else
    warn "Python non trouve directement (normal si vous utilisez UV)"
    echo "    -> Utilisez: uv run python --version"
fi
echo ""

# --- Conda (doit etre desactive) ---
echo "=== CONDA (devrait etre desactive) ==="
if command -v conda &> /dev/null; then
    fail "Conda est encore ACTIF !"
    echo "    Emplacement: $(which conda)"
    if [ -n "$CONDA_PREFIX" ]; then
        echo "    Environnement actif: $CONDA_PREFIX"
    fi
    echo ""
    echo "    ACTIONS REQUISES:"
    echo "    1. conda deactivate"
    echo "    2. conda config --set auto_activate_base false"
    echo "    3. Supprimer les blocs 'conda initialize' de ~/.bashrc"
else
    ok "Conda desactive"
fi

# Verifier CONDA_PREFIX meme si conda n'est pas dans PATH
if [ -n "$CONDA_PREFIX" ]; then
    warn "Variable CONDA_PREFIX definie: $CONDA_PREFIX"
    echo "    -> Un environnement conda est actif en arriere-plan"
fi
echo ""

# --- Fichiers de configuration ---
echo "=== FICHIERS DE CONFIGURATION ==="
if [ -f ~/.bashrc ]; then
    ok ".bashrc existe"
    
    # Compter les blocs conda
    conda_blocks=$(grep -c "conda initialize" ~/.bashrc 2>/dev/null || echo "0")
    if [ "$conda_blocks" -gt "0" ]; then
        fail "$conda_blocks bloc(s) 'conda initialize' dans .bashrc !"
        echo "    -> Editez ~/.bashrc et supprimez ces blocs"
    else
        ok "Pas de bloc conda dans .bashrc"
    fi
else
    warn ".bashrc n'existe pas (normal sur certains systemes)"
fi

if [ -f ~/.zshrc ]; then
    ok ".zshrc existe"
    
    conda_blocks=$(grep -c "conda initialize" ~/.zshrc 2>/dev/null || echo "0")
    if [ "$conda_blocks" -gt "0" ]; then
        fail "$conda_blocks bloc(s) 'conda initialize' dans .zshrc !"
        echo "    -> Editez ~/.zshrc et supprimez ces blocs"
    else
        ok "Pas de bloc conda dans .zshrc"
    fi
else
    echo "    .zshrc n'existe pas"
fi
echo ""

# --- PATH ---
echo "=== PATH (5 premiers elements) ==="
echo $PATH | tr ':' '\n' | head -5
echo "..."
echo ""

# Verifier si conda est dans le PATH
if echo $PATH | grep -q -E "(conda|miniconda|anaconda)"; then
    warn "Des chemins conda sont presents dans le PATH !"
    echo "    Chemins conda trouves:"
    echo $PATH | tr ':' '\n' | grep -E "(conda|miniconda|anaconda)"
fi
echo ""

# --- Resume ---
echo "=========================================="
echo "   RESUME"
echo "=========================================="

errors=0

command -v git &> /dev/null || ((errors++))
command -v code &> /dev/null || ((errors++))
command -v uv &> /dev/null || ((errors++))
command -v conda &> /dev/null && ((errors++))
[ -n "$CONDA_PREFIX" ] && ((errors++))

bashrc_conda=$(grep -c "conda initialize" ~/.bashrc 2>/dev/null || echo "0")
zshrc_conda=$(grep -c "conda initialize" ~/.zshrc 2>/dev/null || echo "0")
[ "$bashrc_conda" -gt "0" ] && ((errors++))
[ "$zshrc_conda" -gt "0" ] && ((errors++))

if [ "$errors" -eq "0" ]; then
    echo -e "${GREEN}Tout semble correct !${NC}"
else
    echo -e "${RED}$errors probleme(s) detecte(s)${NC}"
    echo "Consultez FAQ-SETUP.md pour les solutions."
fi

echo ""
echo "=========================================="
echo "   FIN DU DIAGNOSTIC"
echo "=========================================="
