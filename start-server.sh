#!/bin/bash

# start uwsgi and then nginx. catch the server output at the end
uwsgi --ini conf/uwsgi.ini && nginx && tail -f /var/log/uwsgi/ds-app.log
