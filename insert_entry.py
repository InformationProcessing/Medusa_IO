from pprint import pprint
import boto3

def insert_entry(username, totalscore, kills, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameData')
    response = table.put_item(
       Item={
            "username": username,
            "other_key": "a75",
            "totalscore":totalscore,
            "kills":kills
        }

    )
    return response

if __name__ == '__main__':
    movie_resp = insert_entry("jwickerson", 787,511)
    print("Put movie succeeded:")
    pprint(movie_resp)
