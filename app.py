import dash
import dash_bootstrap_components as dbc


external_stylesheets = [
    # dbc.themes.SLATE,
    "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
]

meta_tags = [
    {
        "name": "description",
        "content": "Coronavirus News, Statistics, and Visualizations",
    },
    {"name": "viewport", "content": "width=device-width, initial-scale=1.0"},
]



app = dash.Dash(__name__, external_stylesheets=external_stylesheets,meta_tags=meta_tags)
server = app.server
app.config.suppress_callback_exceptions = True
