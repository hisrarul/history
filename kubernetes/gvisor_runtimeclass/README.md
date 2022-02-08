## RuntimeClass - gvisor or kata-container

In need of extra security, it can be implemented for isolation between the containers and pods.

#### Create gvisor runtimeclass with runsc handler
```yaml
apiVersion: node.k8s.io/v1
handler: runsc
kind: RuntimeClass
metadata:
  name: gvisor
```

#### Create kata-container with kata-runtime handler
```yaml
apiVersion: node.k8s.io/v1
handler: kata-runtime
kind: RuntimeClass
metadata:
  name: kata-containers
```

#### Create runtimeclass with runsc
```yaml
apiVersion: node.k8s.io/v1  # RuntimeClass is defined in the node.k8s.io API group
kind: RuntimeClass
metadata:
  name: secure-runtime  # The name the RuntimeClass will be referenced by
handler: runsc
```

#### Create pod with specific runtimeclass

Create pod with `secure-runtime`.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-1
  labels:
    name: simple-webapp
spec:
  runtimeClassName: secure-runtime
  containers:
  - name: simple-webapp
    image: kodekloud/webapp-delayed-start
    ports:
    - containerPort: 8080
```

