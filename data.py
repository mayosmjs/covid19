import requests
import pandas as pd
import numpy as np
import glob
import re
import os
from io import BytesIO
from datetime import date, timedelta
from urllib.request import urlopen
from zipfile import ZipFile
import time
from newsapi import NewsApiClient
import logging
import sys
import requests





apis = {
    'newsapi' : '26c22844bef74367bafc37791a204fea',
    'mapbox': 'pk.eyJ1IjoiY2ttYXBib3giLCJhIjoiY2s4bHNvM3FhMDRtbjNtbzczc2oyOW55ciJ9.rmWgbvV2cC9Cu6Oxtl3eQw'
}



# Read the three features
common_path = 'data/COVID-19-master/csse_covid_19_data/csse_covid_19_time_series/'
raw_confirmed = pd.read_csv(common_path+'time_series_covid19_confirmed_global.csv')
raw_recovered = pd.read_csv(common_path+'time_series_covid19_recovered_global.csv')
raw_deaths    = pd.read_csv(common_path+'time_series_covid19_deaths_global.csv')



#Melt the data
rw_conf = pd.melt(raw_confirmed,id_vars=['Province/State','Country/Region','Lat','Long'],var_name='Date',value_name='Confirmed')
rw_recov = pd.melt(raw_recovered,id_vars=['Province/State','Country/Region','Lat','Long'],var_name='Date',value_name='Recovered')
rw_deaths = pd.melt(raw_deaths,id_vars=['Province/State','Country/Region','Lat','Long'],var_name='Date',value_name='Deaths')

rw_conf['Date'] = pd.to_datetime(rw_conf.Date) #change to date format
rw_recov['Date'] = pd.to_datetime(rw_recov.Date) #change to date format
rw_deaths['Date'] = pd.to_datetime(rw_deaths.Date) #change to date format


#Full join data   https://www.shanelynn.ie/merge-join-dataframes-python-pandas-index-1/
#https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/
full_data = pd.merge(pd.merge(rw_conf,rw_recov,how='left'),rw_deaths,how='left')
full_data['Active'] = (full_data['Confirmed'] - full_data['Recovered'] - full_data['Deaths'])
full_data_2 = pd.melt(full_data,id_vars=['Province/State','Country/Region','Lat','Long','Date'],var_name='Cases')

#merge pdf with continents
continents_csv = pd.read_csv("continents.csv")
full_data.rename(columns = {'Country/Region':'Country','Province/State':'State'}, inplace = True)
final_merged = pd.merge(full_data,continents_csv,on='Country',how='left')
final_merged = final_merged.replace(np.nan, 0)


Africa_data = final_merged[final_merged.Continent.eq("Africa")]
African_countries = sorted(full_data['Country'].unique())

continents = final_merged['Continent'].unique()
continent_options= [ {"label":val[0], "value":val[1]} for val in zip(continents, continents)]
continent_options.append({'label' : 'World','value':'World'})


African_countries_options= [ {"label":val[0], "value":val[1]} for val in zip(African_countries, African_countries)]
African_countries_options.append( {'label' : 'Africa','value':'Africa'} )





# top_5_countries = full_data \
#   .query('Cases == "Active"')\
#   .groupby('Country/Region')\
#   .agg('min')


# new_df = new_df \
#     .query('Emoji !="" ') \
#     .groupby(['Emoji','Name'])\
#     .size()\
#     .reset_index(name="Count")\


African_countries = sorted(full_data['Country'].unique())

sorted_country_df = final_merged[final_merged['Date']  == final_merged['Date'].max()].groupby('Country').sum()

all_countries = sorted(full_data['Country'].unique())
all_countries_options = [{"label":val[0], "value":val[1]} for val in zip(all_countries, all_countries)]



#cases per day
full_data = full_data.sort_values(by=["Country","State","Date"])

cols_to_mutate = ['Confirmed','Deaths','Recovered']
for col in cols_to_mutate:
    full_data[col+'_new_case'] = full_data[col].diff()



a = ['Confirmed_new_case','Deaths_new_case','Recovered_new_case']
for i in a:
    full_data[i] = full_data[i].apply(lambda x: 0 if x <= 0 else x)



# full_data['Confirmed_new_case'] =full_data.Confirmed_new_case.apply(neg_vals)


# dt = full_data[full_data.Country.eq('China')]\
#   .groupby(['Date','Country'])\
#   .sum()\
#   .reset_index()



# Remove negative values
# def neg_vals(val):
#     i = 0 if val < 0 else val
#     return  i


# def zero_if_negative(x):

#     if x < 0:
#         return 0
#     return x


# df['Confirmed_new_case'] = df['Confirmed_new_case'].apply(lambda x: 0 if x <= 0 else x)


# fold_date = time.ctime(os.path.getmtime('data'))

# fold_date = os.stat('data').st_mtime



# read last line from the log file
with open("log.log", "r") as file:
   lastline = (list(file)[-1])
fold_date =  lastline


# with open('output.txt', 'r') as f:
#     lines = f.read().splitlines()
#     last_line = lines[-1]
#     print last_line
