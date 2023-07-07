### BootInstances
A tool created using Python 3 for starting or stopping EC2 instances using the instance id. 

### How to use

Install boto3
```
pip install boto3
```
Make sure your AWS credentials are set correctly with the appropriate permissions to interact with EC2 instances.

```
python3 switch.py
```
Enter "start", "stop" or "q" as needed.

### Take note

This tool works for standalone instances, instances associated with autoscaling groups will just be replaced when stopped. I will be releasing a tool for that soon.

### Developer
This tool was created by Daniel Pereowei Iwenya. <a href="mailto:iwenyadaniel@icloud.com">Contact Developer.</a>
