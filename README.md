## s3-check-encryption

A lambda function that emails using SNS of the list of buckets that do not have the default bucket level encryption turned on. 

### Prerequisites
- At the time of writing this, boto3 on lambda by default [didnt](https://github.com/boto/boto3/issues/1340) seem to be updated to the latest version, which has the required get_bucket_encryption functionality. Kindly package boto3 manually and upload with the code. 

- Setup an SNS topic with a verified email address before running the SAM template. Keep the topic name and arn handy.

### The SAM template creates the following resources:
- 1 Lambda Function, python 2.7 with 1 environment variable(SNS ARN)
- 1 IAM Role with 3 Policies


### High level flow
Once set up, this would work as follows:

- When triggered(manually or via cloudwatch cron), this function will list the s3 buckets on the account, check which ones have default bucket encryption turned on and then send an email using SNS of the list of buckets that do not have encryption turned on.

### Additional Considerations/Limitations

- 


