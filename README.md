# balance-service

Example Django service to record user balances in various currencies.

Balance-service is a Django (Python) app with a Postgres database.
The service can be run from docker using docker compose.

## Development Setup

1. Create a .env file in the root dir to hold environment vars. An example is included in the project:

```
cd balance-service
cp example.env .env
```

2. Install [Docker](https://docs.docker.com/desktop/), if needed, and launch it to install the command line tools.

3. Build the docker containers:
   `docker compose -f local.yml build`

4. Initialize the database by running the database migrations:
   `docker compose -f local.yml run django python manage.py migrate`

5. (Optional) Setup username/password access the Django admin backend:
   `docker compose -f local.yml run django python manage.py createsuperuser`

6. (Optional) Spin up the development server on port 8000:
   `docker compose -f local.yml up`

7. Run the tests:
   `docker compose -f local.yml run django python manage.py test`
