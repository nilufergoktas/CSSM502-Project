# CSSM502 - Fall 2022
# Nilüfer Göktaş, 49837
# Final Project - Investigating Measurement Invariance in PISA 2012

# Script 2 - Cleaning data for missing values in Math Self Efficacy Scale & Checking frequencies for "gender" and "education"

import numpy as np
import pandas as pd

combined_pisa2012 = pd.read_csv('PISA2012_Combined_ALL.csv')

###### DATA CLEANING ######

criterion = [7.0, 8.0, 9.0] # Invalid/missing values
cleaned_data = pd.DataFrame()

for i in range(len(combined_pisa2012)):
    valid = 0
    for j in range(7,15): # SELF EFFICACY ITEMS
        value = combined_pisa2012.iloc[i,j]
        if value not in criterion:
            valid = valid + 1
    if valid == 8:
        valid_items = pd.DataFrame(combined_pisa2012.iloc[i]).T
        cleaned_data = pd.concat([cleaned_data, valid_items])

# This is the index indicating the place of the observation on the raw data.
# For Turkey, ranging 0-4847
# For the Netherlands, ranging 0-4458
cleaned_final = cleaned_data.rename(columns={cleaned_data.columns[0]: 'raw_index'})

cleaned_final.to_csv("PISA2012_Cleaned.csv", index=False) ##### THE FINAL ONE. I WILL RUN MGCFA WITH THIS CSV FILE. #####

###### FREQUENCY FOR "gender" FOR EACH COUNTRY ######

freq_gender = cleaned_final.groupby(['country', 'gender']).size()
print(freq_gender)

###### FREQUENCY FOR "education" FOR EACH COUNTRY ######

freq_edu = cleaned_final.groupby(['country', 'education']).size()
print(freq_edu)