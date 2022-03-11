from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key


def query_and_project(username, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameData')
    print(f"Get Attributes: ")

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
        ProjectionExpression="#usr, totalscore, kills",
        ExpressionAttributeNames={"#usr": "username"},
        KeyConditionExpression=
            Key('username').eq(username)
    )
    return response['Items']


if __name__ == '__main__':
    query_item = "marcus"
    print(f"Get usernames from {query_item}")
    username = query_and_project(query_item)
    print(username)
    ##we know that if no username is fetched length 0. 
    print("Username_length",len(username))
    for user in username:
        print(f"\n{user['username']} : {user['kills']}")
       # pprint(username['info'])
