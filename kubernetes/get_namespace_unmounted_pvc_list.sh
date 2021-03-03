## Get a list of all unmounted pvc in kubernetes cluster 

kubectl get pvc --all-namespaces | egrep -v 'NAMESPACE | Pending' | awk '{print $1,$2}' > pvc-ns.txt

echo "NAMESPACE PVC_NAME" | tee -a unmounted_pvc_$(date +%m%d%Y)
IFS=$'\n'
for i in $(cat pvc-ns.txt)
do
ns=$(echo $i | awk '{print $1}')
pvc=$(echo $i | awk '{print $2}')
mount_status=$(kubectl describe pvc ${pvc} -n ${ns} | grep 'Mounted By' | grep -o 'none')
if [[ $mount_status == 'none' ]] 
then
echo "$i" | tee -a unmounted_pvc_$(date +%m%d%Y)
fi
done

## Expected OUTPUT
```
NAMESPACE PVC_NAME
clickhouse clickhouse-pvc1
clickhouse clickhouse-pvc2
```
