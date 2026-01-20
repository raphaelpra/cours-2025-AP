# Tests Python avec pytest

Les tests automatises permettent de verifier que votre code fonctionne correctement, et qu'il continue de fonctionner apres des modifications.

---

## Pourquoi tester ?

- **Confiance** : savoir que le code fonctionne
- **Regression** : detecter quand une modification casse quelque chose
- **Documentation** : les tests montrent comment utiliser le code
- **Refactoring** : modifier le code en toute securite

---

## pytest vs unittest

Python inclut `unittest` dans la librairie standard, mais **pytest** est plus simple et plus puissant.

| Aspect | unittest | pytest |
|--------|----------|--------|
| Syntaxe | Verbose (classes, self.assertEqual) | Simple (fonctions, assert) |
| Installation | Inclus | `uv add pytest` |
| Decouverte | Manuelle | Automatique |
| Plugins | Peu | Beaucoup |

---

## Installation

```bash
uv add pytest
```

Verification :
```bash
uv run pytest --version
# ou si venv active :
pytest --version
```

---

## Premier test

### Structure du projet

```
mon-projet/
    calcul.py           # Code a tester
    test_calcul.py      # Tests (prefixe test_)
```

### Code a tester (calcul.py)

```python
def addition(a, b):
    return a + b

def division(a, b):
    if b == 0:
        raise ValueError("Division par zero")
    return a / b
```

### Tests (test_calcul.py)

```python
import pytest
from calcul import addition, division

def test_addition_simple():
    assert addition(2, 3) == 5

def test_addition_negatifs():
    assert addition(-1, -1) == -2

def test_division_simple():
    assert division(10, 2) == 5

def test_division_par_zero():
    with pytest.raises(ValueError):
        division(10, 0)
```

---

## Lancer les tests

```bash
# Tous les tests
pytest

# Avec details
pytest -v

# Un fichier specifique
pytest test_calcul.py

# Une fonction specifique
pytest test_calcul.py::test_addition_simple

# Avec affichage des prints
pytest -s
```

### Sortie typique

```
==================== test session starts ====================
collected 4 items

test_calcul.py ....                                    [100%]

==================== 4 passed in 0.02s ====================
```

Signification :
- `.` = test passe
- `F` = test echoue (failure)
- `E` = erreur (exception inattendue)
- `s` = test skippe

---

## Syntaxe des assertions

pytest utilise simplement `assert` :

```python
# Egalite
assert result == expected

# Verite
assert is_valid

# Appartenance
assert item in liste

# Comparaisons
assert value > 0
assert len(liste) == 3

# Approximation (floats)
assert result == pytest.approx(3.14, rel=0.01)
```

---

## Tester les exceptions

```python
import pytest

def test_erreur_attendue():
    with pytest.raises(ValueError):
        division(1, 0)

def test_message_erreur():
    with pytest.raises(ValueError, match="Division par zero"):
        division(1, 0)
```

---

## Fixtures : preparer les donnees

Les fixtures permettent de preparer des donnees reutilisables :

```python
import pytest

@pytest.fixture
def liste_notes():
    return [15, 12, 18, 14, 16]

@pytest.fixture
def etudiant():
    return {"nom": "Alice", "age": 20}

def test_moyenne(liste_notes):
    moyenne = sum(liste_notes) / len(liste_notes)
    assert moyenne == 15

def test_etudiant_majeur(etudiant):
    assert etudiant["age"] >= 18
```

### Fixtures courantes

```python
@pytest.fixture
def fichier_temporaire(tmp_path):
    # tmp_path est une fixture integree
    fichier = tmp_path / "test.txt"
    fichier.write_text("contenu test")
    return fichier

def test_lecture_fichier(fichier_temporaire):
    contenu = fichier_temporaire.read_text()
    assert contenu == "contenu test"
```

---

## Organisation des tests

### Convention de nommage

```
projet/
    src/
        module1.py
        module2.py
    tests/
        test_module1.py     # Prefixe test_
        test_module2.py
        conftest.py         # Fixtures partagees
```

### conftest.py

Fichier special pour les fixtures partagees entre plusieurs fichiers de test :

```python
# tests/conftest.py
import pytest

@pytest.fixture
def db_connection():
    # Setup
    conn = create_connection()
    yield conn
    # Teardown
    conn.close()
```

---

## Parametrisation

Tester plusieurs cas avec une seule fonction :

```python
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_addition_parametree(a, b, expected):
    assert addition(a, b) == expected
```

Sortie :
```
test_calcul.py::test_addition_parametree[2-3-5] PASSED
test_calcul.py::test_addition_parametree[0-0-0] PASSED
test_calcul.py::test_addition_parametree[-1-1-0] PASSED
test_calcul.py::test_addition_parametree[100-200-300] PASSED
```

---

## pytest dans VS Code

### Configuration

1. `Ctrl+Shift+P` -> `Python: Configure Tests`
2. Choisir **pytest**
3. Choisir le dossier des tests (`.` pour racine)

### Utilisation

- Icone **Testing** dans la barre laterale (becher)
- Lancer tous les tests ou un seul
- Voir les resultats directement dans l'editeur

### Indicateurs dans le code

VS Code affiche des icones a cote des fonctions de test :
- ✅ Test passe
- ❌ Test echoue
- ▶️ Lancer le test

---

## Options utiles

```bash
# Arreter au premier echec
pytest -x

# Derniers tests echoues seulement
pytest --lf

# Afficher les 5 tests les plus lents
pytest --durations=5

# Couverture de code (necessite pytest-cov)
pytest --cov=mon_module
```

---

## Exemple complet

### calcul.py

```python
def moyenne(notes):
    if not notes:
        raise ValueError("Liste vide")
    return sum(notes) / len(notes)

def est_admis(moyenne):
    return moyenne >= 10
```

### test_calcul.py

```python
import pytest
from calcul import moyenne, est_admis

class TestMoyenne:
    def test_moyenne_simple(self):
        assert moyenne([10, 20]) == 15

    def test_moyenne_un_element(self):
        assert moyenne([15]) == 15

    def test_moyenne_liste_vide(self):
        with pytest.raises(ValueError, match="Liste vide"):
            moyenne([])

    @pytest.mark.parametrize("notes, expected", [
        ([20, 20, 20], 20),
        ([0, 10, 20], 10),
        ([12.5, 13.5], 13),
    ])
    def test_moyenne_parametree(self, notes, expected):
        assert moyenne(notes) == expected

class TestAdmission:
    @pytest.mark.parametrize("note, admis", [
        (10, True),
        (9.9, False),
        (15, True),
        (0, False),
    ])
    def test_admission(self, note, admis):
        assert est_admis(note) == admis
```

---

## Bonnes pratiques

1. **Un test = une chose** : chaque test verifie un seul comportement
2. **Noms explicites** : `test_division_par_zero_leve_erreur`
3. **Tests independants** : un test ne doit pas dependre d'un autre
4. **Arrange-Act-Assert** :
   ```python
   def test_exemple():
       # Arrange (preparer)
       liste = [1, 2, 3]
       
       # Act (executer)
       resultat = sum(liste)
       
       # Assert (verifier)
       assert resultat == 6
   ```

---

## Ressources

- [Documentation pytest](https://docs.pytest.org/)
- [pytest dans VS Code](https://code.visualstudio.com/docs/python/testing)

---

*Commande rapide : `pytest -v` pour lancer tous les tests avec details*
