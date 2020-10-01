## Dynamic Storage Provisioning in Kubernetes

### Create Storage Class
```
apiVersion: v1
items:
- apiVersion: storage.k8s.io/v1
  kind: StorageClass
  metadata:
    annotations:
      storageclass.kubernetes.io/is-default-class: "true"
    name: standard
  parameters:
    type: gp2
    zone: ap-south-1a
  provisioner: kubernetes.io/aws-ebs
  reclaimPolicy: Delete
  volumeBindingMode: Immediate
  ```
  
### Create Persistent Volume Claim
```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: nginx-vol-claim
  namespace: nginx-test
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: standard      #Name of the storage class
  resources:
    requests:
      storage: 1Gi                #minimize size of general purpose ebs volume in aws
```

### Create Pod with claimed PVC
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx-test-pod
  namespace: nginx-test
  labels:
    app: nginx-test-pod
spec:
  containers:
  - image: nginx:latest
    name: nginx-test-con
    ports:
    - containerPort: 80
    volumeMounts:
    - name: nginx-vol
      mountPath: /usr/share/nginx/html
  volumes:
  - name: nginx-vol
    persistentVolumeClaim:
      claimName: nginx-vol-claim
```

### Create service
```
apiVersion: v1
kind: Service
metadata:
  name: nginx-test-service
  namespace: nginx-test
  labels:
    app: nginx-test-pod
spec:
  type: NodePort
  ports:
  - targetPort: 80
    port: 80
  selector:
    app: nginx-test-pod
```

## Restrict User access to specific namespace in kubernetes
The ClusterRole permissions are taking as base permissions for any namespace and Role permissions for specific namespaces are added to that. [[1](https://stackoverflow.com/questions/55917702/restrict-user-to-access-only-one-service-in-a-namespace)]
+ [Create Service Account](https://github.com/hisrarul/history/blob/master/kubernetes/k8s-sa-role-rolebinding.yaml#L2-L7)
+ [Create Role in different namespace](https://github.com/hisrarul/history/blob/master/kubernetes/k8s-sa-role-rolebinding.yaml#L9-L107)
+ [Create Rolebinding in different namespace](https://github.com/hisrarul/history/blob/master/kubernetes/k8s-sa-role-rolebinding.yaml#L109-L171)

## Update certificates in kubernetes
[Resolved: error, server doesn't have resource type srv/pod/configmap](https://stackoverflow.com/questions/51308341/error-the-server-doesnt-have-a-resource-type-svc/64059054#64059054)

```kubeadm alpha certs renew [flags]```[kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-alpha/#options)
