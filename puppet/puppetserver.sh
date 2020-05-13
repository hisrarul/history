wget https://apt.puppetlabs.com/puppet5-release-xenial.deb
dpkg -i puppet5-release-xenial.deb
apt-get update
apt-get install puppetserver

vi /etc/default/puppetserver
JAVA_ARGS="-Xms512m -Xmx512m"

systemctl status puppetservier
systemctl status puppetserver
systemctl start puppetserver
journalctl -xe
systemctl status puppetserver
vi /etc/default/puppetserver
systemctl restart puppetserver
systemctl status puppetserver
systemctl enable puppetserver
