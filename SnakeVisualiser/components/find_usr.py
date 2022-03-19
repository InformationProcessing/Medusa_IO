from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_user(username, sort_key, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameDataV2')

    try:
        response = table.get_item(Key={'username': username, 'other_key': sort_key})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    user_info = get_user("jjo", "a75")
    print(len(user_info))
    if user_info:
        print("get_user worked")
        pprint(user_info)
    else:
        print("nope")
