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
Provide your desired region

Select the instance(s) you want to start/stop from the list

Use spacebar to select, arrow keys to navigate and Enter to execute

Enter "start", "stop" or "q" as needed.

### Take note

This tool works for standalone instances, instances associated with autoscaling groups will just be replaced when stopped. I have a tool for that also.
<a href="https://github.com/Real-Artisan/AutoSwitchingGroups">AutoSwitchingGroups</a>

### Developer
This tool was created by Daniel Pereowei Iwenya. <a href="mailto:iwenyadaniel12@gmail.com">Contact Developer.</a>
