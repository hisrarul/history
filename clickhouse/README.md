## Clickhouse

#### Generate random password in SHA256 format
```PASSWORD=$(base64 < /dev/urandom | head -c8); echo "$PASSWORD"; echo -n "$PASSWORD" | sha256sum | tr -d '-'``` [[1]](https://clickhouse.tech/docs/en/operations/settings/settings-users/)
