import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from extends import navbar,footer
import dash_table
from dash_table.Format import Format, Scheme
from app import app
import plotly.express as px
import plotly.graph_objects as go
import data as dt
import gc
import flask
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
import feedparser
import requests
from components import static_charts as sc
# https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/





layout = html.Div([
      	navbar,
            html.Br(),

         html.Div([

             html.H5([
                  "Last updated at (EAT) ", dt.fold_date
                      ],className="text-center text-amber"),
             html.H6([
                  "Our systems updates every 5 Hrs"
                      ],className="text-center text-info text-sm"),


            html.Div([
                   html.Div([
                       dcc.Dropdown(
                           id = "continents_in_the_world",
                           placeholder ="Select a continent",
                           className = "",
                           options = dt.continent_options,
                           value ="Africa",
                           clearable= False
                           
                       ) 
                  ],className = 'col-md-3')
                       
                  ],className="row"),
             
              html.Br(),



#stats
      html.Div([

            html.Div([
                  html.Div([
                        html.Div([
                              html.H4(["Confirmed"
                                    ],className="card-title"),
                              html.H6(["Korona Virus"
                                    ],className="card-subtitle"),
                              dcc.Loading([
                              html.Div(["2.78M+",
                                    ],className="stats__info text-blue",id="stats1")
                              ],color="#ffc021"),

                              html.I(className = "fa fa-bar-chart-o pull-right fa-4x  stats__1 stats__chart  text-blue"),
                             
                              ],className='card-body ')
                        ],className="card")
                  ],className="col-md-3"),



            html.Div([
                  html.Div([
                        html.Div([
                              html.H4(["Recovered cases"
                                    ],className="card-title"),
                              html.H6(["Korona Virus"
                                    ],className="card-subtitle"),
                              dcc.Loading([
                                    html.Div(["2.78M+",
                                    ],className="stats__info text-amber",id="stats4")
                              ],color="#ffc021"),
                              
                              html.I(className = "fa fa-pie-chart pull-right fa-4x  stats__2 stats__chart text-amber"),

                              ],className='card-body ')
                        ],className="card")
                  ],className="col-md-3"),



            html.Div([
                  html.Div([
                        html.Div([
                              html.H4(["Fatality cases"
                                    ],className="card-title"),
                              html.H6(["Korona Virus"
                                    ],className="card-subtitle"),
                              dcc.Loading([
                              html.Div(["2.78M+",
                                    ],className="stats__info text-orange",id="stats3")
                               ],color="#ffc021"),
                             html.I(className = "fa fa-bar-chart-o pull-right fa-4x  stats__3 stats__chart text-orange")

                              ],className='card-body ')
                        ],className="card")
                  ],className="col-md-3"),




            html.Div([
                  html.Div([
                        html.Div([
                              html.H4(["Active Cases"
                                    ],className="card-title"),
                              html.H6(["Korona Virus"
                                    ],className="card-subtitle"),
                              dcc.Loading([
                              html.Div(["2.78M+",
                                    ],className="stats__info text-pink",id="stats2")
                              ],color="#ffc021"),
                              html.I(className = "fa fa-bar-chart-o pull-right fa-4x cdi stats__4 stats__chart text-pink"),

                              ],className='card-body ')
                        ],className="card")
                  ],className="col-md-3"),




            ],className="row"),











#row
html.Div([


#World Map

 html.Div([
        html.Div([
            html.Div([
                  dcc.Loading([
                     dcc.Graph(id="display_map", style={"height": "500px","width":"100%"})
                  ],color="#ffc021")
                 
            ],className="card-body",style={"padding":"0"})
        ],className="card bg-dark")
    ],className='col-md-5'),




#singlc Country Daily Cases
      html.Div([
          html.Div([
            html.Div([

                 dcc.Dropdown(
                          id='new_cases_per_day_input',
                          style={'width': '100%', 'float': 'center'},
                          # options=[{'label': i, 'value': i} for i in eda.countries],
                          options = dt.all_countries_options,
                          value='Kenya',
                          placeholder="Select a city",
                          ),

                 dcc.Loading([
                   dcc.Graph(
                     id="new_cases_per_day")
                  ],color="#ffc021")


                 ],className= 'card-body ')
          ],className = 'card ',style={'background':''}) 
      ],className="col-md-4"),


       html.Div([
        html.Div([
            dcc.Loading(
                 html.Div([

                 ],className="card-body  ",id="display_table",style={"padding":"10","height":"500px"})
            ),
           
        ],className="card stats-table-div")
    ],className='col-md-3 hid-card'),



      ],className="row"),
#End of row











#charts   
      html.Div([
                  html.Div([

                              html.Div([
                              html.Div([
                                    html.Div([
                                            dcc.Dropdown(
                                                  id='select_country',
                                                  multi=True,
                                                  style={'width': '100%', 'float': 'center'},
                                                  # options=[{'label': i, 'value': i} for i in eda.countries],
                                                  options = dt.all_countries_options,
                                                  value= ['China', 'Italy', 'South Korea', 'US', 'Spain', 'France', 'Germany','Iran'],
                                                  placeholder="Select a city",
                                                  ),
                                            html.Div([
                                                 dcc.RadioItems(id='top_ten-input',
                                                options=[{'label': i, 'value': i} for i in ['Confirmed', 'Recovered','Active','Deaths']],
                                                value='Confirmed',
                                                
                                            ),
                                                ],className="radio-toolbar"),
                                           
                                    dcc.Loading([
                                    dcc.Graph(id="top_ten-chart")
                                    ],color="#ffc021")

                                          ],className='card-body')
                                    ],className="card")
                              ],className="col-md-4"),



                        html.Div([
                              html.Div([
                                    html.Div([
                                          html.H4(["World Infections"
                                                ],className="card-title text-amber"),
                                          html.H6(["Korona Virus"
                                                ],className="card-subtitle"),
                                    dcc.Loading([
                                    dcc.Graph(
                                       id="world-chart",
                                       figure = sc.world_trends() 
                                       )
                                    ],color="#ffc021")

                                          ],className='card-body')
                                    ],className="card")
                              ],className="col-md-4"),




                        html.Div([
                          html.Div([
                              html.Div([
                              html.H4(["Google News"],className="card-title text-amber"),
                              html.H6(["Korona Virus"],className="card-subtitle"),
                              html.Hr(),
                              ],className="card-body"),
                              dcc.Loading([ html.Div(id="display_news",style={"height":"383px"})],color="#ffc021")
                          ],className="card news ")
                      ],className='col-md-4')


                  ],className="row")


      
      ])

   ],className="container-fluid"),

footer

])


