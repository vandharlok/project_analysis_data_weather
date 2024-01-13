from collections import namedtuple
from functools import reduce
import statistics
def segment_data(weather_data, coluna, inicio, fim=None,limiar=None,tipo_limiar='none'):
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

    

    

def showDateData(dict, dia, dado=None, unidade=None):
    if dia not in dict:
        return "Dia não encontrado no dicionário."

    if dado == 'day':
        return f"Dia {dict[dia][0]}"
    elif dado == 'data':
        if unidade == 'celsius':
            return f"{dict[dia][1]} graus {unidade} neste dia"
        elif unidade == '%':
            return f"{dict[dia][1]} {unidade} de umidade neste dia"
        elif unidade == 'km/h':
            return f"{dict[dia][1]} {unidade} neste dia"
        elif unidade == 'mm':
            return f"{dict[dia][1]} {unidade} de precipitação neste dia"
        else:
            return "Unidade desconhecida ou não especificada."
    else:
        return "Tipo de dado desconhecido ou não especificado."
    
def showDataMonth(list,unidade):  
        for data,temperature in list:
            print (f"No dia {data} foi {temperature}  graus {unidade}")
        
#using pandas
def lowestDatas(weather_data,data,days):
    list=[]
    tuple=()
    lowest_data = weather_data.nsmallest(days, data)

    # Acessar as datas correspondentes
    corresponding_dates = lowest_data['Date']

    # Imprimir os resultados
    for date, ndata in zip(corresponding_dates, lowest_data[data]):
        tuple=(date,ndata)
        list.append(tuple)
    return list

def HighestData(weather_data, data,days):
    list=[]
    tuple=()
    highest_data = weather_data.nlargest(days, data)

    # Acessar as datas correspondentes
    corresponding_dates = highest_data['Date']

    # Imprimir os resultados
    for date, ndata in zip(corresponding_dates, highest_data[data]):
        tuple=(date,ndata)
        list.append(tuple)
    return list