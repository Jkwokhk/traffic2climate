# traffic2climate
## Overview
This project aims to investigate the relationship between traffic volume and local climate in the United States. By employing a linear regression model, we analyze how variations in traffic may influence climate-related factors.

## How to run:
  1) git clone the repo
     ```
     git clone https://github.com/Jkwokhk/traffic2climate.git
     ```
  2) cd to your folder
     ```
     cd ./traffic2climate
     ```
  3) run the program
     ```
     python3 traffic_data.py
     python3 main.py
     python3 app.py
     ```

## Key Findings:
  The linear regression model demonstrates a strong fit with an R^2 value of approximately 0.94 and a p value of less than 0.001, which indicates a high variablity and highly significant relationship between traffic volume and CO2 emission. These results suggest a significant correlation between the traffic volume and CO2 emission factors, which contribute to the climate.
      
## Data is acquired from:
  CO2 Emission data : https://www.eia.gov/opendata/browser/co2-emissions/co2-emissions-and-carbon-coefficients
  
  Traffic volume data : https://www.fhwa.dot.gov/policyinformation/tables/tmasdata/

## Footnotes:
  The traffic volume dataset only retrieves the data in Decemeber each year for convenience, the actual result may differ from the program output
