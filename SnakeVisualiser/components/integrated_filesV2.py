from pprint import pprint
import boto3
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key, Attr
from decimal import Decimal
import socket

def query_and_project(username, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameDataV2')
    #print(f"Get Attributes: ")

    # Expression attribute names can only reference items in the projection expression.
    response = table.query(
        ProjectionExpression="#usr, totalscore, highestscore, kills",
        ExpressionAttributeNames={"#usr": "username"},
        KeyConditionExpression=
            Key('username').eq(username)
    )
    return response['Items']


def update_entry(username, score, highestscore, killcount, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameDataV2')

    response = table.update_item(
        Key={
            'username': username,
            'other_key': "a75"
        },
        UpdateExpression="set totalscore =:s, highestscore =:h, kills =:k",
        ExpressionAttributeValues={
            ':s': Decimal(score),
            ':h': Decimal(highestscore),
            ':k': killcount,
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

def insert_entry(username, totalscore, highestscore, kills, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameDataV2')
    response = table.put_item(
       Item={
            "username": username,
            "other_key": "a75",
            "totalscore":totalscore,
            "highestscore":highestscore,
            "kills":kills
        }

    )
    return response

def scan_totalscore(value, input_params, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameDataV2')

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

def scan_highestscore(value, input_params, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('GameDataV2')

    #scan and get the first page of results
    response = table.scan(FilterExpression=Attr('highestscore').gt(value));
    data = response['Items']
    input_params(data)

    #continue while there are more pages of results
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
        input_params(data)

    return data


def return_totalscore_leaderboard(inp_val, dyanmodb=None): 
    def print_movies(things):
        for entry in things:
            1
    
    test = scan_totalscore(inp_val, print_movies)
    ranks = []
    top_rank = []
    for index in range(0,len(test)):
        ranks.append((index,test[index]['totalscore'])) #append a tuple
    ranks.sort(key=lambda x:x[1], reverse=True)
    i = 1
    print("Total: Leaderboard and Rank")
    for element in ranks:
         top_rank.append(test[element[0]])
         print(i,test[element[0]])
         i+=1
    return top_rank

def return_highestscore_leaderboard(inp_val, dyanmodb=None):
    def print_movies(things):
        for entry in things:
            1

    test = scan_highestscore(inp_val, print_movies)
    ranks = []
    top_rank = []
    for index in range(0,len(test)):
        ranks.append((index,test[index]['highestscore'])) #append a tuple
    ranks.sort(key=lambda x:x[1], reverse=True)
    i = 1
    print("Highest: Leaderboard and Rank")
    for element in ranks:
         top_rank.append(test[element[0]])
         print(i,test[element[0]])
         i+=1
    return top_rank


if __name__ == '__main__':

    print("EC2 SERVER..")
    
    server_port = 13000
    welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    welcome_socket.bind(('0.0.0.0', server_port))
    welcome_socket.listen(1)
    print("Serverport: ", server_port)

    while True:
        connection_socket, caddr = welcome_socket.accept()
        cmsg = connection_socket.recv(4096)
        test_str = cmsg.decode()
        split_str = test_str.split(";")

       # print(split_str)
        for entry in split_str:
            tmp = entry.split(",")
            print(tmp)
            user = tmp[0].strip()
            #print(user)
            #print("User is",user)
            curr_val = query_and_project(str(user))
            #print(len(curr_val))
            #print(curr_val)
            points = int(tmp[2])
            highestscore = points
            kills = int(tmp[3])
            if len(curr_val)>0:
                info = curr_val[0]
                #print("Current Value",curr_val)
                #print("Information",info)
                #defining element 3 as kills and 4 as score.
                points += info["totalscore"]
                kills += info["kills"]
                #print(info)
                if highestscore > info["highestscore"]: 
                    update_entry(str(user),points,highestscore,kills)
                else:
                    update_entry(str(user),points,info["highestscore"],kills)
            else:
                insert_entry(str(user),points,highestscore,kills)
        
        ar1 = return_totalscore_leaderboard(0)
        ar2 = return_highestscore_leaderboard(0)

        send_str = ""
        for i in ar1:
            send_str += str(i)
            send_str += ';'
        send_str += '|'
        for i in ar2:
            send_str += str(i)
            send_str += ';'
        
        print(send_str)
        connection_socket.send(send_str.encode())
    
    """
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
    """
        


            




