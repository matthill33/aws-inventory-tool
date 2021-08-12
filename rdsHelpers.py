import math
import boto3
from datetime import date, datetime, timedelta, timezone
from pricing import getRDSPrice

# Helper functions that rds.py calls
# Retreives cloudwatch data with boto3 and pricing info from pricing.py

# time data used for StartTime and EndTime boto3 parameters
today = datetime.now().strftime("%Y-%m-%d")
monthAgo = (date.today() - timedelta(30)).strftime("%Y-%m-%d")
sixMonthsAgo = (date.today() - timedelta(180)).strftime("%Y-%m-%d")

cloudwatch = boto3.client('cloudwatch')

def get30DayRDSCPUAverage(id,engine):
    # add docdb compatibility
    if engine == 'docdb':
        eng = 'DocDB'
    else:
        eng = 'RDS'
    output = cloudwatch.get_metric_statistics(Namespace='AWS/'+eng,
    MetricName='CPUUtilization',
    Dimensions=[{'Name':'DBInstanceIdentifier','Value': id},],
    StartTime=monthAgo,
    EndTime=today,
    Period=2592000,
    Statistics=['Average'])
    avg = ('%.5s' % output['Datapoints'][0]['Average'])
    return avg

def get30DayRDSConnectionAverage(id,engine):
    # add docdb compatibility
    if engine == 'docdb':
        eng = 'DocDB'
    else:
        eng = 'RDS'
    output = cloudwatch.get_metric_statistics(Namespace='AWS/'+eng,
    MetricName='DatabaseConnections',
    Dimensions=[{'Name':'DBInstanceIdentifier','Value': id},],
    StartTime=monthAgo,
    EndTime=today,
    Period=2592000,
    Statistics=['Average'])
    avg = ('%.5s' % output['Datapoints'][0]['Average'])
    return avg

def get30DayRDSWriteAverage(id,engine):
    # add docdb compatibility
    if engine == 'docdb':
        eng = 'DocDB'
    else:
        eng = 'RDS'
    output = cloudwatch.get_metric_statistics(Namespace='AWS/'+eng,
    MetricName='WriteIOPS',
    Dimensions=[{'Name':'DBInstanceIdentifier','Value': id},],
    StartTime=monthAgo,
    EndTime=today,
    Period=2592000,
    Statistics=['Average'])
    avg = ('%.5s' % output['Datapoints'][0]['Average'])
    return avg

def get30DayRDSReadAverage(id,engine):
    # add docdb compatibility
    if engine == 'docdb':
        eng = 'DocDB'
    else:
        eng = 'RDS'
    output = cloudwatch.get_metric_statistics(Namespace='AWS/'+eng,
    MetricName='ReadIOPS',
    Dimensions=[{'Name':'DBInstanceIdentifier','Value': id},],
    StartTime=monthAgo,
    EndTime=today,
    Period=2592000,
    Statistics=['Average'])
    avg = ('%.5s' % output['Datapoints'][0]['Average'])
    return avg


# If this function errors it it most likely becuase the db type/engine is not listed on 
# the pricing.py file. Add to type/engine type to file, change the getRDSPrice function appropriately 
# and it should work. Make sure that the engine name is the correct engine name returned by the CLI
def get30DayPrice(engine, instanceClass, multi):
    demandHourlyPrice = getRDSPrice(engine, instanceClass, multi)
    if demandHourlyPrice is None:
        return 'add price to pricing.py'
    else:
        demandHourlyPrice = demandHourlyPrice*720
    demandHourlyPrice = round(demandHourlyPrice, 2)
    return demandHourlyPrice

# If this function errors it it most likely becuase the db type/engine is not listed on 
# the pricing.py file. Add to type/engine type to file, change the getRDSPrice function appropriately 
# and it should work. Make sure that the engine name is the correct engine name returned by the CLI
def getYearPrice(engine, instanceClass, multi):
    demandHourlyPrice = getRDSPrice(engine, instanceClass, multi)
    if demandHourlyPrice is None:
        return 'add price to pricing.py'
    else:
        demandHourlyPrice = demandHourlyPrice*8760
    demandHourlyPrice = round(demandHourlyPrice, 2)
    return demandHourlyPrice

def getTotalRow(arrOf30DayPrices, arrOfYearPrices):
    sum30 = 0
    sumYear = 0
    for i in arrOf30DayPrices:
        sum30+=i
    for j in arrOfYearPrices:
        sumYear+=j

    # format for output
    sum30 = round(sum30, 2)
    sum30 = "{:0,.2f}".format(float(sum30))

    # format for output
    sumYear = round(sumYear, 2)
    sumYear = "{:0,.2f}".format(float(sumYear))

    return ({'DB Identifier' :'Total', 'Engine' : '-','Instance Class' :'-',
    '30-Day CPU Avg (%)' : '-','30-Day Connection/Sec Avg' : '-','30-Day WriteIOPS/Sec Avg' : '-',
    '30-Day ReadIOPS/Sec Avg' : '-','30-Day Cost ($)' : sum30,'Year Cost ($)' : sumYear,
    'Date Launched' : '-'})