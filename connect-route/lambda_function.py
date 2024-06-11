from json import dumps

def lambda_handler(event, context):
    # add in whatever logic
    stage = event['requestContext']['stage']
    connection_id = event['requestContext']['connectionId']
    print('allowing connection: ', connection_id)
    return {
        'statusCode': 200,
        'body': dumps({"connectionId": connection_id})
    }