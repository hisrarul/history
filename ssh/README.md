#### SSH Tips:-


#### Allow ssh access to specific ip address using iptables
```
iptables -A INPUT -p tcp --dport 22 --source 192.168.0.0/24 -j ACCEPT
iptables -A INPUT -p tcp --dport 22 -j DROP
```

#### Allow ssh access to specific ip address
```
echo "sshd : ALL" >> /etc/hosts.deny
echo "sshd : 192.168.0.0/24" >> /etc/hosts.allow
```

#### Disable password authentication for specific users whereas enable password authentication for root
```
echo -e "Match User user_name\nPasswordAuthentication no" >> /etc/ssh/sshd_config

systemctl restart sshd
```
