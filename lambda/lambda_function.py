import json
import boto3

cw = boto3.client('cloudwatch')
ec2 = boto3.client('ec2')

def get_instance_state(instance_id):
    res = ec2.describe_instances(InstanceIds=[instance_id])
    return res['Reservations'][0]['Instances'][0]['State']['Name']

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    # SNS message parsing
    message = json.loads(event['Records'][0]['Sns']['Message'])

    alarm_name = message['AlarmName']
    instance_id = message['Trigger']['Dimensions'][0]['value']

    state = get_instance_state(instance_id)

    report = {
        "incident": alarm_name,
        "instance": instance_id,
        "state": state
    }

    print("===== INCIDENT DETECTED =====")
    print(json.dumps(report, indent=2))
    print("============================")

    return {
        'statusCode': 200,
        'body': json.dumps(report)
    }