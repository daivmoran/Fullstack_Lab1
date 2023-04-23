#!/usr/bin/env python3
from flask import Flask, request, jsonify
from boto3.dynamodb.conditions import Key
import boto3
app = Flask(__name__)

#use curl or postman for API client simulated call
#curl -i -H "Content-Type: application/json" -X POST -d '{"user":"foo", "status": "bar"}' http://127.0.0.1:8443/write
#curl -i -H "Content-Type: application/json" -X GET -d '{"user":"foo"}' http://127.0.0.1:8443/read

#use the AWS resource abstracted level API (not client class)
dynamodb = boto3.resource('dynamodb') #an object instance
table = dynamodb.Table('lab') #reference the table we made


@app.route('/write', methods=['POST'])
def write():
   data = request.json
   #print(data['somekey'])
   user = str(data['user'])
   status = str(data['status'])
   response = table.put_item(
   #Item is a dictionary parameter needed in put_item method
   Item={
       'user' : user,
       'status' : status
   }
   )
   #return jsonify(data)
   return response

@app.route('/read', methods=['GET'])
def read():
   data = request.json
   #print(data['somekey'])
   user = str(data['user'])
   #status = str(data['status'])
   response = table.query(
   KeyConditionExpression=Key('user').eq(user)
   )
   print(response['Items'])
   #return jsonify(data)
   return response


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8443)