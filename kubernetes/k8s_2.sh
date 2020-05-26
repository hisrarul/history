kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-0.32.0/deploy/static/provider/aws/deploy.yaml
kubectl get pods -n ingress-nginx   -l app.kubernetes.io/name=ingress-nginx --watch
>> ctrl + c
kubectl get pod -n ingress-nginx
kubectl logs ingress-nginx-admission-create-75ch5 -n ingress-nginx
kubectl describe pod ingress-nginx-admission-create-75ch5 -n ingress-nginx
kubectl get service
kubectl delete service nginx
kubectl create service clusterip nginx --tcp 80:80
kubectl get service
vi ingress.yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: simple-fanout-example
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
    - http:
        paths:
        - path: /foo
          backend:
            serviceName: nginx
            servicePort: 80

kubectl create -f ingress.yaml
kubectl get ingress
curl http://localhost/foo

# Deploy dashboard
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0/aio/deploy/recommended.yaml
kubectl get namespace
kubectl get pod -n kubernetes-dashboard
kubectl get service -n kubernetes-dashboard
# Edit the service type for dashboard
kubectl edit service kubernetes-dashboard -n kubernetes-dashboard
>> Change from type=ClusterIP to type=NodePort
kubectl get service -n kubernetes-dashboard
>> Check the port and open the browser. Paste the master ip address with nodeport port
kubectl get pod -n kubernetes-dashboard -o wide
kubectl get clusterrole | grep admin
kubectl create serviceaccount cluster-admin-dashboard
kubectl get sa
kubectl create clusterrolebinding cluster-admin-dashboard-rb --clusterrole=cluster-admin --serviceaccount=default:cluster-admin-dashboard
kubectl get clusterrolebinding | grep dashboard
clear
kubectl get sa
kubectl get secret cluster-admin-dashboard
# Get the token for sa
kubectl describe secret cluster-admin-dashboard

