import pandas as pd
import json
rows =  [1,2,3,4,5,6,7,17,18,20,28,29,42,43,52,53,67,68,69,70,71] 
cols = [0,4]
all_data = {}
state_abbreviations = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
    'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD',
    'Massachusetts': 'MA', 'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO',
    'Montana': 'MT', 'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ',
    'New Mexico': 'NM', 'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH',
    'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'
}
xl_files = [f'traffic_data/{year[-2:]}dectvt.xls' for year in map(str, range(2008, 2019))]
for file_name in xl_files:
    year = file_name.split('/')[1][:2]
    dfs = pd.read_excel(file_name, sheet_name='Page 4', skiprows=rows, usecols= cols, header= None)
    dfs = dfs.dropna()
    dfs = dfs.rename(columns={4:'Vehicle-Miles(Millions)' , 0:'States'})
    dfs['States'] = dfs['States'].map(state_abbreviations)
    data = dfs.to_dict(orient='records')
    all_data[year] = data
    print(dfs.head())
    
with open('traffic_data.json', 'w') as f:
    json.dump(all_data, f, indent=4)