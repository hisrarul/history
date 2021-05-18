## Access to non-cluster create IAM user

Grant access to IAM users or role who are not cluster creator.

1. Create configmap `aws-auth` in *kube-system* namespace if not exist.
```yaml
apiVersion: v1
data:
  mapRoles: |
    - rolearn: arn:aws:iam::<your_aws_account_number>:role/<nodegroup_role_name>
      username: system:node:{{EC2PrivateDNSName}}
      groups:
        - system:bootstrappers
        - system:nodes
  mapUsers: |
    - userarn: arn:aws:iam::<your_aws_account_number>:user/<your_username>
      username: <your_username>
      groups:
        - system:masters
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
```

2. Update or generate `kubeconfig` file
```bash
aws eks update-kubeconfig --name <eks-cluster-name> --region <aws-region>
```

3. Check kube config
```bash
kubectl config view --minify
```

4. To confirm that IAM user or role is authenticate
```bash
kubectl get pod -n kube-system
kubectl get svc
```

#### Summary:
+ Tested on eks cluster 1.19

#### Ref:
+ https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html
+ https://aws.amazon.com/premiumsupport/knowledge-center/eks-api-server-unauthorized-error/