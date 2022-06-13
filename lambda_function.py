import json
from plot import plot

def lambda_handler(event, context):
    leads = []
    
    try:
        leads = json.loads(event['body'])['waveform']
    except:
        return {
            'statusCode': 400,
            "headers": {
                "Content-Type": "application/json"
            },
            'body': json.dumps(
                {
                'message': 'Unable to parse JSON'
            })
        }

    if (leads == None):
        return {
            'statusCode': 400,
            "headers": {
                "Content-Type": "application/json"
            },
            'body': json.dumps(
                {
                'message': 'No waveform provided'
            })
        }

    try:
        generated_chart = plot(leads)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "image/svg+xml"
            },
            "body": generated_chart
        }
    except:
        return {
            'statusCode': 400,
            "headers": {
                "Content-Type": "application/json"
            },
            'body': json.dumps(
                {
                'message': 'Error generating chart'
            })
        }