import pandas as pd 
import os
import sys
import boto3
from ec2 import formatEC2Data, getNumEC2Instances
from rds import formatRDSData, getNumRDSInstances
from ecs import formatECSData, getClusterNames

# This file actually displays all of the AWS account information using tabulate
# It also launches a CSV file with all of the data
# Matt Hill
# 8/12/21

# need iam:ListAccountAliases on resource: * account permissions so list account
# accountAlias = boto3.client('iam').list_account_aliases()['AccountAliases'][0]

arg = 'no arg'

if len(sys.argv) > 1:
    arg = sys.argv[1]

if arg != 'no arg' and arg != 'ec2' and arg != 'rds' and arg != 'ecs' and arg != 'all':
    print("\nInvalid Argument. Valid arguments listed below:")
    print("\"py inventory.py\"")
    print("\"py inventory.py ec2\"")
    print("\"py inventory.py rds\"")
    print("\"py inventory.py ecs\"")
    print("\"py inventory.py all\"\n")

def displayEC2(all):
    # if there are any running ec2 instances, display them
    if getNumEC2Instances() > 0:
        EC2Table, EC2DF = formatEC2Data()
        # print("\n" + accountAlias + " EC2 Data \n")
        print("\nEC2 Data \n")
        print(EC2Table)
        if all == True:
            EC2DF.to_csv(r'C:\Users\MHill\Downloads\InventoryData.csv', index=False) # create new CSV file and add ec2 dataframe to it
        else:
            EC2DF.to_csv(r'C:\Users\MHill\Downloads\EC2Data.csv', index=False) # create new CSV file and add ec2 dataframe to it
            os.startfile(r'C:\Users\MHill\Downloads\EC2Data.csv') # start the csv file up
    else:
        print("\n\nThere are zero running EC2 instances\n\n")

def displayRDS(all):
    # if there are any running rds instances, display them
    if getNumRDSInstances() > 0:
        RDSTable, RDSDF = formatRDSData()
        # print("\n" + accountAlias + " RDS Data \n")
        print("\nRDS Data \n")
        print(RDSTable)
        if all == True:
            RDSDF.to_csv(r'C:\Users\MHill\Downloads\InventoryData.csv', mode='a', index=False) # append rds dataframe to existing CSV file
        else:
            RDSDF.to_csv(r'C:\Users\MHill\Downloads\RDSData.csv', index=False) # create new CSV file and add rds dataframe to it
            os.startfile(r'C:\Users\MHill\Downloads\RDSData.csv') # start the csv file up
    else:
        print("\n\nThere are zero running RDS clusters\n\n")

def displayECS(all):
    # if there are any running ecs clusters, display them
    clusterNames = getClusterNames()
    if len(clusterNames) > 0:
        ECSData = formatECSData()
        print("\nECS Data \n")
        for i in range(0,len(clusterNames)):
            print("Cluster: " + clusterNames[i])
            print(ECSData[i][0])
            if all == True:
                ECSData[i][1].to_csv(r'C:\Users\MHill\Downloads\InventoryData.csv', mode='a', index=False)
            else:
                ECSData[i][1].to_csv(r'C:\Users\MHill\Downloads\ECSData.csv', index=False)  
                os.startfile(r'C:\Users\MHill\Downloads\ECSData.csv') # start the csv file up             
    else:
        print("\n\nThere are zero running ECS clusters\n\n")


# show ec2, rds, ecs data
if arg == 'all' or arg == 'no arg':
    displayEC2(True)
    displayRDS(True)
    displayECS(True)

    os.startfile(r'C:\Users\MHill\Downloads\InventoryData.csv') # start the csv file up

elif arg == 'ec2':
    displayEC2(False)

elif arg == 'rds':
    displayRDS(False)

elif arg == 'ecs':
    displayECS(False)

