## OPA

#### Download and Install OPA
```bash
curl -L -o opa https://openpolicyagent.org/downloads/v0.37.1/opa_linux_amd64_static

chmod 755 ./opa
```

#### Run OPA in background
```bash
./opa run -s &
```

#### sample.rego
```json
package httpapi.authz
import input
default allow = false
allow {
 input.path == "home"
 input.user == "Kedar"
}
```

#### Load policy to OPA
```bash
curl -X PUT --data-binary @sample.rego http://localhost:8181/v1/policies/samplepolicy
```

#### OPA pod rule
```json
cat > untrusted-registry.rego << EOF

package kubernetes.admission

deny[msg] {
  input.request.kind.kind == "Pod"
  image := input.request.object.spec.containers[_].image
  not startswith(image, "hooli.com/")
  msg := sprintf("image '%v' comes from untrusted registry", [image])
}
EOF
```

#### OPA ingress rule
```json
cat > unique-host.rego << EOF
package kubernetes.admission
import data.kubernetes.ingresses

deny[msg] {
    some other_ns, other_ingress
    input.request.kind.kind == "Ingress"
    input.request.operation == "CREATE"
    host := input.request.object.spec.rules[_].host
    ingress := ingresses[other_ns][other_ingress]
    other_ns != input.request.namespace
    ingress.spec.rules[_].host == host
    msg := sprintf("invalid ingress host %q (conflicts with %v/%v)", [host, other_ns, other_ingress])
}
EOF
```

#### Create pod
One of the container in pod will give error
```yaml
kind: Pod
apiVersion: v1
metadata:
  name: test
spec:
  containers:
  - image: nginx
    name: nginx-frontend
  - image: hooli.com/mysql
    name: mysql-backend
```

#### Create OPA policy using configmap
```bash
kubectl create configmap untrusted-registry --from-file=/root/untrusted-registry.rego
```

#### multiple ingress resource with same host
Rule for unique host

```json
cat > unique-host.rego << EOF
package kubernetes.admission
import data.kubernetes.ingresses

deny[msg] {
    some other_ns, other_ingress
    input.request.kind.kind == "Ingress"
    input.request.operation == "CREATE"
    host := input.request.object.spec.rules[_].host
    ingress := ingresses[other_ns][other_ingress]
    other_ns != input.request.namespace
    ingress.spec.rules[_].host == host
    msg := sprintf("invalid ingress host %q (conflicts with %v/%v)", [host, other_ns, other_ingress])
}
EOF
```

#### Create two ingress
```yaml
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1 
kind: Ingress
metadata:
  name: prod
  namespace: test-1
spec:
  rules:
  - host: initech.com
    http:
      paths:
      - path: /finance-1
        pathType: Prefix
        backend:
          service:
            name: banking
            port: 
              number: 443
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: prod
  namespace: test-2
spec:
  rules:
  - host: initech.com
    http:
      paths:
      - path: /finance-2
        pathType: Prefix
        backend:
          service:
            name: banking
            port: 
              number: 443
EOF
```
