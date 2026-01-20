# Debugger Python avec VS Code

Le debugger permet d'executer votre code **pas a pas** pour comprendre ce qui se passe et trouver les bugs.

---

## Pourquoi utiliser le debugger ?

| Methode | Avantages | Inconvenients |
|---------|-----------|---------------|
| `print()` | Simple, rapide | Pollution du code, fastidieux |
| **Debugger** | Interactif, puissant, propre | Necessite un peu de setup |

Le debugger permet de :
- **Arreter** l'execution a un endroit precis (breakpoint)
- **Inspecter** les variables a ce moment
- **Avancer** pas a pas dans le code
- **Comprendre** le flux d'execution

---

## Configuration VS Code

### 1. Installer l'extension Python

Si ce n'est pas deja fait :
- `Ctrl+Shift+X` -> chercher "Python" (Microsoft)
- Installer

### 2. Ouvrir un fichier Python

```bash
code mon_script.py
```

### 3. Selectionner l'interpreteur Python

- `Ctrl+Shift+P` -> `Python: Select Interpreter`
- Choisir celui dans `.venv` si vous utilisez un venv

---

## Utilisation du debugger

### Etape 1 : Poser un breakpoint

Cliquez dans la **marge gauche** (a cote du numero de ligne) pour ajouter un point rouge.

```
    1 | def calcul(x):
  * 2 |     result = x * 2      <-- breakpoint ici (point rouge)
    3 |     return result
    4 |
    5 | print(calcul(5))
```

### Etape 2 : Lancer le debugger

Plusieurs methodes :
- **F5** (raccourci clavier)
- Menu **Run** -> **Start Debugging**
- Cliquer sur **Run and Debug** dans la barre laterale gauche

### Etape 3 : Choisir la configuration

A la premiere utilisation, VS Code demande quelle configuration utiliser :
- Choisissez **"Python File"** pour debugger le fichier courant

### Etape 4 : Explorer !

Quand le code atteint le breakpoint, l'execution s'arrete et vous pouvez :

**Inspecter les variables** (panneau gauche "Variables") :
```
Variables:
  x = 5
  result = 10
```

**Utiliser la console de debug** (en bas) :
```python
>>> x + 100
105
>>> result * 2
20
```

---

## Controles du debugger

Une barre d'outils apparait en haut :

| Icone | Raccourci | Action |
|-------|-----------|--------|
| ▶️ Continue | F5 | Continuer jusqu'au prochain breakpoint |
| ⏭️ Step Over | F10 | Executer la ligne et passer a la suivante |
| ⬇️ Step Into | F11 | Entrer dans la fonction appelee |
| ⬆️ Step Out | Shift+F11 | Sortir de la fonction actuelle |
| 🔄 Restart | Ctrl+Shift+F5 | Relancer le debug |
| ⏹️ Stop | Shift+F5 | Arreter le debug |

### Difference entre Step Over et Step Into

```python
def helper(x):
    return x * 2

def main():
    a = 5
    b = helper(a)  # <-- breakpoint ici
    print(b)
```

- **Step Over (F10)** : execute `helper(a)` en entier, passe a `print(b)`
- **Step Into (F11)** : entre dans la fonction `helper`, ligne par ligne

---

## Exemple pratique

### Code avec un bug

```python
def moyenne(notes):
    total = 0
    for note in notes:
        total += note
    return total / len(notes)

resultat = moyenne([15, 12, 18, 14])
print(f"Moyenne: {resultat}")
```

### Debugger pour comprendre

1. Posez un breakpoint sur `total += note`
2. Lancez le debugger (F5)
3. A chaque iteration, inspectez :
   - La valeur de `note`
   - La valeur de `total`
4. Utilisez F10 pour avancer iteration par iteration

---

## Configuration avancee (launch.json)

Pour des besoins specifiques, creez `.vscode/launch.json` :

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Fichier courant",
            "type": "debugpy",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "cwd": "${workspaceFolder}"
        },
        {
            "name": "Python: main.py",
            "type": "debugpy",
            "request": "launch",
            "program": "${workspaceFolder}/main.py",
            "console": "integratedTerminal",
            "args": ["--verbose", "input.txt"]
        }
    ]
}
```

### Options utiles

| Option | Description |
|--------|-------------|
| `program` | Fichier a executer |
| `args` | Arguments de ligne de commande |
| `cwd` | Dossier de travail |
| `env` | Variables d'environnement |
| `console` | Terminal a utiliser |

---

## Breakpoints conditionnels

Clic droit sur un breakpoint -> **Edit Breakpoint** :

- **Expression** : s'arrete seulement si la condition est vraie
  ```python
  # S'arreter seulement quand i > 100
  i > 100
  ```

- **Hit Count** : s'arrete apres N passages
  ```
  # S'arreter a la 50eme iteration
  50
  ```

---

## Astuces

### Watch expressions

Dans le panneau "Watch", ajoutez des expressions a surveiller :
- `len(ma_liste)`
- `user.name`
- `total / count if count > 0 else 0`

### Debug d'une selection

Selectionnez du code, clic droit -> **Debug Selection in Python Terminal**

### Logpoints

Alternative aux breakpoints : clic droit -> **Add Logpoint**
Affiche un message sans arreter l'execution (comme un print temporaire).

---

## Raccourcis essentiels

| Action | Raccourci |
|--------|-----------|
| Lancer le debug | F5 |
| Step Over | F10 |
| Step Into | F11 |
| Step Out | Shift+F11 |
| Arreter | Shift+F5 |
| Toggle breakpoint | F9 |

---

## Debugger sans VS Code (pdb)

Python inclut un debugger integre : **pdb** (Python DeBugger).

### Ajouter un breakpoint dans le code

Ajoutez `breakpoint()` dans votre code a l'endroit ou vous voulez vous arreter :

```python
def calcul(x):
    result = x * 2
    breakpoint()  # <-- le programme s'arrete ici
    return result

print(calcul(5))
```

### Commandes pdb

Une fois dans le debugger, tapez ces commandes :

| Commande | Raccourci | Action |
|----------|-----------|--------|
| `next` | `n` | Executer la ligne suivante (Step Over) |
| `step` | `s` | Entrer dans la fonction (Step Into) |
| `continue` | `c` | Continuer jusqu'au prochain breakpoint |
| `return` | `r` | Continuer jusqu'au return de la fonction |
| `print(var)` | `p var` | Afficher la valeur d'une variable |
| `list` | `l` | Afficher le code autour de la ligne actuelle |
| `where` | `w` | Afficher la pile d'appels |
| `quit` | `q` | Quitter le debugger |

### Exemple de session

```
$ python mon_script.py
> /home/user/mon_script.py(4)calcul()
-> return result
(Pdb) p x
5
(Pdb) p result
10
(Pdb) n
--Return--
> /home/user/mon_script.py(4)calcul()->10
(Pdb) c
10
```

### Lancer directement en mode debug

```bash
python -m pdb mon_script.py
```

Le script demarre en mode debug des la premiere ligne.

---

*Ressource : [Documentation VS Code - Python Debugging](https://code.visualstudio.com/docs/python/debugging)*
