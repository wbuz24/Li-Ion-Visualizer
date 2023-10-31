import plotly.express as px
from plotly.offline import iplot
import chart_studio.tools as tls
import pandas as pd


filePath = "../include/Li_ion_battery_figure.xlsx" 
    
df = pd.read_excel(filePath)
print(df)


fig = px.scatter_3d(df, x='Year', y='Specific Energy (Wh/kg)', z='Specific Power (W/kg)',
              color='Reference', hover_data={'Year': True, 'Specific Energy (Wh/kg)': True, 'Specific Power (W/kg)': True, 'Reference': True})
fig.update_layout(showlegend=True)
# fig.show()
fig.write_html("../html/chart.html")

# fn = "EESCL/Ragone-Plot"

# plot_url = py.iplot(fig, filename=fn, auto_open=False)

# tls.get_embed(plot_url)
