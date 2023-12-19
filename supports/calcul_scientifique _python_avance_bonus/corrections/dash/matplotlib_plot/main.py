# https://community.plot.ly/t/is-it-possible-to-use-custom-plotly-offline-iplot-mpl-code-in-dash/6897/3
# https://stackoverflow.com/questions/52615425/matplotlib-to-plotly-offline

# limitations de mpl_to_plotly
# https://community.plot.ly/t/mpl-to-plotly-limitations/14686

import matplotlib.pyplot as plt

import plotly
from plotly.tools import mpl_to_plotly

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9], "o")

plotly_fig = mpl_to_plotly(fig)
graph_mpl = dcc.Graph(id="myGraph", figure=plotly_fig)
graph_plotly = dcc.Graph(
    id="example-graph",
    figure={
        "data": [
            {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
            {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": "Montréal"},
        ],
        "layout": {"title": "Dash Data Visualization"},
    },
)

app.layout = html.Div(
    children=[
        html.H1(children="Hello Dash"),
        html.Div(
            children="""
        Dash: A web application framework for Python.
    """
        ),
        graph_mpl,
        graph_plotly,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

