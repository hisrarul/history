## Secure you endpoint with username and password in kubernetes

#### 1. Generate password
```
htpasswd -c auth <username>    #auth is the passwdfile name
```

#### 2. Create kubernetes secret
```
kubectl create secret generic <secret_name> --from-file auth --namespace <your_namespace>
```

#### 3. Add below annotations in your ingress

```
nginx.ingress.kubernetes.io/auth-type: basic
nginx.ingress.kubernetes.io/auth-secret: <secret_name>
nginx.ingress.kubernetes.io/auth-realm: Authentication Required - foo
nginx.ingress.kubernetes.io/whitelist-source-range: <whitelisted_ip_address_1/32>,<whitelisted_ip_address_2/32>
```

#### 4. Verify the ingress with curl
curl -k -u 'username:password' https://<ingress_endpoint_url>


## Secure you endpoind with multiple username and password using htpasswd 

#### 1. Generate password
```
htpasswd -c auth <username>    #auth is the passwdfile name
htpasswd auth username1
htpasswd auth username2
htpasswd auth username3
```

#### 2. Create kubernetes secret
```
kubectl create secret generic <secret_name> --from-file auth --namespace <your_namespace>
```

#### 3. Add below annotations in your ingress
```
nginx.ingress.kubernetes.io/auth-type: basic
nginx.ingress.kubernetes.io/auth-secret: <secret_name>
nginx.ingress.kubernetes.io/auth-realm: Authentication Required - foo
nginx.ingress.kubernetes.io/whitelist-source-range
nginx.ingress.kubernetes.io/auth-secret-type: auth-map
```

#### 4. Repeat step 4
[Click here](https://github.com/hisrarul/history/edit/master/ingress/k8s_ingress_secure.md#L22)

Ref: 
[Medium](https://medium.com/faun/securing-k8s-application-using-ingress-rule-nginx-ingress-controller-a819b0e11281), 
[Annoatation](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/)
