## Main App

#### Login to backend container
```bash
cd main
docker-compose exec backend sh
```

#### Database migration for Flask Application
```bash
export FLASK_APP=main.py
flask db init
flask db migrate
flask db upgrade
```