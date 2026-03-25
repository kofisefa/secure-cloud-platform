import boto3

cw = boto3.client('cloudwatch', region_name='us-east-2')
ec2 = boto3.client('ec2', region_name='us-east-2')
logs = boto3.client('logs', region_name='us-east-2')

def get_active_alarms():
    return cw.describe_alarms(StateValue='ALARM')['MetricAlarms']

def get_instance_state(instance_id):
    res = ec2.describe_instances(InstanceIds=[instance_id])
    return res['Reservations'][0]['Instances'][0]['State']['Name']

def get_cpu_metric(instance_id):
    res = cw.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime='2024-01-01T00:00:00Z',
        EndTime='2030-01-01T00:00:00Z',
        Period=300,
        Statistics=['Average']
    )
    datapoints = res['Datapoints']
    if datapoints:
        return sorted(datapoints, key=lambda x: x['Timestamp'])[-1]['Average']
    return "N/A"

def run():
    alarms = get_active_alarms()

    if not alarms:
        print("No active alarms.")
        return

    for alarm in alarms:
        instance_id = alarm['Dimensions'][0]['Value']

        state = get_instance_state(instance_id)
        cpu = get_cpu_metric(instance_id)

        print("\n===== INCIDENT DETECTED =====")
        print(f"Alarm: {alarm['AlarmName']}")
        print(f"Instance: {instance_id}")
        print(f"State: {state}")
        print(f"CPU: {cpu}")
        print("============================\n")

if __name__ == "__main__":
    run()