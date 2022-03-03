from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr


def scan_movies(value, input_params, dynamodb=None):
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

if __name__ == '__main__':
    inp_value = 20;
    def print_movies(things):
        for entry in things:
            1
        #    print(f"\n{['year']} : {entry['title']}")
           # pprint(movie['info'])
           # pprint(movie)    print(f"Scanning for movies released from {query_range[0]} to {query_range[1]}...")
    
    test = scan_movies(inp_value, print_movies)
    ranks = []
    for index in range(0,len(test)):
        ranks.append((index,test[index]['totalscore'])) #append a tuple
    ranks.sort(key=lambda x:x[1], reverse=True)

    for element in ranks:
         print(test[element[0]])
    #print(test)
