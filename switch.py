import boto3
import inquirer

# Function to get a list of EC2 instances in the specified region with their names
def get_ec2_instances(region):
    ec2_client = boto3.client('ec2', region_name=region)
    instances = ec2_client.describe_instances()
    instance_list = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_name = ""
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
            instance_list.append(f"{instance_name} ({instance_id})")

    return instance_list

# Function to start an EC2 instance
def start_ec2_instance(region, instance_id):
    ec2_client = boto3.client('ec2', region_name=region)
    ec2_client.start_instances(InstanceIds=[instance_id])
    print(f"Started EC2 instance: {instance_id}")

# Function to stop an EC2 instance
def stop_ec2_instance(region, instance_id):
    ec2_client = boto3.client('ec2', region_name=region)
    ec2_client.stop_instances(InstanceIds=[instance_id])
    print(f"Stopped EC2 instance: {instance_id}")

# Main function for interactive CLI
def interactive_cli():
    region = input("Enter the AWS region (e.g., us-east-1): ")
    instance_ids = get_ec2_instances(region)

    if not instance_ids:
        print("No EC2 instances found in the specified region.")
        return

    instance_choices = [{'name': instance} for instance in instance_ids]

    questions = [
        inquirer.Checkbox('selected_instances', message="Select EC2 instances to start/stop:",
                          choices=instance_choices),
    ]

    answers = inquirer.prompt(questions)

    if 'selected_instances' not in answers:
        print("No instances selected.")
        return

    selected_instances = answers['selected_instances']

    action = input("Enter 'start' to start selected instances, 'stop' to stop them, or 'q' to quit: ")
    if action == 'start':
        for selected_instance in selected_instances:
            instance_id = selected_instance.split(" (")[1][:-1]  # Extracting the instance ID from the selection
            start_ec2_instance(region, instance_id)
    elif action == 'stop':
        for selected_instance in selected_instances:
            instance_id = selected_instance.split(" (")[1][:-1]  # Extracting the instance ID from the selection
            stop_ec2_instance(region, instance_id)
    elif action == 'q':
        print("Exiting the program...")
    else:
        print("Invalid input. Please try again.")

# Run the interactive CLI
if __name__ == "__main__":
    interactive_cli()
