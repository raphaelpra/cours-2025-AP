---
marp: true
theme: gaia
class: invert
paginate: true
---

# L'IA en Informatique
## Guide du Developpeur Moderne

**Mines Paris - 03/02/2026**

![bg right:40% contain](https://i.imgflip.com/aih2jk.jpg)

---

# Avertissement

> Ce que vous lisez ici represente l'etat de l'art de **janvier 2026**.
> 
> Dans 6 mois, la moitie sera obsolete.
> 
> C'est la beaute (et le cauchemar) de ce domaine.

---

# Plan du cours

1. **Vocabulaire essentiel** - LLM, Context, Tools, Agent
2. **Les 3 niveaux d'usage** - Chat, Autocomplete++, Agent
3. **Panorama des modeles** - Qui fait quoi ?
4. **Tools & MCP** - L'architecture moderne
5. **OpenCode en pratique** - Demo live
6. **L'IA pedagogique** - Apprendre avec l'IA

---

<!-- _class: lead -->

# 1. Vocabulaire essentiel

---

# LLM (Large Language Model)

Un **LLM** predit le prochain mot/token le plus probable.

```
Entree: "La capitale de la France est"
Sortie: "Paris" (avec haute probabilite)
```

**Exemples** : GPT-5, Claude, Llama, Mistral, Gemini

---

# Context (Contexte)

Ce que le modele "voit" pour generer sa reponse :

- Votre prompt actuel
- L'historique de la conversation
- Les fichiers partages
- Les instructions systeme

**Limite** : 128K-1M tokens selon le modele

---

# Tools (Outils)

Fonctions que le LLM peut appeler :

- Lire/ecrire des fichiers
- Executer du code
- Chercher sur le web
- Appeler des APIs

Ex: `read_file`, `write_file`, `bash`, `web_search`...

---

# Agent

**Agent = LLM + Tools + Boucle de raisonnement**

| Etape | Action |
|-------|--------|
| 1 | Analyser la tache |
| 2 | Planifier les etapes |
| 3 | Executer via Tools |
| 4 | Observer les resultats |
| 5 | Ajuster et continuer |

---

# Hands-on #1 (5 min)

Ouvrez ChatGPT ou Claude et demandez :

> "Explique-moi la difference entre un LLM et un agent, comme si j'avais 12 ans"

Observez comment l'IA adapte son langage !

---

<!-- _class: lead -->

# 2. Les 3 niveaux d'usage

---

# Niveau 1 : Le Chat

**Produits** : ChatGPT, Claude.ai

```
Vous: "Comment faire un tri a bulles en Python ?"
IA: "[explique + code]"
Vous: *copie le code dans votre editeur*
```

| Avantages | Inconvenients |
|-----------|---------------|
| Simple, gratuit | Copier-coller |
| Bon pour apprendre | Pas de contexte projet |
| Universel | Erreurs de copie |

---

# Niveau 2 : L'Autocomplete++

**Produits** : GitHub Copilot, Cursor, Cody

```python
def calculer_moyenne(notes):
    # L'IA complete automatiquement :
    return sum(notes) / len(notes)
```

| Avantages | Inconvenients |
|-----------|---------------|
| Integration IDE | Payant (~10-20€/mois) |
| Temps reel | Code parfois incorrect |
| Tab-Tab-Tab | "Tab addiction" |

---

# Hint : Le commentaire d'abord !

> Ecrivez un commentaire **avant** de coder.
> L'IA autocomplete mieux quand elle comprend votre intention.

```python
# Fonction qui calcule la distance euclidienne entre deux points
def distance(p1, p2):
    # L'IA complete avec confiance car elle sait ce que vous voulez
```

---

# Niveau 3 : L'Agent

**Produits** : Claude Code, Codex, OpenCode, Aider

L'IA a acces a **tout** votre projet. Elle peut :
1. Lire les fichiers
2. Ecrire du code
3. Executer les tests
4. Corriger les erreurs

---

# Niveau 3 : Avantages / Inconvenients

| Avantages | Inconvenients |
|-----------|---------------|
| Multi-fichiers | Plus cher |
| Autonome | Supervision necessaire |
| Refactoring | Changements inattendus |

---

# Tableau recapitulatif

| Critere | Chat | Autocomplete++ | Agent |
|---------|------|----------------|-------|
| **Complexite** | Simple | Moyenne | Elevee |
| **Contexte projet** | Non | Partiel | Total |
| **Autonomie** | Nulle | Faible | Forte |
| **Prix** | Gratuit-20€ | 10-20€/m | 20-100€/m |
| **Meilleur pour** | Apprendre | Coder vite | Gros projets |

---

# Hands-on #2 (10 min)

1. **Chat** : "Comment lire un fichier JSON en Python ?"
2. **Autocomplete** : Tapez `def load_json(` et observez
3. **Agent** : (demo) "Cree un script qui lit config.json"

---

<!-- _class: lead -->

# 3. Panorama des modeles

---

# Les principaux providers

| Provider | Modeles phares | Force |
|----------|---------------|-------|
| **OpenAI** | GPT-5.2, GPT-5.1 | Ecosysteme, multimodal |
| **Anthropic** | Claude Opus 4.5, Sonnet 4.5 | Code, agents |
| **Google** | Gemini 3, Gemini 3 Flash | Multimodal, Google |
| **xAI** | Grok 3 | Temps reel (X) |
| **Alibaba** | Qwen3 | Open-source |
| **MiniMax** | M2.1, Hailuo | Video |
| **Mistral** | Large 2, Pixtral | Europe, francais |

---

# Criteres d'evaluation

1. **Qualite** : Precision, pertinence, absence d'erreurs
2. **Cout** : Prix par million de tokens
3. **Latence** : Temps de reponse

---

# Tableau comparatif (Jan 2026)

| Modele | Qualite | Cout | Latence | Ideal pour |
|--------|---------|------|---------|------------|
| **Claude Opus 4.5** | ★★★★★ | ★★☆☆☆ | ★★★☆☆ | Code, agents |
| **Claude Sonnet 4.5** | ★★★★★ | ★★★★☆ | ★★★★☆ | Rapport Q/P |
| **GPT-5.2** | ★★★★★ | ★★★☆☆ | ★★☆☆☆ | General |
| **Gemini 3** | ★★★★★ | ★★★☆☆ | ★★★★☆ | Multimodal |
| **Gemini 3 Flash** | ★★★★☆ | ★★★★★ | ★★★★★ | Budget |
| **Qwen3 235B** | ★★★★★ | ★★★★★ | ★★★☆☆ | Open-source |

> Ces notes evoluent TRES vite !

---

# Prix indicatifs ($/1M tokens)

| Modele | Input | Output |
|--------|-------|--------|
| Claude Opus 4.5 | $15 | $75 |
| Claude Sonnet 4.5 | $3 | $15 |
| GPT-5.2 | $5 | $15 |
| Gemini 3 Flash | $0.075 | $0.30 |

---

<!-- _class: lead -->

# 4. Tools, MCP et integration

---

# Architecture d'un agent moderne

**AGENT = LLM + TOOLS + MCP**

- **LLM** : Le cerveau (Claude, GPT...)
- **TOOLS** : Read, Write, Bash, Grep, WebFetch
- **MCP** : Formatter, LSP, Recherche Web

---

# MCP (Model Context Protocol)

Standard ouvert pour connecter des outils aux LLMs.

- Standard unifie (marche avec Claude, GPT, etc.)
- Securise (permissions explicites)
- Extensible

Exemples : filesystem, brave-search, postgres, github...

---

# LSP + Agent = Intelligence

Le **LSP** permet a l'agent de :

- Detecter les erreurs en temps reel
- Comprendre les types et signatures
- Naviguer dans le code (go to definition)
- Refactoring intelligent

L'agent "comprend" vraiment votre code, pas juste le texte.

---

<!-- _class: lead -->

# 5. OpenCode en pratique

---

# Installation OpenCode

```bash
# Installation
brew install opencode
# ou: npm install -g @anthropic/opencode

# Configuration
export ANTHROPIC_API_KEY=sk-ant-...
```

---

# AGENTS.md - Le fichier magique

Fichier a la racine du projet que l'agent lit automatiquement.

- Contexte du projet
- Conventions de code
- Commandes utiles (`uv sync`, `uv run pytest`)
- Structure des dossiers

**L'agent adapte son comportement en fonction !**

---

# Skills & Commands

**Skills** : Instructions specialisees par techno
- `.opencode/skills/django.md`
- `.opencode/skills/fastapi.md`

**Commands** : Raccourcis personnalises
- `/test` - Lance tests + analyse erreurs
- `/deploy` - Deploie en production

---

# Hands-on #3 : Demo Live (10 min)

```bash
$ opencode

> Lis fibonacci.py et explique son fonctionnement

> Ajoute une version recursive memoizee

> Lance les tests et corrige les erreurs
```

---

<!-- _class: lead -->

# 6. L'IA comme outil pedagogique

---

# La methode des niveaux

Adaptez le niveau d'explication :

- "Explique [X] comme si j'avais **5 ans**"
- "Explique [X] comme si j'avais **12 ans**"
- "Explique [X] pour un **bachelier**"
- "Explique [X] pour un **doctorant**"

---

# Exemple : les pointeurs

- **5 ans** : "Une fleche qui montre ou est range un jouet"
- **12 ans** : "Une adresse, comme ton adresse postale"
- **Bachelier** : "Variable contenant l'adresse memoire"
- **Doctorant** : "Reference indirecte, aliasing..."

---

# NotebookLM : l'IA pour reviser

**notebooklm.google.com**

1. Uploadez vos cours (PDF, docs)
2. Posez des questions sur VOS documents
3. Generez des podcasts audio !
4. Creez des flashcards

---

# Strategies d'apprentissage

| Strategie | Prompt exemple |
|-----------|---------------|
| **Analogie** | "Compare X a la vie quotidienne" |
| **Socratique** | "Pose-moi des questions sur X" |
| **Exemples** | "Donne 5 exemples concrets de X" |
| **Erreurs** | "Erreurs courantes des debutants ?" |
| **Code** | "Montre X avec du Python simple" |

---

# Attention aux pieges !

> L'IA peut avoir l'air tres convaincante...
> **meme quand elle a tort.**

**Bonnes pratiques :**
- Testez TOUJOURS le code genere
- Demandez a l'IA de **reviewer son propre code**
- Demandez-lui d'**ecrire des tests**
- Croisez avec d'autres sources

---

# Hands-on #4 (10 min)

Choisissez un concept difficile et testez :

1. "Explique comme si j'avais 12 ans"
2. "Montre-moi avec du code Python simple"
3. "Quelles erreurs font les debutants ?"

---

<!-- _class: lead -->

# Conclusion

---

# Ce qu'il faut retenir

1. **Vocabulaire** : LLM, Context, Tools, Agent

2. **3 niveaux** :
   - Chat = simple, copier-coller
   - Autocomplete++ = fluide, dans l'editeur
   - Agent = puissant, autonome

3. **Modeles** : Qualite / Cout / Latence

4. **L'IA evolue vite** : Restez curieux !

---

# Le message final

> L'IA ne remplace pas la comprehension des fondamentaux.
> 
> Elle amplifie vos capacites... **si vous savez ce que vous faites.**

Vous avez appris Python ce semestre.

L'IA peut vous aider a coder plus vite, mais c'est **VOUS** qui comprenez ce que fait le code.

---

# Ressources

| Outil | Type | Lien |
|-------|------|------|
| ChatGPT | Chat | chat.openai.com |
| Claude | Chat | claude.ai |
| GitHub Copilot | Autocomplete | github.com/features/copilot |
| Cursor | IDE + IA | cursor.sh |
| OpenCode | Agent | github.com/opencode-ai/opencode |

**Pour aller plus loin** : modelcontextprotocol.io, learnprompting.org, notebooklm.google.com

---

<!-- _class: lead -->

# Questions ?

*Cours prepare pour Mines Paris - Python 2025-2026*

*Ce cours a été rédigé par l'IA ;)*
