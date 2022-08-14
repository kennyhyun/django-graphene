# django-graphene
a seed project for Django-graphene with authentication

## Initialising

### DB Migration
  - `docker compose run web python manage.py migrate`
  
### Creating superuser
  - `docker compose run web python manage.py createsuperuser`

## Commands

- Run the containers
  - `docker compose up -d`
- Stop the containers
  - `docker compose down -v`
- Building the docker image
  - `docker compose build`
- Check for the logs
  - `docker compose logs -f web`
  - or `docker logs -f core-web-1`
