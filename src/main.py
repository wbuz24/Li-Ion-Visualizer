import plotly.express as px
import pandas as pd


filePath = "../Li-Ion-Visualizer/include/Li_ion_battery_figure.xlsx" 
    
df = pd.read_excel(filePath)
print(df)

fig = px.scatter_3d(df, x='Year', y='Specific Energy (Wh/kg)', z='Specific Power (W/kg)',
              color='Color', hover_data={'Year': True, 'Specific Energy (Wh/kg)': True, 'Specific Power (W/kg)': True, 'Color': False})
fig.update_layout(showlegend=False)
fig.write_html("../Li-Ion-Visualizer/html/chart.html")
