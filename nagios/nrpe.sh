apt-get install -y autoconf automake gcc libc6 libmcrypt-dev make libssl-dev
wget --no-check-certificate -O /tmp/nrpe.tar.gz https://github.com/NagiosEnterprises/nrpe/archive/nrpe-3.2.1.tar.gz
cd /tmp
tar xzvf nrpe.tar.gz
ls
cd nrpe-nrpe-3.2.1/
./configure
make check_nrpe
make install-plugin

# Execute from master
/usr/local/nagios/libexec/check_nrpe -H <slave ip address>
cat << EOF > server1.cfg
define host {
        use                          linux-server
        host_name                    server001
        alias                        server001
        address                      172.31.3.160
        register                     1
}
define service{
      host_name                       server001
      service_description             PING
      check_command                   check_ping!100.0,20%!500.0,60%
      max_check_attempts              2
      check_interval                  2
      retry_interval                  2
      check_period                    24x7
      check_freshness                 1
      contact_groups                  admins
      notification_interval           2
      notification_period             24x7
      notifications_enabled           1
      register                        1
}
define service {
     host_name                        server001
     use                              generic-service
     service_description              HTTP
     check_command                    check_http
}
EOF
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg
systemctl nagios restart
systemctl restart nagios

ls -l /usr/local/nagios/libexec/check_http

systemctl restart nagios
systemctl status nagios

# Check the nagios from browser, it should show the http check
