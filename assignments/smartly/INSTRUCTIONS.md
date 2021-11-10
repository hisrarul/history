# Code Review Exercise

Take a look at the code within this package and review it like you would do in a real life situation for a pull request.
It's recommended to take notes. You should set up a test environment. It is quite likely you will not find all the 
pitfalls without testing the pull request manually.

We'll then discuss the code in the interview. You can also think about how would you refactor this code. The platform to 
run this is expected to be Ubuntu 16.04 LTS, 64bit. Compatible with Ansible 2.6+. The application code itself is not on 
the scope of the review.

For the sake of this exercise, this "pull request" was submitted with the following description:

## Add playbooks and roles to deploy database and postdo app behind a loadbalancer

Deployment of the postdo app. Listens on http/https with REST API.
* role to install and configure postgresql
* role to install and configure postdo app
* role to install and configure loadbalancer
* nginx terminates ssl


#### Solution
```bash
ansible-playbook --ask-vault-pass --private-key test1.pem -u ubuntu -e ansible_python_interpreter=/usr/bin/python -i hosts common.yaml
```