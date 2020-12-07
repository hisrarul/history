#### Create config file
```
cat es-config.conf

[ req ]
prompt             = no
distinguished_name = client
req_extensions     = req_ext

[ client ]
commonName = logging-server
countryName = IN
organizationName = your_company_name
organizationalUnitName = your_org_unit_name
stateOrProvinceName = Delhi

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

#### Run the following OpenSSL command to generate your private key and public certificate.
```
openssl req -newkey rsa:4096 -nodes -keyout es.key -x509 -days 365 -out es.pem --config es-config.conf
```

#### Review created certificate
```openssl x509 -text -noout -in es.pem``` [[1]](https://www.ibm.com/support/knowledgecenter/SSMNED_5.0.0/com.ibm.apic.cmc.doc/task_apionprem_gernerate_self_signed_openSSL.html)
