import math
import boto3
import json
from datetime import date, datetime, timedelta, timezone

# Helper functions that ecs.py calls
# Retreives cloudwatch data with boto3 and pricing info from pricing.py

# class DateTimeEncoder(json.JSONEncoder):
#     def default(self, z):
#         if isinstance(z, datetime):
#             return (str(z))
#         else:
#             return super().default(z)



# # serviceData = ecs.describe_services(cluster='preview-gpet', services=['frontend2'],)
# serviceData = ecs.describe_services(cluster='fargate-hosting', services=['wordpress-familyfirst-prod'],)

# jsonStr = json.dumps(serviceData, cls=DateTimeEncoder, indent=2)
# print(type(jsonStr))
# print(jsonStr)