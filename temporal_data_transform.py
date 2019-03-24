#temporal_data_transform.py


import pandas as pd
import numpy as np
import datetime
from dateutil.rrule import rrule, MONTHLY
from dateutil.relativedelta import relativedelta, MO
import csv
dfData = pd.read_excel("/Users/agupta21/Downloads/MSE246/externaldata.xlsx")
infoDict = {}

for index, row in dfData.iterrows():
        #in timestamp format
        infoDict[row['Date']] = [row['P/E'],row['Unemployment'],row['Fed_Funds_Rate'],row['GDP_prev_q']]

df = pd.read_excel("/Users/agupta21/Downloads/MSE246/data_2.xlsx")

with open('/Users/agupta21/Downloads/MSE246/data_time_series1.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['BS','BS','Program','BorrName','BorrStreet', 'BorrCity', 'BorrState','BorrZip','CDC_Name',
    'CDC_Street','CDC_City','CDC_State','CDC_Zip','ThirdPartyLender_Name','ThirdPartyLender_City','ThirdPartyLender_State',
    'ThirdPartyDummy','ThirdPartyDollars','GrossApproval','LoanSum','ApprovalDate',	'ApprovalFiscalYear','DeliveryMethod',
    'subpgmdesc', 'InitialInterestRate','TermInMonths','NaicsCode',	'NaicsDescription', 'ProjectCounty','ProjectState',
    'BusinessType', 'LoanStatusCat','LoanStatus', 'ChargeOffDate', 'GrossChargeOffAmount', 'T-t0(months)','Cur_T', 'P/E_t','unemp_t','interest_rate_t',
    'GDPchange_t','value'])
    count = 0
    for index, row in df.iterrows():
        if count < 1000000:
            count+=1
            print(count)
            startDate = row['ApprovalDate']
            startDate = startDate.replace(day=1)
            lastMonth = 0
            if pd.isnull(row['ChargeOffDate']): #case where there is no charge off
                termLen = int(row['TermInMonths']) #iterate from start thru end
            else: #case where there is a charge off
                chargeOffDate = row['ChargeOffDate']
                chargeOffDate = chargeOffDate.replace(day=1)
                #print(chargeOffDate,startDate)
                termLen = len([dt for dt in rrule(MONTHLY, dtstart=startDate, until=chargeOffDate)])
                #print(termLen)
                lastMonth = 1
            #MANUALLY ADD t-t0 from data 2 later on!!
            for i in range(termLen):
                #add one month
                originfo = row.tolist()
                if i ==0:
                    concat_list_0 = originfo + [i, startDate] + infoDict[startDate] + [0]
                    writer.writerow(concat_list_0)
                originfo = row.tolist()
                t_t0 = i+1
                startDate = startDate + relativedelta(months=1)
                if startDate in infoDict:
                    features = infoDict[startDate]
                else:
                    break
                if i < termLen-1:
                    list2 = [t_t0,startDate, features[0],features[1],features[2],features[3],0]
                else: #equals it
                    list2 = [t_t0,startDate, features[0],features[1],features[2],features[3],lastMonth]
                concat_list = originfo + list2
                writer.writerow(concat_list)


            #put in last month
        #new column of t-to, all features
