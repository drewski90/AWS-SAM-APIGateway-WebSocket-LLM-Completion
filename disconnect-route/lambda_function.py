
def lambda_handler(event, context):
    
  connection_id = event['requestContext']['connectionId']
  print(event)
  return {
      'statusCode': 200,
      'body': None
  }
