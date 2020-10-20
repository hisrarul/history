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
