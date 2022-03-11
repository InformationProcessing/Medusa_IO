from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal
def query_and_project(username, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameData')
    #print(f"Get Attributes: ")

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
        ProjectionExpression="#usr, totalscore, kills",
        ExpressionAttributeNames={"#usr": "username"},
        KeyConditionExpression=
            Key('username').eq(username)
    )
    return response['Items']


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

def scan_data(value, input_params, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameData')

    #scan and get the first page of results
    response = table.scan(FilterExpression=Attr('totalscore').gt(value));
    data = response['Items']
    input_params(data)

    #continue while there are more pages of results
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
        input_params(data)

    return data

def return_leaderboard(inp_val, dyanmodb=None): 
    def print_movies(things):
        for entry in things:
            1
    
    test = scan_data(inp_val, print_movies)
    ranks = []
    top_rank = []
    for index in range(0,len(test)):
        ranks.append((index,test[index]['totalscore'])) #append a tuple
    ranks.sort(key=lambda x:x[1], reverse=True)
    i = 1
    print("Leaderboard and Rank")
    for element in ranks:
         top_rank.append(test[element[0]])
         print(i,test[element[0]])
         i+=1
    return top_rank


if __name__ == '__main__':
    test_str = "Matthew,a75,15,21; James,a75,15,21; jjo,a75,0,29"
    split_str = test_str.split(";")

   # print(split_str)
    for entry in split_str:
        tmp = entry.split(",")
       # print(tmp)
        user = tmp[0].strip()
        #print(user)
        #print("User is",user)
        curr_val = query_and_project(str(user))
        #print(len(curr_val))
        #print(curr_val)
        points = int(tmp[2])
        kills = int(tmp[3])
        if len(curr_val)>0:
            info = curr_val[0]
            #print("Current Value",curr_val)
            #print("Information",info)
            #defining element 3 as kills and 4 as score.
            points += info["totalscore"]
            kills += info["totalscore"]
            update_entry(str(user),points,kills)
        else:
            insert_entry(str(user),kills,points)
    return_leaderboard(15)

        


            




