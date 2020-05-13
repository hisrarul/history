wget https://apt.puppetlabs.com/puppet5-release-xenial.deb
dpkg -i puppet5-release-xenial.deb
apt-get update
apt-get install puppet-agent -y
hostnamectl set-hostname puppet-agent01.example.com
hostname
