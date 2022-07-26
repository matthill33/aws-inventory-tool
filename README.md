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
Have the aws account you want to take inventory of setup in your credentials 
file in your .aws folder. You need to have your access key, secrety access
key, and region setup. 

### To run: 
Navigate to "aws inventory tool" folder and run 
* py inventory.py profile
* example: I have companyA profile setup in my credentials file
* py inventory.py companyA


Can also pass arguments 'ec2', 'rds', or 'ecs' to only get data for that service
and it's own csv file.