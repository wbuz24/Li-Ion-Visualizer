from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
from base64 import b64encode
import io

app = Dash(__name__)

buffer = io.StringIO("Ragone.html")

df = pd.read_excel("../Li-Ion-Visualizer/include/Li_ion_battery_figure.xlsx") # replace with your own data source
fig = px.scatter_3d(df, x='Year', y='Specific Energy (Wh/kg)', z='Specific Power (W/kg)',
              color='Color', hover_data={'Year': True, 'Specific Energy (Wh/kg)': True, 'Specific Power (W/kg)': True, 'Color': False})
fig.write_html(buffer)

html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

app.layout = html.Div([
    html.H4('Simple plot export options'),
    html.P("↓↓↓ try downloading the plot as PNG ↓↓↓", style={"text-align": "right", "font-weight": "bold"}),
    dcc.Graph(id="graph", figure=fig),
    html.A(
        html.Button("Download as HTML"), 
        id="download",
        href="data:text/html;base64," + encoded,
        download="ragone_graph.html"
    )
])


app.run_server(debug=True)
