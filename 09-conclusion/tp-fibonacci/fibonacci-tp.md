# TP - Fibonacci : approches multiples

## Preparation

Le projet est deja initialise avec UV. Pour installer les dependances :

```bash
cd 09-conclusion/tp-fibonacci
uv sync
```

Cela installe `pytest` (defini dans `pyproject.toml`).

Pour lancer les tests :

```bash
uv run pytest -v
```

---

## Introduction

La suite de Fibonacci est definie par :

- F(0) = 0
- F(1) = 1
- F(n) = F(n-1) + F(n-2) pour n >= 2

Les premiers termes : 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144...

Ce TP explore **5 facons differentes** d'implementer Fibonacci, chacune illustrant des concepts vus pendant le cours.

---

## Etape 0 : Ecrire les tests d'abord (TDD)

Avant d'ecrire la moindre ligne de code, on commence par les tests.

Un fichier `test_fibonacci.py` est deja fourni. Regardez son contenu :

```python
import pytest

# Valeurs de reference
EXPECTED = {
    0: 0,
    1: 1,
    2: 1,
    3: 2,
    4: 3,
    5: 5,
    6: 8,
    7: 13,
    8: 21,
    9: 34,
    10: 55,
    20: 6765,
    30: 832040,
}


class TestFibNaive:
    """Tests pour l'implementation naive (petites valeurs seulement)."""

    @pytest.mark.parametrize("n,expected", [
        (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (10, 55),
    ])
    def test_small_values(self, n, expected):
        from fibonacci import fib_naive
        assert fib_naive(n) == expected


class TestFibMemo:
    """Tests pour l'implementation avec memoisation."""

    @pytest.mark.parametrize("n,expected", list(EXPECTED.items()))
    def test_values(self, n, expected):
        from fibonacci import fib_memo
        assert fib_memo(n) == expected


class TestFibIterative:
    """Tests pour l'implementation iterative."""

    @pytest.mark.parametrize("n,expected", list(EXPECTED.items()))
    def test_values(self, n, expected):
        from fibonacci import fib_iterative
        assert fib_iterative(n) == expected


class TestFibonacciGenerator:
    """Tests pour l'implementation objet."""

    @pytest.mark.parametrize("n,expected", list(EXPECTED.items()))
    def test_default_values(self, n, expected):
        from fibonacci import FibonacciGenerator
        gen = FibonacciGenerator()
        assert gen.compute(n) == expected

    @pytest.mark.parametrize("n,expected", [
        (0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11),
    ])
    def test_lucas_sequence(self, n, expected):
        """Test suite de Lucas : u0=2, u1=1."""
        from fibonacci import FibonacciGenerator
        lucas = FibonacciGenerator(u0=2, u1=1)
        assert lucas.compute(n) == expected


class TestFibBinet:
    """Tests pour la formule fermee (Binet)."""

    @pytest.mark.parametrize("n,expected", [
        (0, 0), (1, 1), (2, 1), (3, 2), (5, 5), (10, 55), (20, 6765),
    ])
    def test_values(self, n, expected):
        from fibonacci import fib_binet
        assert fib_binet(n) == expected
```

