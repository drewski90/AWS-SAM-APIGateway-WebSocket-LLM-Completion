import requests
from os import environ
from json import dumps, loads
import boto3

# Create a boto3 client for API Gateway
api_gateway_client = boto3.client(
  'apigatewaymanagementapi',
  endpoint_url=f"https://{environ['WEBSOCKET_ID']}.execute-api.{environ['AWS_REGION']}.amazonaws.com/production"
  )

URL = environ['OPENAI_BASE_URL'] + "/chat/completions"
API_KEY = environ['OPENAI_API_KEY']
MODEL_ID = environ['OPENAI_MODEL_ID']

def parse_line(line):
  # if the line st
  if line.startswith(b'data: {'):
    try:
      return loads(line[6:])
    except Exception as e:
      print(e)  
      return

def lambda_handler(event, context):
  
  # get websocket connection id
  connection_id = event['requestContext']['connectionId']
  
  # get the body from the event
  body = loads(event['body'])
  
  # request id helps the frontend match incoming data to a request
  request_id = body['id']
  
  # get request payload...sent directly to the completions api
  payload = body['payload']
  payload['model'] = MODEL_ID
  payload['stream'] = True
  
  # make request headers
  headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
  }
  
  # Send POST request with streaming response
  response = requests.post(URL, json=payload, headers=headers, stream=True)
  
  # Iterate over response content as it streams in
  for line in response.iter_lines():
    print(line)
    # if the line starts with data try to parse it as json
    data = parse_line(line)
    if data:
      # if we were able to parse the data, send it to the client
      post_to_connection(connection_id, {
        "id": request_id,
        "object": 'chat-completion',
        "data": data
      })
      
  return {
    'statusCode': 200,
    'body': "ok"
  }

def post_to_connection(connection_id:str, data:dict):

  try:
    api_gateway_client.post_to_connection(
      ConnectionId = connection_id, 
      Data = dumps(data)
    )
  except Exception as e:
    print('Error posting message:', e)