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
#session = boto3.session.Session(aws_access_key_id="IASIAWUH6QJOWHNVX47XN",aws_secret_access_key="DwgjuWJ1pnNfyEHWptDpewIkpEY5EYKmfDUs8hBN",aws_session_token="FwoGZXIvYXdzEPT//////////wEaDEvvTHUObzf3hqumoCL6AWWO+mIzKfzZPnc0vC4nnXlfBgCkm/LVtyiUclWVTfGAJ7RSiuExirBhqUOAgdxEK9IyzFQl7Zyqd1ZQfNis72hDC0hmV6bBskt7paz3/ww9lyCEHSG3sXW4bqKLH64x5rQoChIb5iH7YqmEXDiYGyGKeMQOSB43PGVkQZNgAtgFnomLPrWVoJksyvHipiLEzX6cAxaFZBuomlsH3RfMcq7/zRA0APdq/D1LM+9X2bnlS5fHrnpDjyiPv/5tD0hkFU7wQKP8pM4/dYwMHNwdGnXPbhaDEjwbvS8NK2ZhRDjOjaRwj34ZAYIthstba+72XTmtnnv3F+P9Yxoo8N6bngYyKxTKYsPq4oZNJo7odxijdjxaUIFD8BT1bA+s1/GEzPNu8AgBc1aazizBU6Q=",region_name="us-west-2")
#asr=session.resourse("autoscaling")
#ec2=session.resourse("ec2")
client = boto3.client('autoscaling',region_name="us-west-2",aws_access_key_id='ASIAWUH6QJOWE64IWVGF',aws_secret_access_key='Zjv5KaVZqYUFipv0slQYOG34K4O7Cs/5bOGm5ykl',aws_session_token='FwoGZXIvYXdzEPb//////////wEaDK+ZBdBiskrMdBFj6yL6AVrazFehS4YYpRrRum9VPAOuJVFzLlNceDq+Qw/+rNeIn4zu5dEH4k20lMiiNJwXb13UcBcwb7n77BuLgwlmJ8jSb2sb9XGPobS8IrkIXdum5/NyAbDc74pz9prL2sa8/iin7r3iDGuBv5udTh3EpXsb3d1fz5V8V/8NnK67Y+hk1Ojl08ipRkbmQDHg9aY6GntDAkW3QUQ12ix+eAgWdy8Ud5J34AJaEKnhm4U61GVwGCOlSCRqqSV3IB9pL6wyhxOFBt/bQsji5LmITfCk9Yp8Ub97zFrEqjs2fMAr553+/wikWIvNBMJCzMOlLwIpzzIatFKXlsQv0XMo8f+bngYyK87uEdkX1KmgUZSqK7V7B9+dEk+T291xb+b1MXEgdWbCAx5+bBZnGBrHOpk=')
client1 = boto3.client('ec2',region_name="us-west-2",aws_access_key_id='ASIAWUH6QJOWE64IWVGF',aws_secret_access_key='Zjv5KaVZqYUFipv0slQYOG34K4O7Cs/5bOGm5ykl',aws_session_token='FwoGZXIvYXdzEPb//////////wEaDK+ZBdBiskrMdBFj6yL6AVrazFehS4YYpRrRum9VPAOuJVFzLlNceDq+Qw/+rNeIn4zu5dEH4k20lMiiNJwXb13UcBcwb7n77BuLgwlmJ8jSb2sb9XGPobS8IrkIXdum5/NyAbDc74pz9prL2sa8/iin7r3iDGuBv5udTh3EpXsb3d1fz5V8V/8NnK67Y+hk1Ojl08ipRkbmQDHg9aY6GntDAkW3QUQ12ix+eAgWdy8Ud5J34AJaEKnhm4U61GVwGCOlSCRqqSV3IB9pL6wyhxOFBt/bQsji5LmITfCk9Yp8Ub97zFrEqjs2fMAr553+/wikWIvNBMJCzMOlLwIpzzIatFKXlsQv0XMo8f+bngYyK87uEdkX1KmgUZSqK7V7B9+dEk+T291xb+b1MXEgdWbCAx5+bBZnGBrHOpk=')
#client = boto3.client('autoscaling',region_name="us-west-2",aws_access_key_id='ASIAWUH6QJOWHNVX47XN',aws_secret_access_key='DwgjuWJ1pnNfyEHWptDpewIkpEY5EYKmfDUs8hBN',aws_session_token='FwoGZXIvYXdzEPT//////////wEaDEvvTHUObzf3hqumoCL6AWWO+mIzKfzZPnc0vC4nnXlfBgCkm/LVtyiUclWVTfGAJ7RSiuExirBhqUOAgdxEK9IyzFQl7Zyqd1ZQfNis72hDC0hmV6bBskt7paz3/ww9lyCEHSG3sXW4bqKLH64x5rQoChIb5iH7YqmEXDiYGyGKeMQOSB43PGVkQZNgAtgFnomLPrWVoJksyvHipiLEzX6cAxaFZBuomlsH3RfMcq7/zRA0APdq/D1LM+9X2bnlS5fHrnpDjyiPv/5tD0hkFU7wQKP8pM4/dYwMHNwdGnXPbhaDEjwbvS8NK2ZhRDjOjaRwj34ZAYIthstba+72XTmtnnv3F+P9Yxoo8N6bngYyKxTKYsPq4oZNJo7odxijdjxaUIFD8BT1bA+s1/GEzPNu8AgBc1aazizBU6Q=')
#client1 = boto3.client('ec2',region_name="us-west-2",aws_access_key_id='ASIAWUH6QJOWHNVX47XN',aws_secret_access_key='DwgjuWJ1pnNfyEHWptDpewIkpEY5EYKmfDUs8hBN',aws_session_token='FwoGZXIvYXdzEPT//////////wEaDEvvTHUObzf3hqumoCL6AWWO+mIzKfzZPnc0vC4nnXlfBgCkm/LVtyiUclWVTfGAJ7RSiuExirBhqUOAgdxEK9IyzFQl7Zyqd1ZQfNis72hDC0hmV6bBskt7paz3/ww9lyCEHSG3sXW4bqKLH64x5rQoChIb5iH7YqmEXDiYGyGKeMQOSB43PGVkQZNgAtgFnomLPrWVoJksyvHipiLEzX6cAxaFZBuomlsH3RfMcq7/zRA0APdq/D1LM+9X2bnlS5fHrnpDjyiPv/5tD0hkFU7wQKP8pM4/dYwMHNwdGnXPbhaDEjwbvS8NK2ZhRDjOjaRwj34ZAYIthstba+72XTmtnnv3F+P9Yxoo8N6bngYyKxTKYsPq4oZNJo7odxijdjxaUIFD8BT1bA+s1/GEzPNu8AgBc1aazizBU6Q=')

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
#tc_temp_add.clear()
totallTlist.clear()
