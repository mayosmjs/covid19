#static charts that needs to be called before the applayout
import  plotly.graph_objs as go
import data as dt
import folium
import numpy as np
import plotly.express as px
import dash_leaflet as dl
import dash_html_components as html




colors = {
    'background': 'transparent',
    'text': '#7996a9',
    'grid': '#485760',
    'red': '#BF0000'
}

access_token = 'pk.eyJ1IjoiY2ttYXBib3giLCJhIjoiY2s4bHNvM3FhMDRtbjNtbzczc2oyOW55ciJ9.rmWgbvV2cC9Cu6Oxtl3eQw'
mapbox_url = "https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{{z}}/{{x}}/{{y}}{{r}}?access_token={access_token}"




def world_trends():
    traces =[]
    
    traces.append(go.Scatter(
        x=dt.full_data.groupby('Date')['Date'].first(),
        y=dt.full_data.groupby('Date')['Confirmed'].sum(),
        # fill = "tonexty",
        # line=dict(width=0.7),
        # color ="#ac66f5",
        name="Confirmed",
        mode='lines'))

    traces.append(go.Scatter(
        x=dt.full_data.groupby('Date')['Date'].first(),
        y=dt.full_data.groupby('Date')['Active'].sum(),
        # fill = "tonexty",
        # line=dict(width=0.7),
        # color ="#ffc021",
        name="Active",
        mode='lines'))

    traces.append(go.Scatter(
        x=dt.full_data.groupby('Date')['Date'].first(),
        y=dt.full_data.groupby('Date')['Recovered'].sum(),
        # fill = "tonexty",
        # line=dict(width=0.7),
        # color ="#e91e63",
        name="Recovered",
        mode='lines'))

    traces.append(go.Scatter(
        x=dt.full_data.groupby('Date')['Date'].first(),
        y=dt.full_data.groupby('Date')['Deaths'].sum(),
        # fill = "tonexty",
        # line=dict(width=0.7),
        # color ="#00f3e7",
        name="Deaths",
        mode='lines'))


    layout = {  "title": "World Infections Since January 2020",
                "font":dict(color=colors['text']),
                "paper_bgcolor":colors['background'],
                "plot_bgcolor":colors['background'],
                "xaxis":dict(gridcolor=colors['grid']),
                "yaxis":dict(gridcolor=colors['grid']),
                "legend":dict(orientation = 'h'),
                "height":400,
                "margin": dict(l=18,r=5)
            }

    return {
        "data":traces,
        "layout":layout
    }



def world_folium():
    

    return ''


def render_map():
    haversine_series = []
    for index, row in eda.full_data.iterrows():
        haversine_series.append(
        dl.Circle(center=[56.145, 10.21], radius=2000, color='rgb(255,128,0)'))

    map =  dl.Map(style={'width': '100%', 'height': '800px'},
               center=[20, 20],
               zoom=3,
               children=[
                     
                    #  haversine_series[:],

                     dl.TileLayer(url=mapbox_url.format(id="dark-v9", access_token=access_token)),

                     dl.Circle(center=[eda.full_data['Lat'][5], eda.full_data['Long'][7]], radius=6000, color='rgb(255,128,0)'),

                     dl.Circle(center=[43.145, 18.21], radius=4000, color='rgb(255,128,0)'),

                     dl.Circle(center=[34.145, 40.21], radius=2000, color='rgb(255,128,0)')
                   
                  
               ])

    return map