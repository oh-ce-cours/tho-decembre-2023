import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go

from dash.dependencies import Input, Output, State
from plotly import tools


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)

server = app.server

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("data").resolve()

# API Requests for news div
news_requests = requests.get(
    "https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=da8e2e705b914f9f86ed2e9692e66012"
)
