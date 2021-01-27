## HELM

#### Install helm v2.16.1
```
wget https://get.helm.sh/helm-v2.16.1-linux-amd64.tar.gz
tar -xvzf helm-v2.16.1-linux-amd64.tar.gz
cp linux-amd64/helm /usr/local/bin/helm
chmod +x /usr/local/bin/helm
```


#### Error creating: pods "tiller-deploy-84cfd9467d-" is forbidden: error looking up service account kube-system/tiller: serviceaccount
```
kubectl create serviceaccount --namespace kube-system tiller
kubectl create clusterrolebinding tiller-cluster-rule --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
kubectl patch deploy --namespace kube-system tiller-deploy -p '{"spec":{"template":{"spec":{"serviceAccount":"tiller"}}}}'
helm init --service-account tiller --upgrade
```
