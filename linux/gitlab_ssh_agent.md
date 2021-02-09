## Linux
#### GitLab, working with non-defaut SSH key pair paths
```
# Ref https://docs.gitlab.com/ee/ssh/
eval $(ssh-agent -s)
ssh-add <path to private SSH key>
```
