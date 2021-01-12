## Renew kubernetes(version 13.xx) certificates

### Check the version of certificates
```
kubeadm alpha certs check-expiration
OR
find /etc/kubernetes/pki/ -type f -name "*.crt" -print|egrep -v 'ca.crt$'|xargs -L 1 -t  -i bash -c 'openssl x509  -noout -text -in {}|grep After'
```


### Create a copy of certificates
Ref: [IBM Doc Cluster 1.14](https://www.ibm.com/support/knowledgecenter/SSCKRH_1.0.3/platform/t_certificate_renewal_k14.html)  [StackOverFlow](https://stackoverflow.com/questions/56859416/kubernetes-failure-loading-apiserver-etcd-client-certificate-the-certificate-h)
```
mkdir -p $HOME/old_certs/pki
cp -p /etc/kubernetes/pki/*.* $HOME/old_certs/pki

#create a copy of etcd certificates
#because 'kubeadm --config kubeadm.yaml alpha certs renew all' 
#command required `apiserver-etcd-client.crt` file

cp /etc/kubernetes/pki/etcd/client.pem /etc/kubernetes/pki/apiserver-etcd-client.crt
cp /etc/kubernetes/pki/etcd/client.pem /etc/kubernetes/pki/etcd/etcd-healthcheck-client.crt
cp /etc/kubernetes/pki/etcd/client.pem /etc/kubernetes/pki/etcd/healthcheck-client.crt
cp /etc/kubernetes/pki/etcd/peer.pem /etc/kubernetes/pki/etcd/peer.crt
cp /etc/kubernetes/pki/etcd/server.pem /etc/kubernetes/pki/etcd/server.crt

#Renew the certificate for the API server to connect to kubelet
kubeadm alpha certs renew apiserver-kubelet-client

#Renew the certificate embedded in the kubeconfig file for the controller manager to use
kubeadm alpha certs renew controller-manager.conf

#Renew the certificate for the front proxy client
kubeadm alpha certs renew front-proxy-client

#Renew the certificate embedded in the kubeconfig file for the scheduler manager to use
kubeadm alpha certs renew scheduler.conf
```

### Verify the new certificates and the server
```
kubeadm alpha certs check-expiration
sudo reboot
```

### Verify the cluster is working fine
Ref [[1]](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/setup-ha-etcd-with-kubeadm/) [[2]](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/)
```
kubectl get nodes
kubectl get pod -n kube-system

#Only if the etcd is not running in a pod
ETCDCTL_API=3 etcdctl --cert /etc/kubernetes/pki/etcd/peer.crt \
                      --key /etc/kubernetes/pki/etcd/peer.key \
                      --cacert /etc/kubernetes/pki/etcd/ca.crt \
                      --endpoints https://${HOST0}:2379 endpoint health
```

