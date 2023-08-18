FROM python:3-slim
RUN mkdir /code
COPY . /code
WORKDIR  /code/
RUN pip install django django-crispy-forms crispy-bootstrap5
RUN python manage.py migrate
EXPOSE 8000
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
