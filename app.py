from flask import Flask, jsonify, request
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


import bcrypt
import time
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    # REQUIRE AN EMAIL AND PASSWORD
    if not data.get('email', None) or not data.get('password', False):
        return jsonify({'error': 'must provide email and password'})

    # VERIFY THAT THIS USER DOES NOT ALREADY EXIST
    check_status = table.get_item(Key={"email": str(data['email']).upper()})
    if(check_status.get('Item')):
        return jsonify({'error': 'profile exists already'})


    #CREATE A HASHED PASSWORD AND POST OBJECT
    hashed_password = bcrypt.hashpw(str(data['password']), bcrypt.gensalt())
    post_obj = {
        'email': data['email'].upper(),
        'password_hash': hashed_password,
        'created_at': int(time.time())
    }

    save_user = table.put_item(
        Item=post_obj
    )

    return jsonify({'message': 'user created'})

if __name__ == "__main__":
    app.run(debug=True)
