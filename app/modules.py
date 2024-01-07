from collections import namedtuple
from functools import reduce
import statistics
def segment_data(weather_data, coluna, inicio, fim,limiar=None,tipo_limiar='none'):
    dados = weather_data[inicio:fim].reset_index(drop=True)
    if limiar is not None:
        if tipo_limiar == 'high':
            return [(dados['Date'][indice], valor) for indice, valor in enumerate(dados[coluna]) if valor > limiar]
        elif tipo_limiar == 'low':
            return [(dados['Date'][indice], valor) for indice, valor in enumerate(dados[coluna]) if valor < limiar]
    return [(dados['Date'][indice], valor) for indice, valor in enumerate(dados[coluna])]

def ListToDict(lista):
    days_of_week=["monday","tuesday","wednesday",'thursday','friday','saturday','sunday']
    dict_day={}
    for indice,value in enumerate(lista):
        dia=days_of_week[indice]
        dict_day[dia]=value
        
    return dict_day

def average_weather(weather_data,data):
    average_month=[data for data in weather_data[data]]
    average=statistics.mean(average_month)
    
    return average

