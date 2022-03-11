from decimal import Decimal
from pprint import pprint
import boto3


def update_entry(username, score, killcount, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameData')

    response = table.update_item(
        Key={
            'username': username,
            'other_key': "a75"
        },
        UpdateExpression="set totalscore =:s, kills =:k",
        ExpressionAttributeValues={
            ':s': Decimal(score),
            ':k': killcount,
        },
        ReturnValues="UPDATED_NEW"
    )
    return response


if __name__ == '__main__':
    update_response = update_entry("lollycraft", 49,35)
    print("Update Entry succeeded:")
    pprint(update_response)
