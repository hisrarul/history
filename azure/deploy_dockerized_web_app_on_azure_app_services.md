## Deploy dockerized web app on Azure app services

#### Define variables value
```
RG="<enter resource group>"
ACR="<enter acr name to create>"
```

#### create azure container registry
```
az acr create --resource-group $RG --name $ACR --sku Basic --admin-enabled true
```

#### build the docker image and push to acr
```
# project source
# git clone --branch js-docker https://github.com/linuxacademy/content-AZ-104-Microsoft-Azure-Administrator.git ./js-docker

cd js-docker
az acr build --image js-docker:v1 --registry $ACR --file Dockerfile .
```