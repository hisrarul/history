## Created by Israrul Haque
#
## This script has been tested on CentOS Linux release 7.6.1810 (Core)

#!/bin/bash
echo "Please run as root to run this script, press Y to process otherwise N: "
read login

if [ $login == 'N' ]
then
    echo "Better see you next time."
elif [ $login == 'Y' ] && [ $(id -u) == '0' ]
then
    echo "Starting the installation of LAMP.."
    yum install -y http://rpms.remirepo.net/enterprise/remi-release-7.rpm
    yum-config-manager --enable remi-php56
    yum install wget httpd git php php-pear php-mysql php-mbstring php-gd mariadb-server mariadb -y
    # start mysql service
    systemctl start mariadb

    # Configure database
    pass='Assignment@321'
    mysql -e "SET PASSWORD FOR root@localhost = PASSWORD('Assignment@321');FLUSH PRIVILEGES;" 
    printf "Assignment@321\n n\n n\n n\n y\n y\n y\n" | mysql_secure_installation
    mysql -u root -p"$pass" -e "create database wpdb";
    mysql -u root -p"$pass" -e "create user wpuser@localhost identified by 'Haptik@321';"
    mysql -u root -p"$pass" -e "grant all privileges on wpdb.* to wpuser@localhost;"
    mysql -u root -p"$pass" -e "FLUSH PRIVILEGES;"


    echo "Install wordpress latest version.."
    wget https://wordpress.org/latest.tar.gz
    tar xzvf latest.tar.gz
    cp -rf wordpress/* /var/www/html/

    # To store the uploaded file
    mkdir /var/www/html/wp-content/uploads
    
    
    echo "Configure wordpress .."
    git clone https://hisrarul@bitbucket.org/hisrarul/assignment.git
    cp assignment/wp-config.php /var/www/html/wp-config.php
    sed -i 's/database_name_here/wpdb/g' /var/www/html/wp-config.php
    sed -i 's/username_here/wpuser/g' /var/www/html/wp-config.php
    sed -i 's/password_here/Haptik@321/g' /var/www/html/wp-config.php
    chown -R apache:apache /var/www/html
    chcon -R --reference /var/www /var/www/html

    echo "Restarting Apache service .."
    systemctl restart httpd

    echo 'Wordpress has been successfull configure!!'
    echo ''
    echo -e "Please keep wordpress user details confidential with you: \nUsername: wpuser \nPassword: Haptik@321"

else
    echo "Please login as root user"
    exit 1
fi