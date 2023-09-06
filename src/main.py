import plotly.express as px
import pandas as pd


filePath = "../Li-Ion-Visualizer/include/Li_ion_battery_figure.xlsx" 
    
df = pd.read_excel(filePath)
print(df)

def update_point(trace, points, selector):
    c = list(scatter.marker.color)
    s = list(scatter.marker.size)
    for i in points.point_inds:
        c[i] = '#bae2be'
        s[i] = 20
        with f.batch_update():
            scatter.marker.color = c
            scatter.marker.size = s

# scatter.on_click(update_point)

fig = px.scatter_3d(df, x='Year', y='Specific Energy (Wh/kg)', z='Specific Power (W/kg)',
              color='Color', hover_data={'Year': True, 'Specific Energy (Wh/kg)': True, 'Specific Power (W/kg)': True, 'Color': False})
fig.update_layout(showlegend=True)
fig.write_html("../Li-Ion-Visualizer/html/chart.html")
