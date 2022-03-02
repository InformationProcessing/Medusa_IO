from decimal import Decimal
import json
import boto3

#function to read from json file.
def load_data(game_data, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('GameData')
    for entry in game_data:
        username = game_data['username']
        totalscore = int(game_data['totalscore'])
        print("Adding entry:", username, totalscore)
        table.put_item(Item=game_data)
if __name__ == '__main__':
    with open("game_entries.json") as json_file:
        game_entries = json.load(json_file, parse_float=Decimal)
    load_data(game_entries)
