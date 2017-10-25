from flask import Flask, jsonify
import boto3

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
        "hello": "world"
    })


import boto3
session = boto3.Session()
dynDB = session.resource('dynamodb')
table = dynDB.Table('PYKC-Auth')

#I don't actually recommend creating this endpoint. just for demo purposes.
@app.route('/<email>')
def check_email(email):
    response = table.get_item(Key={"email": email.upper()})
    if response.get('Item', None):
        return jsonify(response)
    else:
        return jsonify({'error': 'user not found'})

if __name__ == "__main__":
    app.run(debug=True)
