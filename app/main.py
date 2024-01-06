
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
"""
temp_first_week= [temp for temp in weather_data['Temperature'][0:7]]
temp_second_week= [temp for temp in weather_data['Temperature'][7:14]]
temp_third_week= [temp for temp in weather_data['Temperature'][14:21]]
temp_last_week= [temp for temp in weather_data['Temperature'][21:28]]
"""
#forma eficiente, com uso da funcao segment_data
#pegando a temp para as semanas do mes
temp_first_week = modules.segment_data(weather_data,'Temperature', 3, 10)
temp_second_week = modules.segment_data(weather_data,'Temperature', 10, 17)
temp_third_week = modules.segment_data(weather_data,'Temperature', 17, 24)
temp_fourth_week = modules.segment_data(weather_data,'Temperature', 24, 32)

#pegando a humidade para as semanas do mes
humid_first_week = modules.segment_data(weather_data,'Humidity', 3, 10)
humid_second_week = modules.segment_data(weather_data,'Humidity', 10, 17)
humid_third_week = modules.segment_data(weather_data,'Humidity', 17, 24)
humid_fourth_week = modules.segment_data(weather_data,'Humidity', 24, 32)

#pegando a velocidade do vento
wind_speed_first_week = modules.segment_data(weather_data,'WindSpeed', 3, 10)
wind_speed_second_week = modules.segment_data(weather_data,'WindSpeed', 10, 17)
wind_speed_third_week = modules.segment_data(weather_data,'WindSpeed', 17, 24)
wind_speed_fourth_week = modules.segment_data(weather_data,'WindSpeed', 24, 32)


#pegando a precipitacao da chuva
precip_first_week = modules.segment_data(weather_data,'Precipitation', 3, 10)
precip_second_week = modules.segment_data(weather_data,'Precipitation', 10, 17)
precip_third_week = modules.segment_data(weather_data,'Precipitation', 17, 24)
precip_fourth_week = modules.segment_data(weather_data,'Precipitation', 24, 32)


#Pegando as altas temperaturas, ventos fortes, bastante chuva, e humidade alta
high_temp_first_week = modules.segment_data(weather_data,'Temperature', 3, 10,30)
high_temp_second_week = modules.segment_data(weather_data,'Temperature', 10, 17,30)
high_temp_third_week = modules.segment_data(weather_data,'Temperature', 17, 24,30)
high_temp_fourth_week = modules.segment_data(weather_data,'Temperature', 24, 32,30)



#pegando a humidade para as semanas do mes acima de 60, o qual e considerada alta
high_humid_first_week = modules.segment_data(weather_data,'Humidity', 3, 10,60)
high_humid_second_week = modules.segment_data(weather_data,'Humidity', 10, 17,60)
high_humid_third_week = modules.segment_data(weather_data,'Humidity', 17, 24,60)
high_humid_fourth_week = modules.segment_data(weather_data,'Humidity', 24, 32,60)



#pegando a velocidade do vento acima de 20, o qual e considerado alta
high_wind_first_week = modules.segment_data(weather_data,'WindSpeed', 3, 10,20)
high_wind_second_week = modules.segment_data(weather_data,'WindSpeed', 10, 17,20)
high_wind_third_week = modules.segment_data(weather_data,'WindSpeed', 17, 24,20)
high_wind_fourth_week = modules.segment_data(weather_data,'WindSpeed', 24, 32,20)


#pegando a precipitacao da chuva acima de 10, o qual e considera alta
high_precip_first_week = modules.segment_data(weather_data,'Precipitation', 3, 10,10)
high_precip_second_week = modules.segment_data(weather_data,'Precipitation', 10, 17,10)
high_precip_third_week = modules.segment_data(weather_data,'Precipitation', 17, 24,10)
high_precip_fourth_week = modules.segment_data(weather_data,'Precipitation', 24, 32,10)


high_temp_moth=modules.segment_data(weather_data,'Temperature',0,32,30)
high_wind_moth=modules.segment_data(weather_data,'Temperature',0,32,60)
high_humid_moth=modules.segment_data(weather_data,'Temperature',0,32,20)
high_precip_moth=modules.segment_data(weather_data,'Temperature',0,32,10)
#tenho os dados, agora vou pegar esses dados e atribuir 
#vou atribuir um dictionary para que cada posicao da lista seja um dia da semana 
#porem quero criar uma funcao para fazer isso, que recebe essa lista, percorre dando a key e o valor


# vou guardar cada lista em um dict, que cada key e o dia, e o valor e o graus em celsius

dict_temp_week_one= modules.ListToDict(temp_first_week,'celsius')
dict_temp_week_two=modules.ListToDict(temp_second_week,'celsius')
dict_temp_week_three=modules.ListToDict(temp_third_week,'celsius')
dict_temp_week_four=modules.ListToDict(temp_fourth_week,'celsius')

dict_high_temp_week_one=modules.ListToDict(high_temp_first_week,'celsius')

#
#print(dict_temp_week_one['monday'][0][1])
#print(dict_temp_week_two)
#print(dict_temp_week_three)
#print(dict_temp_week_four)
"""
valor_temp=dict_temp_week_one['monday']
partes = valor_temp.split(" ")
temp=partes[1]
print(temp)
"""
#print(high_temp_moth)
#print(dict_temp_week_one)

average_temp=modules.average_weather(weather_data,'Temperature')
average_precip=modules.average_weather(weather_data,'Precipitation')
average_wind=modules.average_weather(weather_data,'WindSpeed')
average_humid=modules.average_weather(weather_data,'Humidity')

print(average_temp)
print(average_humid)
print(average_wind)
print(average_precip)
