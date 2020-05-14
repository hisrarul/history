##### History of server
pwd
mkdir demo
ls
cd demo/
echo $PATH
puppet module generate intelli-demo
ls
tree
apt install tree -y
clear
tree
vi demo/manifests/init.pp
ls
puppet module build demo
ls -l /root/demo/demo/pkg/intelli-demo-0.1.0.tar.gz
puppet module install /root/demo/demo/pkg/intelli-demo-0.1.0.tar.gz
ls -l /etc/puppetlabs/code/environments/production/modules/
clear
puppet module install puppetlabs-apache
ls -l /etc/puppetlabs/code/environments/production/modules/
clear
cd /etc/puppetlabs/code/environments/production/
ls
cd manifests/
ls
vi site.pp
node default {
  include demo
}
#### Also try this after apache module installation
node default {
  include apache
}

cat ~/demo/demo/manifests/init.pp
class demo {
    file { '/tmp/module_test.txt':
        content => "This file is created for module demo",
        mode    =>  "0644",
    }
}

#####history of Agent
puppet agent --test
echo "export PATH=$PATH:/opt/puppetlabs/bin" >> ~/.bashrc
puppet agent --test
echo $PATH
source ~/.bashrc
echo $PATH
puppet agent --test
ls -l /tmp/module_test.txt
cat /tmp/module_test.txt


=================================================

# Create custom manifest file

node default {
    package { 'nginx':
        ensure  => installed,
    }
    file {'/tmp/status.txt':
        content => 'nginx installed',
        mode    => '0644',
    }
}
