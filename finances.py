import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web


quotation_ibov = web.DataReader('^BVSP', data_source='yahoo', start='2020-1-1', end='2020-11-10')
print(quotation_ibov)
quotation_ibov['Adj Close'].plot(figsize=(15, 5))
return_ibov = quotation_ibov['Adj Close'][-1] / quotation_ibov['Adj Close'][0] - 1
print('Retorno de {:.2%}'.format(return_ibov))

#Média móvel da bolsa

quotation_ibov['Adj Close'].plot(figsize=(15, 5), label='IBOV')
quotation_ibov['Adj Close'].rolling(21).mean().plot(label='MM21')
quotation_ibov['Adj Close'].rolling(34).mean().plot(label='MM34')
plt.legend()
plt.show()
