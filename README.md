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


# Usage Notes

1. Django admin is available at http://localhost:8000/admin
2. The API is available at http://localhost:8000/api/v1

3. Adding Transaction objects from the django admin backend will automatically update the user's balance. No checks are
performed to ensure that the user has sufficient funds to cover the transaction, thus allowing for negative balances.

4. Currency is currently ignored for simplicity, but it would be easily to filter transactions by currency and calculate balances for each currency.

# API

1. User balance can be fetched via the API at http://localhost:8000/api/v1/balances/{user_id}/
2. User balance can be fetched via the API at http://localhost:8000/api/v1/balances/?username={username}
3. You must be authenticated as a superuser to access the API.

# Using invoke

1. Run the tests:
   `inv docker.test`
2. Linting + security testing:
   `inv check`
