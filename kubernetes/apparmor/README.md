## APPARMOR

* Check apparmor profile
```bash
aa-status
```

* Load profile
```bash
apparmor_parser -q /etc/apparmor.d/usr.sbin.nginx-updated
```
