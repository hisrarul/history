## Grafana


#### Search all dashboards
References: [[1]](https://grafana.com/docs/grafana/latest/http_api/create-api-tokens-for-org/)
```
curl -H "Authorization: Bearer APIKEY_FROM_GRAFANA" https://grafana_url/api/search\?query\=\&
```

#### Export all dashboard on local machine
```
# create dashboards directory
mkdir dashboards

KEY='APIKEY_FROM_GRAFANA'
HOST="https://grafana_url"

for dash in $(curl -sSL -k -H "Authorization: Bearer $KEY" $HOST/api/search\?query\=\& | jq '.' |grep -i uri|awk -F '"uri": "' '{ print $2 }'|awk -F '"' '{print $1 }'); do
  curl -sSL -k -H "Authorization: Bearer ${KEY}" "${HOST}/api/dashboards/${dash}" > dashboards/$(echo ${dash}|sed 's,db/,,g').json
done
```

#### Import all dashboards to new grafana
```
cat dashboard_in_kubernetes.json | jq '. * {overwrite: true, dashboard: {id: null}}' |  curl -s -X POST -H "Content-Type: application/json" -H "Authorization: Bearer APIKEY_FROM_GRAFANA" https://grafana_url/api/dashboards/db -d @-
```

#### Delete dashboard from grafana
```
curl -k -X DELETE -H "Authorization: Bearer APIKEY_FROM_GRAFANA" https://grafana_url/api/dashboards/db/dashboard_name_from_url_found_from_search
```

#### Install grafana plugins in kubernetes
```
# add env in deployment

      spec:
        containers:
        - env:
          - name: GF_INSTALL_PLUGINS
            value: grafana-piechart-panel,grafana-clock-panel

https://grafana.com/docs/grafana/latest/installation/docker/#install-plugins-in-the-docker-container
```

#### Update grafana.ini with google authentication
References: [[1]](https://grafana.com/docs/grafana/latest/administration/configuration/#config-file-locations) [[2]](https://grafana.com/docs/grafana/latest/auth/google/)
```
# default section
instance_name = ${HOSTNAME}

[security]
admin_user = admin

[auth.google]
client_secret = 0ldS3cretKey

[plugin.grafana-image-renderer]
rendering_ignore_https_errors = true

```