@app.callback(
    Output('stats1', 'children'),
    [Input('continents_in_the_world', 'value')])
def display_stats1(cont):
    if cont == 'World':
        df = dt.final_merged
    else:
       df = dt.final_merged[dt.final_merged.Continent.eq(cont)]

    value = df[df['Date'] == df['Date'].iloc[-1]]['Confirmed'].sum()
    return  '{:,.0f}'.format(value)



@app.callback(
    Output('stats2', 'children'),
    [Input('continents_in_the_world', 'value')])
def display_stats2(cont):
    if cont == 'World':
        df = dt.final_merged
    else:
        df = dt.final_merged[dt.final_merged.Continent.eq(cont)]

    value = df[df['Date'] == df['Date'].iloc[-1]]['Active'].sum()
    return '{:,.0f}'.format(value)


@app.callback(
    Output('stats3', 'children'),
    [Input('continents_in_the_world', 'value')])
def display_stats3(cont):
    if cont == 'World':
        df = dt.final_merged
    else:
        df = dt.final_merged[dt.final_merged.Continent.eq(cont)]

    value = df[df['Date'] == df['Date'].iloc[-1]]['Deaths'].sum()
    return '{:,.0f}'.format(value)


@app.callback(
    Output('stats4', 'children'),
    [Input('continents_in_the_world', 'value')])
def display_stats4(cont):
    if cont == 'World':
        df = dt.final_merged
    else:
        df = dt.final_merged[dt.final_merged.Continent.eq(cont)]

    value = df[df['Date'] == df['Date'].iloc[-1]]['Recovered'].sum()
    return '{:,.0f}'.format(value)





@app.callback(
    Output("new_cases_per_day","figure"),
    [Input("new_cases_per_day_input","value")]
    )
