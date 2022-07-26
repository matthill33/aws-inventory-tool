import sys
import math
import boto3
from datetime import date, datetime, timedelta
from pricing import getEC2Price

# Helper functions that ec2.py calls
# Retreives cloudwatch data with boto3 and pricing info from pricing.py

# time data used for StartTime and EndTime boto3 parameters
today = datetime.now().strftime("%Y-%m-%d")
monthAgo = (date.today() - timedelta(30)).strftime("%Y-%m-%d")
sixMonthsAgo = (date.today() - timedelta(180)).strftime("%Y-%m-%d")

profile = sys.argv[1]
session = boto3.Session(profile_name = profile)
cloudwatch = session.client('cloudwatch')

def get30DayCPUAverage(instanceId):
    output = cloudwatch.get_metric_statistics(Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name':'InstanceId','Value': instanceId},],
    StartTime=monthAgo,
    EndTime=today,
    Period=2592000,
    Statistics=['Average'])
    avg = ('%.5s' % output['Datapoints'][0]['Average']) # format to 5 chars
    return avg

def get180DayCPUAverage(instanceId):
    output = cloudwatch.get_metric_statistics(Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name':'InstanceId','Value': instanceId},],
    StartTime=sixMonthsAgo,
    EndTime=today,
    Period=15552000,
    Statistics=['Average'])
    avg = ('%.5s' % output['Datapoints'][0]['Average']) # format to 5 chars
    return avg

def get30DayCPUMax(instanceId):
    output = cloudwatch.get_metric_statistics(Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name':'InstanceId','Value': instanceId},],
    StartTime=monthAgo,
    EndTime=today,
    Period=2592000,
    Statistics=['Maximum'])
    maxCPU = ('%.5s' % output['Datapoints'][0]['Maximum']) # format to 5 chars
    return maxCPU

def get180DayCPUMax(instanceId):
    output = cloudwatch.get_metric_statistics(Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[{'Name':'InstanceId','Value': instanceId},],
    StartTime=monthAgo,
    EndTime=today,
    Period=15552000,
    Statistics=['Maximum'])
    maxCPU = ('%.5s' % output['Datapoints'][0]['Maximum']) # format to 5 chars
    return maxCPU

# any errors associated with this function probabably mean that you
# need to add the instance price to the correct pricing.py dict
def get30DayPrice(type):
    demandHourlyPrice = getEC2Price(type) 
    if demandHourlyPrice is None:
        return 'add price to pricing.py'
    else:
        demandHourlyPrice = demandHourlyPrice*720
    demandHourlyPrice = round(demandHourlyPrice, 2)
    return demandHourlyPrice

# any errors associated with this function probabably mean that you
# need to add the instance price to the correct pricing.py dict
def getYearPrice(type):
    demandHourlyPrice = getEC2Price(type)
    if demandHourlyPrice is None:
        return 'add price to pricing.py'
    else:
        demandHourlyPrice = demandHourlyPrice*8760
    demandHourlyPrice = round(demandHourlyPrice, 2)
    return demandHourlyPrice

def getNameTag(arrOfTags):
    arrSize = len(arrOfTags)
    if(arrSize == 0): # check if there are no tags, return hyphen
        return "-"
    for i in range(0, arrSize): # loop through tag keys and check for Name
        if(arrOfTags[i]['Key'] == 'Name'):
            nameTag = arrOfTags[i]['Value']
            return nameTag[:30]
    return "-" #there are no tags, return hyphen 

def getTotalRow(arrOf30DayPrices, arrOfYearPrices):
    sum30 = 0
    sumYear = 0
    for i in arrOf30DayPrices:
        sum30+=i
    for j in arrOfYearPrices:
        sumYear+=j

    sum30 = round(sum30, 2)
    sum30 = "{:0,.2f}".format(float(sum30)) # format for output with commas

    sumYear = round(sumYear, 2)
    sumYear = "{:0,.2f}".format(float(sumYear)) # format for output with commas

    return ({'Name' :'Total', 'Id' : '-','Type' :'-', '30-Day CPU Avg %' : '-',
    '6 Month CPU Avg %' : '-','30-Day CPU Max %' : '-','6 Month CPU Max %' : '-',
    '30-Day Cost' : sum30,'Year Cost' : sumYear,'Date Launched' : '-'})