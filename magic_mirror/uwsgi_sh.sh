#!/bin/bash -e

echo uwsgi test >>  /home/pi/uwsgi_log.txt
uwsgi --ini /home/pi/magic_mirror/config/mysite_uwsgi.ini  >> /home/pi/uwsgi_log.txt
