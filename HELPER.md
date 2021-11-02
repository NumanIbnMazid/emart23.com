# emart23 web application's helper markdown file

* Docker Helper

- Buiding Docker Image

    $ docker build -t example_image .

- Run Docker Compose

    $ docker-compose up --build

    * For No Caching

    $ docker-compose build --no-cache

- Remove all images and containers

    $ docker-compose down --rmi all

- Check Docker Images

    $ docker images

- Tag a docker image

    $ docker tag example_image:latest numanibnmazid/example_repository:latest

- Pushing image to docker hub

    $ docker push numanibnmazid/example_repository:latest

* Project Runner Helper

- Ruuning Project with Uvicorn

    $ gunicorn emart23.asgi:application -k uvicorn.workers.UvicornWorker