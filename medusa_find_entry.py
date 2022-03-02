from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_user(username, totalscore, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameData')

    try:
        response = table.get_item(Key={'username': username, 'totalscore': totalscore})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    user_info = get_user("jjo", 81)
    if user_info:
        print("get_user worked")
        pprint(user_info)
    else:
        print("nope")
