from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import requests, json

app = Flask(__name__)
CORS(app)

status = []
services_data = [{'service_name': 'Gerrit', 'service_url': 'https://gerrit.com'}, 
                 {'service_name': 'Jenkins', 'service_url': 'https://jenkins.com'}, 
                 {'service_name': 'Artifactory', 'service_url': 'http://artifactory.com'}]

@app.route("/api/services/ui/health")
def gerritui():
    data = {}
    status.clear()
    try:
        for url in services_data:
            response = requests.get(url['service_url'])
            if response.status_code == 200:
                data['service_name'] = url['service_name']
                data['service_status'] = 'Operational'
            else:
                data['service_name'] = url['service_name']
                data['service_status'] = 'Non-Operational'
            status.append(data.copy())
    except Exception as err:
        print(err)
    return jsonify(status)
