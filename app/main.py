
#project using lambda function, list comprehension, exception and erros, itertolls, logging , collections 
#comecando preciso definir o que cada coluna do meu arquivo csv e
import pandas as pd
import logging
from collections import namedtuple
import modules
import modulexcep 

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
try:
    name_user = input("Hello user, what can I call you?\n")
    modulexcep.ensure_string(name_user)  
    print(f"Hi, {name_user}, I'm a programmer who can provide you with some data about the meteorology in the month of December.")
           
    while True:
        select_weather_user=input("What would you like to know about?\n-Temperature\n-Precipitation of Rain\n-Windspeed\n-Umidity of air\n-Leave\n").lower()
        if select_weather_user == 'leave':
            break
        if select_weather_user == 'temperature':
            try: 
                select_temp_user=float(input("Here are some data I can provide about the temperature:\n1- Monthly Temperatures\n2- Hottest Days of the Month\n3- Coldest Days of the Month\n4-Monthly Temperature Average\n5-Back"
                
            ))
                modulexcep.test_value_user(select_temp_user)
            except ValueError:
                print("Invalid Input. Please enter a valid number")
            except modulexcep.Wrong_input as error:
                print(error.message,error.value)
            if select_temp_user == 1:
                try:
                    select_temp=int(input("Which week would you like to know about:\n1- First week of the month2- Second week of the month\n3- Third week of the month"
                    "4- Last week of the month\n5- Last week of the month\n6- All days of the month\n"
    ))
                    modulexcep.value_selected_user(select_temp)
                except ValueError:
                    print("Invalid input. Please enter a valid number")
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
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
                try:
                    amount_hot_day=int(input("How many of the hottest days would you like to know about?\n"))
                    modulexcep.valid_length_day(temp_month,amount_hot_day)
                    modules.showDataMonth(modules.HighestData(weather_data,'Temperature',amount_hot_day),'Celsius')
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
            elif select_temp_user ==3:
                try:
                    amount_cold_days=int(input("How many of the coldest days would you like to know about?\n"))
                    modulexcep.valid_length_day(temp_month,amount_cold_days)
                    modules.showDataMonth(modules.lowestDatas(weather_data,'Temperature',amount_cold_days),'Celsius')
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
            elif select_temp_user ==4:
                print(f"The average temperature for this month was {average_temp: .2f} degrees Celsius")
        elif select_weather_user == 'precipitation of rain':
            try:
                select_precip_user=float(input("Here are some data I can provide about rainfall:\n1- Monthly Precipitation\n2- Highest Precipitations\n"
                "3- Lowest Precipitations\n4- Monthly Precipitation Average\n"
            ))
                modulexcep.test_value_user(select_precip_user)
            except ValueError:
                print("Invalid input.Please enter a valid number")
            except modulexcep.Wrong_input as error:
                print(error.message,error.value)    
            if select_precip_user == 1:
                select_precip=float(input("Which week would you like to know about:\n1- First week of the month2- Second week of the month\n3- Third week of the month"
                    "4- Last week of the month\n5- Last week of the month\n6- All days of the month\n"))
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
                try:
                    amount_hot_day=int(input("How many days would you like to know about?\n"))
                    modulexcep.valid_length_day(temp_month,amount_hot_day)
                    modules.showDataMonth(modules.HighestData(weather_data,'Precipitation',amount_hot_day),'mm')
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
            elif select_precip_user ==3:
                try:
                    amount_cold_days=int(input("How many days would you like to know about?\n"))
                    modulexcep.valid_length_day(precip_month,amount_cold_days)
                    modules.showDataMonth(modules.lowestDatas(weather_data,'Precipitation',amount_cold_days),'mm')
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)       
            elif select_precip_user ==4:
                print(f"The average precipitation this month was {average_precip: .2f} mm")
        elif select_weather_user == 'windspeed':
            try:
                select_wind_user=float(input("Here are some data I can provide about wind speed:\n1- Wind Speed in the Month\n2- Highest Wind Speeds\n"
                "3- Lowest Wind Speeds\n4- Monthly Wind Speed Average\n"
                
            ))
                modulexcep.test_value_user(select_wind_user)
            except modulexcep.Wrong_input as error:
                print(error.message,error.value)
            if select_wind_user == 1:
                try:
                    select_wind=float(input("Which week would you like to know about:\n1- First week of the month2- Second week of the month\n3- Third week of the month"
                    "4- Last week of the month\n5- Last week of the month\n6- All days of the month\n"))
                    modulexcep.value_selected_user(select_wind)
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
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
                try:
                    amount_hot_day=int(input("How many days would you like to know about?\n"))
                    modulexcep.valid_length_day(wind_speed_month,amount_hot_day)
                    modules.showDataMonth(modules.HighestData(weather_data,'WindSpeed',amount_hot_day),'km/h')
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
            elif select_wind_user ==3:
                try:
                    amount_cold_days=int(input("How many days would you like to know about?\n"))
                    modulexcep.valid_length_day(wind_speed_month,amount_cold_days)
                    modules.showDataMonth(modules.lowestDatas(weather_data,'WindSpeed',amount_cold_days),'km/h')
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
            elif select_wind_user ==4:
                print(f"The average wind speed for this month was {average_precip: .2f} km/h")
        elif select_weather_user == 'umidity of air':
            try:
                select_umid_user=float(input("Here are some data I can provide about air humidity:\n1- Air Humidity in the Month\n2- Highest Humidity Levels\n"
                "3- Lowest Humidity Levels\n4- Monthly Air Humidity Average\n"
            ))
                modulexcep.value_selected_user(select_umid_user)
            except modulexcep.Wrong_input as error:
                print(error.message,error.value)
            if select_umid_user == 1:
                try:
                    select_umid=float(input("Which week would you like to know about:\n1- First week of the month2- Second week of the month\n3- Third week of the month"
                    "4- Last week of the month\n5- Last week of the month\n6- All days of the month\n"))
                    modulexcep.value_selected_user(select_umid)
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
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
                try:
                    amount_hot_day=int(input("How many days would you like to know about?\n"))
                    modulexcep.valid_length_day(humid_month,amount_hot_day)
                    modules.showDataMonth(modules.HighestData(weather_data,'Humidity',amount_hot_day),'%')
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
            elif select_umid_user ==3:
                try:
                    amount_cold_days=int(input("How many days would you like to know about?\n"))
                    modulexcep.valid_length_day(humid_month,amount_cold_days)
                    modules.showDataMonth(modules.lowestDatas(weather_data,'Humidity',amount_cold_days),'%')
                except modulexcep.Wrong_input as error:
                    print(error.message,error.value)
            elif select_umid_user ==4:
                print(f"The average air humidity for this month was {average_precip: .2f} %")
        teste=input('Would you like to know more about?\n').lower()
        if teste == 'yes':
            continue
        else:
            print("Thank u for ur interation")
            break
        

except modulexcep.Wrong_input as error:
    print(error.message)
except ValueError as error:
    print("Invalid input. Please enter a valid number.")