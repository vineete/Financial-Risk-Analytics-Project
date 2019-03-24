#mergedata.py

#add info at start date into data1
import pandas as pd
import numpy as np

dfHuge = pd.read_csv('/Users/agupta21/Downloads/MSE246/data_time_series.csv')
dfHuge.drop(columns=['BS','BS','BorrName','BorrStreet','CDC_Name','CDC_Street','ThirdPartyLender_Name','ProjectCounty','NaicsDescription','DeliveryMethod','ApprovalFiscalYear'])
print("DROPPED")
dfHuge.to_csv("/Users/agupta21/Downloads/MSE246/time_series_shortened1.csv")

#
# dfBig = pd.read_excel("/Users/agupta21/Downloads/MSE246/data_1.xlsx")
# dfData = pd.read_excel("/Users/agupta21/Downloads/MSE246/externaldata.xlsx")
#
# peDict = {}
#
#
# for index, row in dfData.iterrows():
#         #in timestamp format
#         peDict[row['Date']] = [row['P/E'],row['Unemployment'],row['Fed_Funds_Rate'],row['GDP_prev_q']]
# count = 0
#
# peList = []
# unempList = []
# fed_fundsList = []
# GDPlist = []
# count = 0
# for index, row in dfBig.iterrows():
#     #first convert date
#     count += 1
#     print(count)
#     date = row['ApprovalDate']
#     date = date.replace(day=1)
#     info = peDict[date] #query
#     peList.append(info[0])
#     unempList.append(info[1])
#     fed_fundsList.append(info[2])
#     GDPlist.append(info[3])
#
# dfBig['P/E_t0'] = peList
# dfBig['unemp_t0'] = unempList
# dfBig['interest_rate_t0'] = fed_fundsList
# dfBig['GDPchange_t0'] = GDPlist
#
# dfBig.to_excel("/Users/agupta21/Downloads/MSE246/data_2.xlsx")
