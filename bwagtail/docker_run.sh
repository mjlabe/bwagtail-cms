#!/bin/sh

./wait-for.sh db echo Database Ready && \
  python manage.py makemigrations && \
  python manage.py migrate && \
  python manage.py collectstatic --noinput && \
  echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('wagtail', 'wagtail@myproject.com', 'wagtail')" | python manage.py shell && \
  gunicorn bwagtail.wsgi:application --bind 0.0.0.0:8000 --workers 3
