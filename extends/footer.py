import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


footer = html.Div([
             html.Div([
                 html.Div([
                     html.Div([
                         html.Div([
                                html.P(["© 2020 CBOORE All rights reserved"],className="transition"),

                                html.Ul([

                                    html.Li([
                                        html.I([
                                        ],className="fa fa-computer fa-2x"),                                     
                                    ],className="list-inline-item"),


                                    html.Li([
                                        html.I([
                                        ],className="fa fa-github fa-2x"),                                     
                                    ],className="list-inline-item"),


                                    html.Li([
                                        html.I([
                                        ],className="fa fa-twitter fa-2x text-info"),                                     
                                    ],className="list-inline-item")


                                ],className="list-inline")

                        
      
                         ],className="copyright")
                     ],className="col-md-12 text-center")
                 ],className="row")
             ],className="container")
            ],className="bottom section-padding")

                 
  

