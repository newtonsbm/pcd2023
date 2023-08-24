FROM python:3-slim
RUN mkdir /code
COPY . /code
WORKDIR  /code/
RUN pip install django django-crispy-forms crispy-bootstrap5 psycopg2-binary
