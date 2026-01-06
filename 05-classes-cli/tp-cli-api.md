# TP - Créer une CLI qui interroge une API

Projet pratique pour maîtriser argparse et les appels HTTP.

➜ Créez vos fichiers dans le dossier `perso/` pour travailler librement sans conflit git.

---

## Objectifs pédagogiques

Ce TP met l'accent sur :
- **argparse** : créer une interface en ligne de commande propre
- **requests** : effectuer des appels HTTP
- **Gestion d'erreurs** : gérer les cas où l'API ne répond pas

---

## Prérequis : installer requests

```bash
# Avec UV
uv add requests

# Ou avec pip
pip install requests
```

---

## Partie 1 : Exemple guidé - API de blagues

**Fichier :** `perso/blague.py`

### 1.1 L'API

On utilise l'API gratuite : https://v2.jokeapi.dev/

**Endpoint :** `https://v2.jokeapi.dev/joke/Any?lang=fr`

**Exemple de réponse (blague en deux parties) :**

```json
{
  "type": "twopart",
  "setup": "Pourquoi les plongeurs plongent-ils toujours en arrière ?",
  "delivery": "Parce que sinon ils tomberaient dans le bateau.",
  "category": "Misc",
  "lang": "fr"
}
```

**Exemple de réponse (blague simple) :**

```json
{
  "type": "single",
  "joke": "Un crocodile rencontre un chien. Il lui dit : Salut sac à puces ! Le chien répond : Salut sac à main !",
  "category": "Pun",
  "lang": "fr"
}
```

### 1.2 Fonction d'appel API

```python
import requests

def get_joke(category: str = "Any", lang: str = "fr") -> dict:
    """
    Récupère une blague depuis l'API.

    Args:
        category: Catégorie (Any, Programming, Misc, Pun, Dark, Spooky, Christmas)
        lang: Langue (fr, en, de, es, pt, cs)

    Returns:
        Un dictionnaire avec les données de la blague

    Raises:
        requests.RequestException: Si l'API ne répond pas
    """
    url = f"https://v2.jokeapi.dev/joke/{category}"
    params = {"lang": lang}

    response = requests.get(url, params=params, timeout=5)
    response.raise_for_status()  # Lève une exception si erreur HTTP

    data = response.json()

    if data.get("error"):
        raise ValueError(f"Erreur API: {data.get('message')}")

    return data
```

### 1.3 Formatage de la blague

```python
def format_joke(data: dict) -> str:
    """
    Formate une blague pour l'affichage.

    Gère les deux types : 'single' et 'twopart'
    """
    category = data.get("category", "Unknown")

    if data.get("type") == "single":
        content = data["joke"]
    else:
        # twopart
        content = f"{data['setup']}\n→ {data['delivery']}"

    return f"[{category}] {content}"
```

### 1.4 CLI avec argparse

```python
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Affiche une blague aléatoire"
    )

    parser.add_argument(
        "-c", "--category",
        default="Any",
        choices=["Any", "Programming", "Misc", "Pun", "Dark"],
        help="Catégorie de blague (défaut: Any)"
    )

    parser.add_argument(
        "-l", "--lang",
        default="fr",
        choices=["fr", "en", "de", "es"],
        help="Langue (défaut: fr)"
    )

    parser.add_argument(
        "-n", "--nombre",
        type=int,
        default=1,
        help="Nombre de blagues à afficher (défaut: 1)"
    )

    args = parser.parse_args()

    try:
        for i in range(args.nombre):
            data = get_joke(category=args.category, lang=args.lang)
            print(format_joke(data))
            if i < args.nombre - 1:
                print()  # Ligne vide entre les blagues
    except requests.RequestException as e:
        print(f"Erreur réseau : {e}")
    except ValueError as e:
        print(f"Erreur : {e}")


if __name__ == "__main__":
    main()
```

### 1.5 Utilisation

```bash
# Blague aléatoire en français
python perso/blague.py

# 3 blagues de programmation en anglais
python perso/blague.py -c Programming -l en -n 3

# Aide
python perso/blague.py --help
```

---

## Partie 2 : À vous de jouer !

Choisissez **une API** parmi les suivantes et créez votre propre CLI.

### Structure attendue

Votre code doit avoir :

1. **Une fonction** qui appelle l'API et retourne les données
2. **Une fonction** qui formate les données pour l'affichage
3. **Une CLI** avec au moins 2 options pertinentes
4. **Gestion d'erreurs** (réseau, API)

---

## APIs gratuites suggérées

### 1. Météo - Open-Meteo

**Fichier suggéré :** `perso/meteo.py`

**Documentation :** https://open-meteo.com/en/docs

**Endpoint exemple :**
```
https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&current_weather=true
```

**Réponse :**
```json
{
  "current_weather": {
    "temperature": 15.2,
    "windspeed": 12.5,
    "weathercode": 3,
    "time": "2024-01-15T14:00"
  }
}
```

**Suggestions CLI :**
- `--ville` ou `--lat/--lon` pour la localisation
- `--unite` pour Celsius/Fahrenheit
- `--details` pour afficher plus d'infos

**Bonus :** Utiliser une API de géocodage pour convertir nom de ville → coordonnées :
```
https://geocoding-api.open-meteo.com/v1/search?name=Paris&count=1
```

---

### 2. Pays du monde - REST Countries

**Fichier suggéré :** `perso/pays.py`

**Documentation :** https://restcountries.com/

