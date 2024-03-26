**To run the project on new server**

- [ ] copy `.env` files

```shell
cp .env.app.example .env.app.production
cp .env.postgres.example .env.postgres.production
```
- [ ] add new machine's ip address to `.env` file
```shell
ALLOWED_HOSTS=localhost app 127.0.0.1 put_ip_here [::1]
```

- [ ] spin up the containers
```shell
docker compose -f docker-compose.production.yml up --build
```
- [ ] run
```shell

docker compose -f docker-compose.production.yml exec app python ./src/manage.py collectstatic --no-input
docker compose -f docker-compose.production.yml exec app python ./src/manage.py migrate --no-input
```


**How to log exceptions**

```python
import traceback
from datetime import datetime
with open("/applogs/exceptions.log", "a") as file:
    file.write(
        f"an error happened at {datetime.datetime.now()}\n"
    )
    file.write(f"Exception details: {str(e)}\n")
    file.write(f"Full traceback: \n{traceback.format_exc()}\n")
    file.write("-------------------------------------------------------")
```
---
**To run the django app individually to test static changes**
```shell
docker build -f ./app/Dockerfile -t hello_django:latest ./app
```
```shell
docker run -d \
    -p 8006:8000 \
    -e "SECRET_KEY=please_change_me" -e "DEBUG=1" -e "DJANGO_ALLOWED_HOSTS=*" \
    hello_django python /usr/src/app/manage.py runserver 0.0.0.0:8000
```
---
**to execute a command into a container**
```shell
docker-compose exec app python manage.py flush --no-input
docker-compose exec app python manage.py migrate
```
