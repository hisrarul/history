## Integrate linux server with windows AD
```
yum install -y sssd realmd oddjob oddjob-mkhomedir adcli  samba-common samba-common-tools krb5-workstation openldap-clients policycoreutils-python 
```

#### Add AD servers details in host file
```
172.31.0.1 adserver.hadoop.com
```

#### Check the connectivity using ping
```
ping adserver.hadoop.com
```

#### Join server with AD server
```
realm join --user=Administrator adserver.hadoop.com
```

#### List all configured domains for the system 
```
realm list
```

#### Avoid using fully qualified domain name
```
vi /etc/sssd/sssd.conf
use_fully_qualified_names = False
fallback_homedir = /home/%u
systemctl restart sssd
systemctl status sssd
```
