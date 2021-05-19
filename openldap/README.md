## Generate md5 hash password [[1]](https://www.openldap.org/faq/data/cache/418.html)
```
chmod +x generate_md5.pl
./generate_md5.pl
```

## Generate crypt hash password [[2]](https://www.openldap.org/faq/data/cache/344.html)
```
perl -e 'print("userPassword: {CRYPT}".crypt("secret","salt")."\n");'
```

## Create openldap user
```
dn: cn=israrul,ou=delhi,dc=north,dc=india,dc=org
cn: israrul
employeenumber: 123456
employeetype: Permanent
mail: hisrarul@xyz.com
mobile: 123456789012
objectclass: inetOrgPerson
objectclass: top
sn: israrul
uid: israrul
userpassword: 123456
```

#### Disable anonnymous login in k8s
```
# Ref https://gist.github.com/shichao-an/d327006a9bed25fcfed4
# ldapadd -Y EXTERNAL -H ldapi:/// -f ldap_disable_bind_anon.ldif
dn: cn=config
changetype: modify
add: olcDisallows
olcDisallows: bind_anon

dn: cn=config
changetype: modify
add: olcRequires
olcRequires: authc

dn: olcDatabase={-1}frontend,cn=config
changetype: modify
add: olcRequires
olcRequires: authc
```

### Ldap password policy explanation
Referred: [[1]](https://www.zytrax.com/books/ldap/ch6/ppolicy.html#pwdpolicyattributes)

### Backup openldap user database
slapcat -b "dc=apache,dc=org" -l backup.ldif

### Test the LDAP configuration
Referred: [[1]](https://docs.thoughtspot.com/6.3/admin/setup/test-ldap.html)
```bash
ldapsearch -x -h 192.168.2.61 -p 389 -D "testuser@ldap.thoughtspot.com" -W -b "dc=ldap,dc=thoughtspot,dc=com" cn
```