**Endpoint :**
```
https://restcountries.com/v3.1/name/{nom}
```

**Exemple :** `https://restcountries.com/v3.1/name/france`

**Réponse (simplifiée) :**
```json
[{
  "name": {"common": "France", "official": "French Republic"},
  "capital": ["Paris"],
  "population": 67390000,
  "region": "Europe",
  "languages": {"fra": "French"},
  "currencies": {"EUR": {"name": "Euro", "symbol": "€"}}
}]
```

**Suggestions CLI :**
- `nom` (argument positionnel) : nom du pays
- `--lang` : afficher les langues parlées
- `--full` : affichage détaillé

---

### 3. Chiens aléatoires - Dog API

**Fichier suggéré :** `perso/chien.py`

**Documentation :** https://dog.ceo/dog-api/

**Endpoints :**
```
https://dog.ceo/api/breeds/image/random       # Image aléatoire
https://dog.ceo/api/breed/{race}/images/random  # Image d'une race
https://dog.ceo/api/breeds/list/all           # Liste des races
```

**Suggestions CLI :**
- `--race` : filtrer par race
- `--liste` : afficher toutes les races disponibles
- `--telecharger` : télécharger l'image localement

---

### 4. Faits sur les chats - Cat Facts

**Fichier suggéré :** `perso/chat.py`

**Documentation :** https://catfact.ninja/

**Endpoints :**
```
https://catfact.ninja/fact           # Un fait aléatoire
https://catfact.ninja/facts?limit=5  # Plusieurs faits
https://catfact.ninja/breeds         # Races de chats
```

**Suggestions CLI :**
- `-n` / `--nombre` : nombre de faits
- `--races` : lister les races
- `--max-length` : longueur max du texte

---

### 5. Activités ennui - Bored API

**Fichier suggéré :** `perso/activite.py`

**Documentation :** https://www.boredapi.com/

**Endpoint :**
```
https://www.boredapi.com/api/activity
https://www.boredapi.com/api/activity?type=social&participants=2
```

**Réponse :**
```json
{
  "activity": "Learn a new programming language",
  "type": "education",
  "participants": 1,
  "price": 0,
  "accessibility": 0.1
}
```

**Suggestions CLI :**
- `--type` : type d'activité (education, social, recreational, cooking, etc.)
- `--participants` : nombre de participants
- `--gratuit` : activités gratuites uniquement (price = 0)

---

## Checklist de progression

### Partie 1 - Exemple guidé (blagues)
- [ ] Installation de `requests`
- [ ] Fonction `get_joke` avec gestion d'erreurs
- [ ] Fonction `format_joke` pour l'affichage
- [ ] CLI avec argparse (category, lang, nombre)
- [ ] Test manuel des différentes options

### Partie 2 - Votre API
- [ ] Choix d'une API
- [ ] Fonction d'appel API
- [ ] Fonction de formatage
- [ ] CLI avec au moins 2 options
- [ ] Gestion des erreurs réseau
- [ ] Test avec `--help`
- [ ] Test des différentes options

---

## Bonus

### 1. Ajouter des couleurs

```bash
uv add colorama
```

```python
from colorama import Fore, Style

print(f"{Fore.GREEN}Succès !{Style.RESET_ALL}")
print(f"{Fore.RED}Erreur !{Style.RESET_ALL}")
```

### 2. Barre de progression

```bash
uv add tqdm
```

```python
from tqdm import tqdm
import time

for i in tqdm(range(10)):
    time.sleep(0.1)
```

### 3. Cache des résultats

Éviter de rappeler l'API si on a déjà la réponse :

```python
import json
from pathlib import Path

CACHE_FILE = Path("perso/.cache.json")

def load_cache():
    if CACHE_FILE.exists():
        return json.loads(CACHE_FILE.read_text())
    return {}

def save_cache(cache):
    CACHE_FILE.write_text(json.dumps(cache, indent=2))
```

### 4. Configuration par fichier

Créer un fichier `perso/config.json` pour stocker les préférences :

```json
{
  "langue_defaut": "fr",
  "ville_defaut": "Paris"
}
```

---

## Ressources

- **requests** : https://requests.readthedocs.io/
- **argparse tutorial** : https://docs.python.org/3/howto/argparse.html
- **API publiques** : https://github.com/public-apis/public-apis

---

## Points d'attention pédagogiques

### Gestion d'erreurs HTTP

```python
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()
except requests.Timeout:
    print("L'API met trop de temps à répondre")
except requests.HTTPError as e:
    print(f"Erreur HTTP : {e.response.status_code}")
except requests.RequestException as e:
    print(f"Erreur réseau : {e}")
```

### Types d'arguments argparse

| Type | Exemple | Usage |
|------|---------|-------|
| Positionnel | `parser.add_argument("nom")` | Obligatoire, dans l'ordre |
| Option flag | `parser.add_argument("-v", action="store_true")` | Bool on/off |
| Option valeur | `parser.add_argument("-n", type=int, default=1)` | Avec valeur |
| Choix | `parser.add_argument("--lang", choices=["fr","en"])` | Liste fermée |

### Passage de paramètres à l'URL

```python
# Méthode 1 : construction manuelle (déconseillé)
url = f"https://api.example.com/data?param1={value1}&param2={value2}"

# Méthode 2 : avec params (recommandé)
url = "https://api.example.com/data"
params = {"param1": value1, "param2": value2}
response = requests.get(url, params=params)
# requests construit automatiquement : https://api.example.com/data?param1=...&param2=...
```
