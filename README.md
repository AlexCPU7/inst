Create dirs:
docker/database/;
docker/logs/;
media/;
static/

Create:
project/conf.py

Update:
docker-compose.yml

docker-compose build --no-cache
docker-compose up -d

python manage.py migrate
python manage.py createsuperuser
