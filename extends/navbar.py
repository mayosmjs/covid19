import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


navbar =  navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("ABOUT", href="/about")),
        dbc.NavItem(dbc.NavLink("HOPKINS CSSE", href="https://github.com/CSSEGISandData/COVID-19",target="_blank")),
        dbc.NavItem(dbc.NavLink("WHO", href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019",target="_blank")),
        dbc.NavItem(dbc.NavLink("DISCLAIMER", href="/about")),

    ],
    brand="VIRUSI VYA KOVID19",
    brand_href="/",
    color="dark",
    dark=True,
)



