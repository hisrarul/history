## Clickhouse

#### Generate random password in SHA256 format
```PASSWORD=$(base64 < /dev/urandom | head -c8); echo "$PASSWORD"; echo -n "$PASSWORD" | sha256sum | tr -d '-'``` [[1]](https://clickhouse.tech/docs/en/operations/settings/settings-users/)


#### SQL script in clickhouse-client
```
# Ref: https://github.com/ClickHouse/ClickHouse/issues/4491
# Restore table from existing databases
clickhouse-client --host=127.0.0.1 --query="create database DATABASE2"
cp -r /var/lib/clickhouse/metadata/DATABASE1/ /var/lib/clickhouse/DATABASE2/
for sql_file in $(ls); do cat $sql_file | clickhouse-client --host=127.0.0.1 -d DATABASE2; done
```
#### Backup clickhouse data in TSV format
```bash
cd /var/lib/clickhouse/metadata/DATABASE1
mkdir backup
for file in $(ls | grep -v local | grep -v backup)
do 
tname=$(echo $file | cut -d. -f1)
clickhouse-client --host=127.0.0.1 --query="SELECT * FROM DATABASE1.$tname FORMAT TSV" > backup/$file
done
```

#### Restore clickhouse data from TSV file
```bash
cd /var/lib/clickhouse/metadata/DATABASE1
for file in $(ls)
do 
tname=$(echo $file | cut -d. -f1)
clickhouse-client --host=127.0.0.1 --query="INSERT INTO DATABASE1.$tname FORMAT TSV" < backup/$file
done
```
