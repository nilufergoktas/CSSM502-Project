# CSSM502 - Fall 2022
# Nilüfer Göktaş, 49837
# Final Project - Investigating Measurement Invariance in PISA 2012

# Script 1 - Combining observations from Turkey and the Netherlands

import numpy as np
import pandas as pd

pisa2012 = pd.read_csv('Desktop/FALL 2022/2.CSSM502/5.FINAL PROJECT/2.PISA 2012/DATA/INT_STU12_DEC03.txt', header=None)

# NOTE: The locations of the all variables in the text file were provided by the "Codebook for PISA 2012 Student Questionnaire", which I shared in my repository in the GitHub. I utilized this codebook while splicing the variables below. 

###### OBSERVATIONS - FOR TURKEY ######

turkey_data = np.array([])
for i in range(460074,464922): # Participants from Turkey were between 460074-464921 in the text file. 
    turkey_data = np.append(turkey_data, pisa2012.loc[i])

####### DESCRIPTIVES -  FOR TURKEY #######
# For each participant from Turkey, variables of  "identifier", "country", "gender", "age", and "stratum" were spliced. 
    
tr_identifier = np.array([])
tr_country = np.array([])
tr_gender = np.array([])
tr_age = np.array([])
tr_stratum = np.array([])

for i in range(len(turkey_data)):
    tr_rows = str(turkey_data[i])
    
    splice_trid = tr_rows[0:36]  
    tr_identifier = np.append(tr_identifier, splice_trid)
    
    splice_trcountry = tr_rows[0:3]  
    tr_country = np.append(tr_country, splice_trcountry)
    
    splice_trgender = int(tr_rows[46:47])
    tr_gender = np.append(tr_gender, splice_trgender)
    
    splice_trage = float(tr_rows[518:526])
    tr_age = np.append(tr_age, splice_trage)
    
    splice_trstratum = int(tr_rows[15:17])
    tr_stratum = np.append(tr_stratum, splice_trstratum)
    
# Stratums were grouped based on information given "Student Questionnaire Codebook".
# Each participant from Turkey was given an value ranging between 1-4 for the variable of "education". 

primary = [1,4,7,10,14,18,21,24,27,30,33,36] # Education Group 1: Primary
secondary = [2,5,8,11,15,19,22,25,28,31,34,37] # Education Group 2: General Secondary 
voc_tech = [3,6,9,12,16,20,23,26,29,32,35,38] # Education Group 3: Vocational and Technical Secondary
police_ed = [13,17] # Education Group 4: Police Education

tr_education = np.array([])
for i in range(len(turkey_data)):
    if tr_stratum[i] in primary:
        tr_education = np.append(tr_education, '1')
    elif tr_stratum[i] in secondary:
        tr_education = np.append(tr_education, '2')
    elif tr_stratum[i] in voc_tech:
        tr_education = np.append(tr_education, '3')
    else:
        tr_education = np.append(tr_education, '4')
        
####### MATH SELF EFFICACY ITEMS - FOR TURKEY #######
# 8-item-long mathematics self efficacy scale was spliced for each participant from Turkey. 

tr_self1 = np.array([])
tr_self2 = np.array([])
tr_self3 = np.array([])
tr_self4 = np.array([])
tr_self5 = np.array([])
tr_self6 = np.array([])
tr_self7 = np.array([])
tr_self8 = np.array([])

for j in range(0,8):
    for i in range(len(turkey_data)):
        trself_rows = str(turkey_data[i])
        splice_trself = int(trself_rows[(139+j):(139+1+j)])
        if j == 0:
            tr_self1 = np.append(tr_self1, splice_trself)
        elif j == 1:
            tr_self2 = np.append(tr_self2, splice_trself)
        elif j == 2:
            tr_self3 = np.append(tr_self3, splice_trself)
        elif j == 3:
            tr_self4 = np.append(tr_self4, splice_trself)
        elif j == 4:
            tr_self5 = np.append(tr_self5, splice_trself)
        elif j == 5:
            tr_self6 = np.append(tr_self6, splice_trself)
        elif j == 6:
            tr_self7 = np.append(tr_self7, splice_trself)
        else:
            tr_self8 = np.append(tr_self8, splice_trself)

####### MATH PERFORMANCE 'PLAUSIBLE VALUES' - FOR TURKEY ######
# Five plausible values reflecting overall math performance of each participant were spliced. 

tr_PV1 = np.array([])
tr_PV2 = np.array([])
tr_PV3 = np.array([])
tr_PV4 = np.array([])
tr_PV5 = np.array([])

for j in range(0,5):
    for i in range(len(turkey_data)):
        trPV_rows = str(turkey_data[i])
        splice_trPV = float(trPV_rows[1149+(9*j):1158+(9*j)])
        if j == 0:
            tr_PV1 = np.append(tr_PV1, splice_trPV)
        elif j == 1:
            tr_PV2 = np.append(tr_PV2, splice_trPV)
        elif j == 2:
            tr_PV3 = np.append(tr_PV3, splice_trPV)
        elif j == 3:
            tr_PV4 = np.append(tr_PV4, splice_trPV)
        else:
            tr_PV5 = np.append(tr_PV5, splice_trPV)

###### DATAFRAME - FOR TURKEY ######

tr_combining_dict = {'identifiers':tr_identifier, 'country':tr_country, 'gender':tr_gender, 'age':tr_age, 'stratum':tr_stratum, 'education':tr_education, 'efficacy1':tr_self1, 'efficacy2':tr_self2, 'efficacy3':tr_self3, 'efficacy4':tr_self4, 'efficacy5':tr_self5, 'efficacy6':tr_self6, 'efficacy7':tr_self7, 'efficacy8':tr_self8, 'PVMATH1':tr_PV1, 'PVMATH2':tr_PV2, 'PVMATH3':tr_PV3, 'PVMATH4':tr_PV4, 'PVMATH5':tr_PV5}

