import dash
import dash_bootstrap_components as dbc


external_stylesheets = [
    # dbc.themes.SLATE,
    "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
]

meta_tags = [
    {
        "name": "description",
        "content": "Live coronavirus news, statistics, and visualizations tracking the number of cases and death toll due to COVID-19, with up-to-date testing center information by US states and counties. Also provides current SARS-COV-2 vaccine progress and treatment research across different countries. Sign up for SMS updates.",
    },
    {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
]



app = dash.Dash(__name__, external_stylesheets=external_stylesheets,meta_tags=meta_tags)
server = app.server
app.config.suppress_callback_exceptions = True