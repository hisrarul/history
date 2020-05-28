apt-get update
apt-get install nagios-nrpe-server nagios-plugins

vi /etc/nagios/nrpe.cfg
allowed_hosts=127.0.0.1,<add the master ip address>

/etc/init.d/nagios-nrpe-server restart


echo "Installing apache2 for HTTP monitoring"
apt-get install apache2
systemctl start apache2
systemctl status apache2
