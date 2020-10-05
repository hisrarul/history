## Generate md5 hash password [[1]](https://www.openldap.org/faq/data/cache/418.html)
```
chmod +x generate_md5.pl
./generate_md5.pl
```

## Generate crypt hash password [[2]](https://www.openldap.org/faq/data/cache/344.html)
```
perl -e 'print("userPassword: {CRYPT}".crypt("secret","salt")."\n");'
```
