#MS&E 246
#localdata.py
#adding more local features

import numpy as np
import pandas as pd

#Part 1:
#dataset one : read in zip code to tax return values (year is 2016) --> need to do some averaging
#go through data 1 file and add in the corresponding information to data stream based off of zip code
#base off borrow zip
#new vars to put in are below
#[adj_gross_income	biz_net_income	scorp_income	net_cap_gain	unemp_comp]

zipDF = pd.read_csv("/Users/agupta21/Downloads/MSE246/zipcodedata_irs.csv")
zipDF2 = zipDF.groupby(['zipcode']).agg({'A00100':'mean','A00900':'mean','A10300':'mean','A01000':'mean','A02300':'mean'}).reset_index()
zipDict = zipDF2.set_index('zipcode').T.to_dict('list')
#mean imputation
meanVals = zipDF2.mean(axis=0)
meanVals = meanVals[1:].tolist()
print(meanVals)

stateDF = pd.read_excel("/Users/agupta21/Downloads/MSE246/states.xlsx")

stateDF.drop(stateDF.columns[1], axis=1)
print(stateDF.shape)

stateDict = stateDF.set_index('State').T.to_dict('list')

#col names: unemp_comp	biz_net_income	adj_gross_income	net_cap_gain
#total_tax_liab	2018-2010	2010-2010	2000-1990
data2 = pd.read_excel("/Users/agupta21/Downloads/MSE246/data_2.xlsx")
print(data2.shape)
for index, row in data2.iterrows():
    print(index)
    targetzip = row["BorrZip"]
    targetState = row["BorrState"]
    if targetzip in zipDict:
        zip = zipDict[targetzip]
    else:
        zip = meanVals
    # row["unemp_comp"] = zip[0]
    data2.loc[index,"unemp_comp"] = zip[0]
    data2.loc[index,"biz_net_income"] = zip[1]
    data2.loc[index,"adj_gross_income"] = zip[2]
    data2.loc[index,"net_cap_gain"] = zip[3]
    data2.loc[index,"total_tax_liab"] = zip[4]
    # row["biz_net_income"] = zip[1]
    # row["adj_gross_income"] = zip[2]
    # row["net_cap_gain"] = zip[3]
    # row["total_tax_liab"] = zip[4]

    if targetState in stateDict:
        st = stateDict[targetState]
        data2.loc[index,"2018-2010"] = st[0]
        data2.loc[index,"2010-2000"] = st[1]
        data2.loc[index,"2000-1990"] = st[2]
        # row["2018-2010"] = st[0]
        # row["2010-2000"] = st[1]
        # row["2000-1990"] = st[2]

data2.to_excel("/Users/agupta21/Downloads/MSE246/dataMoreFeatures.xlsx")



#print(stateDict['WI'])
#statepopmap



# print(zipDF2.head)
# print(zipDF2.shape)