**Lancez les tests** (ils doivent tous echouer pour l'instant) :

```bash
pytest test_fibonacci.py -v
```

> **Principe TDD** : On ecrit d'abord les tests, puis on implemente jusqu'a ce qu'ils passent.

> **Note** : `@pytest.mark.parametrize` permet de tester plusieurs valeurs avec un seul test.

---

## Etape 1 : Implementation naive (recursion simple)

La traduction directe de la definition mathematique :

```
F(n) = F(n-1) + F(n-2)
```

### A vous de jouer

Dans `fibonacci.py`, implementez `fib_naive(n)` :

```python
def fib_naive(n):
    """
    Implementation naive recursive de Fibonacci.
    
    Attention : tres lent pour n > 35 !
    """
    # A completer...
    pass
```

**Indice** : C'est une traduction directe de la definition. N'oubliez pas les cas de base.

### Questions

1. Pourquoi cette implementation est-elle lente ?
2. Combien de fois `fib_naive(5)` appelle-t-il `fib_naive(2)` ?

<details>
<summary>Indice pour la question 2</summary>

Dessinez l'arbre des appels :
```
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2) ← 
│   │   └── fib(1)
│   └── fib(2) ←
└── fib(3)
    ├── fib(2) ←
    └── fib(1)
```
</details>

---

## Etape 2 : Memoisation (cache des resultats)

Le probleme de l'approche naive : on recalcule les memes valeurs plusieurs fois.

**Solution** : stocker les resultats deja calcules dans un dictionnaire.

### A vous de jouer

Implementez `fib_memo(n)` avec un cache :

```python
def fib_memo(n, cache=None):
    """
    Fibonacci avec memoisation.
    
    Le cache stocke les valeurs deja calculees pour eviter
    les recalculs inutiles.
    """
    if cache is None:
        cache = {}
    
    # A completer...
    # 1. Verifier si n est dans le cache
    # 2. Sinon, calculer et stocker dans le cache
    pass
```

**Variante avec decorateur** (optionnel) :

Python propose `@functools.lru_cache` pour la memoisation automatique :

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo_decorator(n):
    # Meme code que fib_naive, mais avec le decorateur !
    pass
```

### Questions

1. Quelle est la complexite temporelle de `fib_memo` ?
2. Quelle est la complexite spatiale (memoire) ?

---

## Etape 3 : Approche iterative (bottom-up)

Au lieu de partir de `n` et descendre (top-down), on part de 0 et on monte.

**Idee** : On n'a besoin que des deux derniers termes pour calculer le suivant.

```
u_{n+2} = u_{n+1} + u_n
```

Donc on maintient deux variables `u_n` et `u_n1` qu'on met a jour a chaque iteration.

### A vous de jouer

```python
def fib_iterative(n):
    """
    Fibonacci iteratif.
    
    On maintient les deux derniers termes et on avance pas a pas.
    Plus efficace en memoire que la memoisation.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # A completer...
    # Initialiser u_n = 0, u_n1 = 1
    # Boucler et mettre a jour
    pass
```

**Indice** : A chaque iteration, le nouveau terme vaut `u_n + u_n1`, puis on "decale" les variables.

### Questions

1. Quelle est la complexite spatiale de cette approche ?
2. Pourquoi est-elle preferable a la memoisation pour les tres grands `n` ?

---

## Etape 4 : Approche objet

Encapsulons la logique dans une classe qui peut etre configuree avec des valeurs initiales differentes.

### A vous de jouer

```python
class FibonacciGenerator:
    """
    Generateur de Fibonacci avec valeurs initiales configurables.
    
    Par defaut : F(0)=0, F(1)=1
    Mais on peut creer des suites de type Fibonacci avec d'autres valeurs.
    
    Exemple - Suite de Lucas : L(0)=2, L(1)=1
    >>> lucas = FibonacciGenerator(u0=2, u1=1)
    >>> [lucas.compute(i) for i in range(6)]
    [2, 1, 3, 4, 7, 11]
    """
    
    def __init__(self, u0=0, u1=1):
        """
        Initialise le generateur.
        
        Args:
            u0: Premiere valeur de la suite (F(0))
            u1: Deuxieme valeur de la suite (F(1))
        """
        # A completer...
        pass
    
    def compute(self, n):
        """
        Calcule le n-ieme terme de la suite.
        
        Args:
            n: Indice du terme a calculer (n >= 0)
            
        Returns:
            Le n-ieme terme de la suite
        """
        # A completer...
        # Utilisez l'approche iterative
        pass
    
    def __repr__(self):
        """Representation textuelle du generateur."""
        return f"FibonacciGenerator(u0={self.u0}, u1={self.u1})"
```

### Questions

1. Quel avantage apporte l'approche objet ici ?
2. Comment genereriez-vous les 10 premiers termes de la suite de Lucas (2, 1, 3, 4, 7, ...) ?

---

## Etape 5 : Formule fermee (Binet)

Il existe une formule mathematique directe pour calculer F(n) :

```
F(n) = (phi^n - psi^n) / sqrt(5)

ou :
- phi = (1 + sqrt(5)) / 2  ≈ 1.618 (nombre d'or)
- psi = (1 - sqrt(5)) / 2  ≈ -0.618
```

### A vous de jouer

```python
import math

def fib_binet(n):
    """
    Fibonacci par la formule de Binet.
    
    Avantage : O(1) en temps (si on ignore le cout de pow)
    Inconvenient : Erreurs d'arrondi pour les grands n
    """
    sqrt5 = math.sqrt(5)
    phi = (1 + sqrt5) / 2
    psi = (1 - sqrt5) / 2
    
    # A completer...
    # Appliquer la formule et arrondir au plus proche entier
    pass
```

**Indice** : Utilisez `round()` pour obtenir un entier.

### Questions

1. Pourquoi cette formule donne-t-elle des resultats faux pour les grands `n` ?
2. A partir de quel `n` environ les erreurs apparaissent-elles ?

---

## Comparaison des approches

Une fois toutes les implementations terminees, comparez-les :

```python
import time

def benchmark(fib_func, n, name):
    """Mesure le temps d'execution."""
    start = time.perf_counter()
    result = fib_func(n)
    elapsed = time.perf_counter() - start
    print(f"{name:20} F({n}) = {result:15} en {elapsed:.6f}s")

# Test avec n=35
n = 35
print(f"Benchmark pour n={n}")
print("-" * 60)

# Attention : fib_naive est TRES lent pour n > 35
benchmark(fib_naive, n, "Naive")
benchmark(fib_memo, n, "Memoisation")
benchmark(fib_iterative, n, "Iteratif")
benchmark(FibonacciGenerator().compute, n, "Objet")
benchmark(fib_binet, n, "Binet")
```

### Tableau recapitulatif

| Approche | Complexite temps | Complexite espace | Avantages | Inconvenients |
|----------|------------------|-------------------|-----------|---------------|
| Naive | O(2^n) | O(n) pile | Simple | Tres lent |
| Memo | O(n) | O(n) | Rapide | Memoire |
| Iteratif | O(n) | O(1) | Efficace | Moins lisible |
| Objet | O(n) | O(1) | Configurable | Verbeux |
| Binet | O(1)* | O(1) | Instantane | Precision limitee |

*En ignorant le cout de `pow()` pour les grands exposants.

---

## Pour aller plus loin (optionnel)

### Generateur infini

Implementez un generateur Python qui produit la suite de Fibonacci indefiniment :

```python
def fibonacci_generator():
    """
    Generateur infini de Fibonacci.
    
    Usage:
    >>> gen = fibonacci_generator()
    >>> [next(gen) for _ in range(10)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    # A completer avec yield...
    pass
```

### Matrice et exponentiation rapide

Pour les tres grands `n`, on peut utiliser l'exponentiation de matrice :

```
[F(n+1)]   [1 1]^n   [1]
[F(n)  ] = [1 0]   * [0]
```

Avec l'exponentiation rapide, cela donne une complexite O(log n).

Implementez `fib_matrix(n)` si vous etes motives !

---

## Verification finale

Tous les tests doivent passer :

```bash
pytest test_fibonacci.py -v
```

Sortie attendue :
```
test_fibonacci.py::TestFibNaive::test_small_values[0-0] PASSED
test_fibonacci.py::TestFibNaive::test_small_values[1-1] PASSED
...
test_fibonacci.py::TestFibMemo::test_values[0-0] PASSED
...
test_fibonacci.py::TestFibIterative::test_values[0-0] PASSED
...
test_fibonacci.py::TestFibonacciGenerator::test_default_values[0-0] PASSED
test_fibonacci.py::TestFibonacciGenerator::test_lucas_sequence[0-2] PASSED
...
test_fibonacci.py::TestFibBinet::test_values[0-0] PASSED
...

========================= X passed in X.XXs =========================
```
