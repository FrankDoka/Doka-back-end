import json, boto3

client = boto3.client('dynamodb')
TableName = 'cloud-resume-stat-test'

def lambda_handler(event, context):
    
    '''
    data = client.get_item(
        TableName='cloud-resume-stats-test',
        Key = {
            'stat': {'S': 'view-count'}
        }
    )
    '''
    
    #data['Item']['Quantity']['N'] = str(int(data['Item']['Quantity']['N']) + 1)
    
    response = client.update_item(
        TableName='cloud-resume-stats-test',
        Key = {
            'stat': {'S': 'view-count'}
        },
        UpdateExpression = 'ADD Quantity :inc',
        ExpressionAttributeValues = {":inc" : {"N": "1"}},
        ReturnValues = 'UPDATED_NEW'
        )
        
    value = response['Attributes']['Quantity']['N']
    
    return {      
            'statusCode': 200,
            'body': value}