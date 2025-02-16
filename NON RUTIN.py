import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import random
import altair as alt
from dash import dash_table
from dash import Dash, dash_table
from dash import Dash, Input, Output, callback, dash_table

import dash
import dash_table
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_excel('monitoring.xlsx', sheet_name='NON RUTIN')

st.write(df)

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='tabel',
        columns=[{'name': 'NO', 'id': 'no'}, {'name': 'JUDUL PAKET KONTRAK', 'id': 'judul paket kontrak'}, {'name': 'DISIPLIN', 'id': 'disiplin'}, {'name': 'START DATE', 'id': 'start date'}, {'name': 'END DATE', 'id': 'end date'}, {'name': 'PIC', 'id': 'pic'}, {'name': 'STATUS PROSES', 'id': 'status proses'}, {'name': 'TASKLIST', 'id': 'tasklist'}, {'name': 'SERAPAN ANGGARAN', 'id': 'serapan anggaran'}, {'name': 'WO', 'id': 'wo'}, {'name': 'PO', 'id': 'po'}, {'name': 'KETERANGAN', 'id': 'keterangan'}],
        data=[{'NO': '', 'JUDUL PAKET KONTRAK': '', 'DISIPLIN': '', 'START DATE': '', 'END DATE': '', 'PIC': '', 'STATUS PROSES': '', 'TASKLIST': '', 'SERAPAN ANGGARAN': '', 'WO': '', 'PO': '', 'KETERANGAN': ''}],
        editable=True
    ),
])

Output('tabel', 'data'),

[Input('tabel', 'data')],

def update_tabel(data, columns):
    # Lakukan sesuatu dengan data
    return data

# Buat callback untuk menyimpan data ke database
@app.callback(
    Output('simpan-button', 'n_clicks'),
    [Input('simpan-button', 'n_clicks')],
    [Input('tabel', 'data')]

)

def simpan_data(n_clicks, data):
    # Lakukan sesuatu dengan data
    if n_clicks > 0:
        # Simpan data ke database
        return n_clicks + 1
    return n_clicks

if __name__ == '__main__':

    app.run_server(debug=True)

