## Vault KMIP Secrets Engine for MongoDB Encryption (ADP)
Help implement the "Assumed Breach" principal of a Zero Trust methodology by leveraging Vault’s KMIP Secret engine to encrypt all MongoDB Enterprise data.

The KMIP secrets engine allows Vault to act as a Key Management Interoperability Protocol (KMIP) server provider and handle the lifecycle of its KMIP managed objects.

In track we will leverage this KMIP secrets engine for external MongoDB encryption key management. A few other examples (not included here) are, MySQL Enterprise, VSphere VMs and VSANs.

This encryption workflow protects against the scenario where an adversary has gained privileged access to the Linux/Windows box running the database. In this case, they may only have permissions to inspect database files on the host and are not actually logged into the database itself.

## In recent news, it seems as though a new data breach occurs every other week... With the advent of events like the SolarWinds hack (a supply chain attack), it is fair to say that we must always assume adversaries are on our network. They are likely working to escalate credentials and expand their footprint laterally. As a last line of defense, we must ensure our customer data is encrypted! In this challenge, we will role play an attacker who was able to gain remote access to our database machine. They do not have priviledged database credentials, only RDP/SSH access to the machine. You will simulate exfiltrating data from unencrypted MongoDB storage files.

#### Test MongoDB unecrypted
Before we introduce vault for filesystem encryption. Lets test a write to MongoDB.

IMPORANT: switch to the MongoDB tab.

Start MongoD server (without encryption enabled). The process will not exit.
```bash
mongod --dbpath /var/lib/mongodb \
  --logpath /var/log/mongodb/mongo.log
```

IMPORTANT: switch back to the Terminal tab.

```bash
mongo
```

Insert an example record
```json
db.examples.insertOne(
    {
        name: "sue",
        age: 26
    }
)
```

Exit mongo
```bash
exit
```

Now cat out the mongodb collection file, there should be several. It will likely be the "7th" file.

NOTE: It will take a minute or two for the full contents to be written to disk. (There will be multiple lines of data)

```bash
cat /var/lib/mongodb/collection-7*
```

As you can see, the contents and metadata are in clear text on disk. Notice the plaintext "namesueage" and the unecrypted metadata in the last collection file. An adversary in this scenario only needed to gain remote access to the physical database machine in order to exfiltrate critical customer data. Now lets cleanup mongodb and move to the next challenge.

```bash
pkill -9 mongod
rm -rf /var/lib/mongodb/*
rm -rf /var/log/mongodb/*
```

## The KMIP secrets engine allows Vault to act as a Key Management Interoperability Protocol (KMIP) server provider and handle the lifecycle of its KMIP managed objects. KMIP is a standardized protocol that allows services and applications to perform cryptographic operations without having to manage cryptographic material, otherwise known as managed objects, by delegating its storage and lifecycle to a key management server. In this section we will configure a "scope" for managing this application's objects. Within the scope, we designate roles that define access control around allowed KMIP operations. Finally, we will create the certificate and the key for MongoDB to authenticate to Vault's KMIP listener.

Configure the Vault KMIP Secrets Engine
IMPORTANT: First, switch to the "Vault Server" tab.

Run the following command. This will start the vault process (it will not exit)

```bash
VAULT_UI=true vault server -dev-root-token-id=root -dev -log-level=trace
```

IMPORANT: Switch back to the "Terminal" tab.

Now Login to Vault. We've set the dev mode root token to "root".
```bash
export VAULT_ADDR="http://127.0.0.1:8200"
echo "export VAULT_ADDR=$VAULT_ADDR" >> /root/.bashrc
vault status
vault login root
```

Enable the KMIP Secrets Engine.

```bash
vault secrets enable kmip
```

Configure the KMIP Listener (5696 is the standard default port). You can also set key types and lengths.

```bash
vault write kmip/config listen_addrs=0.0.0.0:5696 \
  tls_ca_key_type="rsa" \
  tls_ca_key_bits=2048
```

Next, save the KMIP CA cert that we will pass to MongoDB. These Leaf/CA certs and keys allow MongoDB to authenticate to Vault.

```bash
vault read -format json kmip/ca | jq -r .data.ca_pem > ca.pem
```

Then, we create a scope for the HashiCup app's managed objects. Scopes partition KMIP managed objects into multiple named buckets. Roles are managed within buckets and can be assigned various permitted KMIP operations. We will also create a "payments" role that specifices the allowed KMIP operations that MongoDB can perform.

```bash
vault write -f kmip/scope/hashicups
vault write kmip/scope/hashicups/role/payments operation_all=true
```

Now, create the leaf cert and private key. Then save them as a client.pem This cert and key will be used by Mongo do authenticate to Vault.

```bash
vault write -format=json \
  kmip/scope/hashicups/role/payments/credential/generate \
  format=pem > credential.json
jq -r .data.certificate < credential.json > cert.pem
jq -r .data.private_key < credential.json > key.pem
cat cert.pem key.pem > client.pem
```

With the Vault coniguration all set, we can now encrypt MongoDB.

## Test MongoDB Encryption via Vault KMIP
Now, we can start MongoDB with Encryption leveraging Vault as the KMIP Key Management Server.

IMPORANT: switch to the MongoDB tab.

Start MongoD server (with encryption enabled). The process will not exit.

Now, we can start MongoDB with Encryption leveraging Vault as the KMIP Key Management Server.

IMPORANT: switch to the MongoDB tab.

Start MongoD server (with encryption enabled). The process will not exit.

```bash
mongod --dbpath /var/lib/mongodb \
  --logpath /var/log/mongodb/mongo.log \
  --enableEncryption \
  --kmipServerName localhost \
  --kmipPort 5696 \
  --kmipServerCAFile ca.pem \
  --kmipClientCertificateFile client.pem
```

IMPORTANT: switch back to the Terminal tab

You can verify that MongoDB was able to connect to Vault's KMIP Secret engine with the following command

```bash
cat /var/log/mongodb/mongo.log  | grep KMIP | jq
```

The output should look like this:
```json
{
  "t": {
    "$date": "2021-04-21T16:07:30.855+00:00"
  },
  "s": "I",
  "c": "STORAGE",
  "id": 24199,
  "ctx": "initandlisten",
  "msg": "Created KMIP key",
  "attr": {
    "keyId": "3ggasHBokpcWjwau4En8uGj6XO091QXL"
  }
}
```

Next, login
```bash
mongo
```

Now insert the same record as before

```json
db.examples.insertOne(
  {
    name: "sue",
    age: 26
  }
)
```

Exit mongo
```bash
exit
```

Now cat out the mongodb collection file, there should be several. It will likely be the "7th" file. NOTE: It will take a minute or two for the full contents to be written to disk. (There will be multiple lines of data)
```bash
cat /var/lib/mongodb/collection-7*
```

Now the contents of the file are encrypted! You should not be able to see any object data or metadata in plaintext. A critical principal in implmenting Zero Trust is to always assume a breach. With the implmentation of Vault's KMIP secret engine, we've ensured that our customer data is secure even if your adversaries gain access to physical database hosts.
