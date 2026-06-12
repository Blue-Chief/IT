import json

string = '{"region": "us-east-1", "cluster": "k8s-prod", "replicas": 4}'

metric = json.loads(string)

dict = {
    "cluster" : "",
    "region" : "",
    "replicas" : ""
}

# cluster = ""
# region = ""
# replicas = ""

# for key, value in metric.items():
#     if key == "region":
#         region = value
#     elif key == "cluster":
#         cluster = value
#     elif key == "replicas":
#         replicas = value

for key, value in metric.items():
    if key in dict.keys():
        dict[key] = value

multi_line = f"""
Deploying cluster: {dict['cluster']}
Region: {dict['region']}
Replicas: {dict['replicas']}
"""

print(multi_line)