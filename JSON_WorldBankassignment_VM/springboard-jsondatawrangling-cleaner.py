import pandas as pd
import json
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt

real_json_df = pd.read_json('/Users/vickimoore/Desktop/Springboard/data_wrangling_json/data/world_bank_projects.json') 
print('=====BOOKKEEPING INFO=====\n')
print(real_json_df.head()) 
print(real_json_df.columns) 
print(real_json_df.info()) 

#for countryname top 10 list
countries = real_json_df['countryname'] 
country_count = countries.value_counts() 
print('\n =====TOP COUNTRIES BY NUMBERS OF PROJECTS=====\n')
print(country_count.head(11)) 
countries = countries[~countries.isin(['Africa'])] #remove Africa as a "country"
country_count = countries.value_counts()
print('\n =====TOP 10 COUNTRIES BY NUMBERS OF PROJECTS WITH ONLY COUNTRIES IN LIST=====\n')
print(country_count.head(10)) 


#for major project theme top 10 list
#make sure reading in string file, not dataframe for normalize
real_json = json.load(open('/Users/vickimoore/Desktop/Springboard/data_wrangling_json/data/world_bank_projects.json'))
real_json = json_normalize(real_json, 'mjtheme_namecode', ['id']) #normalize this string file for these properties, enables meaningful entries for major codes

#for filling in missing names to go with corresponding major theme codes
print('\n =====INVESTIGATIVE CODE TO VIEW THE MISSING THEME NAME FOR CODE 3=====\n')
print(real_json.groupby('name').code.nunique().sort_values(ascending=False).head(11)) #for me to find missing name because name for code 3 wasn't in my truncated output view
print('\n =====ALL ENTRIES ORGANIZED BY THEME=====\n')
print(real_json.sort_values(real_json.columns[0])) #to organize for simplicity for my own viewing 
json_dict = {'1': 'Economic management', '2': 'Public sector governance', '3': 'Rule of law', '4': 'Financial and private sector development', '5': 'Trade and integration', '6': 'Social protection and risk management', '7': 'Social dev/gender/inclusion', '8': 'Human development', '9': 'Urban development', '10': 'Rural development', '11': 'Environment and natural resources management'}
real_json['name'] = real_json['code'].map(json_dict) 
print('\n =====TO CONFIRM FILLED-IN ENTRIES FOR NAMES=====\n')
print(real_json.sort_values(real_json.columns[0])) #so it's organized for me to see the difference in before-after application of dictionary
print('\n =====CONFIRM MATCHING NUMBERS FOR CODES AND FILLED-IN NAMES=====\n')
print(real_json.groupby('code').count()) #confirm match between code and name filled-in entries
names = real_json['name']
name_count = names.value_counts()
print('\n =====MAJOR PROJECT THEME TOP 10 COUNT=====\n')
print(name_count.head(10))

#to explore financial characteristics associated with some of these projects
amounts = real_json_df[['totalcommamt', 'totalamt', 'grantamt', 'ibrdcommamt', 'idacommamt', 'countryname', 'approvalfy']]
amounts_sort = amounts.sort_values('totalcommamt', ascending=False)
print('\n =====PROJECTS WITH THE GREATEST AMOUNTS OF FUNDS COMMITTED=====\n')
print(amounts_sort.head(15))
print('\n =====PROJECTS WITH THE LEAST FUNDS COMMITTED=====\n')
print(amounts_sort.tail(15))

plt.style.use('ggplot')
amounts_sort.iloc[0:14].plot.bar(x='countryname', y=['ibrdcommamt', 'idacommamt'], label='total committed ($)', color=('blue','red'))
plt.title('Highest-ranking amounts of World Bank funds ($ US billions) per project by country\n\n', fontsize=11, fontweight='bold')
plt.xlabel('\nCountry name', fontweight='bold', fontsize=10)
plt.ylabel('World Bank funds ($)\n', fontweight='bold', fontsize=10)
print('\n\n ==PROJECTS WITH THE GREATEST AMOUNTS OF FUNDS COMMITTED BY RECIPIENT COUNTRY==')
plt.show()

