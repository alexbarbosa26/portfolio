from django.http import request
import pandas as pd
import requests
from pandas_datareader import data as wb
from datetime import date
from .models import Nota

def reader_yahoo():
    proxies = {
    'http': 'http://alex.barbosa:tivit123@186.231.6.2:3128',
    #'https': 'https://alex.barbosa:tivit123@186.231.6.2:3128'
    }
    session = requests.Session()
    session.proxies = proxies
    
    no = Nota.objects.values('ativo')    
    tik = []
    for i in no:        
        tik.append(i['ativo']+'.SA',)

    tickers = tik

    data_now = date.today()
    sec_data = pd.DataFrame()

    for t in tickers:
        sec_data[t] = wb.DataReader(t, data_source='yahoo', start='2020-12-04', session=session)['Adj Close']

    return sec_data