FROM python:3.12-alpine
RUN pip install pika
RUN mkdir /code
COPY . /code
WORKDIR /code
RUN apk add --no-cache bash
RUN wget -O /bin/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x /bin/wait-for-it.sh
CMD python main.py