def segment_data(weather_data,coluna,inicio,fim,limiar=None):
    dados=weather_data[coluna][inicio:fim]
    if limiar is not None:
        dados=[valor for valor in dados if valor > limiar]
    return dados

def ListToDict(lista,unidade):
    days_of_week=["monday","tuesday","wednesday",'thursday','friday','saturday','sunday']
    dict_day={}
    
    for indice,value in enumerate(lista):
        dia=days_of_week[indice]
        dict_day[dia]=f"{value}{unidade}"
        
    return dict_day

