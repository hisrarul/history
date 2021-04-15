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

class scale_statefulsets:

    def __init__(self):
        self.dbEndpoint = os.environ['DB_ENDPOINT']
        self.dbLoginUser = os.environ['DB_USER']
        self.dbLoginPassword = os.environ['DB_PASSWORD']
        self.dbName = os.environ['DB_NAME']
        self.dbconn = connection.MySQLConnection(user=self.dbLoginUser, password=self.dbLoginPassword, host=self.dbEndpoint, database=self.dbName)
        self.cursor = self.dbconn.cursor()


    def get_all_statefulset_list(self):
        self.cursor.execute("SELECT namespace, statefulset, desired_replica_size FROM statefulsets")
        ns_deploy_t = self.cursor.fetchall()
        
        return ns_deploy_t


    def statefulset_scale_down(self):

        for ns_name, sts_name, desired_replica_size in self.get_all_statefulset_list():
            stp_time = datetime.utcnow()
            strt_time =None
            replica_size = self.get_statefulset_replica_size(ns_name, sts_name)
            scaling_col = ("INSERT INTO scaling_txn "
                        "(namespace, object_type, object_name, rs_old_count, stop_time, start_time) "
                        "VALUES (%s, %s, %s, %s, %s, %s)")
            scaling_data = (ns_name, 'statefulset', sts_name, replica_size, stp_time, strt_time)
            self.cursor.execute(scaling_col, scaling_data)
            cursor_res = self.cursor._executed
            self.dbconn.commit()
            logging.info("Updated database with following query \n {}".format(cursor_res))
            self.statefulset_scale(ns_name, sts_name, 0)
        self.cursor.close()
        self.dbconn.close()

    def statefulset_scale_up(self):
        self.cursor.execute("SELECT namespace, statefulset, desired_replica_size FROM statefulsets")
        ns_deploy_t = self.cursor.fetchall()
        strt_time = datetime.utcnow()

        for ns_name, sts_name, desired_replica_size in ns_deploy_t:
            try:
                self.statefulset_scale(ns_name, sts_name, desired_replica_size)
                scaling_col = ("UPDATE scaling_txn "
                            "SET start_time = %s "
                            "where namespace=%s and object_name=%s and start_time IS NULL")
                scaling_data = (strt_time, ns_name, sts_name)
                self.cursor.execute(scaling_col, scaling_data)
                self.dbconn.commit()
            except Exception as err:
                logging.error(err)
        self.cursor.close()
        self.dbconn.close()


    def get_statefulset_replica_size(self, namespace_name, statefulset_name):
        with kubernetes.client.ApiClient(configuration) as api_client:
            api_instance = kubernetes.client.AppsV1beta1Api(api_client)
            name = statefulset_name
        namespace = namespace_name
        try:
            api_response = api_instance.read_namespaced_stateful_set(name, namespace)
            jsonstr = api_client.sanitize_for_serialization(api_response)
        except ApiException as e:
            logging.error("Exception when calling AppsV1Api->read_namespaced_stateful_set: %s\n" % e)
        
        return jsonstr['spec']['replicas']
        

    def statefulset_scale(self, namespace_name, statefulset_name, replica_size):
        
        sts_template = kubernetes.client.V1PodTemplateSpec()
        spec = kubernetes.client.V1beta1StatefulSetSpec(replicas=replica_size,service_name = 'dummy',template=sts_template)
        statefulset = kubernetes.client.V1beta1StatefulSet(spec=spec)

        with kubernetes.client.ApiClient(configuration) as api_client:
            api_instance = kubernetes.client.AppsV1Api(api_client)
            name = statefulset_name
        namespace = namespace_name
        body = statefulset

        try:
            logging.info("Updating statefulset {} replica size to {} ...".format(statefulset_name, replica_size))
            api_response = api_instance.patch_namespaced_stateful_set_scale(name, namespace, body)
            logging.info("Statefulset {} successfully updated.".format(statefulset_name))
            logging.info(api_response)
        except ApiException as e:
            logging.error("Exception when calling AppsV1Api->patch_namespaced_stateful_set_scale: %s\n" % e)
