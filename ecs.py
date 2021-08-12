import boto3
import math 
import pandas as pd 
from tabulate import tabulate
from datetime import date, datetime, timedelta

ecs = boto3.client('ecs')
clusterList = ecs.list_clusters()
numRunningClusters = len(clusterList['clusterArns'])

clusterArns = (clusterList['clusterArns'])
clusterNames = []
serviceNames = []

for i in clusterArns:
    output = i.split("/")
    clusterNames.append(output[len(output)-1])

for i in clusterNames:
    servicesData = ecs.list_services(cluster=i)
    servicesData = servicesData['serviceArns']
    services = []
    s = []
    for j in servicesData:
        services = j.split("/")
        s.append(services[len(services)-1])
    serviceNames.append(s)

# process a single cluster and get the desired fields
def processCluster(clusterName, services):
    # Arrays for formatted display
    arrOfNames = []
    arrOfStatuses = []
    arrOfDesiredTasks = []
    arrOfRunningTasks = []
    arrOfLaunchTypes = []
    arrOfLaunchDates = []

    # loop through each service for the given cluster
    for i in range(0,len(services)):
        serviceData = ecs.describe_services(cluster=clusterName, services=[services[i]],)
        serviceData = serviceData['services'][0]
        arrOfNames.append(serviceData['serviceName'])
        arrOfStatuses.append(serviceData['status'])

        if serviceData['deployments'] != []:
            arrOfDesiredTasks.append(serviceData['deployments'][0]['desiredCount'])
            arrOfRunningTasks.append(serviceData['deployments'][0]['runningCount'])
            arrOfLaunchTypes.append(serviceData['deployments'][0]['launchType'])
            dateLaunched = serviceData['deployments'][0]['createdAt']
            dateLaunched = dateLaunched.strftime('%b %d %Y')
            arrOfLaunchDates.append(dateLaunched)
        else:
            arrOfDesiredTasks.append(serviceData['taskSets'][0]['computedDesiredCount'])
            arrOfRunningTasks.append(serviceData['taskSets'][0]['runningCount'])
            arrOfLaunchTypes.append(serviceData['taskSets'][0]['launchType'])
            dateLaunched = serviceData['taskSets'][0]['createdAt']
            dateLaunched = dateLaunched.strftime('%b %d %Y')
            arrOfLaunchDates.append(dateLaunched)       

    return arrOfNames, arrOfStatuses, arrOfDesiredTasks, arrOfRunningTasks, arrOfLaunchTypes, arrOfLaunchDates

def getClusterNames():
    return clusterNames

# return a list of formattedTables and dataframes
# one for each ecs cluster by calling processCluster for as many clusters as there are
def formatECSData():
    list_df_clusters = []
    for i in range(0,numRunningClusters):
        arrOfNames, arrOfStatuses, arrOfDesiredTasks, arrOfRunningTasks, arrOfLaunchTypes, arrOfLaunchDates = processCluster(clusterNames[i], serviceNames[i])
        formatData = {'Service Name' : arrOfNames,
                  'Status' : arrOfStatuses,
                  'Desired Tasks' : arrOfDesiredTasks,
                  'Running Tasks' : arrOfRunningTasks,
                  'Launch Type' : arrOfLaunchTypes,
                  'Launch Date' : arrOfLaunchDates}
        df = pd.DataFrame(formatData)
        formattedTable = tabulate(df, headers = 'keys', tablefmt = 'pretty')
        tableAndDF = [formattedTable, df]
        list_df_clusters.append(tableAndDF)

    return list_df_clusters