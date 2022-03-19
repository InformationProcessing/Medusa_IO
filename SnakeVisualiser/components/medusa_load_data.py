from decimal import Decimal
import json
import boto3

#function to read from json file.
def load_data(game_data, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('GameDataV2')
    for entry in game_data:
        username = entry['username']
        sortkey_val = entry['other_key']
        print("Adding entry:", username, sortkey_val)
        table.put_item(Item=entry)

if __name__ == '__main__':
    with open("game_entries.json") as json_file:
        game_entries = json.load(json_file, parse_float=Decimal)
    load_data(game_entries)
