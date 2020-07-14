## Create a role directory structure using ansible-galaxy
ansible-galaxy init <role_name> --offline

## Install ansible 2.5.0
```
pip install ansible==2.5.0
find / -name ansible  #look for bin path
export PATH=$PATH:/usr/local/bin/ansible
```

## Ansible pre-requisites for aws
```
apt update
apt install software-properties-common
apt-add-repository --yes --update ppa:ansible/ansible
apt install ansible -y
apt install python-pip -y
pip install boto
pip install awscli
```
