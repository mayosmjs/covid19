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

                                            dcc.RadioItems(id='top_ten-input',
                                                options=[{'label': i, 'value': i} for i in ['Confirmed', 'Recovered','Active','Deaths']],
                                                value='Confirmed',
                                                
                                            ),
                              
                                    dcc.Graph(id="top_ten-chart")

                                          ],className='card-body')
                                    ],className="card")
                              ],className="col-md-4"),



                        html.Div([
                              html.Div([
                                    html.Div([
                                          html.H4(["World Infections"
                                                ],className="card-title text-amber"),
                                          html.H6(["Corona Virus"
                                                ],className="card-subtitle"),

                                          dcc.Graph(
                                       id="world-chart",
                                       figure = sc.world_trends() 
                                       )
                                          ],className='card-body')
                                    ],className="card")
                              ],className="col-md-4"),