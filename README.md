### install python
```bash
sudo apt install python3.12
```

### set up virtual environment to install django
```bash
python -m venv env
source env/bin/activate
pip install django
pip install -r requirements.txt
```

### Create a Django Project
```bash
django-admin startproject django_demo
cd django_demo
```

### Create an App
```bash
python manage.py startapp blog
```

Add your app to INSTALLED_APPS in mysite/settings.py.

### Docker
#### Install Docker
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_users

docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
docker-compose run web python manage.py seed_users
```

### Docker
#### access container
```bash
docker exec -it django-demo-web-1 sh
```

### Ansible
#### Install Ansible
```bash
sudo apt update
sudo apt install pipx sshpass
pipx install ansible-core==2.18.4
pipx install --include-deps ansible --force
pipx ensurepath
ansible --version

ansible-galaxy collection install community.general
ansible-galaxy collection install community.postgresql
ansible-galaxy collection list

pipx upgrade --include-injected ansible
```

```bash
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ansible/inventory.ini ansible/main.yml --vault-password-file vault_pass.txt
```

#### Ansible vault
```bash
ansible-vault encrypt ansible/host_vars/149.248.59.53.yml
```

https://stribny.name/posts/ansible-postgresql/