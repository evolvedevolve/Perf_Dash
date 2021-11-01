# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:02:10 2021

A live dashboard to display and log performance during testing
usage: launch the app and youll see your current perf metrics 
        press 'start tracking' to write cpu, memory and ? to the logs
        after the fact the graph is saved??

@author: Patty Whack
"""

import psutil as pu
from datetime import datetime as dt
import time 
import plotly.graph_objs as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

app = dash.Dash(__name__)
cpu_list = []
x_list = []

app.layout = html.Div(children = [
    html.Button('Start', id='start_button', n_clicks=0),
    html.H1('Current Performance'),
    html.H2('CPU: '),
    html.H4(id='cpu_out'),
    dcc.Graph(id='cpu_live_graph', animate=False),
    dcc.Interval(id='metric_update_interval', interval=1*2000, disabled=False, n_intervals=0, max_intervals=-1),
    html.H2('Memory: '),
    html.H4(id='mem_out'),
    html.Button('Record Session')
        ])

@app.callback(
    [Output('cpu_out', 'children'),
     Output('cpu_live_graph', 'figure')],
    Input('metric_update_interval','n_intervals'),
    preventupdate=True,
    )
def do_graph(num_intervals):
    if num_intervals==0:
        print('still at zero')
        raise PreventUpdate       
    x_value = dt.now()
    x_list.append(x_value) 
    cpu = pu.cpu_percent()
    print(cpu, x_value)
    cpu_list.append(cpu)
    #y_data=num_clicks
    fig = go.Figure(data=go.Line(x=x_list, y=cpu_list),layout=go.Layout(yaxis=dict(tickfont=dict(size=22))))
    return cpu, fig

memory = pu.virtual_memory()
app.run_server(debug=True)


#.strftime("%Y/%m/%d-HHMM")
#Input('start_button','n_clicks')
#go.Layout(yaxis=dict(tickfont=dict(size=22))))

#print(cpu)
#print(memory.percent)

# use cputimes percent

# page layout
# header which says "current perf metrics!!!"
# below a div for each cpu and memory (for now)
# print out what each is at in an interval
# 'Start Tracking' button which creates a csv for cpu and memory each
# then it runs and maybe starts real time graphing 
# after the fact maybe with plotly express it generates a save able graph

# needs to load stuff to a csv
# needs to load last ten points from the csv and graph them


# this is for the start_button but i can't make it work
# moving on first to get the csv created and written to
# @app.callback(
#     Output('metric_update_interval','disabled'),
#     Input('start_button','n_clicks')
#     )
# def start_graph(clicks):
#     enabled = False
#     if clicks > 0:
#         enabled = True
#     else:
#         enabled = False
#         raise PreventUpdate
#     return enabled




