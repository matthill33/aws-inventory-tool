import sys
import boto3
import math 
import pandas as pd 
from datetime import date, datetime, timedelta
from rdsHelpers import *
from tabulate import tabulate

profile = sys.argv[1]
session = boto3.Session(profile_name = profile)
rds = session.client('rds')
data = rds.describe_db_instances()
numRunningInstances = len(data['DBInstances'])

# Return arrays for formatted display
arrOfIdentifiers = []
arrOfEngines = []
arrOfDBInstanceClass = []
arrOf30CPUAvgs = []
arrOf30ConnectionsAvgs = []
arrOf30WritesAvgs = []
arrOf30ReadsAvgs = []
arrOf30DayPrices = []
arrOfYearPrices = []
arrOfDatesLaunched = []
 
# loop through all rds data and populate return arrays
for i in range(0,numRunningInstances):

    allInstanceData = data['DBInstances'][i]
    launched = allInstanceData['InstanceCreateTime'] 
    dateLaunched = launched.strftime('%b %d %Y') # format date for output  
    identifier = allInstanceData['DBInstanceIdentifier']
    engine = allInstanceData['Engine']
    dbInstanceClass = allInstanceData['DBInstanceClass']
    multiAZ = allInstanceData['MultiAZ']
    cpu30DayAvg = get30DayRDSCPUAverage(identifier,engine)
    connection30DayAvg = get30DayRDSConnectionAverage(identifier,engine)
    write30DayAvg = get30DayRDSWriteAverage(identifier,engine)
    read30DayAvg = get30DayRDSReadAverage(identifier,engine)
    thirtyDayPrice = get30DayPrice(engine, dbInstanceClass, multiAZ)
    yearPrice = getYearPrice(engine, dbInstanceClass, multiAZ)

    # append current instance data to return arrays
    arrOfIdentifiers.append(identifier)
    arrOfEngines.append(engine)
    arrOfDBInstanceClass.append(dbInstanceClass)
    arrOf30CPUAvgs.append(cpu30DayAvg)
    arrOf30ConnectionsAvgs.append(connection30DayAvg)
    arrOf30WritesAvgs.append(write30DayAvg)    
    arrOf30ReadsAvgs.append(read30DayAvg)
    arrOf30DayPrices.append(thirtyDayPrice)
    arrOfYearPrices.append(yearPrice)    
    arrOfDatesLaunched.append(dateLaunched)    

def getNumRDSInstances():
    return numRunningInstances

def formatRDSData():
    formatData = {'Identifier' : arrOfIdentifiers,
                  'Engine' : arrOfEngines,
                  'Instance Class' : arrOfDBInstanceClass,
                  '30-Day cpu av %' : arrOf30CPUAvgs,
                  '30-Day connection' : arrOf30ConnectionsAvgs,
                  '30-Day WIOPS/sec' : arrOf30WritesAvgs,
                  '30-Day RIOPS/sec' : arrOf30ReadsAvgs,
                  '30-Day cost' : arrOf30DayPrices,
                  'Year cost' : arrOfYearPrices,
                  'Date Launched' : arrOfDatesLaunched}
    
    df = pd.DataFrame(formatData)

    # append total row if there are any running instances
    if numRunningInstances > 0:
        totalRow = getTotalRow(arrOf30DayPrices, arrOfYearPrices)    
        df.loc[' '] = totalRow
        formattedTable = tabulate(df, headers = 'keys', tablefmt = 'pretty')
        return formattedTable, df
        # mod_df = df.append(totalRow, ignore_index=True)
        # formattedTable = tabulate(mod_df, headers = 'keys', tablefmt = 'pretty')
        # return formattedTable, mod_df
    else:
        formattedTable = tabulate(df, headers = 'keys', tablefmt = 'pretty')
        return formattedTable, df