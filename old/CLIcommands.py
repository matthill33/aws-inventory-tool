# Not used anymore, switched to boto3 becuase of efficency
# contains get methods for CLI commands

# EC2 Commands
def getRunningEC2InstancesCommand():
    return "aws ec2 describe-instances \
                --filters Name=instance-state-code,Values=16 \
                --output json"

def get30DayEC2CPUAvgCommand(startTime,endTime,instance):
    return "aws cloudwatch get-metric-statistics \
                --namespace AWS/EC2 \
                --metric-name CPUUtilization \
                --dimensions Name=InstanceId,Value=" + instance +" \
                --statistics Average \
                --start-time " + startTime +" \
                --end-time " + endTime +" \
                --period 2592000"

def get180DayEC2CPUAvgCommand(startTime,endTime,instance):
    return "aws cloudwatch get-metric-statistics \
                --namespace AWS/EC2 \
                --metric-name CPUUtilization \
                --dimensions Name=InstanceId,Value=" + instance +" \
                --statistics Average \
                --start-time " + startTime +" \
                --end-time " + endTime +" \
                --period 15552000"

def get30DayEC2CPUMaxCommand(startTime,endTime,instance):
    return "aws cloudwatch get-metric-statistics \
                --namespace AWS/EC2 \
                --metric-name CPUUtilization \
                --dimensions Name=InstanceId,Value=" + instance +" \
                --statistics Maximum \
                --start-time " + startTime +" \
                --end-time " + endTime +" \
                --period 2592000"

def get180DayEC2CPUMaxCommand(startTime,endTime,instance):
    return "aws cloudwatch get-metric-statistics \
                --namespace AWS/EC2 \
                --metric-name CPUUtilization \
                --dimensions Name=InstanceId,Value=" + instance +" \
                --statistics Maximum \
                --start-time " + startTime +" \
                --end-time " + endTime +" \
                --period 15552000"

# RDS Commands
def getRunningRDSInstancesCommand():
    return "aws rds describe-db-instances \
                --output json"

def get30DayRDSCPUAvgCommand(startTime,endTime,instance):
    return "aws cloudwatch get-metric-statistics \
                --namespace AWS/RDS \
                --metric-name CPUUtilization \
                --dimensions Name=DBInstanceIdentifier,Value=" + instance +" \
                --statistics Average \
                --start-time " + startTime +" \
                --end-time " + endTime +" \
                --period 2592000"

def get30DayRDSConnectionAvgCommand(startTime,endTime,instance):
    return "aws cloudwatch get-metric-statistics \
                --namespace AWS/RDS \
                --metric-name DatabaseConnections \
                --dimensions Name=DBInstanceIdentifier,Value=" + instance +" \
                --statistics Average \
                --start-time " + startTime +" \
                --end-time " + endTime +" \
                --period 2592000"                

def get30DayRDSWriteAvgCommand(startTime,endTime,instance):
    return "aws cloudwatch get-metric-statistics \
                --namespace AWS/RDS \
                --metric-name WriteIOPS \
                --dimensions Name=DBInstanceIdentifier,Value=" + instance +" \
                --statistics Average \
                --start-time " + startTime +" \
                --end-time " + endTime +" \
                --period 2592000"   

def get30DayRDSReadAvgCommand(startTime,endTime,instance):
    return "aws cloudwatch get-metric-statistics \
                --namespace AWS/RDS \
                --metric-name ReadIOPS \
                --dimensions Name=DBInstanceIdentifier,Value=" + instance +" \
                --statistics Average \
                --start-time " + startTime +" \
                --end-time " + endTime +" \
                --period 2592000"               