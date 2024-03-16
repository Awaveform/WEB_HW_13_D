# WEB_HW_13_D

poetry add django
poetry add psycopg2

docker run --name contacts-postgres -p 5433:5432 -e POSTGRES_PASSWORD=567234 -d postgres

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser :: admin
