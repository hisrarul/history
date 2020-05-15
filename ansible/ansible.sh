
## Install ansible on ubuntu
sudo apt update
apt install software-properties-common
apt-add-repository --yes --update ppa:ansible/ansible
apt install ansible
ansible --version


## Steps to follow after ansible installation on both master and hosts

useradd ansible
vi /etc/group
#### Add ansible user to the group "adm, sudo"
ls -l /home
mkdir /home/ansible
chown -R /home/ansible
chown -R ansible:ansible /home/ansible
su - ansible
passwd ansible
su - ansible
sudo visudo
## update the line as below
%sudo   ALL=(ALL:ALL) NOPASSWD:ALL


## Steps to follow on master
su - ansible
ssh-keygen
ls -l .ssh/
cat .ssh/id_rsa.pub
ls -ld .ssh/
ssh ansible@172.31.47.19

## Steps to follow on slave/managed host
su - ansible
mkdir .ssh
chmod 700 .ssh
cd .ssh/
vi authorized_keys
ls -l
chmod 600 authorized_keys
ifconfig


## Ready to test from ansible master
su - ansible
echo -e "[israrul]\n172.31.47.19" | sudo tee -a /etc/ansible/hosts
tail -3 /etc/ansible/hosts
ansible israrul -m ping

## Ready to work with playbook and roles
ansible israrul -m command -a "date"
ls -l
vi first_playbook.yaml
ansible-playbook first_playbook.yaml -s
ansible-playbook first_playbook.yaml --check
vi first_playbook.yaml
ansible-playbook first_playbook.yaml --check
vi first_playbook.yaml
ansible-playbook first_playbook.yaml --check
ansible-playbook first_playbook.yaml --check --ask-pass
ansible-playbook first_playbook.yaml --check --ask-pass
sudo useradd test2
visudo
sudo visudo
sudo useradd test2
id test2
vi first_playbook.yaml
ansible-playbook first_playbook.yaml --check
ansible-playbook first_playbook.yaml
cat first_playbook.yaml
ansible-galaxy init nginx --offline
ls -l
cd nginx/
ls -l
tree
sudo apt-get install tree -y
tree
ls
cd tasks/
ls
vi play1.yaml
vi play2.yaml
vi main.yml
tree
cd ..
tree
vi files/index.html
vi tasks/play3.yaml
vi tasks/main.yml
vi meta/main.yml
pwd
cd ..
vi site.yaml
ansible-playbook site.yaml --check
cd nginx/
vi tasks/play1.yaml
cd ..
ansible-playbook site.yaml --check
vi nginx/tasks/play2.yaml
ansible-playbook site.yaml --check
vi nginx/tasks/play3.yaml
ansible-playbook site.yaml --check
ansible-playbook site.yaml
vi site.yaml
ansible-playbook site.yaml
cat site.yaml
cat /etc/ansible/hosts | tail -3
pwd
vi inventory.txt
ansible-playbook site.yaml -i inventory.txt
vi site.yaml
ansible-playbook site.yaml -i inventory.txt


list = ["item1", "item2"]

list:
  - item1
  - item2

{
    "list": ["item1", "item2"]
}

## Create a playbook
---
- hosts: israrul
  become_method: sudo
  become: yes
  become_user: root
  name: Play1
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: latest

## Dry run
ansible-playbook first_playbook.yaml --check

## Apply the changes
ansible-playbook first_playbook.yaml


## Ansible Role
echo "<html><h1>Ngnix configured by us.</h1></html>" | sudo tee -a index.html

vi play1.yaml
---
- name: Install nginx
  apt:
    name: nginx
    state: latest

vi play2.yaml
---
- name: Copy file from master to host
  copy:
    src: index.html
    dest: /var/www/html/index.html
    mode: u+rwx,g+rx,o+rx

vi play3.yaml
---
- name: restart nginx
  service:
    name: nginx
    state: restarted

vi site.yaml
---
- hosts: israrul
  become_user: root
  become: true
  become_method: sudo
  roles:
    - nginx
