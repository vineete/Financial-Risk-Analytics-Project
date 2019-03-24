#temporal_data_transform.py


import pandas as pd
import numpy as np
import datetime
from dateutil.rrule import rrule, MONTHLY
from dateutil.relativedelta import relativedelta, MO
import csv


#each row: add column value reading in from infoDict

dfData = pd.read_excel("/Users/agupta21/Downloads/MSE246/externaldata.xlsx")
infoDict = {}

for index, row in dfData.iterrows():
        #in timestamp format
        infoDict[row['Date']] = [row['P/E'],row['Unemployment'],row['Fed_Funds_Rate'],row['GDP_prev_q']]

#need to integrate these four values into the row in addition to the 0-1 label

df = pd.read_excel("/Users/agupta21/Downloads/MSE246/dataMoreFeatures.xlsx")

with open('/Users/agupta21/Downloads/MSE246/data_time_series3.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['LoanNum','Program','BorrName','BorrStreet', 'BorrCity', 'BorrState','BorrZip','CDC_Name',
    'CDC_Street','CDC_City','CDC_State','CDC_Zip','ThirdPartyLender_Name','ThirdPartyLender_City','ThirdPartyLender_State',
    'ThirdPartyDummy','ThirdPartyDollars','GrossApproval','LoanSum','ApprovalDate',	'ApprovalFiscalYear','DeliveryMethod',
    'subpgmdesc', 'InitialInterestRate','TermInMonths','NaicsCode',	'NaicsDescription', 'ProjectCounty','ProjectState',
    'BusinessType', 'LoanStatusCat','LoanStatus', 'ChargeOffDate', 'GrossChargeOffAmount','unemp_comp','biz_net_income',
    'adj_gross_income','net_cap_gain','total_tax_liab','2018-2010','2010-2000', '2000-1990','T-t0(years)','Cur_T', 'P/E_t','unemp_t','interest_rate_t',
    'GDPchange_t','value'])
    count = 0
    for index, row in df.iterrows():
        count+=1
        if pd.isnull(row["2018-2010"]):
            continue
        if count < 10000000:
            print(count)
            startDate = row['ApprovalDate']
            startDate = startDate.replace(day=1) #make it the first of the month
            lastMonth = 0 #FINAL VALUE
            if pd.isnull(row['ChargeOffDate']): #case where there is no charge off
                termLen = int(row['TermInMonths']/12) #iterate from start thru end
            else: #case where there is a charge off
                chargeOffDate = row['ChargeOffDate']
                chargeOffDate = chargeOffDate.replace(day=1)
                #print(chargeOffDate,startDate)
                #termLen = len([dt for dt in rrule(YEARLY, dtstart=startDate, until=chargeOffDate)])
                termLen = relativedelta(chargeOffDate, startDate).years
                #print(termLen)
                lastMonth = 1
            #MANUALLY ADD t-t0 from data 2 later on!!
            for i in range(termLen):
                #add one month
                originfo = row.tolist() #all the information
                if i ==0:
                    concat_list_0 = [count] + originfo + [i, startDate] + infoDict[startDate] + [0]
                    writer.writerow(concat_list_0)
                originfo = row.tolist()
                t_t0 = i+1
                startDate = startDate + relativedelta(months=12)
                if startDate in infoDict:
                    features = infoDict[startDate]
                else:
                    break
                if i < termLen-1:
                    list2 = [t_t0,startDate, features[0],features[1],features[2],features[3],0]
                else: #equals it
                    list2 = [t_t0,startDate, features[0],features[1],features[2],features[3],lastMonth]
                concat_list = [count]+ originfo + list2
                writer.writerow(concat_list)
