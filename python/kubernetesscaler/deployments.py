"""
CREATE TABLE `deployments` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `namespace` varchar(255) NOT NULL,
  `deployment` varchar(255) NOT NULL,
  `desired_replica_size` int NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `scaling_txn` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `namespace` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `object_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `object_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `rs_old_count` int NOT NULL,
  `stop_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `start_time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `statefulsets` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `namespace` varchar(255) NOT NULL,
  `statefulset` varchar(255) NOT NULL,
  `desired_replica_size` int NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
"""

import time
import logging
import kubernetes.client
from kubernetes.client.rest import ApiException
import os
from datetime import datetime
from mysql.connector import (connection)

# Set log level
logging.basicConfig()
logger = logging.getLogger()
logger.setLevel(logging.INFO)

configuration = kubernetes.client.Configuration()
configuration.verify_ssl=False
configuration.api_key['authorization'] = os.environ['API_AUTH_KEY'] 
configuration.api_key_prefix['authorization'] = 'Bearer'
configuration.host = os.environ['API_SERVER_WITH_PORT']

class scale_deployments:

    def __init__(self):
        self.dbEndpoint = os.environ['DB_ENDPOINT']
        self.dbLoginUser = os.environ['DB_USER']
        self.dbLoginPassword = os.environ['DB_PASSWORD']
        self.dbName = os.environ['DB_NAME']
        self.dbconn = connection.MySQLConnection(user=self.dbLoginUser, password=self.dbLoginPassword, host=self.dbEndpoint, database=self.dbName)
        self.cursor = self.dbconn.cursor()


    def get_all_deployment_list(self):
        self.cursor.execute("SELECT namespace, deployment, desired_replica_size FROM deployments")
        ns_deploy_t = self.cursor.fetchall()
        
        return ns_deploy_t


    def deployment_scale_down(self):

        for ns_name, deploy_name, desired_replica_size in self.get_all_deployment_list():
            stp_time = datetime.utcnow()
            strt_time =None
            replica_size = self.get_deployment_replica_size(ns_name, deploy_name)
            scaling_col = ("INSERT INTO scaling_txn "
                        "(namespace, object_type, object_name, rs_old_count, stop_time, start_time) "
                        "VALUES (%s, %s, %s, %s, %s, %s)")
            scaling_data = (ns_name, 'deployment', deploy_name, replica_size, stp_time, strt_time)
            self.cursor.execute(scaling_col, scaling_data)
            cursor_res = self.cursor._executed
            self.dbconn.commit()
            logging.info("Updated database with following query \n {}".format(cursor_res))
            self.deployment_scale(ns_name, deploy_name, 0)
        self.cursor.close()
        self.dbconn.close()

    def deployment_scale_up(self):
        self.cursor.execute("SELECT namespace, deployment, desired_replica_size FROM deployments")
        ns_deploy_t = self.cursor.fetchall()
        strt_time = datetime.utcnow()

        for ns_name, deploy_name, desired_replica_size in ns_deploy_t:
            try:
                self.deployment_scale(ns_name, deploy_name, desired_replica_size)
                scaling_col = ("UPDATE scaling_txn "
                            "SET start_time = %s " 
                            "where namespace=%s and object_name=%s and start_time IS NULL")
                scaling_data = (strt_time, ns_name, deploy_name)
                self.cursor.execute(scaling_col, scaling_data)
                self.dbconn.commit()
            except Exception as err:
                logging.error(err)
        self.cursor.close()
        self.dbconn.close()


    def get_deployment_replica_size(self, namespace_name, deployment_name):
        with kubernetes.client.ApiClient(configuration) as api_client:
            api_instance = kubernetes.client.AppsV1beta1Api(api_client)
            name = deployment_name
        namespace = namespace_name
        try:
            api_response = api_instance.read_namespaced_deployment(name, namespace)
            jsonstr = api_client.sanitize_for_serialization(api_response)
        except ApiException as e:
            logging.error("Exception when calling AppsV1beta1Api->read_namespaced_deployment: %s\n" % e)
        
        return jsonstr['spec']['replicas']
        

    def deployment_scale(self, namespace_name, deployment_name, replica_size):
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
            logging.error("Exception when calling AppsV1beta1Api->patch_namespaced_deployment_scale: %s\n" % e)

