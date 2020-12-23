### Wazuh enable vpcflow log
```
#add this into configmap of wazuh if running it on k8s
          <bucket type="vpcflow">
              <name>s3-bucket-name</name>
              <only_logs_after>2019-JAN-17</only_logs_after>
              <remove_from_bucket>yes</remove_from_bucket>
          </bucket>
```

### Error: kibana is loading or wazuh plugin is not showing security and integrity events
```
###
#Errors: 
#There are no index patterns (/elastic/index-patterns)
#Settings. Error getting API entries
###

Solution:
1. Check if elasticsearch is working fine, kubectl logs -f elasticsearch-0 -n namespace
2. Check the logs of kibana
3. Check the logs of wazuh, if your disk is not free then delete the old data
4. If everything is fine with elasticsearch and kibana then check for .kibana* and .wazuh index
curl -k -s -X GET -u "username:password" "https://localhost:9200/_cat/indices" | egrep -i '.kibana*|.wazuh'
5. Delete .kibana index 
curl -k -X DELETE -u "username:password" "https://localhost:9200/.kibana*"
6. Delete .wazuh index
curl -k -X DELETE -u "username:password" "https://localhost:9200/.wazuh"
7. Open the kibana and click on wazuh plugin.
8. Enter the wazuh master url with username and password
9. Wait for some time, it should start reflecting data.
```

### Search data in wazuh index
```
GET .wazuh/_search
{
  "query": {
    "match_all": {}
  }
}
```
