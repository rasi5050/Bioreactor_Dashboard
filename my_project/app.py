#import packages
import os
import sys
import pandas as pd
from dash import Dash, dcc, html
import psycopg2


def main():

    #connecting postgres DB using ENV variables
    conn = psycopg2.connect(database=os.getenv("POSTGRES_DB"),
                            host=os.getenv("POSTGRES_HOST"),
                            user=os.getenv("POSTGRES_USER"),
                            password=os.getenv("POSTGRES_PASSWORD"),
                            port=os.getenv("POSTGRES_PORT"))


    # setting curson to read data from db
    cursor = conn.cursor()

    #read data from each tables to pandas dataframes; all 4 tables cannot be joined 
    #into one single dataframe because the time interval is not consistent between other tables
    cursor.execute("SELECT * FROM \"CM_HAM_DO_AI1/Temp_value\"")

    dataTemp = pd.DataFrame(cursor.fetchall(), columns =['Date', 'Temperature'])

    cursor.execute("SELECT * FROM \"CM_HAM_PH_AI1/pH_value\"")
    dataPh = pd.DataFrame(cursor.fetchall(), columns =['Date', 'pH'])

    cursor.execute("SELECT * FROM \"CM_PID_DO/Process_DO\"")
    dataOxygen = pd.DataFrame(cursor.fetchall(), columns =['Date', 'Distilled Oxygen'])

    cursor.execute("SELECT * FROM \"CM_PRESSURE/Output\"")
    dataPressure = pd.DataFrame(cursor.fetchall(), columns =['Date', 'Pressure'])


    external_stylesheets = [
        {
            "href": (
                "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap"
            ),
            "rel": "stylesheet",
        },
  

        
    ]
    #initializing dash package; ref: https://pypi.org/project/dash/
    app = Dash(__name__, external_stylesheets=external_stylesheets)
    app.title = "BioReactor Dashboard"

    
    #setting up html components with css inline styling; although I was able to load the external css files 
    # when running locally, but not able to run it while inside docker compose, 
    # Hence, I had to modify to inline css to make it work.
    app.layout = html.Div(
        children=[
            html.Div(
                children=[
                    html.P(children="☢️", style={'fontSize': '48px', 'margin': '0 auto', 'text-align': 'center'}),
                    html.H1(
                        children="BioReactor Dashboard", 
                        style={'color': '#FFFFFF', 'fontSize': '48px', 'fontWeight': 'bold', 'textAlign': 'center', 'margin': '0 auto'},
                    ),
                    html.P(
                        children=(
                            "View realtime status of bioreactor"
                        ),
                        style={'color': '#CFCFCF','margin': '4px auto','textAlign': 'center','maxWidth': '584px','fontSize': '26px'},

                    ),
                    html.P(
                        children=(
                            "(Features: select time window along both axeses or in box, double click to reset, auto-refresh the page, download plot as png, pan, zoom)"
                        ),
                        style={'color': '#CFCFCF','margin': '4px auto','textAlign': 'center','maxWidth': '584px','fontSize': '18px'},
                    ),
                ],
                style={'backgroundColor': '#222222','height': '198px','padding': '16px 0 0 0'},
            ),
            html.Div(
                children=[
                    html.Div(
                        #graph components, which plots graph against coordinates axes, 4 of these graphs are used in total
                        children=dcc.Graph(
                            id="temperature-chart",
                            config={"displayModeBar": True},
                            figure={
                                "data": [
                                    {
                                        "x": dataTemp["Date"],
                                        "y": dataTemp["Temperature"],
                                        "type": "lines",
                                        "hovertemplate": (
                                            "$%{y:.2f}<extra></extra>"
                                        ),
                                    },
                                ],
                                "layout": {
                                    "title": {
                                        "text": "Temperature of bioreactors: Time(x-axis) v/s Temperature(Celsius)(y-axis)",
                                        "x": 0.05,
                                        "xanchor": "left",
                                    },
                                    "xaxis": {"fixedrange": False},
                                    "yaxis": {
                                        "tick": "°",
                                        "fixedrange": False,
                                    },
                                    "colorway": ["#17b897"],
                                },
                            },
                        ),
                        style={ 'marginBottom': '24px', 'box-shadow': '0 4px 6px 0 rgba(0, 0, 0, 0.18)'},
                    ),
                    html.Div(
                        children=dcc.Graph(
                            id="pH-chart",
                            config={"displayModeBar": True},
                            figure={
                                "data": [
                                    {
                                        "x": dataPh["Date"],
                                        "y": dataPh["pH"],
                                        "type": "lines",
                                    },
                                ],
                                "layout": {
                                    "title": {
                                        "text": "pH of bioreactor: Time(x-axis) v/s pH(y-axis)",
                                        "x": 0.05,
                                        "xanchor": "left",
                                    },
                                    "xaxis": {"fixedrange": False},
                                    "yaxis": {"fixedrange": False},
                                    "colorway": ["#E12D39"],
                                },
                            },
                        ),
                        style={ 'marginBottom': '24px', 'box-shadow': '0 4px 6px 0 rgba(0, 0, 0, 0.18)'},
                    ),
                    html.Div(
                        children=dcc.Graph(
                            id="oxygen-chart",
                            config={"displayModeBar": True},
                            figure={
                                "data": [
                                    {
                                        "x": dataOxygen["Date"],
                                        "y": dataOxygen["Distilled Oxygen"],
                                        "type": "lines",
                                    },
                                ],
                                "layout": {
                                    "title": {
                                        "text": "Percentage of Distilled oxygen in bioreactor: Time(x-axis) v/s Percentage of Distilled Oxygen(y-axis)",
                                        "x": 0.05,
                                        "xanchor": "left",
                                    },
                                    "xaxis": {"fixedrange": False},
                                    "yaxis": {"fixedrange": False},
                                    "colorway": ["#E12D39"],
                                },
                            },
                        ),
                        style={ 'marginBottom': '24px', 'box-shadow': '0 4px 6px 0 rgba(0, 0, 0, 0.18)'},
                    ),
                    html.Div(
                        children=dcc.Graph(
                            id="pressure-chart",
                            config={"displayModeBar": True},
                            figure={
                                "data": [
                                    {
                                        "x": dataPressure["Date"],
                                        "y": dataPressure["Pressure"],
                                        "type": "lines",
                                    },
                                ],
                                "layout": {
                                    "title": {
                                        "text": "Pressure in bioreactor: Time(x-axis) v/s Pressure(psi)(ya-xis)",
                                        "xaxis_title":"X Axis Title",
                                        "x": 0.05,
                                        "xanchor": "left",
                                    },
                                    "xaxis": {"fixedrange": False},
                                    "yaxis": {"fixedrange": False},
                                    "colorway": ["#E12D39"],
                                },
                            },
                        ),
                        style={ 'marginBottom': '24px', 'box-shadow': '0 4px 6px 0 rgba(0, 0, 0, 0.18)'},
                    ),
                ],
                style={'marginRight': 'auto','marginLeft': 'auto','maxWidth': '1024px','paddingRight': '10px','paddingLeft': '10px','marginTop': '32px'},
            ),
        ]
    )
    #run dash web app
    app.run_server(debug=True,port=8888,host="0.0.0.0")
if __name__ == "__main__":
    main()
    
