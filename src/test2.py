import plotly.express as px
import pandas as pd


filePath = "./include/Li_ion_battery_figure.xlsx" 
    
df = pd.read_excel(filePath)

fig = px.scatter_3d(df, x='Year', y='Specific Energy (Wh/kg)', z='Specific Power (W/kg)',
              color='Color')
fig.update_layout(showlegend=False)
fig.write_html("./html/chart1.html")
