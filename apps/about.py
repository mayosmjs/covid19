import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from extends import navbar,footer
import dash_bootstrap_components as dbc


from app import app

layout = html.Div([
    navbar,
    html.Br(),

    html.Div([

        html.Div([
            html.H4([
                  "CORONA COVID19 VIRUS"
            ],className="display-5 text-warning"),

            html.P([
            "Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.  Older people, and those with underlying medical problems like cardiovascular disease, diabetes, chronic respiratory disease, and cancer are more likely to develop serious illness.The best way to prevent and slow down transmission is be well informed about the COVID-19 virus, the disease it causes and how it spreads. Protect yourself and others from infection by washing your hands or using an alcohol based rub frequently and not touching your face. The COVID-19 virus spreads primarily through droplets of saliva or discharge from the nose when an infected person coughs or sneezes, so it’s important that you also practice respiratory etiquette (for example, by coughing into a flexed elbow).At this time, there are no specific vaccines or treatments for COVID-19. However, there are many ongoing clinical trials evaluating potential treatments. WHO will continue to provide updated information as soon as clinical findings become available.",

            ],className='text-light'),

            html.A(["For More information visit WORLD HEALTH ORGANISATION"
            ],className="text-warning",href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019"),

            html.Br(), html.Br(), html.Br(),

            html.H4([
                "Disclaimer"
            ],className="text-danger"),

            html.P([
                "Please note! that this website relies solely on data that is publicly available of github from John Hopkins CSSE and news from Google's news API. Hence this data may be highly inaccurate and should not be used as official data whatsoever. Only use for Educational purpose"
            ],className="text-danger")

        ],className="jumbotron bg-dark"),

    footer

],className="container")


])
