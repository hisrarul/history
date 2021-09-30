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

Run query
```sql
select int64_field_6 as hour, count(*) as hitcount from logdata.accesslog
group by hour
order by hour

-- Using bq
bq query "select string_field_10 as request, count(*) as requestcount from logdata.accesslog group by request order by requestcount desc"
```