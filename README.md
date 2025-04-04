# chat_box
Simple chatbox to discuss with trading AI agent about strategy, stock market or whatever. I'm using openAI.


## Run locally
Linux:
```bash
git clone https://github.com/professorkazarinoff/simple-streamlit-app.git
cd simple-streamlit-app
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run simple_app.py
```
Windows:
```powershell
git clone https://github.com/Flowter78/chat_box.git
cd chat_box
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run my_app.py
```

## Deploy on Heroku
Installer Heroku CLI + Créer un compte

```
heroku login
heroku create [nom-application]
git push heroku chat_box_heroku:main
heroku open
```

https://my-app-heroku-f62b22c3bd7c.herokuapp.com/

## Annexe 

### Avancement

- Structure de projet Streamlit bien formée ✅
- Utilisation de .env pour la sécurité ✅
- Variables d’environnement Heroku ✅
- Gestion des branches et des remotes Git comme un pro ✅
- Debug d’un crash Heroku avec les logs ✅
- Et surtout… un déploiement réussi

### Commandes Git utiles pour `git push`

| Commande                                      | Ce que ça fait                                                        |
|-----------------------------------------------|------------------------------------------------------------------------|
| `git push origin main`                        | Pousse ta branche locale `main` vers `origin/main`                    |
| `git push origin dev`                         | Pousse `dev` local vers `origin/dev`                                  |
| `git push heroku chat_box_heroku:main`        | Pousse `chat_box_heroku` local vers `heroku/main`                     |
| `git push origin feature-x:super-feature`     | Pousse `feature-x` local vers `origin/super-feature`                  |
| `git push origin main:dev`                    | Pousse `main` local vers `origin/dev` (⚠️ utile pour tester rapidement) |

```git
git push <remote> <branche_locale>:<branche_distant>
```

- `origin` : dépôt distant GitHub
- `heroku` : dépôt distant de déploiement
- `main` ou `master` sont les seules branches surveillées par Heroku pour déployer automatiquement