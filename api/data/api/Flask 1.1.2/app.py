from flask import Flask, request, jsonify, make_response
from db import init_db

app = Flask(__name__)
db = init_db(app)

class Message(db.Model):
    __tablename__ = 'MESSAGES'
    id = db.Column(db.Integer, primary_key=True, name='ID', autoincrement=True)
    content = db.Column(db.String, unique=False, nullable=True, name='CONTENT')

    def __init__(self, content):
        self.content = content

    def as_dict(self):
        return {'id': self.id, 'content': self.content}


db.init_app(app)
db.create_all()


@app.route('/api/messages', methods=["GET"])
def get_messages():
    response_body = [row.as_dict() for row in Message.query.all()]
    return make_response(jsonify(response_body), 200)


@app.route('/api/messages', methods=["POST"])
def post_message():
    req_data = request.get_json(force=True)
    message = Message(content=req_data['content'])
    db.session.add(message)
    db.session.commit()
    response_body = message.as_dict()
    return make_response(jsonify(response_body), 200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
