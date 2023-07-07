import boto3

def start_ec2_instance(instance_id):
    ec2_client = boto3.client('ec2')
    ec2_client.start_instances(InstanceIds=[instance_id])
    print("Started EC2 instance: {instance_id}")

def stop_ec2_instance(instance_id):
    ec2_client = boto3.client('ec2')
    ec2_client.stop_instances(InstanceIds=[instance_id])
    print("Stopped EC2 instance: {instance_id}")

# Interactive CLI
def interactive_cli():
    while True:
        action = input("Enter 'start' to start an instance, 'stop' to stop an instance, or 'q' to quit: ")

        if action == 'start':
            instance_id = input("Enter the instance ID to start: ")
            start_ec2_instance(instance_id)
        elif action == 'stop':
            instance_id = input("Enter the instance ID to stop: ")
            stop_ec2_instance(instance_id)
        elif action == 'q':
            print("Exiting the program...")
            break
        else:
            print("Invalid input. Please try again.")

# Run the interactive CLI
interactive_cli()
