from flask import Flask, request, jsonify, make_response
from db import get_cursor


app = Flask(__name__)


@app.route('/api/messages', methods=["GET"])
def get_messages():
    cursor = get_cursor()
    cursor.execute('select ID, CONTENT from MESSAGES')
    
    response_body = []
    
    # while True:
    #     row = cursor.fetchnone()
    #     if not row:
    #         break
    #     _id, content = row
    #     response_body.append({'id':_id, 'content':content})
    
    return make_response(jsonify(response_body), 200)


@app.route('/api/messages', methods=["POST"])
def post_message():
    cursor = get_cursor()
    content = 'abc'
    cursor.execute(f"insert into MESSAGES (content) values ('{content}')")
    response_body = [{"id": 1, "content": "abc"}]
    return make_response(jsonify(response_body), 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