def display_per_country(country):
    if country == "All":
        data = dt.full_data\
        .groupby(['Date','Country'])\
        .sum()\
        .reset_index()

    else: 
        # full_data.query("country" =="china")
        data = dt.full_data[dt.full_data.Country.eq(country)]\
        .groupby(['Date','Country'])\
        .sum()\
        .reset_index()


    traces =[]
    traces.append(go.Bar(
                x= data['Date'],
                y= data['Confirmed_new_case'],
                name="Confirmed",
                # mode='lines',
                hoverinfo='x+y+name'))
    traces.append(go.Bar(
                x= data['Date'],
                y= data['Recovered_new_case'],
                name='Recovered',
                # mode='lines',
                hoverinfo='x+y+name'))
    traces.append(go.Bar(
                x= data['Date'],
                y= data['Deaths_new_case'],
                name='Deaths',
                # mode='lines',
                hoverinfo='x+y+name'))

     
    layout = {  "title": "Daily Cases in" + " " + str(country),
                "font":dict(color=sc.colors['text']),
                "paper_bgcolor":sc.colors['background'],
                "plot_bgcolor":sc.colors['background'],
                "xaxis":dict(gridcolor=sc.colors['grid']),
                "yaxis":dict(gridcolor=sc.colors['grid'],rangemode='tozero'),
                "legend":dict(orientation = 'h'),
                # "width":1200, 
                "height":400,
                "margin": dict(l=15,r=15),
                "marker": dict(color = ["rgba(169,169,169,1)", "rgba(255,160,122,1)", "rgba(176,224,230,1)", "rgba(255,228,196,1)", "rgba(189,183,107,1)", "rgba(188,143,143,1)", "rgba(221,160,221,1)"])

            }

    return {
        "data":traces,
        "layout":layout
    }



#MAP DISPLAY =========================================================================================

@app.callback(
    Output('display_map', 'figure'),
    [Input('continents_in_the_world', 'value')])

def display_map(value):
    if(value == 'World'):
        data = dt.final_merged[dt.final_merged['Date']  == dt.final_merged['Date'].max()].groupby(['Country','State']).sum().reset_index()
        # data.fillna(0)

    else:
        data = dt.final_merged[dt.final_merged['Continent'] == value]
        data = data[data['Date']  == data['Date'].max()].groupby(['Country','State']).sum().reset_index()

    px.set_mapbox_access_token("pk.eyJ1IjoiY2ttYXBib3giLCJhIjoiY2s4bHNvM3FhMDRtbjNtbzczc2oyOW55ciJ9.rmWgbvV2cC9Cu6Oxtl3eQw")
    color_scale = [
        
        "#f9d67a",
        "#f8d066",
        "#f8c952",
        "#f7c33d",
        "#f6bd29",
        "#f5b614",
        "#F4B000",
        "#eaa900",
        "#e0a200",
        "#dc9e00",
        "#ffc021"
    ]

    data["scaled"] = data["Confirmed"] ** 0.70
    data['scaled'] = data['scaled'].replace(np.nan,5)

    if(value == 'Africa'):
        lat, lon = 2.20,26.46
    elif(value =='Europe'):
        lat, lon = 44.78,48.34
    elif(value =='America'):
        lat, lon = 23,-78.75
    elif(value =='Asia'):
        lat, lon = 43.20,74.53
    elif(value =='Oceania'):
        lat, lon = -12.73, 133.59
    else:
        lat, lon = 20,20

    fig = px.scatter_mapbox(
        data,
        lat="Lat",
        lon="Long",
        color="Confirmed",
        size="scaled",
        size_max=50,
        hover_name= "State" if "State" !=0  else "Country" ,
        hover_data=["State" if "State" !=0  else "Country",  "Confirmed","Recovered", "Deaths",  "Active"],
        color_continuous_scale=color_scale,
    )

    fig.layout.update(
        margin={"r": 0, "t": 0, "l": 0, "b": 0,"pad":0},
        coloraxis_showscale=False,
        mapbox_style="mapbox://styles/ckmapbox/ck9839n580ehd1ip9nbza6q6h",
        # mapbox_style="ck8vbomch1hl61irrt5dxfns3",

        mapbox=dict(center=dict(lat=lat, lon=lon), zoom=2),
    )

    fig.data[0].update(
        hovertemplate="<br>Country/State: <b>%{customdata[0]}</b>,<br><br>Confirmed: %{customdata[1]}, <br>Recovered: %{customdata[2]}<br>Deaths: %{customdata[3]}<br>Active: %{customdata[4]}"
    )


    return fig



    #NEWS ====================================================================================================================================





@app.callback(
    Output('display_news', 'children'),
    [Input('continents_in_the_world', 'value')])
