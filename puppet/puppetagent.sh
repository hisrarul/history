wget https://apt.puppetlabs.com/puppet5-release-xenial.deb
dpkg -i puppet5-release-xenial.deb
apt-get update
apt-get install puppet-agent -y
hostnamectl set-hostname puppet-agent01.example.com
hostname
echo "172.31.33.138 puppet-agent01.example.com puppet-agent01" >> /etc/hosts
echo "172.31.40.41 puppet-server.example.com puppet-server" >> /etc/hosts



cat /etc/puppetlabs/puppet/puppet.conf
[main]
certname = puppet-agent01.example.com
server = puppet-server.example.com
