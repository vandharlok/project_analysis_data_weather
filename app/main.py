
#project using lambda function, list comprehension, exception and erros, itertolls, logging , collections 
#comecando preciso definir o que cada coluna do meu arquivo csv e
import pandas as pd
import logging
from collections import namedtuple
import modules
#caminho para o arquivo CSV

try:
    file_data_path= '/Users/vande/Desktop/project_analysis_data_weather/app/weather_data_december.csv'
except:
    print("File not found")
#carregar os dados do meu arquivo csv
#read_csv carrega os dados do csv em um dataframe, que e basicamente uma estrutura de dados bidimensional semelhante a uma tabela.
#voce pode atribuir os dados a uma variavel, mas e mais eficiente trabalhar diretamente com o dataframe.

try:
    weather_data= pd.read_csv(file_data_path)
except:
    print("file not found")




#vou fazer uma filtragem de dados para mostrar como foi os dados de temperatura , humidade, velocidade do vento, precipitacao, em cada semana no mes de dezembro
#pegando a temperatura da semana 1, como o dataframe e basicamente uma tabela bidimensaional, ela se comporta como uma matriz, logo, passo 2 parametros, linha e coluna

#funcao que itera direm


#pegando as temperaturas altas acima de 30 para o mes de dezembro
#forma nao tao eficiente, 
#maneira robusta de guardar dados.

#forma eficiente, com uso da funcao segment_data
#pegando a temp para as semanas do mes
dict_temp_first_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 0, 7))
dict_temp_second_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 7, 14))
dict_temp_third_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 14, 21))
dict_temp_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 21, 28))
dict_temp_last_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 28,None))

#pegando a humidade para as semanas do mes
dict_humid_first_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 0, 7))
dict_humid_second_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 7, 14))
dict_humid_third_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 14, 21))
dict_humid_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 21,28))
dict_humid_last_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 28,None))
#pegando a velocidade do vento
dict_wind_speed_first_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 0, 7))
dict_wind_speed_second_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 7, 14))
dict_wind_speed_third_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 14, 21))
dict_wind_speed_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 21, 28))
dict_wind_speed_last_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 28, None))

#pegando a precipitacao da chuva
dict_precip_first_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 0, 7))
dict_precip_second_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 7, 14))
dict_precip_third_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 14, 21))
dict_precip_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 21, 28))
dict_precip_last_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 28,None))

average_temp=modules.average_weather(weather_data,'Temperature')
average_precip=modules.average_weather(weather_data,'Precipitation')
average_wind=modules.average_weather(weather_data,'WindSpeed')
average_humid=modules.average_weather(weather_data,'Humidity')

#print(modules.showDateData(dict_temp_first_week,'monday','data','celsius'))
#print(dict_temp_last_week)
"""
#---------------------------- MAIN ------------------------  # INTERFACE

print("Boa tarde usuario \nVou fornecer a voce alguns dados sobre a meteorologia do mes de dezembro")
#fazer um try com excessao para que ele selecione apenas de 1 a 4
select_weather_user=(input("Sobre o que deseja saber?\n-Temperatura\n-Precipitacao da Chuva\n-Velocidade do Vento\n-Humidade do Ar\n"))
if select_weather_user == 'Temperatura':
    select_temp_user=float(input("Aki estao alguns dados que posso fornecer sobre a temperatura:\n1-Temperatura da primeira semana do mes\n2-Temperatura da segunda semana do mes\n"
        "3-Temperatura para terceira semana do mes\n4-Temperatura para quarta semana do mes\n5-Dias mais quentes do mes\n"
        "6-Dias mais frescos do mes\n7-Media da temperatura do mensal"
    ))
    if select_temp_user == 1:
        
"""
#print(modules.lowestDatas(weather_data,'Temperature',10))
#print(modules.fiveHighestData(weather_data,'Temperature',10))

print(dict_humid_first_week)