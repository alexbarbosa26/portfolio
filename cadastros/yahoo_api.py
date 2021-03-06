import requests
from bs4 import BeautifulSoup
from .models import Cotacao, Nota
from django.db.models import Count, Sum, Avg
from datetime import datetime
from pytz import timezone



def get_yahoo_cotacao():
    proxies = {
    'http': 'http://alex.barbosa:tivit123@proxyop.tivit.bpo:3128',
    'https': 'https://alex.barbosa:tivit123@proxyop.tivit.bpo:3128'
    }
   
    result_compra = Nota.objects.values('ativo').annotate(qt=Sum('quantidade'), preco_f=Sum('total_compra'), custos=Sum('total_custo'), preco_m=Sum('preco'), v_mercado=Sum('preco'), lucro=Sum('preco')).filter(tipo='C')
    result_venda = Nota.objects.values('ativo').annotate(qt=Sum('quantidade'), preco_f=Sum('total_compra'), custos=Sum('total_custo')).filter(tipo='V')
        
    for venda in result_venda:
        for compra in result_compra:
        #compra.quantidade = compra.quantidade - venda.quantidade
            if compra['ativo'] == venda['ativo']:
                compra['qt'] = compra['qt'] - venda['qt']
                compra['preco_f'] = compra['preco_f'] - venda['preco_f']
                compra['custos'] = compra['custos'] - venda['custos']
    
    for compra in result_compra:
        data_e_hora_atuais = datetime.now()
        fuso_horario = timezone('America/Sao_Paulo')
        if compra['qt'] != 0:
            url = 'https://br.financas.yahoo.com/quote/'+compra['ativo']+'.SA'
            #pegando cotação no yahoo            
            response = requests.get(url, '''proxies=proxies''')
            soup = BeautifulSoup(response.text, 'lxml')
            preco_mercado = soup.find_all('div', {'class':'D(ib) Mend(20px)'})[0].find('span').text
            variacao_mercado = soup.find_all('span', {'data-reactid':'33'})[1].text
            mercado_aberto_fechado = soup.find('span', {'data-id':'mk-msg'}).text
            variacao_mercado = variacao_mercado.split(' ')

            Cotacao.objects.filter(ativo=compra['ativo']).update(ativo=compra['ativo'], fechamento_ajustado = preco_mercado, variacao_1 = variacao_mercado[0], variacao_2 = variacao_mercado[1], status_fechado_aberto = mercado_aberto_fechado, data_instante = data_e_hora_atuais.astimezone(fuso_horario))
        else:
            pass            