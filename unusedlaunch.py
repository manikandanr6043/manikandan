###Raja###
import boto3
import pygsheets
import pandas as pd
#authorization
gc = pygsheets.authorize(service_file='C:/Users/mravich1/Downloads/manikandan2019-46a83072151f.json')
# Create empty dataframe
df = pd.DataFrame()
df1 = pd.DataFrame()
df2 = pd.DataFrame()
df3 = pd.DataFrame()
client = boto3.client('autoscaling',region_name="us-west-2")
client1 = boto3.client('ec2',region_name="us-west-1")
response = client.describe_launch_configurations()
response5 = client1.describe_launch_templates()
totallTlist=[]
lanchconflistfind=[]
lanuchconfigurationlist=[]
launchtemplatelist=[]
for i4 in response5["LaunchTemplates"]:
    lcttotal=i4["LaunchTemplateId"]
    totallTlist.append(lcttotal)
for i in response["LaunchConfigurations"]:
    lanuchconfiguration_name = i["LaunchConfigurationName"]
    lanuchconfigurationlist.append(lanuchconfiguration_name)
#print(lanuchconfigurationlist)
Total_LC_configuration = lanuchconfigurationlist
response1 = client.describe_auto_scaling_groups()
for i1 in response1["AutoScalingGroups"]:
    for keys in i1:
        if "LaunchConfigurationName" == keys:
            lanchconflistfinded = i1["LaunchConfigurationName"]
            lanchconflistfind.append(lanchconflistfinded)
            tc_add_ac = lanchconflistfind
        elif "LaunchTemplate" == keys:
            lanchtemplate_id=i1["LaunchTemplate"]["LaunchTemplateId"]
            launchtemplatelist.append(lanchtemplate_id)
            tc_temp_add = launchtemplatelist
#df['Total Launch Template'] = launchtemplatelist
df['Total_Launch_Configuration'] = lanuchconfigurationlist
df1['Total_Launch_Template'] = totallTlist
print(launchtemplatelist)
print(lanchconflistfind)
s=set(lanchconflistfind)
ASG_Not_Attached_LC=[x for x in lanuchconfigurationlist if x not in s]
df2['ASG_Not_Attached_LC'] = ASG_Not_Attached_LC
print(ASG_Not_Attached_LC)
s1=set(launchtemplatelist)
ASG_Not_Attached_LT=[x1 for x1 in totallTlist if x1 not in s1]
df3['ASG_Not_Attached_LT'] = ASG_Not_Attached_LT
print(ASG_Not_Attached_LC)
sh = gc.open('LC Report')
#select the first sheet
wks = sh[0]
#update the first sheet with df, starting at cell B2.
wks.set_dataframe(df,(1,1))
wks.set_dataframe(df1,(1,2))
wks.set_dataframe(df2,(1,3))
wks.set_dataframe(df3,(1,4))
Total_LC_configuration.clear()
tc_add_ac.clear()
tc_temp_add.clear()
totallTlist.clear()
