# L'IA en Informatique - Guide du Developpeur Moderne

**Duree estimee : 1h | Date : 03/02/2026**

> **Avertissement** : Ce que vous lisez ici represente l'etat de l'art de janvier 2026. Dans 6 mois, la moitie sera obsolete. C'est la beaute (et le cauchemar) de ce domaine.

![Meme IA](https://i.imgflip.com/aih2jk.jpg)

---

## Table des matieres

1. [Vocabulaire essentiel](#1-vocabulaire-essentiel)
2. [Les 3 niveaux d'usage de l'IA](#2-les-3-niveaux-dusage-de-lia)
3. [Panorama des modeles](#3-panorama-des-modeles)
4. [Focus : Tools, MCP et integration](#4-focus--tools-mcp-et-integration)
5. [Focus : OpenCode - l'agent en pratique](#5-focus--opencode---lagent-en-pratique)
6. [L'IA comme outil pedagogique](#6-lia-comme-outil-pedagogique)

---

## 1. Vocabulaire essentiel

Avant de plonger, definissons les termes que vous entendrez partout.

### LLM (Large Language Model)

Un **LLM** est un modele de langage entraine sur d'enormes quantites de texte. Il predit le prochain mot/token le plus probable.

```
Entree: "La capitale de la France est"
Sortie: "Paris" (avec haute probabilite)
```

**Exemples** : GPT-4, Claude, Llama, Mistral, Gemini

### Context (Contexte)

Le **contexte** est l'ensemble des informations que le modele "voit" pour generer sa reponse :
- Votre prompt actuel
- L'historique de la conversation
- Les fichiers que vous avez partages
- Les instructions systeme

**Limite importante** : Chaque modele a une "fenetre de contexte" limitee (ex: 128K tokens pour GPT-4, 200K pour Claude).

```
┌─────────────────────────────────────────┐
│           Fenetre de contexte           │
├─────────────────────────────────────────┤
│ [System prompt] [Historique] [Fichiers] │
│              [Votre question]           │
└─────────────────────────────────────────┘
```

### Tools (Outils)

Les **tools** sont des fonctions que le LLM peut appeler pour interagir avec le monde exterieur :
- Lire/ecrire des fichiers
- Executer du code
- Chercher sur le web
- Appeler des APIs

```python
# Exemple conceptuel
tools = [
    {"name": "read_file", "params": ["path"]},
    {"name": "run_bash", "params": ["command"]},
    {"name": "web_search", "params": ["query"]}
]
```

### Agent

Un **agent** est un LLM + des tools + une boucle de raisonnement. Il peut :
1. Analyser une tache
2. Planifier les etapes
3. Executer des actions (via tools)
4. Observer les resultats
5. Ajuster et continuer

```
┌──────────────────────────────────────┐
│              AGENT                   │
│  ┌─────┐    ┌───────┐    ┌─────┐   │
│  │ LLM │ -> │ Tools │ -> │ Env │   │
│  └──┬──┘    └───────┘    └──┬──┘   │
│     └──────── feedback ─────┘       │
└──────────────────────────────────────┘
```

---

### Hands-on #1 : Testez votre vocabulaire (5 min)

Ouvrez ChatGPT ou Claude et demandez :

> "Explique-moi la difference entre un LLM et un agent, comme si j'avais 12 ans"

Observez comment l'IA adapte son langage !

---

## 2. Les 3 niveaux d'usage de l'IA

L'IA peut s'integrer a votre workflow de 3 facons distinctes :

### Niveau 1 : Le Chat

**Produit emblematique** : ChatGPT, Claude.ai

**Comment ca marche** :
- Interface conversationnelle (question/reponse)
- Copier-coller du code
- L'IA n'a pas acces a vos fichiers

**Usage typique** :
```
Vous: "Comment faire un tri a bulles en Python ?"
IA: "[explique + code]"
Vous: *copie le code dans votre editeur*
```

**Avantages** :
- Simple a utiliser
- Gratuit (versions de base)
- Bon pour apprendre des concepts
- Fonctionne pour tout (pas que le code)

**Inconvenients** :
- Beaucoup de copier-coller
- L'IA ne voit pas votre projet
- Pas de contexte persiste
- Risque d'erreurs lors du copier-coller

---

### Niveau 2 : L'Autocomplete++

**Produits emblematiques** : GitHub Copilot, Cursor, Cody

**Comment ca marche** :
- Extension dans votre IDE
- L'IA voit le fichier courant (et parfois le projet)
- Suggestions en temps reel pendant que vous tapez

**Usage typique** :
```python
def calculer_moyenne(notes):
    # L'IA complete automatiquement :
    return sum(notes) / len(notes)
```

**Avantages** :
- Integration fluide dans l'editeur
- Gain de temps sur le code repetitif
- Voit le contexte de votre fichier
- Tab-Tab-Tab = productivite

**Inconvenients** :
- Abonnement payant (~10-20€/mois)
- Peut suggerer du code incorrect
- Ne fait pas de taches complexes
- "Tab addiction" - on arrete de reflechir

> **Hint** : Ecrivez d'abord un commentaire decrivant ce que vous voulez faire.
> L'IA autocomplete bien mieux quand elle comprend votre intention !
>
> ```python
> # Fonction qui calcule la distance euclidienne entre deux points
> def distance(p1, p2):
>     # L'IA complete avec confiance car elle sait ce que vous voulez
> ```

---

### Niveau 3 : L'Agent

**Produits emblematiques** : Claude Code, Codex (OpenAI), OpenCode, Aider

**Comment ca marche** :
- Terminal ou interface dediee
- L'IA a acces a TOUT votre projet
- Peut lire, ecrire, executer, tester
- Travaille de facon autonome sur des taches

**Usage typique** :
```bash
$ opencode
> Ajoute une fonctionnalite de recherche dans le fichier users.py
  avec des tests unitaires

# L'agent :
# 1. Lit les fichiers existants
# 2. Comprend la structure
# 3. Ecrit le code
# 4. Cree les tests
# 5. Execute les tests
# 6. Corrige si erreur
```

**Avantages** :
- Taches complexes multi-fichiers
- Peut refactorer un projet entier
- Execute et corrige automatiquement
- Comme un pair programmer infatigable

**Inconvenients** :
- Plus cher (usage intensif)
- Necessite une bonne supervision
- Peut faire des changements inattendus
- Courbe d'apprentissage

---

### Tableau recapitulatif

| Critere | Chat | Autocomplete++ | Agent |
|---------|------|----------------|-------|
| **Complexite** | Simple | Moyenne | Elevee |
| **Contexte projet** | Non | Partiel | Total |
| **Autonomie** | Nulle | Faible | Forte |
| **Prix** | Gratuit-20€/m | 10-20€/m | 20-100€/m |
| **Courbe apprentissage** | Basse | Basse | Moyenne |
| **Meilleur pour** | Apprendre | Coder vite | Gros projets |

---

### Hands-on #2 : Comparaison en direct (10 min)

Si vous avez acces a un outil de chaque niveau :

1. **Chat** : Demandez "Comment lire un fichier JSON en Python ?"
2. **Autocomplete** : Commencez a taper `def load_json(` et observez
3. **Agent** : (demo prof) "Cree un script qui lit config.json et affiche son contenu"

---

## 3. Panorama des modeles

### Les principaux providers

| Provider | Modeles phares | Force principale |
|----------|---------------|------------------|
| **OpenAI** | GPT-5.2, GPT-5.1 | Polyvalence, ecosysteme, multimodal |
| **Anthropic** | Claude Opus 4.5, Claude Sonnet 4.5 | Code, raisonnement, agents |
| **Google** | Gemini 3, Gemini 3 Flash | Multimodal, integration Google |
| **xAI** | Grok 3, Grok 3 mini | Raisonnement, integration X/Twitter |
| **Alibaba** | Qwen3, Qwen-Max | Open-source, multilingue |
| **MiniMax** | M2.1, Hailuo (video) | Multimodal, video generation |
| **Mistral** | Mistral Large 2, Pixtral | Europe, francais, vision |

### Criteres d'evaluation

Trois criteres principaux pour choisir un modele :

1. **Qualite** : Precision, pertinence, absence d'erreurs
2. **Cout** : Prix par million de tokens (entree/sortie)
3. **Latence** : Temps de reponse (important pour l'autocomplete)

### Tableau comparatif (Janvier 2026)

| Modele | Qualite | Cout | Latence | Ideal pour |
|--------|---------|------|---------|------------|
| **Claude Opus 4.5** | ★★★★★ | ★★☆☆☆ | ★★★☆☆ | Code complexe, agents, computer use |
| **Claude Sonnet 4.5** | ★★★★★ | ★★★★☆ | ★★★★☆ | Meilleur rapport qualite/prix |
| **GPT-5.2** | ★★★★★ | ★★★☆☆ | ★★☆☆☆ | Usage general, multimodal |
| **Grok 3** | ★★★★★ | ★★★☆☆ | ★★★★☆ | Raisonnement, temps reel (X) |
| **Gemini 3** | ★★★★★ | ★★★☆☆ | ★★★★☆ | Multimodal, 1M+ tokens contexte |
| **Gemini 3 Flash** | ★★★★☆ | ★★★★★ | ★★★★★ | Apps rapides, budget |
| **Qwen3 235B** | ★★★★★ | ★★★★★ | ★★★☆☆ | Open-source, multilingue |
| **MiniMax M2.1** | ★★★★☆ | ★★★★☆ | ★★★★☆ | Code, agents, multilingue |
| **Mistral Large 2** | ★★★★☆ | ★★★★☆ | ★★★★☆ | Europe, francais, 128K contexte |

> **Note** : Ces notes evoluent TRES vite. Verifiez les benchmarks recents !

### Prix indicatifs ($/1M tokens)

| Modele | Input | Output |
|--------|-------|--------|
| Claude Opus 4.5 | $15 | $75 |
| Claude Sonnet 4.5 | $3 | $15 |
| GPT-5.2 | $5 | $15 |
| Gemini 3 Flash | $0.075 | $0.30 |
| Qwen3 (via API) | $0.50 | $2.00 |

---

## 4. Focus : Tools, MCP et integration

### L'architecture moderne d'un agent

```
┌─────────────────────────────────────────────────────────┐
│                      AGENT                              │
│  ┌─────────────────────────────────────────────────┐   │
│  │                    LLM                          │   │
│  └───────────────────────┬─────────────────────────┘   │
│                          │                              │
│  ┌───────────────────────┼─────────────────────────┐   │
│  │                    TOOLS                        │   │
│  │  ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────────┐  │   │
│  │  │Read │ │Write│ │Bash │ │Grep │ │WebFetch │  │   │
│  │  └─────┘ └─────┘ └─────┘ └─────┘ └─────────┘  │   │
│  └─────────────────────────────────────────────────┘   │
│                          │                              │
│  ┌───────────────────────┼─────────────────────────┐   │
│  │                    MCP                          │   │
│  │  ┌───────────┐ ┌───────────┐ ┌───────────────┐ │   │
│  │  │ Formatter │ │    LSP    │ │ Recherche Web │ │   │
│  │  │  (black)  │ │ (pylsp)   │ │   (brave)     │ │   │
│  │  └───────────┘ └───────────┘ └───────────────┘ │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### MCP (Model Context Protocol)

**MCP** est un standard ouvert (propose par Anthropic) pour connecter des outils aux LLMs.

**Pourquoi c'est important :**
- Standard unifie (un outil MCP marche avec Claude, GPT, etc.)
- Securise (permissions explicites)
- Extensible (creez vos propres servers MCP)

**Exemples de servers MCP :**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-filesystem", "/home/user/projects"]
    },
    "brave-search": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-brave-search"]
    },
    "postgres": {
      "command": "npx",
      "args": ["@anthropic-ai/mcp-server-postgres", "postgresql://..."]
    }
  }
}
```

### Integration LSP (Language Server Protocol)

Le **LSP** permet a l'agent de :
- Detecter les erreurs de syntaxe en temps reel
- Comprendre les types et signatures
- Naviguer dans le code (go to definition)
- Faire du refactoring intelligent

```
Agent + LSP = L'agent "comprend" vraiment votre code
             (pas juste le texte, mais la structure)
```

### Recherche documentaire integree

Les agents modernes peuvent :
- Chercher dans la doc officielle
- Trouver des exemples sur GitHub
- Verifier sur Stack Overflow
- Lire les changelogs de vos deps

```bash
> Utilise la derniere version de pytest avec les fixtures modernes
# L'agent va chercher la doc de pytest pour verifier
```

---

## 5. Focus : OpenCode - l'agent en pratique

### Installation

```bash
# Via Homebrew (Mac/Linux)
brew install opencode

# Via npm
npm install -g @anthropic/opencode

# Via pip
pip install opencode-cli
```

### Configuration

```bash
# Premiere utilisation
opencode init

# Configure votre cle API
export ANTHROPIC_API_KEY=sk-ant-...
# ou
export OPENAI_API_KEY=sk-...
```

### AGENTS.md - Le fichier de contexte

Chaque projet peut avoir un fichier `AGENTS.md` a la racine :

```markdown
# AGENTS.md

## Contexte du projet
Ce projet est une API REST en Python/FastAPI.

## Conventions
- Noms de variables en francais
- Tests avec pytest
- Formater avec black

## Structure
- src/ : code source
- tests/ : tests unitaires
- docs/ : documentation

## Commandes utiles
- `uv sync` : installe les dependances
- `uv run pytest` : lance les tests
```

**L'agent lit ce fichier automatiquement** et adapte son comportement !

### Skills : enseigner des competences a l'agent

Les **skills** sont des instructions specialisees :

```markdown
# .opencode/skills/django.md

Quand tu travailles sur du Django :
- Utilise les class-based views
- Prefere les querysets aux boucles Python
- Toujours valider les forms cote serveur
```

### Commands : raccourcis personnalises

```bash
# .opencode/commands/test.md
# Command: /test

Lance les tests et montre un resume :
1. Execute pytest
2. Si echec, analyse les erreurs
3. Propose des corrections
```

Utilisation :
```bash
> /test
```

### Session : persistance du contexte

```bash
# Nouvelle session
opencode

# Reprendre une session
opencode --resume

# Voir les sessions passees
opencode sessions list
```

---

### Hands-on #3 : Demo OpenCode (10 min)

```bash
# Le prof montre :
$ opencode

> Lis le fichier fibonacci.py et explique son fonctionnement

> Ajoute une version recursive memoizee de fibonacci

> Lance les tests et corrige les erreurs si necessaire
```

Observez :
- Comment l'agent lit les fichiers
- Comment il planifie ses actions
- Comment il reagit aux erreurs

---

## 6. L'IA comme outil pedagogique

### La methode des "niveaux d'explication"

L'IA excelle pour adapter ses explications. Testez ces prompts :

```
"Explique [concept] comme si j'avais 5 ans"
"Explique [concept] comme si j'avais 12 ans"
"Explique [concept] pour un bachelier"
"Explique [concept] pour un doctorant en informatique"
```

**Exemple avec les "pointeurs" :**

- **5 ans** : "C'est comme une fleche qui montre ou est range un jouet"
- **12 ans** : "C'est une adresse, comme ton adresse postale pour ta maison"
- **Bachelier** : "Variable contenant l'adresse memoire d'une autre variable"
- **Doctorant** : "Reference indirecte permettant l'aliasing et l'allocation dynamique..."

### NotebookLM : l'IA pour reviser

**NotebookLM** (Google) permet de :
- Uploader vos cours (PDF, docs)
- Poser des questions sur VOS documents
- Generer des podcasts audio (!)
- Creer des flashcards

```
1. Allez sur notebooklm.google.com
2. Uploadez vos notes de cours
3. Demandez : "Resume les points cles du chapitre 3"
4. Ou : "Cree 10 questions pour reviser"
```

### Strategies d'apprentissage avec l'IA

| Strategie | Prompt exemple |
|-----------|---------------|
| **Analogie** | "Compare X a quelque chose de la vie quotidienne" |
| **Socratique** | "Pose-moi des questions pour m'aider a comprendre X" |
| **Exemples** | "Donne 5 exemples concrets de X" |
| **Erreurs** | "Quelles erreurs font souvent les debutants avec X ?" |
| **Schema** | "Dessine un schema ASCII pour expliquer X" |
| **Code** | "Montre X avec du code Python simple" |

### Attention aux pieges !

> L'IA peut avoir l'air tres convaincante... meme quand elle a tort.

**Bonnes pratiques :**
- Testez TOUJOURS le code genere
- Demandez a l'IA de **reviewer son propre code**
- Demandez-lui d'**ecrire des tests** pour verifier
- Croisez avec d'autres sources

![IA tres sure d'elle](https://i.imgflip.com/4acd7j.png)
*"L'IA quand elle invente une fonction qui n'existe pas"*

---

### Hands-on #4 : Apprenez avec l'IA (10 min)

Choisissez un concept que vous trouvez difficile et testez :

1. Demandez une explication "comme si j'avais 12 ans"
2. Puis demandez "montre-moi avec du code Python simple"
3. Enfin demandez "quelles erreurs font les debutants ?"

---

## Conclusion

### Ce qu'il faut retenir

1. **Vocabulaire** : LLM, Context, Tools, Agent - vous savez ce que ca veut dire

2. **3 niveaux** :
   - Chat = simple, copier-coller
   - Autocomplete++ = fluide, dans l'editeur
   - Agent = puissant, autonome

3. **Modeles** : Choisissez selon qualite/cout/latence

4. **L'IA evolue vite** : Restez curieux, experimentez

5. **Pour apprendre** : L'IA est un excellent tuteur patient

### Le message final

> L'IA ne remplace pas la comprehension des fondamentaux.
> Elle amplifie vos capacites... si vous savez ce que vous faites.

Vous avez appris Python ce semestre. L'IA peut vous aider a coder plus vite, mais c'est VOUS qui comprenez ce que fait le code.

---

## Ressources

### Outils a essayer

| Outil | Type | Lien |
|-------|------|------|
| ChatGPT | Chat | chat.openai.com |
| Claude | Chat | claude.ai |
| GitHub Copilot | Autocomplete | github.com/features/copilot |
| Cursor | IDE + IA | cursor.sh |
| OpenCode | Agent | github.com/opencode-ai/opencode |
| Claude Code | Agent | anthropic.com/claude-code |

### Pour aller plus loin

- **MCP Spec** : modelcontextprotocol.io
- **Prompt Engineering** : learnprompting.org
- **NotebookLM** : notebooklm.google.com
- **AI News** : daily.dev, tldr.tech

---

*Cours prepare pour Mines Paris - Python 2025-2026*
*Derniere mise a jour : Janvier 2026*
