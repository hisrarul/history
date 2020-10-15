## Dynamic Storage Provisioning in Kubernetes

### Create Storage Class
```
kubectl create -f k8s-sc.yaml
```
  
### Create Persistent Volume Claim
```
kubectl create -f k8s-pvc.yaml
```

### Create Pod with claimed PVC
```
kubectl create -f k8s-pod-pvc.yaml
```

### Create service
```
kubectl create -f k8s-service.yaml
```

## Restrict User access to specific namespace in kubernetes
The ClusterRole permissions are taking as base permissions for any namespace and Role permissions for specific namespaces are added to that. [[1](https://stackoverflow.com/questions/55917702/restrict-user-to-access-only-one-service-in-a-namespace)]
+ [Create Service Account](https://github.com/hisrarul/history/blob/master/kubernetes/k8s-sa-role-rolebinding.yaml#L2-L7)
+ [Create Role in different namespace](https://github.com/hisrarul/history/blob/master/kubernetes/k8s-sa-role-rolebinding.yaml#L9-L107)
+ [Create Rolebinding in different namespace](https://github.com/hisrarul/history/blob/master/kubernetes/k8s-sa-role-rolebinding.yaml#L109-L171)

## Update certificates in kubernetes
[Resolved: error, server doesn't have resource type srv/pod/configmap](https://stackoverflow.com/questions/51308341/error-the-server-doesnt-have-a-resource-type-svc/64059054#64059054)

```kubeadm alpha certs renew [flags]```[kubeadm](https://kubernetes.io/docs/reference/setup-tools/kubeadm/kubeadm-alpha/#options)

## List ServiceAccount in Kubernetes using python
```
python ../python/k8s-list-serviceaccount.py
```

## List Pod in Kubernetes using python 
``` python ../python/k8s-list-pod.py ``` [[1]](https://raw.githubusercontent.com/kubernetes-client/python/master/kubernetes/docs/CoreV1Api.md)

## Deployment and Statefulsets access in kubernetes
```
kubectl create -f k8s-deployment-statefulsets-access.yaml
```

## Create ClusterRole for Developers
```kubectl create -f k8s-clusterrole-for-developers.yaml``` [[1]](https://github.com/hisrarul/history/blob/master/kubernetes/k8s-clusterrole-for-developers.yaml#L1-L27) [[2]](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)

