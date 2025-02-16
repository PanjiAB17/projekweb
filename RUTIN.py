import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import datetime
import random
import altair as alt
from dash import Dash, dash_table
from dash import Dash, Input, Output, callback, dash_table

import dash
import dash_table
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

df = pd.read_excel('monitoring.xlsx', sheet_name='RUTIN')

st.write(df)

app = dash.Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        id='tabel',
        columns=[{'name': 'NO', 'id': 'no'}, {'name': 'JUDUL PAKET KONTRAK', 'id': 'judul paket kontrak'}, {'name': 'DISIPLIN', 'id': 'disiplin'}, {'name': 'START DATE', 'id': 'start date'}, {'name': 'END DATE', 'id': 'end date'}, {'name': 'STATUS', 'id': 'status'}, {'name': 'PIC', 'id': 'pic'}, {'name': 'POSISI AKTUAL', 'id': 'posisi aktual'}, {'name': 'NILAI KONTRAK', 'id': 'nilai kontrak'}, {'name': 'TOTAL TAGIHAN', 'id': 'total tagihan'}, {'name': 'SERAPAN ANGGARAN', 'id': 'serapan anggaran'}, {'name': 'AKTUAL PROGRES', 'id': 'aktual proses'}],
        data=[{'NO': '', 'JUDUL PAKET KONTRAK': '', 'DISIPLIN': '', 'START DATE': '', 'END DATE': '', 'STATUS': '', 'PIC': '', 'POSISI AKTUAL': '', 'NILAI KONTRAK': '', 'TOTAL TAGIHAN': '', 'SERAPAN ANGGARAN': '', 'AKTUAL PROGRES': ''}],
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
