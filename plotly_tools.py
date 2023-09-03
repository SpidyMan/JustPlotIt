#Plotly tools 
# How to change plot data using dropdowns
#
# This example shows how to manually add traces
# to the plot and configure the dropdown to only
# show the specific traces you allow.
import pandas as pd
from plotly import graph_objects as go
fig = go.Figure()
data_file = ".//data/testdata.csv"
df = pd.read_csv(data_file)

# Imports
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

import pandas as pd

app = Dash(__name__)

data_file = ".//data/testdata.csv"
df = pd.read_csv(data_file)

app.layout = html.Div([
    html.Div([
        html.Div([
            dcc.Dropdown(
                df['SERIAL_NUM'].unique(),
                'SEIRAL_NUMBER',
                id='serial_select',multi=True
            )
        ], style={'width': '48%', 'display': 'inline-block'}),

    ]),

    dcc.Graph(id='indicator-graphic'),
])


@callback(
    Output('indicator-graphic', 'figure'),
    Input('serial_select', 'value'))

def update_graph(serial_select):  
    dff = df[df['SERIAL_NUM'] == serial_select.tolist()]
    #print(dff)
    fig = px.line(dff,x='HTR_DAC',y='DETECTOR4',color='SPC_ID',markers='o')
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    return fig


if __name__ == '__main__':
    app.run(debug=False)