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

#### Install secret plugin on helm
```
helm  plugin install https://github.com/jkroepke/helm-secrets
```

#### Error: error initializing: Looks like "https://kubernetes-charts.storage.googleapis.com" is not a valid chart repository or cannot be reached: Failed to fetch https://kubernetes-charts.storage.googleapis.com/index.yaml : 403 Forbidden 
```
helm init --stable-repo-url https://charts.helm.sh/stable --service-account tiller
```
