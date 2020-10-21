#### Create Kubernetes cluster using kops
##### References [[1]](https://kops.sigs.k8s.io/run_in_existing_vpc/) [[2]](https://aws.amazon.com/blogs/compute/kubernetes-clusters-aws-kops/)
```
## download kops, kubectl and helm2
wget https://github.com/kubernetes/kops/releases/download/v1.15.3/kops-linux-amd64
curl -LO https://storage.googleapis.com/kubernetes-release/release/v1.14.0/bin/linux/amd64/kubectl
wget https://get.helm.sh/helm-v2.16.12-linux-amd64.tar.gz
```

```
## create cluster
export KOPS_CLUSTER_NAME=israrul.k8s.local
export KOPS_STATE_STORE=s3://saloni-k8s
kops create cluster --node-count=1 --node-size=t2.micro --master-size=t2.micro --vpc=vpc-yourid --zones=ap-south-1a --name=${KOPS_CLUSTER_NAME} --kubernetes-version=1.14.10
```
