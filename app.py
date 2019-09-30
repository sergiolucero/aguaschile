import dash
import dash_table
import pandas as pd

df = pd.read_parquet('DATA/derechos_de_agua.pq')
df = df.sort_values('Caudal_Promedio', ascending=False)
dfc = list(df.columns)
dfc = dfc[:7]+['Caudal_Promedio']+dfc[7:-1]    # para la visualizacion inmediata
df = df[dfc]

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')   # para poder correrlo en un servidor externo
