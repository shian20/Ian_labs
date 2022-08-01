import logging
import random
import uuid
from datetime import datetime, timezone
from decimal import Decimal
from pathlib import Path, PosixPath
import boto3
import operator as op
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
logging.basicConfig(
        level=logging.INFO,
        format='[%(asctime)s] %(levelname)s %(module)s %(lineno)d - %(message)s',)
log = logging.getLogger()

def create_sns_topic(topic_name):
    sns = boto3.client('sns')
    sns.create_topic(Name=topic_name)
    return True
    
    
def list_sns_topics(next_token=None):
    sns = boto3.client('sns')
    params = {'NextToken': next_token} if next_token else {}
    topics = sns.list_topics(**params)
    return topics.get('Topics', []), topics.get('NextToken', None)
    
    
def list_sns_subscriptions(next_token=None):
    sns = boto3.client('sns')
    params = {'NextToken': next_token} if next_token else {}
    subscriptions = sns.list_subscriptions(**params)
    return subscriptions.get('Subscriptions', []), subscriptions.get('NextToken', None)
    
    
def subscribe_sns_topic(topic_arn, email_address):
    sns = boto3.client('sns')
    params = {
        'TopicArn': topic_arn,
        'Protocol': 'email',
        'Endpoint': email_address,
    }
    res = sns.subscribe(**params)
    print(res)
    return True
    
    
def send_sns_message(topic_arn, message):
    sns = boto3.client('sns')
    params = {
        'TopicArn': topic_arn,
        'Message': message,
    }
    res = sns.publish(**params)
    print(res)
    return True
    

def unsubscribe_sns_topic(subscription_arn):
    sns = boto3.client('sns')
    params = {
        'SubscriptionArn': subscription_arn,
    }
    res = sns.unsubscribe(**params)
    print(res)
    return True
    
    
def delete_sns_topic(topic_arn):
    # This will delete the topic and all it's subscriptions.
    sns = boto3.client('sns')
    sns.delete_topic(TopicArn=topic_arn)
    return True
    
if __name__ == '__main__':
    """
    log.info(list_sns_topics())
    
    log.info(create_sns_topic('ian-debug'))
    
    log.info(create_sns_topic('ian-info'))
    
    log.info(create_sns_topic('ian-warning'))
    
    log.info(create_sns_topic('ian-error'))
    
    log.info(create_sns_topic('ian-critical'))
    
    log.info(list_sns_topics())
    
    log.info(list_sns_subscriptions())
    
    sns_subs_topic = subscribe_sns_topic('arn:aws:sns:us-east-1:337008671328:ian-debug','+639176884454')
    
    sns_subs_topic = subscribe_sns_topic('arn:aws:sns:us-east-1:337008671328:ian-info','+639176884454')
    """
    sns_subs_topic = subscribe_sns_topic('arn:aws:sns:us-east-1:337008671328:ian-critical','adrian.arcilla@globe.com.ph')
    """
    sns_subs_topic = subscribe_sns_topic('arn:aws:sns:us-east-1:337008671328:ian-error','+639176884454')
    
    sns_subs_topic = subscribe_sns_topic('arn:aws:sns:us-east-1:337008671328:ian-warning','+639176884454')
     
    
    log.info(f'{sns_subs_topic}')

    sns_list_subs = list_sns_subscriptions()
    log.info(f'{sns_list_subs}')
    
    sns_sms_message = send_sns_message('arn:aws:sns:ap-southeast-1:337008671328:price_updates-ian', 'Woo Hoodies are no 50% off!')
    log.info(f'{sns_sms_message}')
    
    log.info(list_sns_subscriptions())
    sns_unsubs_topic = unsubscribe_sns_topic('arn:aws:sns:ap-southeast-1:337008671328:price_updates-ian:2d43d82a-3247-457b-9d34-79d4cbd07a3b')
    log.info(f'{sns_unsubs_topic}')
    
    log.info(list_sns_subscriptions())
    sns_delete_topic = delete_sns_topic('arn:aws:sns:ap-southeast-1:337008671328:price_updates-ian')
    
    """
    
    
    
    