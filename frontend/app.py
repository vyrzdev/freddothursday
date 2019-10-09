import dash
import dash_core_components as dcc
import dash_html_components as html
import dash.dependencies as ddp
import redis
#redis_server_address = "localhost"
#redis_server_port = "6379"
#conn = redis.Redis(host=redis_server_address, port=redis_server_port)
app = dash.Dash(__name__)
#Below Function requires renovation. 
def refresh_table():
#    dataframe = conn.hgetall("12VCo1")
    table =[html.Tr(className="table-header", children=[html.Th("Student"), html.Th("Total Contributed")] )] + [html.Tr(className="table-row", children = [html.Td(str(x[0])), html.Td(str(x[1]))]) for x in dataframe]
    return table
tableobject = [html.Tr(className="table-header", children=[html.Th("Student"),html.Th("Total Contribution")]),
        html.Tr(className="table-row", children=[html.Td("Max"), html.Td("0.00")]),
        html.Tr(className="table-row", children=[html.Td("Ben"), html.Td("0.50")])
    ]
#app.layout, is an attribute of the webpage which stores different html objects as a list, data inside the children variables of each
#html object can be modified using callbacks which take input from interactive components and output to the children vars.
app.layout = html.Div(id="parent", className="parent", children=[
        html.Div(className = "main1", id="main"),
        dcc.Interval(id="interval-component", interval=(1*1000), n_intervals=0)
    ])
#Takes input from id='interval-component', from the variable n_intervals, and outputs to the children var of id='main'
#The value outputted is the array returned by the defined function.
@app.callback(ddp.Output('main', 'children'),
              [ddp.Input('interval-component', 'n_intervals')])
def refresh_main(n):
    return [html.H1("Freddo Thursday Leaderboard"), html.Table(className = "leaderboard", id = "leaderboard", children=tableobject)]

if __name__ == "__main__":
    app.run_server(debug=True)
