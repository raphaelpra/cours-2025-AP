# le code de Vigenere

## rappel - le code de César

le code de Cesar est un chiffrement par décalage des lettres de l'alphabet.

```python
def cesar(plain, key, encode=True):
    """
    Chiffre ou déchiffre un caractère avec le code de César.

    Paramètres:
    - plain: str - (un seul) caractère en clair à chiffrer ou déchiffrer
    - key: la clé - un seul caractère qui indique le décalage
    - encode: bool - True pour chiffrer, False pour déchiffrer

    Retourne:
    - str - le texte chiffré ou déchiffré

    par convention, key='a' signifie un décalage de 1, et donc avec la clé 'z' on ne modifie pas le message - convention totalement arbitraire, et pas forcément celle utilisée classiquement

    """

    # simple vérification de la clé
    if not key.isalpha() or len(key) != 1:
        raise ValueError("La clé doit être un seul caractère alphabétique.")

    # pour simplifier on ne gère que les lettres alphabétiques minuscules
    key = key.lower()
    plain = plain.lower()

    # les caractères non alphabétiques ne sont pas modifiés
    if not plain.isalpha():
        return plain

    # de combien doit-on décaler?
    # on a dit 'a' -> 1
    offset = ord(key    ) - ord('a') + 1

    # si on déchiffre, on décale dans l'autre sens
    if not encode:
        offset = -offset

    # pour pouvoir faire un modulo 26 on se projette dans [0..25]
    projected = ord(plain) - ord('a')
    altered_in_proj = (projected + offset) % 26

    # et on retourne dans l'espace des caractères
    restored = altered_in_proj + ord('a')
    return chr(restored)
```

## le code de Vigenere

comme le code de César est trivial à déchiffrer, la première amélioration a été de prendre une clé à plusieurs caractères et de la "faire tourner"

| message | clé | chiffré |
|---------|-----|---------|
| `"l"` | `"c"` | `cesar("l", "c")` |
| `"e"` | `"l"` | `cesar("e", "l")` |
| `"m"` | `"e"` | `cesar("m", "e")` |
| `"e"` | `"c"` | `cesar("e", "c")` |
| `"e"` | `"l"` | `cesar("e", "l")` |
| `"s"` | `"e"` | `cesar("s", "e")` |
| `"s"` | `"c"` | `cesar("s", "c")` |
| `"a"` | `"l"` | `cesar("a", "l")` |
| `"g"` | `"e"` | `cesar("g", "e")` |
| `"e"` | `"c"` | `cesar("e", "c")` |

Ainsi par exemple:

```python
In [21]: vigenere("lemessage", "cle")
Out[21]: 'oqrhexdsj'

In [22]: vigenere("oqrhexdsj", "cle", False)
Out[22]: 'lemessage'
```

## modalités

votre mission est d'écrire une fonction `vigenere(plain, key, encode=True)` qui chiffre ou déchiffre un message avec le code de Vigenere en utilisant la fonction `cesar` définie plus haut.

on vous recommande de travailler dans un fichier `vigenere.py` dans lequel vous
commencez par copier-coller la fonction `cesar` définie plus haut.

## indices

il y a dans le module `itertools` des outils qui vous permettent d'écrire vigenere et notamment la logique de la clé qui "tourne" de façon élégante.
