import dash
import dash_table
import pandas as pd

df = pd.read_parquet('DATA/derechos_de_agua.pq')
df = df.sort_values('CaudalPromedio', ascending=False)

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)