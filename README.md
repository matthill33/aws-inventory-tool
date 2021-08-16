# AWS Inventory Tool

### Description:
AWS inventory tool to quickly summarize the infrastructure of any AWS account.
Makes real-time calls to boto3 (aws sdk) to get cloudwatch metric data. 
Creates and launches CSV file for reporting. 
Uses a static pricing file (pricing.py) to get cost estimates. 

### Dependencies: 
Python, boto3, pandas, and tabulate
* pip install boto3
* pip install pandas
* pip install tabulate

### Prerequisites: 
Use "aws configure" in terminal and enter in an access key and secret
access key of the account that you want to take inventory of. 

### To run: 
Navigate to "aws inventory tool" folder and run 
* py inventory.py


Can also pass arguments 'ec2', 'rds', or 'ecs' to only get data for that service
and it's own csv file.