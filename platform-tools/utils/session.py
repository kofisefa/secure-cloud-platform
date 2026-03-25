import boto3


def get_client(service, region="us-east-2"):
    return boto3.client(service, region_name=region)