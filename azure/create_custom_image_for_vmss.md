## Custom Image for VMSS

#### Bash cli
```
# resource group where configured vm is present
RG=<Paste resource group name>

# source vm for custom image
IMAGE=<Paste resource Id from properties of an VM>
```

#### create image gallery
```
az sig create --resource-group $RG --location westus --gallery-name imageGallery
```

#### create image definition to provide detail of an image
```
az sig image-definition create \
--resource-group $RG \
--location westus \
--gallery-name imageGallery \
--gallery-image-definition imageDefinition \
--publisher acg \
--offer Ubuntu \
--sku Ubuntu-1804 \
--os-type Linux \
--os-state specialized
```

#### create image version
```
az sig image-version create \
--resource-group $RG \
--location westus \
--gallery-name imageGallery \
--gallery-image-definition imageDefinition \
--gallery-image-version 1.0.0 \
--target-regions "westus=1" "eastus=1" \
--managed-image $IMAGE
```

#### create vmss using new image
```
az vmss create \
--resource-group $RG \
--name myVmss \
--image <Paste resource id of image definition> \
--specialized \
--generate-ssh-key \
--location westus
```
