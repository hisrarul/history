### Hands-On GitOps

This repository is a resource provided for Linux Academy students taking the hands-on GitIOps course.

#### Install flux on Ubuntu 18

```sudo snap install fluxctl --classic```

#### Deploy Flux Into Your Cluster
Let's make sure Kubernetes is running, and that we have some nodes:

```kubectl get nodes```

Now let's make sure Flux is installed and running:

```fluxctl version```

We should get response of unversioned, which is fine. Now let's take another look at our Kubernetes deployment:

```kubectl get pods --all-namespaces```

Create a namespace for Flux:

```kubectl create namespace flux```

This will let us make sure it got created:

```kubectl get namespaces```

Set the GHUSER environment variable, then check to make sure it was set:
```bash
export GHUSER=[Our GitHub Handle]
env | grep GH
```

Now we can deploy Flux, using the fluxctl command:
```bash
fluxctl install \
--git-user=${GHUSER} \
--git-email=${GHUSER}@users.noreply.github.com \
--git-url=git@github.com:${GHUSER}/history \
--git-path=gitops/flux-gitops/namespaces,gitops/flux-gitops/workloads \
--namespace=flux | kubectl apply -f -
```

Verify The Deployment and Obtain the RSA Key
Once that fluxctl command is finished running, we can verify:
```bash
kubectl get pods --all-namespaces
kubectl -n flux rollout status deployment/flux
```

Now we can get the Flux RSA key created by fluxctl:

```fluxctl identity --k8s-fwd-ns flux```

Copy that RSA key, and let's head back over to GitHub.

#### Implement the RSA Key in GitHub
In the GitHub user interface, make sure we're in our new repository and click on the Settings tab. In there, click Deploy keys, then click the Add deploy key button. We can give it a Title of something like GitOps Deploy Key, then paste the key we copied earlier down in the Key field. Check the Allow write access box, and then click Add key.

Use the fluxctl sync Command to Synchronize the Cluster with the Repository
Use fluxctl to sync the cluster with the new repository:

```fluxctl sync --k8s-fwd-ns flux```

Then check the existence of the lasample namespace:

```kubectl get namespaces```

Then check that the Nginx deployment is running:

```kubectl get pods --namespace=lasample```

We should see the deployment running, with two replicas.

## Installing and Configuring Flux with GitLab

#### Introduction
This lab is for people who do not utilize GitHub, and prefer to use GitLab or some other VCS repository manager with Flux. This lab walks through installing Flux into a Kubernetes cluster, and connecting it to a repository on GitLab.

#### Set Up A Repository (Project) In GitLab
We need to have a GitLab account, and we've got to set up a repository within that account. The repository should contain two files that are Kubernetes YAML. The first, within the namespaces folder, will create a namespace for the application. The YAML is as follows:
```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    name: laflux
  name: laflux
```

The second file is for creating the actual deployment of an NGINX server, and it should probably go in the workloads folder. That YAML is as follows:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: laflux
  labels:
    app: nginx
spec:
  replicas: 2
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```
#### Establish a Terminal Session on the Kubernetes Master and Install Flux
We'll use the credentials on the hands-on lab overview page to log into the Kubernetes host server as cloud_user:
```bash
ssh cloud_user@[IP Address Here]
```

Once we are in the server, we'll make sure Flux is installed:
```bash
fluxctl version
```

We should get response of unversioned, which is fine. Now we can make sure our Kubernetes cluster was spun up, and then look at some more details:

```bash
kubectl get nodes
kubectl get pods --all-namespaces
```

Before we can run Flux, we have to create a namespace for it:
```bash
kubectl create namespace flux
```

Then we've got to set the GLUSER environment variable, and check afterward to make sure it was set:
```bash
export GLUSER=[your GitLab username]
env | grep GL
```

Now we can run Flux:

```bash
fluxctl install \
--git-user=${GLUSER} \
--git-email=${GLUSER}@gmail.com \
--git-url=git@gitlab.com:${GLUSER}/history \
--git-branch=main \
--git-path=namespaces,workloads \
--namespace=flux | kubectl apply -f -
```

We will check on the deployment with the following command:

```bash
kubectl -n flux rollout status deployment/flux
```

#### Obtain the RSA Key Created by fluxctl, and Grant GitLab Write Permission to the Cluster
If everything rolled out properly, we can get the RSA key that was created by the Flux install procedure:
```bash
fluxctl identity --k8s-fwd-ns flux
```

Copy that RSA key, then let's head back into GitLab. Go to Profile Preference in the main menu, then click on SSH Keys in the left pane. Paste our key into the Key field, and give it a Title of something like flux identity. Now we can click the Add key button.

#### Use the fluxctl sync Command to Synchronize the Cluster
After the GitLab account has been granted write access to the Cluster, we can use fluxctl sync to apply the YAML from the repository:
```bash
fluxctl sync --k8s-fwd-ns flux
```
#### Once the sync command has run, we may check that the namespace has been created and that the NGINX deployment has been applied and is running:

```bash
kubectl get pods --all-namespaces
```

References:
[1](https://github.com/linuxacademy/content-gitops)