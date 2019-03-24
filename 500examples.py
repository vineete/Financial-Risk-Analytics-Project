#Choose 500 examples

import pandas as pd
import numpy as np
from sklearn.utils import shuffle


df = pd.read_excel("/Users/agupta21/Downloads/MSE246/dataMoreFeatures.xlsx")
df = shuffle(df)
#need to extract 500 loans
loanNumList = set()

cutOffYear = 2007
plus1 = 2008
plus5 = 2012

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

for index, row in df.iterrows():
    #print(len(loanNumList))
    if len(loanNumList) >= 500: #how many unique ones are in it
        break
    #otherwise
    if int(row["LoanSum"]) not in loanNumList:
        if row["ChargeOffDate"].year >= 2012 and row["ApprovalDate"].year <= 2007:
            #print(row["ChargeOffDate"].year)
            loanNumList.add(int(row["LoanSum"]))
        else:
            value = (row["ApprovalDate"].year + int(row["TermInMonths"])/12)
            if value >= 2012 and row["ApprovalDate"].year <= 2007 and row["LoanStatus"] == "PIF":#PIF
                loanNumList.add(int(row["LoanSum"]))

dfMid = pd.read_csv("/Users/agupta21/Downloads/MSE246/data_time_series3.csv",encoding="utf-8")
dfMid.columns = [strip_non_ascii(x) for x in dfMid.columns]

loanNums = list(loanNumList)
dfFinal = dfMid.loc[dfMid['LoanNum'].isin(loanNums)]

from datetime import date
value_to_check = pd.Timestamp(2007,12,31)
value_to_check1 = pd.Timestamp(2008,12,31)
value_to_check2 = pd.Timestamp(2011,12,31)
value_to_check3 = pd.Timestamp(2012,12,31)




dfFinal.columns = [strip_non_ascii(x) for x in dfFinal.columns]
dfFinal['Cur_T'] = [pd.to_datetime(x) for x in dfFinal['Cur_T']]
dfWnt = dfFinal.loc[dfFinal['Cur_T'] <= value_to_check]
dfMe = dfFinal.loc[((dfFinal['Cur_T'] > value_to_check) & (dfFinal['Cur_T'] <= value_to_check1)) | ((dfFinal['Cur_T'] > value_to_check2) & (dfFinal['Cur_T'] <= value_to_check3))]
dfFinal.to_excel("/Users/agupta21/Downloads/MSE246/500points_1.xlsx")
dfWnt.to_excel("/Users/agupta21/Downloads/MSE246/pre2007_500pts.xlsx")
dfMe.to_excel("/Users/agupta21/Downloads/MSE246/2018_2012_500pts.xlsx")
