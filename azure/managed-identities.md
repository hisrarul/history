## Managed Identities


#### How managed identities work
https://github.com/microsoft/azure-docs/blob/master/articles/active-directory/managed-identities-azure-resources/how-managed-identities-work-vm.md


#### Access resource group using temp key
https://github.com/Microsoft/azure-docs/blob/master/articles/active-directory/managed-identities-azure-resources/tutorial-linux-vm-access-arm.md

curl https://management.azure.com/subscriptions/fb3c3563-427d-40a1-a3f7-8a4651a1a6d9/resourceGroups/aks-engine?api-version=2016-09-01 -H "Authorization: Bearer <token>"
