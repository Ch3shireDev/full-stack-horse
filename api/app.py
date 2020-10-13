from flask import Flask, request, jsonify, make_response
import project as p

app = Flask(__name__)


@app.route('/api/project', methods=['GET'])
def project():
    
    api = request.args['api']
    client = request.args['client']
    server = request.args['server']
    platform = request.args['platform']

    data = p.get_project(api, client, server, platform)
    
    response_body = {"data": data, "name": f"{api.replace(' ', '_')}_{client.replace(' ', '_')}_{server.replace(' ', '_')}_{platform.replace(' ', '_')}"}

    return make_response(jsonify(response_body), 200)


@app.route('/api/data', methods=['GET'])
def get_data():
    response_body = {"apis": p.get_apis(),
                     "clients": p.get_clients(),
                     "servers": p.get_servers(),
                     "platforms": p.get_platforms(),
                     "databases": p.get_databases(),
                     }
    return make_response(jsonify(response_body), 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
