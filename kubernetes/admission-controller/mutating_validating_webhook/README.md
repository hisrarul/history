## Mutating and Validating Webhook

* Create mutating and validating webhook configuration
* For webhook server, create tls secret

```bash
kubectl create secret tls werbhook-server-tls --cert=keys/webhook-server-tls.crt --key=keys/webhook-server-tls.key
```

* The mutating webhook server will do following changes
  * Will not allow pod to run if security context is not defined
  * Will update the security context to `runAsNonRoot: true` and `runAsUser: 1234`
