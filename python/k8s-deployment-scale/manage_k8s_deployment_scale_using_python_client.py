"""
CREATE TABLE `deployments` (
  `namespace` varchar(255) NOT NULL,
  `deployment` varchar(255) NOT NULL,
  `desired_replica_size` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `scaling_txn` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `namespace` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `object_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `replica_size_before_scale_down` int NOT NULL,
  `scale_down_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `scale_up_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `statefulsets` (
  `namespace` varchar(255) NOT NULL,
  `statefulset` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
"""

from __future__ import print_function
import time
import logging
import kubernetes.client
from kubernetes.client.rest import ApiException
import os
from datetime import datetime
from mysql.connector import (connection)

from mysql.connector import (connection)

cnx = connection.MySQLConnection(user='root', password='exam123',
                                 host='localhost',
                                 database='devops')
cursor = cnx.cursor()

# Set log level
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

configuration = kubernetes.client.Configuration()
configuration.verify_ssl=False
configuration.api_key['authorization'] = '<API_KEY>'
configuration.api_key_prefix['authorization'] = 'Bearer'
configuration.host = "<GET_SERVER_FROM_KUBE_CONFIG_FILE>"


def get_all_deployment_list():
    cursor.execute("SELECT * FROM deployments")
    ns_deploy_t = cursor.fetchall()
    
    return ns_deploy_t


def deployment_scale_down():
    for ns_name, deploy_name, desired_replica_size in get_all_deployment_list():
        stop_time = datetime.utcnow()
        start_time =None
        replica_size = get_deployment_replica_size(ns_name, deploy_name)
        scaling_col = ("INSERT INTO scaling_txn "
                       "(namespace, object_name, replica_size_before_scale_down, scale_down_time, scale_up_time) "
                       "VALUES (%s, %s, %s, %s, %s)")
        scaling_data = (ns_name, deploy_name, replica_size, stop_time, start_time)
        cursor.execute(scaling_col, scaling_data)
        cursor_res = cursor._executed
        cnx.commit()
        logging.info("Updated database with following query \n {}".format(cursor_res))
        deployment_scale(ns_name, deploy_name, 0)
    cursor.close()
    cnx.close()

def deployment_scale_up():
    cursor.execute("SELECT * FROM deployments")
    ns_deploy_t = cursor.fetchall()
    start_time = datetime.utcnow()
    for ns_name, deploy_name, desired_replica_size in ns_deploy_t:
        try:
            deployment_scale(ns_name, deploy_name, desired_replica_size)
            scaling_col = ("UPDATE scaling_txn "
                           "SET scale_up_time = %s " 
                           "where namespace=%s and object_name=%s and scale_up_time IS NULL")
            scaling_data = (start_time, ns_name, deploy_name)
            cursor.execute(scaling_col, scaling_data)
            cnx.commit()
        except Exception as err:
            logging.error(err)
    cursor.close()
    cnx.close()

def get_deployment_replica_size(namespace_name, deployment_name):
    with kubernetes.client.ApiClient(configuration) as api_client:
        api_instance = kubernetes.client.AppsV1beta1Api(api_client)
        name = deployment_name
    namespace = namespace_name

    try:
        api_response = api_instance.read_namespaced_deployment(name, namespace)
        jsonstr = api_client.sanitize_for_serialization(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1beta1Api->read_namespaced_deployment: %s\n" % e)
    
    return jsonstr['spec']['replicas']
    

def deployment_scale(namespace_name, deployment_name, replica_size):
    spec = kubernetes.client.V1ScaleSpec(
            replicas=replica_size)
    deployment = kubernetes.client.V1Scale(
        spec=spec)
    with kubernetes.client.ApiClient(configuration) as api_client:
        api_instance = kubernetes.client.AppsV1beta1Api(api_client)
        name = deployment_name
    namespace = namespace_name
    body = deployment

    try:
        logging.info("Updating deployment {} replica size to {} ...".format(deployment_name, replica_size))
        api_response = api_instance.patch_namespaced_deployment_scale(name, namespace, body)
        logging.info("Deployment {} successfully updated.".format(deployment_name))
        logging.info(api_response)
    except ApiException as e:
        print("Exception when calling AppsV1beta1Api->patch_namespaced_deployment_scale: %s\n" % e)

deployment_scale_down()
deployment_scale_up()
deployment_replica_size()
