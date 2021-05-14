FROM python:3

ENV PYTHONUNBUFFERED 1  

RUN mkdir /project

WORKDIR /project

COPY . /project/

RUN pip install -r requirements.txt

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait ./wait
RUN chmod +x ./wait

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8003

