from keys import eia_key
import matplotlib as plt
import requests
import json
import pandas as pd
# EIA DATA for CO2 emission
eia_key = eia_key
offset, limit = 0, 5000
all_data = []
emissions_by_year_state = {}

while True:
    epi_url=f"https://api.eia.gov/v2/co2-emissions/co2-emissions-and-carbon-coefficients/data/?api_key={eia_key}&frequency=annual&data[0]=emissions&facets[sectorId][]=0&facets[sectorId][]=1&facets[sectorId][]=2&facets[sectorId][]=3&facets[sectorId][]=4&sort[0][column]=period&sort[0][direction]=desc&offset={offset}&length={limit}"
    response = requests.get(epi_url)
    if response.status_code == 200:
        eia_data = response.json()
        if "data" not in eia_data["response"] or not eia_data["response"]["data"]:

            print("ENDED")
            break
        for item in eia_data["response"]["data"]:
            year = item["period"]
            print(year)
            state = item["stateId"]
            # CO2 metric tons
            emissions = float(item["emissions"])
            if year not in emissions_by_year_state:
                emissions_by_year_state[year] = {}
            if state not in emissions_by_year_state[year]:
                emissions_by_year_state[year][state] = 0
            emissions_by_year_state[year][state] += emissions
        offset+=limit
    else:
        print(f"Error {response.status_code}")
        break
eia_output_file = "emissions_data.json"
with open(eia_output_file, "w") as f:
    json.dump(emissions_by_year_state, f, indent = 4)



