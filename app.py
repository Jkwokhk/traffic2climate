import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# For convenience purposes I will only compare data between California and Wyoming
traffic_data = pd.read_json('traffic_data.json')
ca_traffic_data = {}
wy_traffic_data = {}
for year, records in traffic_data.items():
    for record in records:
        state = record['States']
        volume = record['Vehicle-Miles(Millions)']
        if state == 'CA':
            ca_traffic_data[year] = volume
        if state == 'WY':
            wy_traffic_data[year] = volume

ca_traffic_sorted = sorted(ca_traffic_data.items())
wy_traffic_sorted = sorted(wy_traffic_data.items())

# Extract years and volumes for plotting
ca_years, ca_volumes = zip(*ca_traffic_sorted)
wy_years, wy_volumes = zip(*wy_traffic_sorted)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(ca_years, ca_volumes, label='CA Traffic Volume')
plt.plot(wy_years, wy_volumes, label='WY Traffic Volume')
plt.xlabel('Year')
plt.ylabel('Vehicle-Miles (Millions)')
plt.title('Traffic Volume Comparison: CA vs WY')
plt.legend()
plt.grid(True)
plt.tight_layout()

# We now know that CA has high traffic volume and WY has low volume
# Now we compare their carbon emissions
emissions = pd.read_json('emissions_data.json')
ca_emissions = {}
wy_emissions = {}
for year, records in emissions.items():
    if "CA" in records:
        ca_emissions[year] = records["CA"]
    if "WY" in records:
        wy_emissions[year] = records["WY"]

ca_co2_sorted = sorted(ca_emissions.items())
wy_co2_sorted = sorted(wy_emissions.items())
print(ca_co2_sorted)
print(wy_co2_sorted)
ca_year, ca_emi = zip(*ca_co2_sorted)
wy_year, wy_emi = zip(*wy_co2_sorted)
plt.figure(figsize=(10, 6))
plt.plot(ca_year, ca_emi, label='CA CO2 Emission')
plt.plot(wy_year, wy_emi, label='WY CO2 Emission')
plt.xlabel('Year')
plt.ylabel('CO2 emissions (Million metric tons)')
plt.title('CO2 emission Comparison: CA vs WY')
plt.legend()
plt.grid(True)
plt.tight_layout()

#  Now we find the relationship between CO2 emission and traffic volume


plt.show()