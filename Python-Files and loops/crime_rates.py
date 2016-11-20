# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:39:48 2016

@author: toshiba
"""

#Challenge from data quest's Data science -> Python foundation -> Files and loops

crime_rates_file = open("crime_rates.csv")
crime_rates_data = crime_rates_file.read()

crime_rates_raw_list = crime_rates_data.split("\n")
crime_rates_list_of_list = []

for a_value in crime_rates_raw_list:
    a_value_on_split = a_value.split(",")
    crime_rates_list_of_list.append(a_value_on_split)
    
int_crime_rates = []

for each_row in crime_rates_list_of_list:
    crime_rate = each_row[1]
    int_crime_rates.append(crime_rate)
    
print(int_crime_rates)