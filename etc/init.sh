sudo ln -sf ~/web/etc/test_wsgi.conf /etc/nginx/sites-enabled/test_wsgi.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
source ~/web/ask/newenv/bin/activate
gunicorn -b 0.0.0.0:8080 --pythonpath ~/web/etc/ hello:app &
gunicorn -b 0.0.0.0:8000 --pythonpath ~/web/ask/ ask.wsgi:application &
#sudo ln -sf ~/web/etc/hello.conf /etc/supervisor/conf.d/hello.conf
#sudo ln -sf ~/web/etc/ask.conf /etc/supervisor/conf.d/ask.conf
#sudo supervisorctl reread
#sudo supervisorctl update
#sudo supervisorctl start hello
#sudo supervisorctl start ask
