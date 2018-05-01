sudo ln -sf ~/web/etc/test_wsgi.conf /etc/nginx/sites-enabled/test_wsgi.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

