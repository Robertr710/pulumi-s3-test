import pulumi
import pulumi_aws as aws

# Create an S3 bucket
current_stack = pulumi.get_stack()
bucket = aws.s3.Bucket(current_stack + '-bucket')

# Export the bucket name
pulumi.export('bucket_name', bucket.id)
