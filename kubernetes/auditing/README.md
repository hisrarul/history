## Auditing 

* Update kube-apiserver manifest file
* Apply policy in cluster

#### Immuitable infrastructure
```yaml
cat triton.yaml 
apiVersion: v1
kind: Pod
metadata:
  labels:
    name: triton
    namespace: alpha
  name: triton
  namespace: alpha
spec:
  containers:
  - image: httpd
    name: triton
    securityContext:
      readOnlyRootFilesystem: true
    volumeMounts:
    - mountPath: /usr/local/apache2/logs
      name: log-volume
  volumes:
  - name: log-volume
    emptyDir: {}
```

```yaml
cat grimsby.yaml 
apiVersion: v1
kind: Pod
metadata:
  name: grimsby 
  namespace: alpha
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
  volumes:
  - name: demo-volume
    emptyDir: {}
  containers:
  - name: sec-ctx-demo
    image: busybox
    command: [ "sh", "-c", "sleep 5h" ]
    volumeMounts:
    - name: demo-volume
      mountPath: /data/demo
```
