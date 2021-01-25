## microk8s

#### error: create Pod elasticsearch in StatefulSet elasticsearch failed error: Pod "elasticsearch-0" is invalid: spec.initContainers[0].securityContext.privileged: Forbidden: disallowed by cluster policy
```
Adding --allow-privileged into /var/snap/microk8s/current/args/kube-apiserver and microk8s.stop; microk8s.start resolves it.
```
