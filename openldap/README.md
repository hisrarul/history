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
