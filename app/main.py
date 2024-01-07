
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
dict_temp_first_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 3, 10))
dict_temp_second_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 10, 17))
dict_temp_third_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 17, 24))
dict_temp_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 24, 32))

#pegando a humidade para as semanas do mes
dict_humid_first_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 3, 10))
dict_humid_second_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 10, 17))
dict_humid_third_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 17, 24))
dict_humid_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 24, 32))

#pegando a velocidade do vento
dict_wind_speed_first_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 3, 10))
dict_wind_speed_second_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 10, 17))
dict_wind_speed_third_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 17, 24))
dict_wind_speed_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 24, 32))


#pegando a precipitacao da chuva
dict_precip_first_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 3, 10))
dict_precip_second_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 10, 17))
dict_precip_third_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 17, 24))
dict_precip_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 24, 32))


#Pegando as altas temperaturas, ventos fortes, bastante chuva, e humidade alta
dict_high_temp_first_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 3, 10,30,'high'))
dict_high_temp_second_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 10, 17,30,'high'))
dict_high_temp_third_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 17, 24,30,'high'))
dict_high_temp_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Temperature', 24, 32,30,'high'))

dict_low_temp_first_week=modules.ListToDict(modules.segment_data(weather_data,'Temperature',3,10,20,'low'))
dict_low_temp_secpnd_firweek=modules.ListToDict(modules.segment_data(weather_data,'Temperature',3,10,20,'low'))
dict_low_temp_third_week=modules.ListToDict(modules.segment_data(weather_data,'Temperature',3,10,20,'low'))
dict_low_temp_fourth_week=modules.ListToDict(modules.segment_data(weather_data,'Temperature',3,10,20,'low'))

#pegando a humidade para as semanas do mes acima de 60, o qual e considerada alta
dict_high_humid_first_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 3, 10,60,'high'))
dict_high_humid_second_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 10, 17,60,'high'))
dict_high_humid_third_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 17, 24,60,'high'))
dict_high_humid_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Humidity', 24, 32,60,'high'))

#arrumar a temp
dict_low_humid_first_week=modules.ListToDict(modules.segment_data(weather_data,'Humidity',3,10,20,'low'))
dict_low_humid_second_week=modules.ListToDict(modules.segment_data(weather_data,'Humidity',3,10,20,'low'))
dict_low_humid_third_week=modules.ListToDict(modules.segment_data(weather_data,'Humidity',3,10,20,'low'))
dict_low_humid_fourth_week=modules.ListToDict(modules.segment_data(weather_data,'Humidity',3,10,20,'low'))

#pegando a velocidade do vento acima de 20, o qual e considerado alta
dict_high_wind_first_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 3, 10,20,'high'))
dict_high_wind_second_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 10, 17,20,'high'))
dict_high_wind_third_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 17, 24,20,'high'))
dict_high_wind_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 24, 32,20,'high'))


dict_low_wind_first_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 3, 10,10,'low'))
dict_low_wind_second_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 10, 17,10,'low'))
dict_low_wind_third_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 17, 24,10,'low'))
dict_low_wind_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'WindSpeed', 24, 32,10,'low'))


dict_high_precip_first_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 3, 10,8,'high'))
dict_high_precip_second_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 10, 17,8,'high'))
dict_high_precip_third_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 17, 24,8,'high'))
dict_high_precip_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 24, 32,8,'high'))

dict_low_precip_first_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 3, 10,2.5,'low'))
dict_low_precip_second_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 10, 17,2.5,'low'))
dict_low_precip_third_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 17, 24,2.5,'low'))
dict_low_precip_fourth_week = modules.ListToDict(modules.segment_data(weather_data,'Precipitation', 24, 32,2.5,'low'))

high_temp_moth=modules.segment_data(weather_data,'Temperature',0,32,30,'high')
high_wind_moth=modules.segment_data(weather_data,'WindSpeed',0,32,20,'high')
high_humid_moth=modules.segment_data(weather_data,'Humidity',0,32,60,'high')
high_precip_moth=modules.segment_data(weather_data,'Precipitation',0,32,8,'high')

low_temp_moth=modules.segment_data(weather_data,'Temperature',0,32,20,'low')
low_wind_moth=modules.segment_data(weather_data,'WindSpeed',0,32,10,'low')
low_humid_moth=modules.segment_data(weather_data,'Humidity',0,32,20,'low')
low_precip_moth=modules.segment_data(weather_data,'Precipitation',0,32,2.5,'low')

average_temp=modules.average_weather(weather_data,'Temperature')
average_precip=modules.average_weather(weather_data,'Precipitation')
average_wind=modules.average_weather(weather_data,'WindSpeed')
average_humid=modules.average_weather(weather_data,'Humidity')


#print(high_temp_moth)
print(modules.showDataMonth(low_temp_moth,'Celsius'))
#print(high_humid_first_week)
#print(average_temp)
#print(average_humid)
#print(average_wind)
#print(average_precip)


#---------------------------- MAIN ------------------------  # INTERFACE
"""
print("Boa tarde usuario \nVou fornecer a voce alguns dados sobre a meteorologia do mes de dezembro")
#fazer um try com excessao para que ele selecione apenas de 1 a 4
select_weather_user=(input("Sobre o que deseja saber?\n-Temperatura\n-Precipitacao da Chuva\n-Velocidade do Vento\n-Humidade do Ar\n"))
if select_weather_user == 'Temperatura':
    select_temp_user=float(input("Aki estao alguns dados que posso fornecer sobre a temperatura:\n1-Temperatura da primeira semana do mes\n2-Temperatura da segunda semana do mes\n"
        "3-Temperatura para terceira semana do mes\n4-Temperatura para quarta semana do mes\n5-Dias mais quentes do mes\n"
        "6-Dias mais frescos do mes\n7-Media da temperatura do mensal"
    ))
    if select_temp_user == 1:
        print(dict_temp_first_week)
"""
 
#print(modules.showDateData(dict_wind_speed_first_week,'monday','data','km'))