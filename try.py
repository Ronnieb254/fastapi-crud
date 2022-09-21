import pandas as pd
import json

df = pd.read_excel('1663233269_WEEK 36 2022 AMAZON TOLLS (AFP) (1).xlsx') 
# print(df)
output = dict()
# Convert excel to string 
# (define orientation of document in this case from up to down)
thisisjson = df.to_json(orient='records')

# Print out the result
# print('Excel Sheet to JSON:\n', thisisjson)

# Make the string into a list to be able to input in to a JSON-file
thisisjson_dict = json.loads(thisisjson)
output = thisisjson_dict
print(output)
with open('data.json', 'w') as json_file:
    json.dump(output, json_file)

   