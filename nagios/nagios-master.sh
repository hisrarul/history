hostnamectl set-hostname nagios-master
hostname
apt-get update
apt-get install -y wget build-essential unzip openssl libssl-dev
apt-get install apache2 php libapache2-mod-php php-gd libgd-dev
adduser nagios
groupadd nagcmd
grep nagcmd /etc/group
usermod -a -G nagcmd nagios
id nagios
usermod -a -G nagcmd www-data
id www-data
pwd
ls
wget https://assets.nagios.com/downloads/nagioscore/releases/nagios-4.4.6.tar.gz
tar xvzf nagios-4.4.6.tar.gz
ls
cd nagios-4.4.6/
ls
./configure --with-command-group=nagcmd
make all
make install
make install-init
make install-commandmode
make install-config
cp -R contrib/eventhandlers/ /usr/local/nagios/libexec
chown -R nagios:nagios /usr/local/nagios/libexec/eventhandlers
cat << EOF > /tmp/nagios.conf
ScriptAlias /nagios/cgi-bin "/usr/local/nagios/sbin"

<Directory "/usr/local/nagios/sbin">
   Options ExecCGI
   AllowOverride None
   Order allow,deny
   Allow from all
   AuthName "Restricted Area"
   AuthType Basic
   AuthUserFile /usr/local/nagios/etc/htpasswd.users
   Require valid-user
</Directory>

Alias /nagios "/usr/local/nagios/share"

<Directory "/usr/local/nagios/share">
   Options None
   AllowOverride None
   Order allow,deny
   Allow from all
   AuthName "Restricted Area"
   AuthType Basic
   AuthUserFile /usr/local/nagios/etc/htpasswd.users
   Require valid-user
</Directory>
EOF
htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin
ls -l /usr/local/nagios/etc/htpasswd.users
cat /usr/local/nagios/etc/htpasswd.users
a2enconf nagios
a2enmod cgi rewrite
IPADDR=$(ifconfig | egrep '172.* | 192.*' | awk '{print $2}' | awk -F':' '{print $2}')
echo "$IPADDR nagios-server" | sudo tee -a /etc/hosts
ping -c 4 nagios-server
systemctl restart apache2
systemctl status apache2
# Download the nrpe plugin
wget http://www.nagios-plugins.org/download/nagios-plugins-2.2.1.tar.gz
tar xvzf nagios-plugins-2.2.1.tar.gz
ls
cd nagios-plugins-2.2.1/
ls
./configure --with-nagios-user=nagios --with-nagios-group=nagios --with-openssl
make
make install
sed -i 's?#cfg_dir=/usr/local/nagios/etc/servers?cfg_dir=/usr/local/nagios/etc/servers?' /usr/local/nagios/etc/nagios.cfg
mkdir /usr/local/nagios/etc/servers
# Verify the config
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
systemctl restart nagios
systemctl enable nagios
