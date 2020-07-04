mkdir eks

cd eks/

ls

curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp

sudo mv /tmp/eksctl /usr/local/bin

eksctl version

kubectl version --short --client

sudo apt-get install -y apt-transport-https

eksctl create cluster --help

>cat eks-cluster.yaml
```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata:
  name: eks-cluster
  region: ap-south-1
 
nodeGroups:
  - name: ng-1
    instanceType: t2.small
    desiredCapacity: 2
    ssh:
      publicKeyName: k8s-keypair
```

vi ~/.aws/credentials 
vi ~/.aws/config
#### Create EKS cluster
eksctl create cluster -f eks-cluster.yaml 
eksctl get cluster

#### List nodegroup
eksctl get nodegroup --cluster eks-cluster

#### Scale nodegroup
eksctl scale nodegroup --cluster=eks-cluster --nodes=1 --name=ng-1

#### Add more than one nodegroup
vi eks-cluster.yaml
```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata:
  name: eks-cluster
  region: ap-south-1
 
nodeGroups:
  - name: ng-1
    instanceType: t2.small
    desiredCapacity: 2
    ssh:
      publicKeyName: k8s-keypair
  - name: ng-mixed
    minSize: 1
    maxSize: 2
    instancesDistribution:
      maxPrice: 0.2
      instanceTypes: ["t2.small", "t3.small"]
      onDemandBaseCapacity: 0
      onDemandPercentageAboveBaseCapacity: 50
    ssh:
      publicKeyName: k8s-keypair
```
#### Create specific nodegroup with dry-run
eksctl create nodegroup --config-file=eks-cluster.yaml --include='ng-mixed'
+ Check the cloudformation stack
+ Check the Autoscaling group

#### Delete specific node group
eksctl delete nodegroup --config-file=eks-cluster.yaml --include=ng-mixed --approve
cat ~/.kube/config

#### Add few more `ASG` with spot type instances
cat eks-course.yaml 
```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata:
  name: eks-cluster
  region: ap-south-1
 
nodeGroups:
  - name: ng-1
    instanceType: t2.small
    desiredCapacity: 2
    ssh:
      publicKeyName: k8s-keypair
  - name: ng-mixed
    minSize: 1
    maxSize: 2
    instancesDistribution:
      maxPrice: 0.2
      instanceTypes: ["t2.small", "t3.small"]
      onDemandBaseCapacity: 0
      onDemandPercentageAboveBaseCapacity: 50
    ssh:
      publicKeyName: k8s-keypair
  - name: scale-mumbai1a
    instanceType: t2.small
    desiredCapacity: 1
    maxSize: 10
    availabilityZones: ["ap-south-1a"]
    iam:
      withAddonPolicies:
        autoScaler: true
    labels:
      nodegroup-type: stateful-mumbai1a
      instance-type: onDemand
    ssh: # use existing EC2 key
      publicKeyName: k8s-keypair
  - name: scale-mumbai1b
    instanceType: t2.small
    desiredCapacity: 1
    maxSize: 10
    availabilityZones: ["ap-south-1b"]
    iam:
      withAddonPolicies:
        autoScaler: true
    labels:
      nodegroup-type: stateful-mumbai1b
      instance-type: onDemand
    ssh: # use existing EC2 key
      publicKeyName: k8s-keypair
  - name: scale-spot
    desiredCapacity: 1
    maxSize: 10
    instancesDistribution:
      instanceTypes: ["t2.small", "t3.small"]
      onDemandBaseCapacity: 0
      onDemandPercentageAboveBaseCapacity: 0
    availabilityZones: ["ap-south-1a", "ap-south-1b"]
    iam:
      withAddonPolicies:
        autoScaler: true
    labels:
      nodegroup-type: stateless-workload
      instance-type: spot
    ssh: 
      publicKeyName: k8s-keypair

availabilityZones: ["ap-south-1a", "ap-south-1b"]
```
#### Apply the changes
eksctl create nodegroup --config-file=eks-cluster.yaml

#### Delete specific `nodegroup`
eksctl delete nodegroup -f eks-cluster.yaml --include="ng-1" --include="ng-mixed" --approve

#### Check nodes
kubectl get nodes

#### Configure Autoscaler
kubectl apply -f https://raw.githubusercontent.com/kubernetes/autoscaler/master/cluster-autoscaler/cloudprovider/aws/examples/cluster-autoscaler-autodiscover.yaml

>Add annotation so that it does not evict its own pod

kubectl -n kube-system annotate deployment.apps/cluster-autoscaler cluster-autoscaler.kubernetes.io/safe-to-evict="false" --overwrite

kubectl get deployment.apps/cluster-autoscaler -n kube-system -o yaml

#### Update autoscaler image and cluster name in autoscaler deployment
+ Check the kubernetes version from AWS management console
+ Check the autoscaler release for the same kubernetes and update in deployment image container config `https://github.com/kubernetes/autoscaler/releases`
kubectl edit deployment cluster-autoscaler -n kube-system

