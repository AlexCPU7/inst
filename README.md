## Server startup

Create dirs:
```bash
docker/database/;
docker/logs/;
media/;
static/
```

Create:
```bash
project/conf.py
```

Update:
```bash
docker-compose.yml
```
Start docker containers:
```bash
docker-compose build --no-cache
docker-compose up -d
```

Migrate:
```bash
python manage.py migrate
python manage.py createsuperuser
```
