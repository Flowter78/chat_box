# 💬 Chat Box – App Streamlit déployée sur Heroku

Cette application est un projet Streamlit déployé sur Heroku.  
Elle a été conçue et testée localement avant d’être poussée sur une app distante via Git.

## 🚀 Déploiement sur Heroku

### 📁 Structure minimale du projet

```
chat_box/
├── my_app.py
├── requirements.txt
├── Procfile
├── setup.sh
├── runtime.txt (optionnel)
```

- `Procfile` : indique à Heroku comment lancer l’app.
- `setup.sh` : configure Streamlit pour tourner sur Heroku.
- `runtime.txt` : fixe la version de Python (ex. `python-3.10.12`).

### 🧪 Commandes de déploiement

1. Créer une nouvelle app Heroku :

```bash
heroku create my-app-name
```

2. Modifier le remote Heroku si besoin :

```bash
git remote set-url heroku https://git.heroku.com/my-app-name.git
```

3. Pousser la branche locale vers la branche `main` d’Heroku :

```bash
git push heroku nom_de_ta_branche_locale:main
```

---

## 🔀 Remarques Git importantes

- `origin` : dépôt GitHub
- `heroku` : dépôt distant de déploiement
- `main` ou `master` sont les seules branches surveillées par Heroku pour déployer automatiquement

### 📤 Commandes Git utiles pour `git push`

| Commande                                      | Ce que ça fait                                                        |
|-----------------------------------------------|------------------------------------------------------------------------|
| `git push origin main`                        | Pousse ta branche locale `main` vers `origin/main`                    |
| `git push origin dev`                         | Pousse `dev` local vers `origin/dev`                                  |
| `git push heroku chat_box_heroku:main`        | Pousse `chat_box_heroku` local vers `heroku/main`                     |
| `git push origin feature-x:super-feature`     | Pousse `feature-x` local vers `origin/super-feature`                  |
| `git push origin main:dev`                    | Pousse `main` local vers `origin/dev` (⚠️ utile pour tester rapidement) |

---

## 🛠️ Outils utilisés

- [Python 3.10](https://www.python.org)
- [Streamlit](https://streamlit.io)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Git](https://git-scm.com)

---

> Développé avec 💡 par Florent – projet d’apprentissage autour de Git, Heroku et Streamlit.

## Heroku 

Ajoute la clé à Heroku (très important) :
```poxershell
heroku config:set OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxx
```