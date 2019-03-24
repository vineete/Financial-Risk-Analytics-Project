#generate predictor values

#go thru pre-processed csv and 18 csv and extract pertinent values


import numpy as np
import pandas as pd

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

dfFinal = pd.read_csv("processed_hazard_with_number.csv")
print(dfFinal.head)
query = pd.read_excel("2018_2012_500pts.xlsx")


# print(data.shape)
# print(data2.shape)

#get tuple of num rows and then [] of t-t0
#check if for each one its in bigD

#filter one is date
from datetime import date
value_to_check = pd.Timestamp(2007,12,31)
value_to_check1 = pd.Timestamp(2008,12,31)
value_to_check2 = pd.Timestamp(2011,12,31)
value_to_check3 = pd.Timestamp(2012,12,31)

#dfFinal.columns = [strip_non_ascii(x) for x in dfFinal.columns]
dfFinal['Cur_T'] = [pd.to_datetime(x) for x in dfFinal['Cur_T']]

#date check
dfUpd = dfFinal[((dfFinal['Cur_T'] > value_to_check) & (dfFinal['Cur_T'] <= value_to_check1)) | ((dfFinal['Cur_T'] > value_to_check2) & (dfFinal['Cur_T'] <= value_to_check3))]
print(dfUpd.head)
loanNumList = set()

#query.columns = [strip_non_ascii(x) for x in query.columns]

for index, row in query.iterrows():
    curRow = row["LoanNum"]
    loanNumList.add(curRow)


loanNums = list(loanNumList)
print(loanNums)

print(len(loanNums))

#dfFinal = dfMid.loc[dfMid['LoanNum'].isin(loanNums)]

dfUpd = dfUpd.loc[dfUpd["LoanNum"].isin(loanNums)]
print(dfUpd.head)
dfUpd.to_csv("/Users/agupta21/Downloads/MSE246/processed_08_12.csv")
