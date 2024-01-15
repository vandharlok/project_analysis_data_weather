
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
temp_first_week = modules.segment_data(weather_data,'Temperature', 0, 7)
temp_second_week = modules.segment_data(weather_data,'Temperature', 7, 14)
temp_third_week = modules.segment_data(weather_data,'Temperature', 14, 21)
temp_fourth_week = modules.segment_data(weather_data,'Temperature', 21, 28)
temp_last_week = modules.segment_data(weather_data,'Temperature', 28,None)
temp_month=modules.segment_data(weather_data,'Temperature',0,None)

#pegando a humidade para as semanas do mes
humid_first_week = modules.segment_data(weather_data,'Humidity', 0, 7)
humid_second_week = modules.segment_data(weather_data,'Humidity', 7, 14)
humid_third_week = modules.segment_data(weather_data,'Humidity', 14, 21)
humid_fourth_week = modules.segment_data(weather_data,'Humidity', 21,28)
humid_last_week = modules.segment_data(weather_data,'Humidity', 28,None)
humid_month=modules.segment_data(weather_data,'Humidity',0,None)
#pegando a velocidade do vento
wind_speed_first_week = modules.segment_data(weather_data,'WindSpeed', 0, 7)
wind_speed_second_week = modules.segment_data(weather_data,'WindSpeed', 7, 14)
wind_speed_third_week = modules.segment_data(weather_data,'WindSpeed', 14, 21)
wind_speed_fourth_week = modules.segment_data(weather_data,'WindSpeed', 21, 28)
wind_speed_last_week = modules.segment_data(weather_data,'WindSpeed', 28, None)
wind_speed_month=modules.segment_data(weather_data,'WindSpeed',0,None)


#pegando a precipitacao da chuva
precip_first_week = modules.segment_data(weather_data,'Precipitation', 0, 7)
precip_second_week = modules.segment_data(weather_data,'Precipitation', 7, 14)
precip_third_week = modules.segment_data(weather_data,'Precipitation', 14, 21)
precip_fourth_week = modules.segment_data(weather_data,'Precipitation', 21, 28)
precip_last_week = modules.segment_data(weather_data,'Precipitation', 28,None)
precip_month=modules.segment_data(weather_data,'Precipitation',0,None)

average_temp=modules.average_weather(weather_data,'Temperature')
average_precip=modules.average_weather(weather_data,'Precipitation')
average_wind=modules.average_weather(weather_data,'WindSpeed')
average_humid=modules.average_weather(weather_data,'Humidity')




#print(modules.showDateData(dict_temp_first_week,'monday','data','celsius'))
#print(dict_temp_last_week)

#---------------------------- MAIN ------------------------  # INTERFACE
name_user=input("Boa tarde usuario, como voce se chama? \n")
print(f"Boa tarde {name_user}, sou um programa que posso fornecer a voce alguns dados sobre a meteorologia do mes de dezembro")
select_weather_user=input("Sobre o que deseja saber?\n-Temperatura\n-Precipitacao da Chuva\n-Velocidade do Vento\n-Umidade do Ar\n").lower()
if select_weather_user == 'temperatura':
    select_temp_user=float(input("Aki estao alguns dados que posso fornecer sobre a temperatura:\n1-Temperaturas no mes-\n2-Dias mais quentes do mes\n"
        "3-Dias mais frios do mes\n4-Media da temperatura do mensal\n"
    ))
    if select_temp_user == 1:
        select_temp=float(input("Qual semana deseja saber:\n1-Primeira semana do mes\n2-Segunda semana do mes\n3-Terceira semana do mes\n"
              "4-Ultima semana do mes\n5-Ultima semana do mes\n6-Todos dias do mes\n"))
        if select_temp == 1:
            modules.showDataMonth(temp_first_week,'Celsius')
        elif select_temp==2:
            modules.showDataMonth(temp_second_week,'Celsius')
        elif select_temp ==3:
            modules.showDataMonth(temp_third_week,'Celsius')
        elif select_temp ==4:
            modules.showDataMonth(temp_fourth_week,'Celsius')
        elif select_temp ==5:
            modules.showDataMonth(temp_last_week,'Celsius')
        elif select_temp ==6:
            modules.showDataMonth(temp_month,'Celsius')
    elif select_temp_user ==2:
        amount_hot_day=int(input("Qual a quantidade de dias mais quentes deseja saber?\n"))
        modules.showDataMonth(modules.HighestData(weather_data,'Temperature',amount_hot_day),'Celsius')
    elif select_temp_user ==3:
        amount_cold_days=int(input("Qual a quantidade de dias mais frios deseja saber?\n"))
        modules.showDataMonth(modules.lowestDatas(weather_data,'Temperature',amount_cold_days),'Celsius')
    elif select_temp_user ==4:
        print(f"A media da temperatura nesse mes foi {average_temp: .2f} Graus Celsius")
