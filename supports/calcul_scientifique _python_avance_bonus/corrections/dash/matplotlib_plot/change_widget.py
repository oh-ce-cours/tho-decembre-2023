import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="group",
                    options=[
                        {"label": "Group A", "value": "A"},
                        {"label": "Group B", "value": "B"},
                    ],
                    value="A",
                    style={"font-size": "12px"},
                )
            ]
        ),
        html.Div(id="appRangeSlider"),
    ]
)


@app.callback(Output("appRangeSlider", "children"), [Input("group", "value")])
def plotRangeSlider(group):
    if group == "A":
        return dcc.RangeSlider(
            id="my-range-slider", min=0, max=20, step=0.5, value=[5, 15]
        )
    else:
        return dcc.Dropdown(
            id="my-range-slider",
            options=[{"label": "toto", "value": "tata"}],
            value="tata",
        )


if __name__ == "__main__":
    app.run_server(debug=True)

