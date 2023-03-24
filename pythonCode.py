import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
response = requests.get("https://opendata.vancouver.ca/api/v2/catalog/datasets/issued-building-permits/records/")
print(response)
storedata = json.loads(response.content)
jsondata = storedata["records"]
df = pd.json_normalize(jsondata)
for col in df.columns[1:] :
    df[['record.fields.permitnumber' , 'record.fields.applicant' , 'record.fields.projectdescription']].to_csv("permit"+ ".csv", index=False)