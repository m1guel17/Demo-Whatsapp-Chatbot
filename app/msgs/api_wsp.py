from flask import json
import http.client
import os

token_env = os.environ.get('token_env')
req_env = os.environ.get('req_env')

def send_response(data):
    data = json.dumps(data)

    headers = {
        "Content-Type": "application/json",
        "Authorization": token_env
    }
    connection = http.client.HTTPSConnection("graph.facebook.com")    
    try:
        connection.request("POST", req_env, data, headers)
        response = connection.getresponse()
        print(response.status, response.reason)
    except Exception as e:
        print(e)
    finally:
        connection.close()