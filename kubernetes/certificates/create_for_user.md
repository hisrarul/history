#### Create certificate for user

* Step 1: Create certificate
```bash
openssl genrsa -out jane.key 2048
openssl req -new -key jane.key -out jane.csr
```

* Step 2: Create Certificate signing request
```bash
cat > csr.yaml << EOF
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: jane
spec:
  groups:
  - system:authenticated
  request: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0KTUlJQ2xEQ0NBWHdDQVFBd1R6RUxNQWtHQTFVRUJoTUNTVTR4RGpBTUJnTlZCQWdNQlVSbGJHaHBNU0V3SHdZRApWUVFLREJoSmJuUmxjbTVsZENCWGFXUm5hWFJ6SUZCMGVTQk1kR1F4RFRBTEJnTlZCQU1NQkdwaGJtVXdnZ0VpCk1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLQW9JQkFRQ3N0cmZnemdxZGRSRFlkQlNBUVIweDRLZ1EKeGdxcTRaUklmdE43Q0EvdlAyRS93Rk96a0pOMEdSUVhoK0ppWVorVEZaRkJzbE1oNGVac2UrNjRzalF0a3dyOQprTnRXV3M0MUdyc0VUaXErSkZUUDVmYWZybWc5VTk0aXI0LzBicllua211cHpRTGZmZFpoQVJnZTZDY1BmNXUyCkFmTFpZUU9iMEFKNW5xbVFCRWRqaks4R1h0SnVBT3NGMU5GdzNqUFVtK0h2NE9oUk9jeFowaktPMDUxQUlYYWUKa1c5UERqLzVPdi9iSmkyb0NzMEI3UkM5K2MxVnRBNzErcTZmN3pzcjVGTGR6K3F1MHRtN3hFQ3p1Y1h6NjBMMAo3Z3NNdFZrdFhrUmFYLzVodnVQRFc0U1hWT0ExSG9YanhxVVhLY0dyWXVxQll4OEhvVGY3L2IySXNyYVhBZ01CCkFBR2dBREFOQmdrcWhraUc5dzBCQVFzRkFBT0NBUUVBWEE3NzJMWnpYaUF6Y29tR2drb0RxZUhqVTZvWHlSSzIKWGkzYXBtMVBoZDU4WE9GcXhJb1I0WVU5R0ZVdG92eE9zZ3ZWRDg2VHJQVGxxNWl6MTlFRjFaeHJuMm9kbVVKMwpKdlVEaDgzRDhjTnRFWDNwOHN5by9oMVh4OUMxa0RUMmxzRW95VmNlTXdBTXJFRHhsclVVSTBzamdmUDFGcldLCm5xdXowSUFJQlFGWXVVNDNVUU5hR2VUSDJOaWZaeWxLQlJ1c0pHdmFaaUVCQzdIWDdCTWtLOGRQZlFiRlhILzYKQ1ZEMm5NRVFYZGd0SHhTcnoySm1xRHpNU21mTUJFVis5VUl1Vkorc2IzTWVBMG14OE9rdi9CS3F5RE5jUjdxUwpSWlFwQ1dyOHdwcXpuYlVDeXpoQ3FYTjNiSUdvMnpQYzRzNHkxWGV6NFoxUkhia0l1M3VDeGc9PQotLS0tLUVORCBDRVJUSUZJQ0FURSBSRVFVRVNULS0tLS0K
  signerName: kubernetes.io/kube-apiserver-client
  expirationSeconds: 86400  # one day
  usages:
  - client auth
EOF

k apply -f csr.yml
```

* Step 3
  * Approve the certificate `k certificate approve jane`
  * Get CRT from CSR 
  * k get csr jane -o yaml (Copy CRT from status)
  * Decode the CRT from base64 and save as jane.crt

* Step 4: Update the config file
  * k config set-credentials jane --client-key=jane.key --client-certificate=jane.crt
  * In config use REDACTED using embed-certs keyword `k config set-credentials jane --client-key=jane.key --client-certificate=jane.crt --embed-certs`
  * View config in raw format `kubectl config view --raw`
 
* Step 5: Set context (optional)
```bash
kubectl config set-context jane --user=jane --cluster=kubernetes
kubectl config get-contexts
kubectl config use-context jane
```

#### Flow:

Create KEY >> Create CSR >> API >> Download CRT from API >> Use CRT + Key