def display_news(value):
    if(value == 'World'):
        value = 'US'
    elif(value == 'Africa'):
        value = 'KE'
    elif(value == 'Europe'):
        value = 'EU'
    elif(value == 'Oceania'):
        value = 'AU'
    else:
        value = 'US'

    rss_url='https://news.google.com/rss/search?q=corona&gl='+value
    #Read feed xml data
    news_feed = feedparser.parse(rss_url) 
    #Flatten data
    df=json_normalize(news_feed.entries)    
    #Read articles links
    # df_news_feed.link.head()
    max_rows = 50

    list_group =  html.Div([
                      html.A([
                        html.Img([
                              ],className="avatar-img",src=app.get_asset_url("images/news.png")),
                        html.Div([
                              html.H4(f"{df.iloc[i]['title'].split(' - ')[0]}.",),
                              html.P(f"{df.iloc[i]['title'].split(' - ')[1]}"),
                              html.Small([f"{df.iloc[i]['published']}"],className="text-amber")
                              ],className="listview__content")
                        ],className="listview__item",href=df.iloc[i]["link"],target="_blank") for i in range(min(len(df), max_rows))
                  ],className="listview listview--hover listview--truncate")

    return list_group



# TOP TEN ===========================================================================================

@app.callback(Output("top_ten-chart","figure"),
             [Input("top_ten-input","value"),
             Input("select_country","value")
             ])
def update_chart_1(columns,countries):
    traces =[]
    for country in countries:
        traces.append(go.Scatter(
                x=dt.full_data[dt.full_data['Country'] == country].groupby('Date')['Date'].first(),
                y=dt.full_data[dt.full_data['Country'] == country].groupby('Date')[columns].sum(),
                name=country,
                mode='lines',
                hoverinfo='x+y+name'))

    layout = {  "title": columns,
                "font":dict(color=sc.colors['text']),
                "paper_bgcolor":sc.colors['background'],
                "plot_bgcolor":sc.colors['background'],
                "xaxis":dict(gridcolor=sc.colors['grid']),
                "yaxis":dict(gridcolor=sc.colors['grid']),
                "legend":dict(orientation = 'h'),
                "height":400,
                "margin": dict(l=30,r=2)
             }

    return {
        "data":traces,
        "layout":layout
    }



# DISPLAY TABLE


@app.callback(
    Output('display_table', 'children'),
    [Input('continents_in_the_world', 'value')])

def display_value(value):
    if(value == 'World'):
        df = dt.final_merged[dt.final_merged['Date']  == dt.final_merged['Date'].max()].groupby(['Country','Lat','Long']).sum().reset_index()
    else:
        df = dt.final_merged[dt.final_merged['Continent'] == value]
        df = df[df['Date']  == df['Date'].max()].groupby('Country').sum().reset_index()

    font_size_body = ".9vw"
    table = dash_table.DataTable(
        data=df.to_dict('records'),
        # id='table',
        # columns=[{"name": i, "id": i} for i in df.columns],

        columns=[
            {"name": "Country", 
             "id": "Country" ,
             "type": "text"
            },
            {
                "name": "Confirmed",
                "id": "Confirmed",
                "type": "numeric",
                "format": Format(group=","),
            },
            {
                "name": "Recovered",
                "id": "Recovered",
                "type": "numeric",
                "format": Format(group=","),
            },

            {
                "name": "Deaths",
                "id": "Deaths",
                "type": "numeric",
                "format": Format(group=","),
            },
        ],

        editable=False,
        sort_action="native",
        sort_mode="multi",
        column_selectable="single",
        style_as_list_view=True,
        fixed_rows={"headers": True},
        # fill_width=False,
        style_table={
            'overflowX': 'scroll',
            'minWidth': '0',
            "width": "100%",
            "height": "100vh",
        },
        style_header={
            "backgroundColor": '#2b3c46',
            "border": '#2b3c46',
            "fontWeight": "bold",
            "font": "Lato, sans-serif",
            "padding": "1.5vh",
            "height": "2vw",
        },
        style_cell={
            "font-size": '.7vw',
            "border-bottom": "0.01rem solid #313841",
            "backgroundColor": "#2b3c46",
            "color": "#FEFEFE",
            "padding": "1.5vh",
        },
        style_cell_conditional=[
            {
                "if": {"column_id": "Country",},
                "minWidth": "5vw",
                "width": "5vw",
                "maxWidth": "5vw",
                "text-align":"center"
            },
            {
                "if": {"column_id": "Confirmed",},
                "color": "#27a4fb",
                "minWidth": "5vw",
                "width": "5vw",
                "maxWidth": "5vw",
                "text-align":"center"
            },
            {
                "if": {"column_id": "Recovered",},
                "color": "#ffc021",
                "minWidth": "5vw",
                "width": "5vw",
                "maxWidth": "5vw",
                "text-align":"center"
            },

            {
                "if": {"column_id": "Deaths",},
                "color": "#E91E63",
                "minWidth": "3vw",
                "width": "3vw",
                "maxWidth": "3vw",
                "text-align":"center"
            },
        ],

        )
    return table