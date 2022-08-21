# Django Graphene Seed

a seed project for Django-graphene with authentication

This is a sample Graphql API backend with authentication and authorization

With Django Admin, it's useful to manage the contents.

This project would be useful for seeding a MVP backend

## Features

Most of the feature is from Django itself. You can easily add administrative CRUD menu for the database tables.

### Django admin tool

![image](https://user-images.githubusercontent.com/5399854/185773322-0e6e33e9-bc39-4ebb-9b8b-961dde473d8b.png)

![image](https://user-images.githubusercontent.com/5399854/185773324-aa4b5e2c-8ab1-4c33-9060-55db76e497cd.png)

![image](https://user-images.githubusercontent.com/5399854/185773332-50fb196d-959c-4f65-bf0e-1584daa0b541.png)

### Graphql

Only for DEBUG mode

![image](https://user-images.githubusercontent.com/5399854/185773337-c38b9da5-dd6f-4e32-9233-7cf72eace3fb.png)

Set `DEBUG=1` to `.env` if you want to turn it off

## Initialising

### Configuration

create `.env` file to set `HOST`

```
HOST=api.sameleserver.com
```

## Starting

```sh
docker compose up -d
```

### DB Migration
  - `docker compose run web python manage.py makemigrations`
  - `docker compose run web python manage.py migrate`
  
### Creating superuser
  - `docker compose run web python manage.py createsuperuser`

## Sample Books Model

Books app is a sample model for the graphql

## Features

### Admin pages

`/admin/` will provide the Admin pages for CRUD

### graphiql

API documentation with html client (playground)

`/graphql`

### Email backend

If you set `EMAIL_HOST` in `.env`, it will set EMAIL_BACKEND for smtp.

Sample for https://mailtrap.io/ sandbox

```
EMAIL_PORT=2525
EMAIL_HOST=smtp.mailtrap.io
EMAIL_FROM=kenny+orclarm@yeoyou.net
EMAIL_HOST_PASSWORD=yoursandboxsecret
EMAIL_HOST_USER=yoursandboxname
```

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
