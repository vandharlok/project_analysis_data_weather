
#project using lambda function, list comprehension, exception and erros, itertolls, logging , collections 
#comecando preciso definir o que cada coluna do meu arquivo csv e
import pandas as pd
import logging
from collections import namedtuple
import modules
#caminho para o arquivo CSV
file_data_path= '/Users/vande/Desktop/project_analysis_data_weather/app/weather_data.csv'

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
"""
temp_first_week= [temp for temp in weather_data['Temperature'][0:7]]
temp_second_week= [temp for temp in weather_data['Temperature'][7:14]]
temp_third_week= [temp for temp in weather_data['Temperature'][14:21]]
temp_last_week= [temp for temp in weather_data['Temperature'][21:28]]
"""
#forma eficiente, com uso da funcao segment_data
#pegando a temp para as semanas do mes
temp_first_week = modules.segment_data(weather_data,'Temperature', 0, 7)
temp_second_week = modules.segment_data(weather_data,'Temperature', 7, 14)
temp_third_week = modules.segment_data(weather_data,'Temperature', 14, 21)
temp_last_week = modules.segment_data(weather_data,'Temperature', 21, 28)

#pegando a humidade para as semanas do mes
humid_first_week = modules.segment_data(weather_data,'Humidity', 0, 7)
humid_second_week = modules.segment_data(weather_data,'Humidity', 7, 14)
humid_third_week = modules.segment_data(weather_data,'Humidity', 14, 21)
humid_last_week = modules.segment_data(weather_data,'Humidity', 21, 28)

#pegando a velocidade do vento
wind_speed_first_week = modules.segment_data(weather_data,'WindSpeed', 0, 7)
wind_speed_second_week = modules.segment_data(weather_data,'WindSpeed', 7, 14)
wind_speed_third_week = modules.segment_data(weather_data,'WindSpeed', 14, 21)
wind_speed_last_week = modules.segment_data(weather_data,'WindSpeed', 21, 28)
#pegando a precipitacao da chuva
precip_first_week = modules.segment_data(weather_data,'Precipitation', 0, 7)
precip_second_week = modules.segment_data(weather_data,'Precipitation', 7, 14)
precip_third_week = modules.segment_data(weather_data,'Precipitation', 14, 21)
precip_last_week = modules.segment_data(weather_data,'Precipitation', 21, 28)

#Pegando as altas temperaturas, ventos fortes, bastante chuva, e humidade alta
high_temp_first_week = modules.segment_data(weather_data,'Temperature', 0, 7,30)
high_temp_second_week = modules.segment_data(weather_data,'Temperature', 7, 14,30)
high_temp_third_week = modules.segment_data(weather_data,'Temperature', 14, 21,30)
high_temp_last_week = modules.segment_data(weather_data,'Temperature', 21, 28,30)

#pegando a humidade para as semanas do mes acima de 60, o qual e considerada alta
high_humid_first_week = modules.segment_data(weather_data,'Humidity', 0, 7,60)
high_humid_second_week = modules.segment_data(weather_data,'Humidity', 7, 14,60)
high_humid_third_week = modules.segment_data(weather_data,'Humidity', 14, 21,60)
high_humid_last_week = modules.segment_data(weather_data,'Humidity', 21, 28,60)

#pegando a velocidade do vento acima de 20, o qual e considerado alta
high_wind_speed_first_week = modules.segment_data(weather_data,'WindSpeed', 0, 7,20)
high_wind_speed_second_week = modules.segment_data(weather_data,'WindSpeed', 7, 14,20)
high_wind_speed_third_week = modules.segment_data(weather_data,'WindSpeed', 14, 21,20)
high_wind_speed_last_week = modules.segment_data(weather_data,'WindSpeed', 21, 28,20)
#pegando a precipitacao da chuva acima de 10, o qual e considera alta
high_precip_first_week = modules.segment_data(weather_data,'Precipitation', 0, 7,10)
high_precip_second_week = modules.segment_data(weather_data,'Precipitation', 7, 14,10)
high_precip_third_week = modules.segment_data(weather_data,'Precipitation', 14, 21,10)
high_precip_last_week = modules.segment_data(weather_data,'Precipitation', 21, 28,10)

#tenho os dados, agora vou pegar esses dados e atribuir 
#vou atribuir um dictionary para que cada posicao da lista seja um dia da semana 
#porem quero criar uma funcao para fazer isso, que recebe essa lista, percorre dando a key e o valor



day1=modules.ListToDict(temp_first_week)
day2=modules.ListToDict(temp_second_week)
day3=modules.ListToDict(temp_third_week)
day4=modules.ListToDict(temp_last_week)

