import json
import boto3
import urllib.parse
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FileMetadata')

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(record['s3']['object']['key'])
        size = record['s3']['object']['size']

        # Get metadata
        s3 = boto3.client('s3')
        head = s3.head_object(Bucket=bucket_name, Key=key)
        content_type = head.get('ContentType', 'Unknown')
        last_modified = head.get('LastModified', datetime.utcnow())

        # Save to DynamoDB
        table.put_item(
            Item={
                'FileName': key,
                'Size': size,
                'ContentType': content_type,
                'UploadTimestamp': last_modified.isoformat()
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Metadata stored successfully!')
    }
