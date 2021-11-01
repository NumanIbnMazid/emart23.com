FROM python:3.8.8-alpine

# set environment variables
ENV EMART23=/home/app/emart23
ENV APP_USER=emart23_user

RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER
# set work directory


RUN mkdir -p $EMART23
RUN mkdir -p $EMART23/static

# where the code lives
WORKDIR $EMART23

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev linux-headers g++
# install dependencies
RUN pip install --upgrade pip
# copy project
COPY . $EMART23
RUN pip install -r requirements.txt
COPY ./entrypoint.sh $EMART23

CMD ["/bin/bash", "/home/app/emart23/entrypoint.sh"]