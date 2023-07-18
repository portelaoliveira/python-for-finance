import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from datetime import datetime
import yfinance as yf

carteira = pd.read_excel('Carteira.xlsx')
# print(carteira)

cotacoes_carteira = pd.DataFrame()
yf.pdr_override()
start_date = datetime(2022, 4, 1)
end_date = datetime(2023, 7, 18)

for ativo in carteira['Ativos']:
    cotacoes_carteira[ativo] = web.get_data_yahoo('{}.SA'.format(ativo), start=start_date, end=end_date)['Adj Close']
    
# print(cotacoes_carteira)

#df_media = cotacoes_carteira.mean()
#cotacoes_carteira = cotacoes_carteira.fillna(df_media)
cotacoes_carteira = cotacoes_carteira.ffill()
# cotacoes_carteira.info()

carteira_norm = cotacoes_carteira / cotacoes_carteira.iloc[0]
carteira_norm.plot(figsize=(15, 5))
plt.legend(loc='upper left')
# plt.show()

indeces = '^BVSP'
cotacao_ibov = web.get_data_yahoo(indeces, start=start_date, end=end_date)
print(cotacao_ibov)
