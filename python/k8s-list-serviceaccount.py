#### List service account in kubernetes

from kubernetes import client, config
import json

config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing service account: ")
ret = v1.list_service_account_for_all_namespaces(watch=False)
for i in ret.items:
    print("ServiceAccountName   {}".format(i.metadata.name))
    
## References
# https://raw.githubusercontent.com/kubernetes-client/python/master/kubernetes/docs/CoreV1Api.md
# https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ServiceAccountList.md
##
