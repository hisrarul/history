## GCP Fundamentals: Core Infrastructure


#### Create phpinfo page on Linux machine
```bash
sudo sh -c 'echo "<?php phpinfo(); ?>" > apache2/htdocs/phpinfo.php'
```

#### Create Virtual machine using gcloud cli
```bash
# List all zones
gcloud compute zones list

# Set default zone
gcloud config set compute/zone us-central1-b

# Create a VM
gcloud compute instances create "my-vm-1" \
  --machine-type "n1-standard-1" \
  --image-project "debian-cloud" \
  --image-family "debian-10" \
  --subnet "default"
```

#### Deploy a web VM instance
```bash
# Run below commands using startup-script
apt-get update
apt-get install apache2 php php-mysql -y
service apache2 restart
```

#### Create Cloud Storage Bucket using gsutil
```
# Export region
export LOCATION=US

# Create bucket using project id
gsutil mb -l $LOCATION gs://$DEVSHELL_PROJECT_ID

gsutil cp OBJECT_LOCATION gs://DESTINATION_BUCKET_NAME/

# Object will be readable by all
gsutil acl ch -u allUsers:R gs://$DEVSHELL_PROJECT_ID/OBJECT_LOCATION
```


#### Configure php application to use Cloud SQL
```bash
cd /var/www/html

sudo service apache2 restart

curl VM_IP/index.php
```

#### Start a GKE Cluster
```bash
# Export zone
export MY_ZONE=us-central1-a

# Start the cluster
gcloud container clusters create webfrontend --zone $MY_ZONE --num-nodes 2

# Deploy a container
kubectl create deploy nginx --image=nginx:1.17.10

# Expose the container to the Internet
kubectl expose deployment nginx --port 80 --type LoadBalancer

# Scale number of pod to 2
kubectl scale deployment nginx --replicas 2

#### App Engine
```bash
# Initialize the App Engine
gcloud app create --project=$DEVSHELL_PROJECT_ID

# Clone hello world repo
git clone https://github.com/GoogleCloudPlatform/python-docs-samples

# Deploy and run hello world on App Engine
cd python-docs-samples/appengine/standard_python3/hello_world
gcloud app deploy

# Launch browser to view the app
gcloud app browse
```

#### IaC: Deployment Manager
```bash
# Export zone
export MY_ZONE=us-central1-a

# Download template
gsutil cp gs://cloud-training/gcpfcoreinfra/mydeploy.yaml mydeploy.yaml
        
# Update the project id
sed -i -e "s/PROJECT_ID/$DEVSHELL_PROJECT_ID/" mydeploy.yaml

# Update the zone
sed -i -e "s/ZONE/$MY_ZONE/" mydeploy.yaml

# Build a deployment from template
gcloud deployment-manager deployments create my-first-depl --config mydeploy.yaml

# To increase the load
dd if=/dev/urandom | gzip -9 >> /dev/null &
```

#### Bigquery
```bash
# Create table using cloud storage (CSV format)
gs://cloud-training/gcpfci/access_log.csv
```

```sql
-- Run query
select int64_field_6 as hour, count(*) as hitcount from logdata.accesslog
group by hour
order by hour

