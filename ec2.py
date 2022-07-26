import sys
import boto3
import math 
import pandas as pd 
from datetime import date, datetime, timedelta, timezone
from ec2Helpers import *
from tabulate import tabulate

profile = sys.argv[1]
session = boto3.Session(profile_name = profile)
ec2 = session.client('ec2')
data = ec2.describe_instances(Filters=[{'Name': 'instance-state-code','Values': ['16']},])
numRunningInstances = len(data['Reservations'])

# Return arrays for formatted display
arrOfNames = []
arrOfIds = []
arrOfTypes = []
arrOf30CPUAvgs = []
arrOf180CPUAvgs = []
arrOf30CPUMaxs = []
arrOf180CPUMaxs = []
arrOf30DayPrices = []
arrOfYearPrices = []
arrOfDatesLaunched = []
 
# loop through all ec2 data and populate return arrays
for i in range(0,numRunningInstances):

    current = datetime.now(timezone.utc)
    allInstanceData = data['Reservations'][i]['Instances'][0]
    launched = allInstanceData['LaunchTime'] # get date launched
    dateLaunched = launched.strftime('%b %d %Y') # format date for output   
    timeRunning = current-launched # see how long instance has been running

    instanceId = allInstanceData['InstanceId']
    nameTag = getNameTag(allInstanceData['Tags'])
    instanceType = allInstanceData['InstanceType']
    thirtyDayPrice = get30DayPrice(instanceType)
    yearPrice = getYearPrice(instanceType)  

    if timeRunning.days < 1: # instances need to be running for at least 1 day to get metrics
        cpu30DayAvg = '-'
        cpu180DayAvg = '-'
        cpu30DayMax = '-'
        cpu180DayMax = '-'
    else:
        cpu30DayAvg = get30DayCPUAverage(instanceId)
        cpu180DayAvg = get180DayCPUAverage(instanceId)
        cpu30DayMax = get30DayCPUMax(instanceId)
        cpu180DayMax = get180DayCPUMax(instanceId)

    # append current instance data to return arrays
    arrOfNames.append(nameTag)
    arrOfIds.append(instanceId)
    arrOfTypes.append(instanceType)
    arrOf30CPUAvgs.append(cpu30DayAvg)
    arrOf180CPUAvgs.append(cpu180DayAvg)
    arrOf30CPUMaxs.append(cpu30DayMax)
    arrOf180CPUMaxs.append(cpu180DayMax)
    arrOf30DayPrices.append(thirtyDayPrice)
    arrOfYearPrices.append(yearPrice)
    arrOfDatesLaunched.append(dateLaunched)    

def getNumEC2Instances():
    return numRunningInstances

def formatEC2Data():
    formatData = {'Name' : arrOfNames,
                  'Id' : arrOfIds,
                  'Type' : arrOfTypes,
                  '30-Day CPU Avg %' : arrOf30CPUAvgs,
                  '6 Month CPU Avg %' : arrOf180CPUAvgs,
                  '30-Day CPU Max %' : arrOf30CPUMaxs,
                  '6 Month CPU Max %' : arrOf180CPUMaxs,
                  '30-Day Cost' : arrOf30DayPrices,
                  'Year Cost' : arrOfYearPrices,
                  'Date Launched' : arrOfDatesLaunched}

    df = pd.DataFrame(formatData) # create pandas dataframe with retrieved data

    # append total row if there are running instances
    if numRunningInstances > 0:
        totalRow = getTotalRow(arrOf30DayPrices, arrOfYearPrices)
        # mod_df = df.append(totalRow, ignore_index=True)
        # formattedTable = tabulate(mod_df, headers = 'keys', tablefmt = 'pretty')
        # return formattedTable, mod_df
        df.loc[' '] = totalRow
        formattedTable = tabulate(df, headers = 'keys', tablefmt = 'pretty')
        return formattedTable, df

    else:
        formattedTable = tabulate(df, headers = 'keys', tablefmt = 'pretty')
        return formattedTable, df

