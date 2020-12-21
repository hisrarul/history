### Wazuh enable vpcflow log
```
#add this into configmap of wazuh if running it on k8s
          <bucket type="vpcflow">
              <name>s3-bucket-name</name>
              <only_logs_after>2019-JAN-17</only_logs_after>
              <remove_from_bucket>yes</remove_from_bucket>
          </bucket>
```
