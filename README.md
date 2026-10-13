# TaskFlow — dépôt fil rouge CI/CD

TaskFlow est une petite API de gestion de tâches écrite en Python avec FastAPI.
C'est le projet fil rouge du module CI/CD (Mastère DevOps M1, Sup de Vinci) :
pendant trois jours, vous allez construire autour d'elle un pipeline complet
qui teste, construit, sécurise et livre l'application.

## Lancer l'API en local

Prérequis : Python 3.10 ou plus récent.

```bash
python3 -m venv .venv
source .venv/bin/activate          # Windows : .venv\Scripts\activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

L'API répond sur http://localhost:8000 et sa documentation interactive est sur
http://localhost:8000/docs.

## Vérifier le code

```bash
pytest           # tests automatiques
ruff check .     # lint
ruff format .    # mise en forme
```

## Lancer avec Docker

```bash
docker build -t taskflow .
docker run --rm -p 8000:8000 taskflow
```

## Endpoints

| Méthode | Chemin | Rôle |
| --- | --- | --- |
| GET | `/health` | État de l'API et version |
| GET | `/tasks` | Liste des tâches |
| GET | `/tasks/search?q=...` | Recherche dans les titres |
| POST | `/tasks` | Crée une tâche (`{"title": "..."}`) |
| GET | `/tasks/{id}` | Détail d'une tâche |
| PATCH | `/tasks/{id}/done` | Marque une tâche comme faite |
| DELETE | `/tasks/{id}` | Supprime une tâche (en-tête `X-API-Token` requis) |

## Configuration

| Variable | Rôle | Défaut |
| --- | --- | --- |
| `APP_VERSION` | Version affichée par `/health` | `0.1.0` |
| `DB_PATH` | Fichier SQLite | `taskflow.db` |
| `API_TOKEN` | Jeton exigé pour supprimer une tâche | vide (suppression désactivée) |
| `NOTIFY_WEBHOOK_URL` | Webhook appelé à chaque création de tâche | vide (désactivé) |

## Équipe

- Aimen Klai (@aimenklai)
- Aimen Klai (Compte binôme : @aimenklaitest)

## Gouvernance du dépôt

Règles configurées via GitHub Ruleset sur la branche `main` (`protect-main`) :

1. **Restrict deletions** : Empêche la suppression accidentelle ou non autorisée de la branche `main`.
2. **Block force pushes** : Interdit les commandes `git push --force` qui écrasent et détruisent l'historique partagé du dépôt.
3. **Require a pull request before merging** : Interdit tout push direct sur `main` et impose l'ouverture d'une Pull Request pour toute modification.
4. **Required review approvals (1)** : Impose qu'au moins un collaborateur (le binôme) révise et approuve la Pull Request avant de pouvoir fusionner le code.

### Preuve du refus de push direct sur `main`

Lors d'une tentative de push direct sur `main` (`git push origin main`), GitHub rejette l'opération :

```text
$ git commit --allow-empty -m "test: tentative de push direct sur main"
[main efb4d93] test: tentative de push direct sur main
$ git push origin main
 ! [remote rejected] main -> main (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/aimenklai/cicd-fil-rouge.git'
```

