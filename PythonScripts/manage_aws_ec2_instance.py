import boto3
import sys


class EC2Manager:
    def __init__(self, region_name='us-west-2'):
        """
        Initializes the EC2Manager with an AWS region.
        :param region_name: The AWS region where the EC2 instances are located (default is 'us-west-2').
        """
        self.region_name = region_name
        self.ec2_client = boto3.client('ec2', region_name=self.region_name)

    def start_instance(self, instance_id):
        """
        Starts an EC2 instance by its instance ID.
        :param instance_id: The ID of the EC2 instance to start.
        """
        try:
            response = self.ec2_client.start_instances(InstanceIds=[instance_id])
            print(f"Starting EC2 instance: {instance_id}")
            return response
        except Exception as e:
            print(f"Error starting instance {instance_id}: {e}")
            return None

    def stop_instance(self, instance_id):
        """
        Stops an EC2 instance by its instance ID.
        :param instance_id: The ID of the EC2 instance to stop.
        """
        try:
            response = self.ec2_client.stop_instances(InstanceIds=[instance_id])
            print(f"Stopping EC2 instance: {instance_id}")
            return response
        except Exception as e:
            print(f"Error stopping instance {instance_id}: {e}")
            return None

    def get_instance_state(self, instance_id):
        """
        Retrieves the current state of an EC2 instance.
        :param instance_id: The ID of the EC2 instance.
        :return: The state of the instance (e.g., 'running', 'stopped').
        """
        try:
            response = self.ec2_client.describe_instances(InstanceIds=[instance_id])
            state = response['Reservations'][0]['Instances'][0]['State']['Name']
            # Extract instance details
            instance = response['Reservations'][0]['Instances'][0]
            instance_state = instance['State']['Name']
            instance_type = instance['InstanceType']
            instance_launch_time = instance['LaunchTime']
            instance_id = instance['InstanceId']

            print(f"Instance ID: {instance_id}")
            print(f"State: {instance_state}")
            print(f"Instance Type: {instance_type}")
            print(f"Launch Time: {instance_launch_time}")

            # Return the instance state for further logic if needed
            return state
        except Exception as e:
            print(f"Error retrieving state for instance {instance_id}: {e}")
            return None


def main():
    print(""" MAKE SURE BELOW ENV VARS Are SET
        export AWS_ACCESS_KEY_ID=YOUR_ACCESS_KEY
        export AWS_SECRET_ACCESS_KEY=YOUR_SECRET_KEY
        export AWS_DEFAULT_REGION=us-west-1
    """)
    if len(sys.argv) != 3:
        print("Usage: python manage_ec2.py <start|stop|status> <instance_id>")
        sys.exit(1)

    action = sys.argv[1].lower()
    instance_id = sys.argv[2]

    # Initialize EC2Manager
    ec2_manager = EC2Manager(region_name='us-west-2')  # You can change the region as needed

    if action == "start":
        ec2_manager.start_instance(instance_id)
    elif action == "stop":
        ec2_manager.stop_instance(instance_id)
    elif action == "status":
        state = ec2_manager.get_instance_state(instance_id)
        if state:
            print(f"The current state of instance {instance_id} is: {state}")
    else:
        print("Invalid action. Use 'start', 'stop', or 'status'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
