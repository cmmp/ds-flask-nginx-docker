FROM ubuntu:bionic

ENV TZ=:/etc/localtime

RUN apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install -y locales wget curl ca-certificates vim \
    software-properties-common python3-dev python3-pip nginx

RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.utf8

RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64 && \
    chmod +x /usr/local/bin/dumb-init

RUN mkdir -p /var/log/uwsgi

RUN pip3 install pipenv

COPY conf/ds-app.conf /etc/nginx/sites-available/

RUN ln -s /etc/nginx/sites-available/ds-app.conf /etc/nginx/sites-enabled

WORKDIR /usr/src/app

COPY . .

RUN chown -R www-data.www-data /usr/src/app

RUN pipenv install --system

EXPOSE 80

ENTRYPOINT ["/usr/local/bin/dumb-init", "--"]

CMD ["/usr/src/app/start-server.sh"]
