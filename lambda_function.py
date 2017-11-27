import boto3
import os


SNS_ARN= os.environ['SNS_ARN']


def get_bucket_list():
    bucket_list = []
    s3client = boto3.client('s3')
    response = s3client.list_buckets()
    buckets = response['Buckets']
    for bucket in buckets:
        bucket_list.append(bucket['Name'])
    return bucket_list


def send_email(unencrypted_buckets):
    str_unencrypted_buckets = ',\n'.join(unencrypted_buckets)
    snsclient = boto3.client('sns')
    snsclient.publish(
        TopicArn=SNS_ARN,
        Message='Buckets that dont have default encryption turned on:' + '\n\n' + str_unencrypted_buckets,
        Subject='S3 Buckets without Default Encryption'
    )
    return str_unencrypted_buckets

def lambda_handler(event, context):

    unencrypted_buckets = []
    encrypted_buckets = []

    s3client = boto3.client('s3')
    for bucket in get_bucket_list():
        try:
            s3client.get_bucket_encryption(
                Bucket=bucket
            )
            encrypted_buckets.append(bucket)

        except:
            unencrypted_buckets.append(bucket)

    if unencrypted_buckets:
        return send_email(unencrypted_buckets)


    else:
        return 'all buckets are encrypted'


