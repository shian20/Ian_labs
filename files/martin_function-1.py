import requests
import json
import logging
import boto3

log = logging.getLogger('martin_email_notif_service-logger')
log.setLevel(logging.INFO)

BASE_RES_URL = (
    'https://jj2fsi1ci6'
    '.execute-api.ap-southeast-1.amazonaws.com{}'
)

# From the email_consumer.py Function
# EMAIL SENDER API

def send_email_alert(to_email, message):
    subject = '[GTECH EMAIL NOTIF] CRITICAL ERROR ALERT'
    url = BASE_RES_URL.format('/email_sender_service')
    res = requests.post(url, json={
        'to': to_email,
        'subject': subject,
        'body': message,
    })
    try:
        res.raise_for_status()
    except Exception as err:
        # breakpoint()
        raise err
    return res.json()
    
def send_sns(notif, log_level):
    
    if log_level == 'debug':
        client = boto3.client('sns')
        response = client.publish(
            TargetArn = "arn:aws:sns:ap-southeast-1:337008671328:martin_magayanes-TOPIC-DEBUG",
            Message = json.dumps({'default':notif}),
            MessageStructure = 'json'
            )
    elif log_level == 'info':
        client = boto3.client('sns')
        response = client.publish(
            TargetArn = "arn:aws:sns:ap-southeast-1:337008671328:martin_magayanes-TOPIC-INFO",
            Message = json.dumps({'default':notif}),
            MessageStructure = 'json'
            )
    elif log_level == 'warning':
        client = boto3.client('sns')
        response = client.publish(
            TargetArn = "arn:aws:sns:ap-southeast-1:337008671328:martin_magayanes-TOPIC-WARNING",
            Message = json.dumps({'default':notif}),
            MessageStructure = 'json'
            )
    elif log_level == 'error':
        client = boto3.client('sns')
        response = client.publish(
            TargetArn = "arn:aws:sns:ap-southeast-1:337008671328:martin_magayanes-TOPIC-ERROR",
            Message = json.dumps({'default':notif}),
            MessageStructure = 'json'
            )
    else:
        client = boto3.client('sns')
        response = client.publish(
            TargetArn = "arn:aws:sns:ap-southeast-1:337008671328:martin_magayanes-TOPIC-CRITICAL",
            Message = json.dumps({'default':notif}),
            MessageStructure = 'json'
            )
    
    return{
    'statusCode': 200,
    'body': json.dumps(response)
    }       


def lambda_handler(event, context):
    try:
        
        send_sns(event['msg'], event['log_level'])
        
        if event['log_level'] == 'critical':
            send_email_alert(event['email'], event['msg'])
            
    except Exception as err:
        log.error(err)
        log.error(f'Event: {event}')
        return{
            'status': 400,
            'message': 'Invalid request',
        }
