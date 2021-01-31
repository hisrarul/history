## Managed Identities


#### How managed identities work
https://github.com/microsoft/azure-docs/blob/master/articles/active-directory/managed-identities-azure-resources/how-managed-identities-work-vm.md


#### Access resource group using temp key
https://github.com/Microsoft/azure-docs/blob/master/articles/active-directory/managed-identities-azure-resources/tutorial-linux-vm-access-arm.md

curl https://management.azure.com/subscriptions/<subscriptions_id>/resourceGroups/<resourcegroup-name>?api-version=2016-09-01 -H "Authorization: Bearer <token>"
