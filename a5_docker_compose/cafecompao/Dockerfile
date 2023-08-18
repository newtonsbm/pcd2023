FROM python:3-slim
RUN mkdir /code
COPY . /code
WORKDIR  /code/
RUN pip install django django-crispy-forms crispy-bootstrap5
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