tr_combining_data = pd.DataFrame(tr_combining_dict)

####### OBSERVATIONS - FOR THE NETHERLANDS ######

netherlands_data = np.array([])
for i in range(359450,363910): # Participants from the Netherlands were between 359450-363909 in the text file. 
    netherlands_data = np.append(netherlands_data, pisa2012.loc[i])

###### DESCRIPTIVES - FOR THE NETHERLANDS ######
# For each participant from the Netherlands, variables of  "identifier", "country", "gender", "age", and "stratum" were spliced. 
    
nld_identifier = np.array([])
nld_country = np.array([])
nld_gender = np.array([])
nld_age = np.array([])
nld_stratum = np.array([])

for i in range(len(netherlands_data)):
    nld_rows = str(netherlands_data[i])
    
    splice_nldid = nld_rows[0:36]  
    nld_identifier = np.append(nld_identifier, splice_nldid)
    
    splice_nldcountry = nld_rows[0:3]  
    nld_country = np.append(nld_country, splice_nldcountry)
    
    splice_nldgender = int(nld_rows[46:47])
    nld_gender = np.append(nld_gender, splice_nldgender)
    
    splice_nldage = float(nld_rows[518:526])
    nld_age = np.append(nld_age, splice_nldage)
    
    splice_nldstratum = int(nld_rows[15:17])
    nld_stratum = np.append(nld_stratum, splice_nldstratum)

# Each participant from the Netherlands  was given an value ranging between 5-8 for the variable of "education".
# Education Group 5: PRO/VMBO in stratum 1
# Education Group 6: HAVO/VWO in stratum 2
# Education Group 7: General education in stratum 3
# Education Group 8: Private education in stratum 4

nld_education = np.array([])
for i in range(len(netherlands_data)):
    if nld_stratum[i] == 1:
        nld_education = np.append(nld_education, '5')
    elif nld_stratum[i] == 2:
        nld_education = np.append(nld_education, '6')
    elif nld_stratum[i] == 3:
        nld_education = np.append(nld_education, '7')
    else:
        nld_education = np.append(nld_education, '8')
        
####### MATH SELF EFFICACY ITEMS - FOR THE NETHERLANDS ######
# 8-item-long mathematics self efficacy scale was spliced for each participant from the Netherlands. 

nld_self1 = np.array([])
nld_self2 = np.array([])
nld_self3 = np.array([])
nld_self4 = np.array([])
nld_self5 = np.array([])
nld_self6 = np.array([])
nld_self7 = np.array([])
nld_self8 = np.array([])

for j in range(0,8):
    for i in range(len(netherlands_data)):
        nldself_rows = str(netherlands_data[i])
        splice_nldself = int(nldself_rows[(139+j):(139+1+j)])
        if j == 0:
            nld_self1 = np.append(nld_self1, splice_nldself)
        elif j == 1:
            nld_self2 = np.append(nld_self2, splice_nldself)
        elif j == 2:
            nld_self3 = np.append(nld_self3, splice_nldself)
        elif j == 3:
            nld_self4 = np.append(nld_self4, splice_nldself)
        elif j == 4:
            nld_self5 = np.append(nld_self5, splice_nldself)
        elif j == 5:
            nld_self6 = np.append(nld_self6, splice_nldself)
        elif j == 6:
            nld_self7 = np.append(nld_self7, splice_nldself)
        else:
            nld_self8 = np.append(nld_self8, splice_nldself)

###### MATH PERFORMANCE 'PLAUSIBLE VALUES' - FOR THE NETHERLANDS ######
# Five plausible values reflecting overall math performance of each participant were spliced. 

nld_PV1 = np.array([])
nld_PV2 = np.array([])
nld_PV3 = np.array([])
nld_PV4 = np.array([])
nld_PV5 = np.array([])

for j in range(0,5):
    for i in range(len(netherlands_data)):
        nldPV_rows = str(netherlands_data[i])
        splice_nldPV = float(nldPV_rows[1149+(9*j):1158+(9*j)])
        if j == 0:
            nld_PV1 = np.append(nld_PV1, splice_nldPV)
        elif j == 1:
            nld_PV2 = np.append(nld_PV2, splice_nldPV)
        elif j == 2:
            nld_PV3 = np.append(nld_PV3, splice_nldPV)
        elif j == 3:
            nld_PV4 = np.append(nld_PV4, splice_nldPV)
        else:
            nld_PV5 = np.append(nld_PV5, splice_nldPV)
            
###### DATAFRAME - FOR THE NETHERLANDS ######

nld_combining_dict = {'identifiers':nld_identifier, 'country':nld_country, 'gender':nld_gender, 'age':nld_age, 'stratum':nld_stratum, 'education':nld_education, 'efficacy1':nld_self1, 'efficacy2':nld_self2, 'efficacy3':nld_self3, 'efficacy4':nld_self4, 'efficacy5':nld_self5, 'efficacy6':nld_self6, 'efficacy7':nld_self7, 'efficacy8':nld_self8, 'PVMATH1':nld_PV1, 'PVMATH2':nld_PV2, 'PVMATH3':nld_PV3, 'PVMATH4':nld_PV4, 'PVMATH5':nld_PV5}

nld_combining_data = pd.DataFrame(nld_combining_dict)

####### COMBINING TWO COUNTRIES #######

all_combined_data = pd.concat([tr_combining_data, nld_combining_data])

all_combined_data.to_csv("PISA2012_Combined_ALL.csv")
