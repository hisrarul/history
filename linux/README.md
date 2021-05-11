## Linux

#### Test Load
```
stress --vm "1" --vm-bytes 50M --vm-hang "1"
```

#### GitLab, working with non-defaut SSH key pair paths
```
# Ref https://docs.gitlab.com/ee/ssh/
eval $(ssh-agent -s)
ssh-add <path to private SSH key>
```

#### Add comma or any other string at the end of the line
```
sed "s/$/,/" es-open-indices-qa.txt
```

#### Use xargs to delete list of pods
```
kubectl get pod --all-namespaces -o wide | grep airflow-scheduler | awk '{print $2}' | xargs -I{} kubectl delete pod {} -n airflow
```


#### Ldap search
```
ldapsearch -Y EXTERNAL -H ldapi:/// -b cn=config olcDatabase=\*
```

#### SSH to private machine using Jumphost
```
Ref: https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent

eval $(ssh-agent)

ssh-add <ssh-key.pem>

ssh username@<host-with-private-ip> -p 22 -o ConnectTimeout=60 -o ConnectionAttempts=10 -o StrictHostKeyChecking=no -o ProxyCommand="ssh -p 22 -W %h:%p <username>@<jumphost>"
```
