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


### Ansible
```bash
ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook -i ansible/inventory.ini ansible/main.yml --vault-password-file vault_pass.txt
```

#### Ansible vault
```bash
ansible-vault encrypt ansible/host_vars/149.248.59.53.yml
```

https://stribny.name/posts/ansible-postgresql/