# AGENTS.md - Coding Agent Guidelines

This repository contains course materials for Python programming at Mines Paris.

## Repository Overview

- **Type**: Educational Python course repository
- **Language**: Python 3.14+ (French documentation/comments)
- **Structure**: Numbered folders per session (01-introduction, 02-premiers-pas, etc.)
- **Package Manager**: UV (modern Python environment manager)

## Build/Run Commands

### Running Python Files

```bash
# Direct execution
python3 <file>.py

# Or via UV (if project initialized)
uv run python <file>.py
```

### Running Tests

This project uses Python's built-in `unittest` framework.

```bash
# Run all tests in a directory
python3 -m unittest discover -v

# Run a single test file
python3 -m unittest test_vigenere -v

# Run a specific test class
python3 -m unittest test_vigenere.TestVigenere -v

# Run a single test method
python3 -m unittest test_vigenere.TestVigenere.test_encode_basic_example -v
```

### No Build Step

This is a pure Python repository with no build step required.

## Code Style Guidelines

### Language

- **Documentation**: French (this is a French course)
- **Variable names**: French or English (match existing file context)
- **Code comments**: French preferred for course materials

### File Naming

- Course materials: `programme.md`, `td-*.md`, `*-tp.md`
- Corrections: `correction-*.py` (gitignored)
- Personal files: `perso*` prefix (gitignored)
- Test files: `test_*.py`

### Python Style

#### Imports

```python
# Standard library first
import unittest
from itertools import cycle

# Third-party (if any)
import requests

# Local imports
from separate import hello_name, Person
import separate
```

#### Type Hints

Type hints are optional but encouraged for educational examples:

```python
names: list[str] = ["Alice", "Bob", "Charlie"]
var: int = 42

def hello_name(name: str) -> None:
    print(f"hello {name}")
```

#### Function Documentation

Use docstrings with clear explanations (educational context):

```python
def chiffrer_cesar(message, cle):
    """
    Chiffre un message avec le chiffre de César.

    Points cles :
    - Iteration sur chaque caractere (for c in message)
    - Construction progressive avec liste puis join
    - ord() et chr() pour conversions caractere <-> code ASCII
    """
```

#### String Building Pattern

Prefer list + join over string concatenation:

```python
# Good - O(n)
resultat = []
for caractere in message:
    resultat.append(transform(caractere))
return ''.join(resultat)

# Avoid - O(n^2)
resultat = ""
for caractere in message:
    resultat += transform(caractere)
```

#### Main Guard

Always use main guard for executable scripts:

```python
if __name__ == "__main__":
    main()
```

#### Error Handling

Use try/except for user input validation:

```python
while True:
    try:
        valeur = int(input("Cle (1-25) : "))
        if 1 <= valeur <= 25:
            break
        print("Erreur: Cle doit etre entre 1 et 25")
    except ValueError:
        print("Erreur: Entrez un nombre")
```

### Test Style (unittest)

```python
import unittest
from module import function

class TestFunction(unittest.TestCase):

    def test_basic_example(self):
        """Test the main example from spec"""
        result = function("input", param=True)
        self.assertEqual(result, "expected")

    def test_edge_case(self):
        """Test edge case behavior"""
        result = function("", param=True)
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()
```

## Project Structure

```
.
├── README.md                    # Student instructions
├── AGENTS.md                    # This file
├── 01-introduction/             # Session 1
│   ├── programme.md             # Session outline
│   ├── uv.md                    # UV setup guide
│   └── Discord.md               # Discord setup
├── 02-premiers-pas/             # Session 2
│   ├── programme.md
│   └── td-premiers-pas.md
├── 03-conteneurs-chaines/       # Session 3
│   ├── programme.md
│   └── td-pendu.md
├── 04-iterations/               # Session 4
│   ├── programme.md
│   ├── vigenere-tp.md           # TP instructions
│   └── test_vigenere.py         # Unit tests
└── perso/                       # Personal files (gitignored)
```

## Git Workflow

### Files to Never Commit

- `perso*` - Student personal files
- `**/perso/` - Personal directories
- `correction-*.py` - In-class corrections
- `Trombi.pdf` - Class roster
- `presences.csv` - Attendance

### Commit Messages

- Brief, no articles/pronouns
- Start with verb
- Example: `Add vigenere test cases`

## Agent-Specific Notes

### When Helping with Exercises

1. Check if solution exists in `correction-*.py` (gitignored but may exist locally)
2. Refer to `*-tp.md` or `td-*.md` for exercise specifications
3. Match the teaching style: explain concepts, use French comments

### When Writing Tests

- Use `unittest` framework (no pytest)
- Include docstrings explaining test purpose
- Test edge cases: empty strings, single characters, non-alphabetic chars

### Common Patterns in This Codebase

- Caesar/Vigenere ciphers use `ord()` and `chr()` with modulo 26
- Character iteration: `for c in string:`
- List building: `result = []; result.append(x); ''.join(result)`
- Input validation: while True + try/except pattern

### UV Environment

If UV project exists (pyproject.toml present):
```bash
uv venv          # Create virtual environment
uv add <package> # Add dependency
uv run python x  # Run in environment
uv sync          # Update dependencies
```
