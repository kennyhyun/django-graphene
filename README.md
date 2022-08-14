# Django Graphene Seed

a seed project for Django-graphene with authentication

This is a sample Graphql API backend with authentication and authorization

With Django Admin, it's useful to manage the contents.

This project would be useful for seeding a MVP backend


## Initialising

### Configuration

create `.env` file to set `HOST`

```
HOST=api.sameleserver.com
```


### DB Migration
  - `docker compose run web python manage.py makemigrations`
  - `docker compose run web python manage.py migrate`
  
### Creating superuser
  - `docker compose run web python manage.py createsuperuser`
  
## Starting

```sh
docker compose up -d
```
## Sample Books Model

Books app is a sample model for the graphql

## Features

### Admin pages

`/admin/` will provide the Admin pages for CRUD

### graphiql

API documentation with html client (playground)

`/graphql`

### Email backend

because of `EMAIL_BACKEND` setting, it's just output the email body in the stdout

You can see the logs by `docker compose logs web -f`

Please properly set the email backend for sending email. https://www.sitepoint.com/django-send-email/
or set `GMAIL_APP_PASSWORD` and `GMAIL_ADDRESS`

## Sample queries

### List books

```graphql
{
  allBooks{
    id
    title
  }
}
```

### Login

```graphql
mutation{
  tokenAuth(email:"kenny+guest2@yeoyou.net", password: "dihk1234") {
    token
    success
    errors
    user {
      username
    }
    refreshToken
  }
}
```


### Refresh token

```graphql
{
}
```

### Signup

```graphql
mutation{
  register(email:"user@yeoyou.net", password1: "userpa$$w0rd", password2: "userpa$$w0rd", username: "user") {
    success
    errors
    token
    refreshToken
  }
}
```


### Verify email

```graphql
mutation{
  verifyAccount(token: "eyJ1c2VybmFtZ-find-your:token:sent_my_email") {
    success
    errors
  }
}
```

** See also https://django-graphql-auth.readthedocs.io/en/latest/quickstart/#full-schema

## Utilising

### To allow CORS

By default, it will allow subdomains of `COREHOST`

If you specify `CORSHOST=domain.me` in the `.env` file, it will allow `*.domain.me` domains

### To allow same site cookie

TBC

## Other Commands

- Run the containers
  - `docker compose up -d`
- Stop the containers
  - `docker compose down`
- Building the docker image
  - `docker compose build`
- Check for the logs
  - `docker compose logs -f web`
  - or `docker logs -f core-web-1`
