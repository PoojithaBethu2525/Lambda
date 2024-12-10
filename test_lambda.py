import json
def lambda_handler(event, context):
    print("Lambda from my code")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Lambda!! From my code')
    }