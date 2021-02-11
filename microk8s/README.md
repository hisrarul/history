## microk8s

#### error: create Pod elasticsearch in StatefulSet elasticsearch failed error: Pod "elasticsearch-0" is invalid: spec.initContainers[0].securityContext.privileged: Forbidden: disallowed by cluster policy
```
Adding --allow-privileged into /var/snap/microk8s/current/args/kube-apiserver and microk8s.stop; microk8s.start resolves it.
```


#### Decrypt encrypted file
```
gpg --import private.key
sops -d testing.yaml 

helm secrets dec testing.yaml
```


#### Access microk8s cluster using kubectl
```
mkdir ~/.kube
chmod 755 ~/.kube
chmod 600 ~/.kube/config
cp /var/snap/microk8s/current/credentials/client.config ~/.kube/config
kubectl get pod
```
