import streamlit as st
from streamlit_plotly_events import plotly_events
import plotly.express as px
import pandas as pd


filePath = "../include/Li_ion_battery_figure.xlsx" 
    
df = pd.read_excel(filePath)
print(df)

fig = px.scatter_3d(df, x = 'Year', y = 'Specific Energy (Wh/kg)', z = 'Specific Power (W/kg)',
              color = 'Reference', symbol = 'Reference', size = None, hover_data = {'Year': True, 'Specific Energy (Wh/kg)': True, 'Specific Power (W/kg)': True, 'Reference': True})
fig.update_layout(showlegend=False)
# fig.show()
# fig.write_html("../html/chart.html")

st.plotly_chart(fig, use_container_width=True)
curvenumber = df['Reference'].unique()
# select_event = plotly_events(fig, click_event=True)
# selected_gwc_event = [point for point in select_event]
# # st.write("Selected Event:", selected_gwc_event)
# if selected_gwc_event[0]["x"] is not None:
#     import webbrowser
#     webbrowser.open(curvenumber[selected_gwc_event[0]["curveNumber"]])