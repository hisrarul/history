## Admission Controller

* Enable admission controller to create namespace if not exist
  * Update kube-apiserver.yaml file with `--enable-admission-plugins=NamespaceAutoProvision`
* Disable admission controller default storage class
  * Update kube-apiserver.yaml file with `--disable-admission-plugins=DefaultStorageClass`
* Kubelets will only be allowed to modify their own Node API object, and only modify Pod API objects that are bound to their node.
  * Update kube-apiserver.yaml file with `--enable-admission-plugins=NodeRestriction`

