**todo**
- [ ] change `.env.app.example` files to `.env.app.production.example` and `.env.app.development.example`
- [ ] copy `.env` files
**to run the project**
- [ ] 
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
