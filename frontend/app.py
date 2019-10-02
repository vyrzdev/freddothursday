import dash
import dash_core_components as dcc
import dash_html_components as html
import dash.dependencies as ddp
import redis
redis_server_address = "35.210.227.246"
redis_server_port = "80"
conn = redis.Redis(host=redis_server_address, port=redis_server_port)
app = dash.Dash(__name__)

def refresh_table():
    dataframe = conn.hgetall("12VCo1")
    table =[html.Tr(className="table-header", children=[html.Th("Student"), html.Th("Total Contributed")] )] + [html.Tr(className="table-row", children = [html.Td(str(x[0])), html.Td(str(x[1]))]) for x in dataframe]
    return table

app.layout = html.Div(id="parent", className="parent", children=[
        html.Div(className = "main", id="main"),
        dcc.Interval(id="interval-component", interval=(1*1000), n_intervals=0)
    ])

@app.callback(ddp.Output('main', 'children'),
              [ddp.Input('interval-component', 'n_intervals')])
def refresh_main(n):
    return [html.H1("Freddo Thursday Leaderboard"), html.Table(classname = "leaderboard", id = "leaderboard", children=refresh_table())]

if __name__ == "__main__":
    app.run_server(debug=True)