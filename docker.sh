ssh israrul@13.232.136.108
password: israrul

    2  apt-get install docker.io -y
    3  apt-get update
    4  apt-get install docker.io -y
    5  systemctl status docker
    6  docker run hello-world
    7  docker images
    8  top
    9  docker --version
   10  vi /etc/ssh/sshd_config
   11  useradd israrul
   12  su - israrul
   13  mkdir /home/israrul
   14  vi /etc/passwd
   15  ls -ld /home/israrul
   16  chown israrul:israrul /home/israrul
   17  su - israrul
   18  vi /etc/group
   19  passwd israrul
   20  su - israrul
