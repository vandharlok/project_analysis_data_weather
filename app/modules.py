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


def showDateData(dict,day,data,unity=None):
    if day not in dict:
        return "Dia nao encontrado"
    if day =='day':
        return (f" Dia {dict[day][0]}")
    elif data =='data':
        if unity =='celsius':
            return (f"{dict[day][1]} graus {unity} neste dia")
        elif unity =='%':
            return (f"{dict[day][1]} {unity} de umidade neste dia")
        elif unity =='km/h':
            return (f"{dict[day][1]} {unity} neste dia")
        elif unity =='mm':
            return (f"{dict[day][1]} {unity} de precipitacao neste dia")
        else:
            return "Tipo de unidade nao conhecida"
    else:
        return "Tipo de dado desconhecido ou nao especificado"
    
    
def showDataMonth(list,unidade):
        for data,temperature in list:
            return (f"No dia {data} a {temperature} foi graus {unidade}")