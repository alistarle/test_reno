FROM python:3

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64
RUN chmod +x /usr/local/bin/dumb-init

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ARG FLASK_APP_NAME
ENV FLASK_APP_NAME=$FLASK_APP_NAME

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]
CMD ["bash", "-c", "gunicorn -c gunicorn_conf.py app_file:app"]