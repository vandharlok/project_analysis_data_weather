from collections import namedtuple
from functools import reduce
import statistics
def segment_data(weather_data, coluna, inicio, fim, limiar=None):
    # Selecionar a fatia de dados junto com as datas
    dados = weather_data[inicio:fim].reset_index(drop=True)

    if limiar is not None:
        # Filtrar dados baseados no limiar e incluir data e valor
        return [(dados['Date'][indice], valor) for indice, valor in enumerate(dados[coluna]) if valor > limiar]

    # Retornar data e valor sem aplicar limiar
    return [(dados['Date'][indice], valor) for indice, valor in enumerate(dados[coluna])]

def ListToDict(lista,unidade):
    days_of_week=["monday","tuesday","wednesday",'thursday','friday','saturday','sunday']
    dict_day={}
    for indice,value in enumerate(lista):
        dia=days_of_week[indice]
        dict_day[dia]=value,unidade
        
    return dict_day

def average_weather(weather_data,data):
    average_month=[data for data in weather_data[data]]
    average=statistics.mean(average_month)
    
    return average