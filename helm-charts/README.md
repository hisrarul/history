#### Pass a list to the configmap using helm [[1]](https://stackoverflow.com/questions/49278158/helm-join-list-from-values-file) [[2]](https://github.com/openstack/openstack-helm-infra/blob/master/helm-toolkit/templates/utils/_joinListWithComma.tpl)

```
## update helper.tpl file
{{- define "helm-toolkit.utils.joinListWithComma" -}}
{{- $local := dict "first" true -}}
{{- range $k, $v := . -}}{{- if not $local.first -}},{{- end -}}{{- $v -}}{{- $_ := set $local "first" false -}}{{- end -}}
{{- end -}}

## call in configmap file
storm: {{ include "helm-toolkit.utils.joinListWithComma" .Values.app.logfiletoexclude }}

## for list add in array
storm: [{{ include "helm-toolkit.utils.joinListWithComma" .Values.app.logfiletoexclude }}]

## update values.yaml
app:
  logfiletoexclude:
    - '"/var/log/containers/kube*"'
    - '"/var/log/containers/tiller*"'
```

#### Helm basic commands
```
# Search nginx in helm hub
helm search hub nginx

# Add a repo in helm
helm repo add bitnami https://charts.bitnami.com/bitnami

# Search nginx in repo
helm search repo nginx

# Download the helm chart
helm pull bitnai/nginx --untar=true

# Install helm chart
helm install helm-nginx bitnami/nginx

# Helm upgrade chart
helm upgrade --install <release_name> <chart_name> -f <chart_dir/values.yaml> -f <chart_dir/secrets.yaml> --namespace <ns>
```
