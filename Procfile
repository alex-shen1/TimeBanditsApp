release: python manage.py collectstatic --noinput --clear && python manage.py makemigrations && python manage.py migrate
web: gunicorn project.wsgi
