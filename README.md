# vanilladjango

## Getting Started

> 💡 First, `cd` to the project root directory where `manage.py` is.

1. Make env file.
```sh
cp .env.tmpl .env
```

2. Generate django secret key and add to my `.env` file.
Run below command and paste the output to `.env`.

```sh
docker compose exec vanilla python3 -c "import secrets; print(secrets.token_urlsafe(50))"
```

3. Set your database password in `.env` file.

4. Build docker image
```sh
docker compose up db  #build and start `db` container first.
docker compose build vanilla #build `vanilla` image.
docker compose up #start service.
```
