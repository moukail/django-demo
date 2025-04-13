
sudo systemctl restart supervisord

sudo supervisorctl reread
sudo supervisorctl update

sudo supervisorctl start daphne
sudo supervisorctl status daphne