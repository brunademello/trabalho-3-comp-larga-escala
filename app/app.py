from flask import Flask, jsonify, request
import json
import boto3

app = Flask(__name__)

lambda_client = boto3.client('lambda')

@app.route('/')
def home_page():
    return json.dumps({'status': '200', 'message': 'Choose some resource'})

@app.route('/getusers')
def get_users():

    response = lambda_client.invoke(FunctionName='getUsers',
                                    InvocationType='RequestResponse')

    return json.dumps({'status': '200', 'users': json.dumps(response)})

#requests.post('http://localhost:5000/insertusers', 
# json={"payload":{"name": "Bruna", "is_active": 1, "created_date": "2022-12-01"}})

@app.route('/insertusers', methods=['POST'])
def insert_users():

    content = request.json

    lambda_client.invoke(FunctionName='insertUsers',
                         InvocationType='Event',
                         payload = jsonify({"data": content['payload']}))

#requests.post('http://localhost:5000/deleteusers', 
# json={"user_id": 3})

@app.route('/deleteusers', methods=['POST'])
def delete_users():

    content = request.json

    lambda_client.invoke(FunctionName='deleteUsers',
                         InvocationType='Event',
                         payload = jsonify({"data": content['user_id']}))

    

    