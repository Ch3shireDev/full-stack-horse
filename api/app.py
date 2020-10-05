from flask import Flask, request, jsonify, make_response
import project as p

app = Flask(__name__)


@app.route('/api/project')
def project():

    api = p.get_apis()
    client = p.get_clients()
    server = p.get_servers()
    platform = p.get_platforms()

    data = p.get_project(api[0], client[0], server[0], platform[0])
    
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)