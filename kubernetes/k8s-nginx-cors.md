#### CORS Settings in NGINX running on Kubernetes

```
  annotations:
    nginx.ingress.kubernetes.io/cors-allow-credentials: "true"
    nginx.ingress.kubernetes.io/cors-allow-origin: https://yourdomain.com
    nginx.ingress.kubernetes.io/enable-cors: "true"
```

#### Test using curl
```curl -H "Origin: http://example.com"   -X OPTIONS --verbose   https://yourdomain.com```

#### References
https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/
