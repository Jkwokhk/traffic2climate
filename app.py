import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from scipy import stats

# For convenience purposes I will only compare data between California and Wyoming
traffic_data = pd.read_json('traffic_data.json')
ca_traffic_data = {}
wy_traffic_data = {}
all_traffic_data = []

for year, records in traffic_data.items():
    
    for record in records:
        state = record['States']
        volume = record['Vehicle-Miles(Millions)']
        all_traffic_data.append(volume)
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
all_emissions = []

for year, records in emissions.items():

    if "CA" in records:
        ca_emissions[year] = records["CA"]
    if "WY" in records:
        wy_emissions[year] = records["WY"]
    for record in records:
        all_emissions.append(record)





ca_co2_sorted = sorted(ca_emissions.items())
wy_co2_sorted = sorted(wy_emissions.items())

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


#  creating scatterplot to see relationship between traffic volume and CO2 emission

all_emissions_sorted = sorted(all_emissions)
all_traffic_data_sorted = sorted(all_traffic_data)
combined_data = list(zip(all_traffic_data_sorted, all_emissions_sorted))

plt.figure(figsize=(10, 6))
plt.scatter( all_traffic_data_sorted, all_emissions_sorted, label='All States')

plt.xlabel('Traffic Volume (Vehicle-Miles in Millions)')
plt.ylabel('CO2 Emissions (Million Metric Tons)')
plt.title('Traffic Volume vs CO2 Emissions')
plt.legend()
plt.grid(True)
plt.tight_layout()


# Perform Linear regression
X = np.array(all_traffic_data_sorted).reshape(-1,1)
y = np.array(all_emissions_sorted)

model = LinearRegression()
model.fit(X,y)
y_pred = model.predict(X)

# Finding R^2 and p value 
# R^2 shows the goodness of fit in the regression model
#  p value sees if there is a significant linear relationship (lower more significant)
# Needs to flatten from 2d to 1d because linregress only accepts 1d
# p value shows result is statistically highly significant
# r squared shows good fit
slope, intercept, r_value, p_value, std_err = stats.linregress(X.flatten(), y)
print(r_value, p_value)
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', linewidth=2, label='Linear regression line')

plt.text(0.1, 0.5*max(y) ,f'R-squared: {r_value:.6f}', fontsize=12)
plt.text( 0.1, 0.6*max(y), f'P-value: {p_value:.6f}', fontsize=12)
plt.xlabel('Traffic Volume (Vehicle-Miles in Millions)')
plt.ylabel('CO2 Emissions (in units)')
plt.title('Linear Regression: Traffic Volume vs CO2 Emissions')
plt.legend()
plt.grid(True)
plt.tight_layout()




plt.show()