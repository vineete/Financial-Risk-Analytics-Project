#Anshul Gupta and Vineet Edupuganti
#MS&E 246 Final Project
#preprocess.py

import pandas as pd
import numpy as np


#read in file
#remove all rows that have Loan Status as Cancelled or Exempt

def removeCancelledExempt():
    df = pd.read_excel("/Users/agupta21/Downloads/MSE246/MSE246data_0.xlsx")
    df = df[df.LoanStatus != "CANCLD"]
    df = df[df.LoanStatus != "EXEMPT"]
    df = df[df.LoanStatus.notnull()]
    #df = df[df.Program.notnull()]
    print(df.head)

    df.to_excel("/Users/agupta21/Downloads/MSE246/data_1.xlsx")

#make a total loan amount column (sum of 3rd party dollars + gross approval)
    #added column called LoanSum

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
# df = pd.read_excel("/Users/agupta21/Downloads/MSE246/data1.xlsx")
# for index, row in df.iterrows():
#     if row[]
#make a dummy variable column for gross approval for 0 if null, else 1