elif select_weather_user == 'precipitacao da chuva':
    select_precip_user=float(input("Aki estao alguns dados que posso fornecer sobre a precipitacao da chuva:\n1-Precipitacao no mes-\n2-Precipitacoes mais altas\n"
        "3-Precipitacoes mais baixas\n4-Media da precipitacao mensal\n"
    ))
    if select_precip_user == 1:
        select_precip=float(input("Qual semana deseja saber:\n1-Primeira semana do mes\n2-Segunda semana do mes\n3-Terceira semana do mes\n"
              "4-Ultima semana do mes\n5-Ultima semana do mes\n6-Todos dias do mes\n"))
        if select_precip == 1:
            modules.showDataMonth(precip_first_week,'mm')
        elif select_precip==2:
            modules.showDataMonth(precip_second_week,'mm')
        elif select_precip ==3:
            modules.showDataMonth(precip_third_week,'mm')
        elif select_precip ==4:
            modules.showDataMonth(precip_fourth_week,'mm')
        elif select_precip ==5:
            modules.showDataMonth(precip_last_week,'mm')
        elif select_precip ==6:
            modules.showDataMonth(precip_month,'mm')
    elif select_precip_user ==2:
        amount_hot_day=int(input("Qual a quantidade de dias deseja saber?\n"))
        modules.showDataMonth(modules.HighestData(weather_data,'Precipitation',amount_hot_day),'mm')
    elif select_precip_user ==3:
        amount_cold_days=int(input("Qual a quantidade de dias deseja saber?\n"))
        modules.showDataMonth(modules.lowestDatas(weather_data,'Precipitation',amount_cold_days),'mm')
    elif select_precip_user ==4:
        print(f"A media de precipitacao nesse mes foi {average_precip: .2f} mm")
elif select_weather_user == 'velocidade do vento':
    select_wind_user=float(input("Aki estao alguns dados que posso fornecer sobre a velocidade do vento:\n1-Velocidade do vento no mes-\n2-Velocidade mais altas\n"
        "3-Velocidade mais baixas\n4-Media da velocidade mensal\n"
    ))
    if select_wind_user == 1:
        select_wind=float(input("Qual semana deseja saber:\n1-Primeira semana do mes\n2-Segunda semana do mes\n3-Terceira semana do mes\n"
              "4-Ultima semana do mes\n5-Ultima semana do mes\n6-Todos dias do mes\n"))
        if select_wind == 1:
            modules.showDataMonth(precip_first_week,'km/h')
        elif select_wind==2:
            modules.showDataMonth(precip_second_week,'km/h')
        elif select_wind ==3:
            modules.showDataMonth(precip_third_week,'km/h')
        elif select_wind ==4:
            modules.showDataMonth(precip_fourth_week,'km/h')
        elif select_wind ==5:
            modules.showDataMonth(precip_last_week,'km/h')
        elif select_wind ==6:
            modules.showDataMonth(precip_month,'km/h')
    elif select_wind_user ==2:
        amount_hot_day=int(input("Qual a quantidade de dias deseja saber?\n"))
        modules.showDataMonth(modules.HighestData(weather_data,'WindSpeed',amount_hot_day),'km/h')
    elif select_wind_user ==3:
        amount_cold_days=int(input("Qual a quantidade de dias deseja saber?\n"))
        modules.showDataMonth(modules.lowestDatas(weather_data,'WindSpeed',amount_cold_days),'km/h')
    elif select_wind_user ==4:
        print(f"A media da velocidad do vento nesse mes foi {average_precip: .2f} km/h")
elif select_weather_user == 'umidade do ar':
    select_umid_user=float(input("Aki estao alguns dados que posso fornecer sobre a umidade do ar:\n1-Umidade do ar no mes-\n2-Umidades mais altas\n"
        "3-Umidades mais baixas\n4-Media da umidade do ar mensal\n"
    ))
    if select_umid_user == 1:
        select_umid=float(input("Qual semana deseja saber:\n1-Primeira semana do mes\n2-Segunda semana do mes\n3-Terceira semana do mes\n"
              "4-Ultima semana do mes\n5-Ultima semana do mes\n6-Todos dias do mes\n"))
        if select_umid == 1:
            modules.showDataMonth(precip_first_week,'%')
        elif select_umid==2:
            modules.showDataMonth(precip_second_week,'%')
        elif select_umid ==3:
            modules.showDataMonth(precip_third_week,'%')
        elif select_umid ==4:
            modules.showDataMonth(precip_fourth_week,'%')
        elif select_umid ==5:
            modules.showDataMonth(precip_last_week,'%')
        elif select_umid ==6:
            modules.showDataMonth(precip_month,'%')
    elif select_umid_user ==2:
        amount_hot_day=int(input("Qual a quantidade de dias deseja saber?\n"))
        modules.showDataMonth(modules.HighestData(weather_data,'Humidity',amount_hot_day),'%')
    elif select_umid_user ==3:
        amount_cold_days=int(input("Qual a quantidade de dias deseja saber?\n"))
        modules.showDataMonth(modules.lowestDatas(weather_data,'Humidity',amount_cold_days),'%')
    elif select_umid_user ==4:
        print(f"A media da umidade do ar nesse mes foi {average_precip: .2f} %")