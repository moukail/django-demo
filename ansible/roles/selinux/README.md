https://access.redhat.com/articles/6999267


```bash
getenforce
sudo setenforce 1
```

### Identify Denials
```bash
sudo ausearch -m avc -ts recent
```

### Generate a Policy Stub
```bash
sudo ausearch -m avc -ts recent | audit2allow -M nginx_daphne
cat nginx_daphne.te
```

### Install the Policy
```bash
sudo semodule -i nginx_daphne.pp
```
