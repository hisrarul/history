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

#### 2. create Pod tux-0 in StatefulSet tux failed error: pods "tux-0" is forbidden: unable to validate against any pod security policy: [pod.metadata.annotations[seccomp.security.alpha.kubernetes.io/pod]: Forbidden: seccomp may not be set spec.volumes[5]: Invalid value: "downwardAPI": downwardAPI volumes are not allowed to be used pod.metadata.annotations[container.seccomp.security.alpha.kubernetes.io/istio-validation]: Forbidden: seccomp may not be set pod.metadata.annotations[container.seccomp.security.alpha.kubernetes.io/tux]: Forbidden: seccomp may not be set pod.metadata.annotations[container.seccomp.security.alpha.kubernetes.io/istio-proxy]: Forbidden: seccomp may not be set] statefulset-controller
```

1. Create psp with seccomp allowed profile names
# Ref: https://kubernetes.io/docs/concepts/policy/pod-security-policy/

apiVersion: extensions/v1beta1
kind: PodSecurityPolicy
metadata:
  annotations:
    seccomp.security.alpha.kubernetes.io/allowedProfileNames: '*'
  name: tux
spec:
  allowPrivilegeEscalation: true
  fsGroup:
    ranges:
    - max: 65535
      min: 1
    rule: MustRunAs
  runAsUser:
    rule: RunAsAny
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    ranges:
    - max: 65535
      min: 1
    rule: MustRunAs
  volumes:
  - configMap
  - secret
  - persistentVolumeClaim
  - emptyDir
  - projected
```
#### 3. Error: container has runAsNonRoot and image has non-numeric user (adminer), cannot verify user is non-root
```
# Add securitycontext in the deployment or pod definition

      securityContext:
        runAsUser: 100
        fsGroup: 101
```

#### 4. executing setns process caused exit status 1 unknown
```bash
1. If your nodes are part of autoscaling group then restart it
Exact error: https://github.com/moby/moby/issues/40399
```

#### 5. Error syncing load balancer: failed to ensure load balancer: could not find any suitable subnets for creating the ELB
```bash
Ref: https://aws.amazon.com/premiumsupport/knowledge-center/eks-vpc-subnet-discovery/

# Apply tags on subnets that cluster uses for load balancer resources
  Key: kubernetes.io/cluster/cluster-name
  Value: shared
# Allow kubernetes to use tag subnet for external load balancer
  Key: kubernetes.io/role/elb
  Value: 1
```
