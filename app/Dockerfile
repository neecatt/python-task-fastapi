FROM python:3.8

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "celery", "-A", "src.core.celeryconfig", "worker", "--loglevel=info" ]
