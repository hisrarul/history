# RUN on both master and worker ndoe
apt-get update
apt-get install docker.io
clear
apt-get install apt-transport-https curl
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
cat <<EOF | sudo tee /etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF


apt-get update
cat /etc/apt/sources.list.d/kubernetes.list
apt-get install -y kubelet kubeadm kubectl

###################################
## Run on only on master
###################################

# Initialize the cluster
kubeadm init --apiserver-advertise-address=172.31.41.237(master_ip) --pod-network-cidr=192.168.0.0/16

To start using your cluster, you need to run the following as a regular user:
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Check the node status
kubectl get nodes

# Install Network plugin
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml

# After network plugin installation, node status should be changed to "Ready"
kubectl get nodes

# Check the pods in kube-system namespace
kubectl get pods -n kube-system

############################################
# Join the worker/slave nodes in the cluster
############################################

kubeadm join 172.31.41.237:6443 --token 4fa85i.io577nctbbvar4lp \
    --discovery-token-ca-cert-hash sha256:2712525026dfcb8c7be7e7bf04ef30174c8bea38dba930f2be20d0d630a0716d

=====================playaround the pod and deployment object type (run on master only)===============================
kubectl create deployment nginx --image=nginx
kubectl get namespaces
kubectl get deployment --namespace default
kubectl get deployment nginx --namespace default -o yaml | more
kubectl get pod -n default
kubectl exec -it nginx-f89759699-5mzxj(pod_name) -n default /bin/bash

vi nginx-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx
  namespace: application
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        imagePullPolicy: Always
        name: nginx


kubectl create -f nginx-deployment.yaml
kubectl create namespace application
kubectl get namespaces
kubectl create -f nginx-deployment.yaml
kubectl get deployment -n application
kubectl get pod -n application
kubectl describe pod nginx-6b88879868-dc9w5 -n application
kubectl get pod -n application
kubectl logs nginx-6b88879868-dc9w5 -n application

# Create the service for deployment nginx running in "default" namespace
kubectl expose deployment nginx --port=80 --target-port=80 --type=NodePort
kubectl get service
curl http://localhost:30204
kubectl get pod -n default
kubectl get service -n default
# Check on which node(server), my pod is running
kubectl get pod -n default -o wide
