import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import random
import altair as alt

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

pages = {
   "Dashboard Monitoring Kontrak": [
       
        st.Page("DASHBOARD.py", title="DASHBOARD"),
        st.Page("RUTIN.py", title="RUTIN"),
        st.Page("NON RUTIN.py", title="NON RUTIN"),
        st.Page("RESUME TSA.py", title="RESUME TSA"),
        st.Page("DM RUTIN.py", title="DM RUTIN"),
        st.Page("DM NON RUTIN.py", title="DM NON RUTIN"),
        st.Page("DATA AREA.py", title="DATA AREA"),
        st.Page("DATA VIEW.py", title="DATA VIEW"),
        st.Page("HISTORY.py", title="HISTORY"),
        st.Page("SEARCH BOX.py", title="SEARCH BOX"),

    ],

}

pg = st.navigation(pages)

pg.run()

