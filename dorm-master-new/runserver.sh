#!/bin/bash
# python manage.py makemigrations
# python manage.py migrate
# python manage.py collectstatic

# sudo nginx -c /home/jiang/dorm/nginx_conf/dorm_nginx.conf

uwsgi --ini dorm_uwsgi.ini &

sudo python serialrecv.py