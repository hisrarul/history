## Redis

#### redis-cli config
```
https://gist.github.com/kapkaev/4619127#file-gistfile1-bat
https://github.com/helm/charts/issues/3143
```


#### redis-cli commands to delete key
```
keys *
hgetall <key>
keys <*key(>
lrange <key> <start=0> <stop=-1>
del <key>
lrange <key> <start=0> <stop=-1>
```