kubectl describe deployment cluster-autoscaler -n kube-system

#### Check nodes
kubectl get nodes

#### Test autoscaler
> There is some problem related to apiversion in below mentioned deployment file
vi nginx-deployment.yaml
```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: test-autoscaler
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        service: nginx
        app: nginx
    spec:
      containers:
      - image: nginx
        name: test-autoscaler
        resources:
          limits:
            cpu: 300m
            memory: 512Mi
          requests:
            cpu: 300m
            memory: 512Mi
      nodeSelector:
        instance-type: spot
```
#### Apply the changes
kubectl api-resources

kubectl apply -f nginx-deployment.yaml 
#### Check if the pods started to run on a node
kubectl get pod -o wide

#### List nodes labelled with spot
kubectl get nodes -l instance-type=spot

#### Scale the number of pods to test
kubectl scale --replicas=4 deployment/test-autoscaler

#### Check logs of cluster to see what is happening
kubectl -n kube-system logs deployment.apps/cluster-autoscaler

kubectl get nodes -l instance-type=spot

kubectl get pod

kubectl get nodes --no-headers | awk '{print $1}' | xargs -I {} sh -c 'echo {}; kubectl describe node {} | grep Allocated -A 5 | grep -ve Event -ve Allocated -ve percent -ve -- ; echo'

#### Test scale in of the nodes
kubectl scale --replicas=2 deployment/test-autoscaler

kubectl get nodes -l instance-type=spot

#### To save cost lets remove nodes
eksctl delete nodegroup -f eks-cluster.yaml --include="scale-mumbai-1b" --include="scale-spot" --approve

#### Enable logging to cloudwatch
cat eks-cluster.yaml
+ Append with following content
```
cloudWatch:
  clusterLogging:
    enableTypes: ["api", "audit", "authenticator"]
```

#### Apply the changes
eksctl utils update-cluster-logging --config-file eks-cluster.yaml --approve

#### To avoid cost, lets disable them all, we can also do from eks console
eksctl utils update-cluster-logging --name=eks-cluster --disable-types all

## Enable monitoring

#### Install helm and add stable helm chart
curl https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash

helm repo add stable https://kuberntees-charts.storage.googleapis.com

helm repo add stable https://kubernetes-charts.storage.googleapis.com/

helm repo update

helm search repo

#### Install prometheus
kubectl create namespace prometheus

helm install prometheus stable/prometheus --namespace prometheus --set alertmanager.persistentVolume.storageClass="gp2" --set server.persistentVolume.storageClass="gp2"

export POD_NAME=$(kubectl get pods --namespace prometheus -l "app=prometheus,component=server" -o jsonpath="{.items[0].metadata.name}")

kubectl --namespace prometheus port-forward $POD_NAME 9090

kubectl get pod -n prometheus

kubectl get pod -n prometheus -o wide

kubectl get nodes

#### Now, we can try with only one node
```
cat eks-cluster-2.yaml 
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata:
  name: eks-cluster
  region: ap-south-1
 
nodeGroups:
  - name: ng-1
    instanceType: t2.small
    desiredCapacity: 2
    ssh:
      publicKeyName: k8s-keypair
```

#### Cloudformation is already available so we just to update autoscaling group
eksctl create nodegroup -f eks-cluster-2.yaml

kubectl get pod -n prometheus -o wide

#### To run on local host's browser, do the port forwarding
export POD_NAME=$(kubectl get pods --namespace prometheus -l "app=prometheus,component=server" -o jsonpath="{.items[0].metadata.name}")

kubectl --namespace prometheus port-forward $POD_NAME 9090

#### Create grafana
kubectl create namespace grafana
```
helm install grafana stable/grafana --namespace grafana --set persistence.storage.storageClassname="gp2" --set adminPassword='GrafanaAdm!n' --set datasources."datasources\.yaml".apiVersion=1 --set datasources."datasources\.yaml".datasources[0].name=Prometheus --set datasources."datasources\.yaml".datasources[0].type=prometheus --set datasources."datasources\.yaml".datasources[0].url=http://prometheus-server.prometheus.svc.cluster.local --set datasources."datasources\.yaml".datasources[0].access=proxy --set datasources."datasources\.yaml".datasources[0].isDefault=true --set service.type=LoadBalancer
```
#### Get the password
kubectl get secret --namespace grafana grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo

#### Access grafana on browser
+ Copy the service url. At this moment, service type is loadbalancer
> kubectl get svc -n grafana

+ Check the data sources
> Configuration > Data sources > Prometheus should be available

+ Look for the available dashboard
> https://grafana.com/grafana/dashboards?dataSource=prometheus&search=kubernetes

+ At this moment, lets copy the id of the dashboard i.e. 10000 and `import` in grafana
>Click on `+` sign > import > import via grafana.com > Enter id `10000`
>Click on Load.
