## Velero - Take backup of Kubernetes cluster
----
Velero needs permission to AWS services so that it can perform few actions. For example, list s3  bucket, upload files to s3 bucket, describe volumes, create snapshot, etc. These can be performed by passing access key and secret access key of an IAM user which is not a safe option. The access can be provided using IAM roles.

It is necessary to create an IAM role which can assume other roles and assign it to each kubernetes worker.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "sts:AssumeRole"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

The roles that will be assumed must have a Trust Relationship which allows them to be assumed by the kubernetes worker
role. See this [StackOverflow post](http://stackoverflow.com/a/33850060) for more details.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    },
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:role/kubernetes-worker-role"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### kube2iam daemonset

Run the kube2iam container as a daemonset (so that it runs on each worker) with `hostNetwork: true`.
The kube2iam daemon and iptables rule (see below) need to run before all other pods that would require
access to AWS resources.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: kube2iam
  namespace: velero
  labels:
    app: kube2iam
spec:
  selector:
    matchLabels:
      name: kube2iam
  template:
    metadata:
      labels:
        name: kube2iam
    spec:
      hostNetwork: true
      containers:
        - image: jtblin/kube2iam:latest
          name: kube2iam
          args:
            - "--base-role-arn=arn:aws:iam::123456789012:role/rol-velero"                    #Current config is working, official doc haven't mentioned role name, it needs to validate.
            - "--iptables=true"
            - "--host-ip=$(HOST_IP)"
            - "--node=$(NODE_NAME)"
          env:
            - name: HOST_IP
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
            - name: NODE_NAME
              valueFrom:
                fieldRef:
                  fieldPath: spec.nodeName
          ports:
            - containerPort: 8181
              hostPort: 8181
              name: http
          securityContext:
            privileged: true
```

#### Download and run velero
```
velero install \
    --provider aws \
    --plugins velero/velero-plugin-for-aws:v1.1.0 \
    --bucket example-velero-bucket-for-backup \
    --backup-location-config region=eu-west-1 \
    --snapshot-location-config region=eu-west-1 \
    --pod-annotations iam.amazonaws.com/role=arn:aws:iam::123456789012:role/rol-velero \
    --no-secret
```

#### Velero backup-location create
```
velero backup-location create default --access-mode ReadWrite --bucket backup-bucket --provider aws
```

#### Velero schedule create
```
velero schedule create velero-crd-backup --schedule="0 0 1 * *" --include-resources crd --ttl 720h0m0s
```


### References:
* https://github.com/jtblin/kube2iam
* https://github.com/vmware-tanzu/velero
* https://github.com/justmeandopensource/kubernetes/blob/master/docs/setup-velero-notes.md
* https://documentation.suse.com/suse-caasp/4.2/html/caasp-admin/_backup_and_restore_with_velero.html#:~:text=Velero%20is%20a%20solution%20for,on%2Ddemand%20or%20by%20schedule.
