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