-- Using bq
bq query "select string_field_10 as request, count(*) as requestcount from logdata.accesslog group by request order by requestcount desc"
```

#### Summary


#### Comparing compute options

<table>
  <tr>
    <th></th>
    <th>Compute Engine</th>
    <th>Kubernetes Engine</th>
    <th>App Engine Flex</th>
    <th>App Engine Standard</th>
    <th>Cloud Functions</th>
  </tr>
  <tr>
    <td><b>Service model</b></td>
    <td>Iaas </td>
    <td>Hybrid </td>
    <td>PaaS </td>
    <td>PaaS </td>
    <td>Serverless </td>
  </tr>
  <tr>
    <td><b>Use cases</b></td>
    <td>General computing workloads</td>
    <td>Container based workloads</td>
    <td>Web and mobile appcations; container based workloads</td>
    <td>Web and mobile appcations</td>
    <td>Ephemeral functions responding to events</td>
  </tr>
</table>


#### Comparing load balancing options

<table>
  <tr>
    <th>Global HTTP(S)</th>
    <th>Global SSL Proxy</th>
    <th>Global TCP Proxy</th>
    <th>Regional</th>
    <th>Regionl Internal</th>
  </tr>
  <tr>
    <td>Layer 7 load balancing based on load </td>
    <td>Layer 4 load balancing of non-HTTPS SSL traffic based on load</td>
    <td>Layer 4 load balancing of non-SSL TCP traffic</td>
    <td>Load balancing of any traffic (TCP, UDP)</td>
    <td>Load balancing of traffic inside a VPC</td>
  </tr>
  <tr>
    <td>Can route different URLs to different backends</td>
    <td>Supported on specific port numbers</td>
    <td>Supported on specific port numbers</td>
    <td>Supported on any port number</td>
    <td>Used for the internal tiers of multi-tier applications</td>
  </tr>
</table>


#### Comparing interconnect options

<table>
  <tr>
    <th>VPN</th>
    <th>Direct Peering</th>
    <th>Carrier Peering</th>
    <th>Dedicated Interconnect</th>
  </tr>
  <tr>
    <td>Secure multi-Gbps connection over VPN tunnels</td>
    <td>Private connection between you and Google for your hybrid cloud workloads</td>
    <td>Connection through the largest partner network of service providers</td>
    <td>Connect N X 10G tranport circuits for private cloud traffic to Google Cloud at Google POPs</td>
  </tr>
</table>


#### Comparing storage options

<table>
  <tr>
    <th></th>
    <th>Cloud Datastore</th>
    <th>Cloud Bigtable</th>
    <th>Cloud Storage</th>
    <th>Cloud SQL</th>
    <th>Cloud Spanner</th>
    <th>BigQuery</th>
  </tr>
  <tr>
    <td><b>Type</b></td>
    <td>NoSQL document</td>
    <td>NoSQL wide column</td>
    <td>Blobstore</td>
    <td>Relational SQL for OLTP</td>
    <td>Relational SQL for OLTP</td>
    <td>Relational SQL for OLAP</td>
  </tr>
  <tr>
    <td><b>Best for</b></td>
    <td>Getting started, App Engine applications</td>
    <td>"Flat" data, Heavy read/write, events, analytical data</td>
    <td>Structured and unstructured binary or object data</td>
    <td>Web frameworks, existing applications</td>
    <td>Large scale database applications (>~2TB)</td>
    <td>Interactive querying, offline analytics</td>
  </tr>
  <tr>
    <td><b>Use cases</b></td>
    <td>Getting started, App Engine applications</td>
    <td>AdTech, Financial and IoT data</td>
    <td>Images, large media files, backups</td>
    <td>User credentials, customer orders</td>
    <td>Whenever high I/O, global consistency is needed</td>
    <td>Data warehousing</td>
  </tr>
</table>


#### Choosig among Google Cloud Storage classes

<table>
  <tr>
    <th></th>
    <th>Multi-regional</th>
    <th>Regional</th>
    <th>Nearline</th>
    <th>Coldline</th>
  </tr>
  <tr>
    <td><b>Intended for data that is</b></td>
    <td>Most frequently accessed</td>
    <td>Access frequently within a region</td>
    <td>Access less than once a month</td>
    <td>Access less than once a month</td>
  </tr>
  <tr>
    <td><b>Availability SLA</b></td>
    <td>99.95%</td>
    <td>99.90%</td>
    <td>99.00%</td>
    <td>99.00%</td>
  </tr>
  <tr>
    <td><b>Access APIs</b></td>
    <td colspan="4">Consistent APIs</td>
  </tr>
  <tr>
    <td><b>Access time</b></td>
    <td colspan="4">Millisecond access</td>
  </tr>
  <tr>
    <td><b>Storage price</b></td>
    <td colspan="4">Price per GB per month</td>
  </tr>
  <tr>
    <td><b>Retrieval price</b></td>
    <td colspan="4">Total price per GB transferred</td>
  </tr>
  <tr>
    <td><b>Use cases</b></td>
    <td>Content storage and delivery</td>
    <td>In-region analytics, transcoding</td>
    <td>Long-tail content, backups</td>
    <td>Archiving, disaster recovery</td>
  </tr>
</table>