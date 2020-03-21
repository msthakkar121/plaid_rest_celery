# Plaid API with Django Rest & Celery

"Few crazy out there who are willing to change the world will change it"

## TLDR;

```
git clone git@github.com:mjrulesamrat/plaid_rest_celery.git

cd plaid_rest_celery

chmod +x app/entrypoint.sh

docker-compose up -d --build

docker-compose exec web python manage.py migrate --noinput

docker-compose exec web python manage.py collectstatic --noinput
```

## Local Installation Guideline:

- Clone repository

```
git clone git@github.com:mjrulesamrat/plaid_rest_celery.git
```

- go to project directory

```
cd plaid_rest_celery
```

- Create Virtual Environment and install dependencies with [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

```
pipenv install
```

- Activate virtualenv

```
pipenv shell
```

- Setup settings file

```
cp plaid_rest_celery/settings/example-staging.py plaid_rest_celery/settings/staging.py

cp .env.example .env

# change user and password at .env.rabbitmq
```

- Run migrations

```
python manage.py migrate
```

- Run project locally

```
python manage.py runserver
```

## Admin panel

```
localhost:8000/plaid-admin/
```

## API docs using [drf-yasg](https://drf-yasg.readthedocs.io/en/latest/readme.html)

- You'll need to login to admin panel first to access API docs
```
localhost:8000/api/v1/docs/
```

## Celery local setup

- Start rabbitmq docker (Change user and password at .env.rabbitmq)

```
docker-compose -f docker-compose.rabbitmq.yml up -d

# If connection is refused despite right credenials
docker exec -it container_id sh
rabbitmqctl list_users | grep user
rabbitmqctl change_password user password  # reset password
```

- start celery worker

```
celery -A plaid_rest_celery worker --loglevel=info
```

## Update requirements for staging

Update requirements from Pipfile to `requirements.txt`. Everytime we do `pipenv install`, make sure to update `requirements.txt`

    pipenv lock -r > requirements.txt

## Struct Log

```
import structlog
logger = structlog.get_logger("plaid")

logger.log("message here", plaid_request_id=res['request_id'])
```