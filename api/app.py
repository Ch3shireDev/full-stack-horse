from flask import Flask, request, jsonify, make_response
import project as p

app = Flask(__name__)


@app.route('/api/project')
def project():

    api = p.get_apis()[0]
    client = p.get_clients()[0]
    server = p.get_servers()[0]
    platform = p.get_platforms()[0]

    data = p.get_project(api, client, server, platform)
    
    response_body = {"data": data}
    
    return make_response(jsonify(response_body), 200)


@app.route('/api/data')
def get_data():
    response_body = {"apis": p.get_apis(),
                    "clients": p.get_clients(),
                    "servers": p.get_servers(),
                    "platforms": p.get_platforms(),
                    }
    return make_response(jsonify(response_body), 200)
