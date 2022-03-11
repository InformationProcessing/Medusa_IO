from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr


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

    for element in ranks:
         top_rank.append(test[element[0]])
         print(test[element[0]])
    return top_rank



if __name__ == '__main__':
    inp_value = 20
    return_leaderboard(inp_value)
    #print(test)
