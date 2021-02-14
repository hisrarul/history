## K8S ENV AND CONFIGMAP



#### Define variable in the application
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
  labels:
    app: simple-webapp-color
spec:
  containers:
    - image: redis-container
      name: redis
      env:
        - name: USERNAME
          valueFrom:
            configMapKeyRef: 
              name: app-config
              key: username
        - name: SECRET_PASSWORD
          valueFrom:
            secretKeyRef: 
              name: app-secret
              key: password
  tolerations:
    - key: node-role.kubernetes.io/master
      effect: NoSchedule
```

#### Define configmap
```
kubectl create configmap <config-name> --from-literal=<key>=<value>
For example:
kubectl create configmap app-config --from-literal=username=israrul --from-literal=APP_COLOR=pink

kubectl create configmap <config-name> --from-file=<path-to-file>
For example:
kubectl create configmap app-config --from-file=app_config.properties
```

#### Definition file of configmap
```
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_COLOR: blue
  APP_MODE: prod
```

#### Define configmap in pod definition file
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
  labels:
    name: simple-webapp-color
spec:
  containers:
  - name: simple-webapp-color
    image: mmumshad/simple-webapp-color
    ports:
      - containerPort: 8080
    envFrom:
      - configMapRef:
          name: app-config
  tolerations:
    - key: node-role.kubernetes.io/master
      effect: NoSchedule
```

#### Inject data as a file in volume
```
volumes:
  - name: app-config-volume
    configMap:
      name: app-config
```

### Create secrets and inject into pod

#### Create secrets using imperative way
```
kubectl create secret generic <secret-name> --from-literal=<key>=<value>
For example:
kubectl create secret generic app-secret --from-literal=DB_HOST=mysql \
                                         --from-literal=DB_USER=root \
                                         --from-literal=DB_PASSWORD=paswrd
                                         
kubectl create secret generic <secret-name> --from-file=<path-to-file>
For example:
kubectl create secret generic app-secret --from-file=app_secret.properties
```

#### Create secrets using declarative way
```
apiVersion: v1
kind: Secret
metadata:
  name: app-secret
data:
  DB_HOST: <value_in_encoded_format>
  DB_USER: <value_in_encoded_format>
  DB_PASSWORD: <value_in_encoded_format>

#Generate values in encoded format
echo -n "mysql" | base64
echo -n "root" | base64
echo -n "paswrd" | base64
```

#### Define secrets in pod definition file
```
apiVersion: v1
kind: Pod
metadata:
  name: simple-webapp-color
  labels:
    name: simple-webapp-color
spec:
  containers:
  - name: simple-webapp-color
    image: mmumshad/simple-webapp-color
    ports:
      - containerPort: 8080
    envFrom:
      - secretRef:
          name: app-config
  tolerations:
    - key: node-role.kubernetes.io/master
      effect: NoSchedule
```

#### Encrypting secret data at rest
https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/
