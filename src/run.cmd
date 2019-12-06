@echo off

if "%1" EQU "prod" goto prod
    python manage.py runserver --settings=django_vue_app.settings.dev
    goto exit

:prod
    python manage.py collectstatic --noinput
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver --settings=django_vue_app.settings.prod
:exit
