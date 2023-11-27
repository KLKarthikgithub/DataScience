from pandas_datareader import data as pdr
import yfinance as yf
import pandas as pd
import numpy as np
yf.pdr_override()
data=pdr.get_data_yahoo('amzn','2022-01-01','2022-12-31')
display(data)
data2=pdr.get_data_yahoo('TSLA','2022-01-01','2022-12-31')
display(data2)
x=np.cov(data['Volume'],data2['Volume'])
display(x)
print(data['Volume'].corr(data2['Volume']))
data3=pdr.get_data_yahoo('Flipkart','2022-01-01','2022-12-31')
display(data3)
