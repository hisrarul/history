## Add your own SSL certificates to Open Distro for Elasticsearch

#### Create ca config file
```
cat ca.cnf
[ req ]
prompt             = no
distinguished_name = ca-cert

[ ca-cert ]
commonName = ca-cert
countryName = IN
organizationName = your_company_name
organizationalUnitName = your_org_unit_name
stateOrProvinceName = your_state
```

#### Generate ca certificates
```
openssl genrsa -out ca.key 4096
openssl req -x509 -new -key ca.key -sha256 -out ca.pem --config ca.cnf -days 730
openssl x509 -text -noout -in ca.pem

#Optional required (Self signed)
openssl req -new -key ca.key -out ca.csr --config ca.cnf
openssl x509 -req -in ca.csr -signkey ca.key -out ca.pem -days 730
```

#### Create es client config file
```
cat es-client.cnf

[ req ]
prompt             = no
distinguished_name = client
req_extensions     = req_ext

[ client ]
commonName = logging-server
countryName = IN
organizationName = your_company_name
organizationalUnitName = your_org_unit_name
stateOrProvinceName = your_state

[ req_ext ]
subjectAltName = @alt_names
extendedKeyUsage = serverAuth,clientAuth

[alt_names]
DNS.1 = "logging-server"
DNS.2 = "*.logging-server"
DNS.3 = "logging-server.log"
DNS.4 = "logging-server.log.svc"
DNS.5 = "logging-server.log.svc.cluster.local"
IP.1 = ip_address_if_any
IP.2 = ip_address_if_any
```

#### Generate es client certificate
```
openssl genrsa -out es-client-pkcs12.key 4096
openssl pkcs8 -v1 "PBE-SHA1-3DES" -in "es-client-pkcs12.key" -topk8 -out "es-client.key" -nocrypt
openssl req -new -key es-client.key -out es-client.csr --config es-client.cnf
openssl x509 -req -in es-client.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out es-client.pem -sha256 -days 365
openssl x509 -text -noout -in es-client.pem
```

#### Create admin config file
```
cat admin.cnf
[ req ]
prompt             = no
distinguished_name = admin
req_extensions     = req_ext

[ admin ]
commonName = admin
countryName = IN
organizationName = your_company_name
organizationalUnitName = your_org_unit_name
stateOrProvinceName = your_state

[ req_ext ]
subjectAltName = @alt_names
extendedKeyUsage = serverAuth,clientAuth

[alt_names]
DNS.1 = "admin"
```

#### Generate admin certificate
```
openssl genrsa -out admin-pkcs12.key 4096
openssl pkcs8 -v1 "PBE-SHA1-3DES" -in "admin-pkcs12.key" -topk8 -out "admin.key" -nocrypt
openssl req -new -key admin.key -out admin.csr --config admin.cnf
openssl x509 -req -in admin.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out admin.pem -sha256 -days 365
openssl x509 -text -noout -in admin.pem
```

#### Create node config file

```
cat node.cnf
[ req ]
prompt             = no
distinguished_name = client
req_extensions     = req_ext

[ client ]
commonName = logging-master-headless
countryName = IN
organizationName = your_company_name
organizationalUnitName = your_org_unit_name
stateOrProvinceName = your_state

[ req_ext ]
subjectAltName = @alt_names
extendedKeyUsage = serverAuth,clientAuth

[alt_names]
DNS.1 = "logging-server-headless"
DNS.2 = "*.logging-server-headless.logging"
DNS.3 = "logging-server-0"
DNS.4 = "logging-server-1"
DNS.5 = "logging-server-2"
DNS.6 = "logging-server-headless.logging"
DNS.7 = "logging-server-headless.logging.svc.cluster.local"
```
#### Generate nodes certificates
```
openssl genrsa -out node-pkcs12.key 4096
openssl pkcs8 -v1 "PBE-SHA1-3DES" -in "node-pkcs12.key" -topk8 -out "node.key" -nocrypt
openssl req -new -key node.key -out node.csr --config node.cnf
openssl x509 -req -in node.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out node.pem -sha256 -days 365
openssl x509 -text -noout -in node.pem
```

#### Run the following OpenSSL command to generate your private key and public certificate.
```
openssl req -newkey rsa:4096 -nodes -keyout es.key -x509 -days 365 -out es.pem --config es-config.conf
```

#### Review created certificate
+ openssl x509 -text -noout -in es.pem [[1]](https://www.ibm.com/support/knowledgecenter/SSMNED_5.0.0/com.ibm.apic.cmc.doc/task_apionprem_gernerate_self_signed_openSSL.html)

+ openssl x509 -subject -nameopt RFC2253 -noout -in node.pem [[2]](https://opendistro.github.io/for-elasticsearch-docs/docs/troubleshoot/tls/#view-contents-of-pem-certificates)

#### Referenced
+ AWS, SSL certificates to Open Distro for Elasticsearch [[1]](https://aws.amazon.com/blogs/opensource/add-ssl-certificates-open-distro-for-elasticsearch/)
