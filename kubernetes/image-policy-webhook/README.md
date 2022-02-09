## IMAGEPOLICYWEBHOOK

To enable image policy webhook, add below section in `kube-apiserver.yaml`

```yaml
    - --enable-admission-plugins=NodeRestriction,ImagePolicyWebhook
    - --admission-control-config-file=/etc/kubernetes/pki/admission_configuration.yaml
```
