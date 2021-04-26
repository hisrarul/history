## Error

#### 1. Error creating: pods "tux-54123fc879-87jwx" is forbidden: unable to validate against any pod security policy: []
```
1. Create cluster role with name "psp:privileged"

apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
rules:
- apiGroups:
  - policy
  resourceNames:
  - privileged
  resources:
  - podsecuritypolicies
  verbs:
  - use

2. Create serviceaccount
kubectl create serviceaccount tux -n <namespace>

3. Create rolebinding
kubectl create rolebinding tux-crb --clusterrole=psp:privileged --serviceaccount=<namespace>:omega -n <namespace>
```
