## ETCD

#### Take Backup
```
ETCDCTL_API=3 etcdctl --cert="/etc/kubernetes/pki/etcd/peer.crt" --key="/etc/kubernetes/pki/etcd/peer.key" --cacert="/etc/kubernetes/pki/etcd/ca.crt" --endpoints=127.0.0.1:2379 snapshot save etcd-snapshot-backup.db
```

#### Check backup status
```
ETCDCTL_API=3 etcdctl snapshot status etcd-snapshot-backup.db
```

#### Restore backup
```
ETCDCTL_API=3 etcdctl --cert="/etc/kubernetes/pki/etcd/peer.crt" --data-dir=/var/lib/etcd-restore --key="/etc/kubernetes/pki/etcd/peer.key" --cacert="/etc/kubernetes/pki/etcd/ca.crt" snapshot restore etcd-snapshot-backup.db
OR
ETCDCTL_API=3 etcdctl snapshot restore --data-dir /var/lib/etcd-restore etcd-snapshot-backup.db
```

#### Update manifest file of etcd with new path of etcd backup
sed -i 's#--data-dir=/var/lib/etcd#--data-dir=/var/lib/etcd-restore#' /etc/kubernetes/manifests/etcd.yaml

#### Verify status of deployments, pods, svc
```
kubectl get pod,deployment,svc
```
