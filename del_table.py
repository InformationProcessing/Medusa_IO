import boto3

def delete_GameData(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name="us-east-1")

    table = dynamodb.Table('GameData')
    table.delete()


if __name__ == '__main__':
    delete_GameData()
    print("Game Data table deleted.")
