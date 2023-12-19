import math

import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
)
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

options_array = [{"label": name, "value": name} for name in df.continent.unique()]
app.layout = html.Div(
    [
        dcc.Dropdown(
            id="continent-dropdown",
            options=options_array,
            value=options_array[0]["value"],
            multi=True,
        ),
        dcc.Graph(id="graph-with-slider"),
        dcc.Slider(
            id="year-slider",
            min=df["year"].min(),
            max=df["year"].max(),
            value=df["year"].min(),
            marks={str(year): str(year) for year in df["year"].unique()},
            step=None,
        ),
        dash_table.DataTable(id="table"),
    ]
)

## Une fonction qui fait tout
# @app.callback(
#     [
#         Output("graph-with-slider", "figure"),
#         Output("table", "data"),
#         Output("table", "columns"),
#     ],
#     [Input("year-slider", "value"), Input("continent-dropdown", "value")],
# )
# def update_figure_and_table(selected_year, continents):
#     filtered_df = df[df.year == selected_year]
#     traces = []
#     if not isinstance(continents, list):
#         # only 1 continent is selected
#         continents = [continents]
#     print(continents)
#     for continent in continents:
#         df_by_continent = filtered_df[filtered_df["continent"] == continent]
#         traces.append(
#             dict(
#                 x=df_by_continent["gdpPercap"],
#                 y=df_by_continent["lifeExp"],
#                 text=df_by_continent["country"],
#                 mode="markers",
#                 opacity=0.7,
#                 marker={"size": 15, "line": {"width": 0.5, "color": "white"}},
#                 name=continent,
#             )
#         )

#     figure_data = {
#         "data": traces,
#         "layout": dict(
#             xaxis={
#                 "type": "log",
#                 "title": "GDP Per Capita",
#                 "range": [
#                     math.log10(df.gdpPercap.min()),
#                     math.log10(df.gdpPercap.max()),
#                 ],
#             },
#             yaxis={"title": "Life Expectancy", "range": [20, 90]},
#             margin={"l": 40, "b": 40, "t": 10, "r": 10},
#             legend={"x": 0, "y": 1},
#             hovermode="closest",
#             transition={"duration": 500},
#         ),
#     }
#     table_data = df[df.continent.isin(continents)].to_dict("records")
#     columns = [{"name": i, "id": i} for i in sorted(df.columns)]

#     return figure_data, table_data, columns


## Ou une fonction par composant


@app.callback(
    Output("graph-with-slider", "figure"),
    [Input("year-slider", "value"), Input("continent-dropdown", "value")],
)
def update_figure(selected_year, continents):
    filtered_df = df[df.year == selected_year]
    traces = []
    if not isinstance(continents, list):
        # only 1 continent is selected
        continents = [continents]
    print(continents)
    for continent in continents:
        df_by_continent = filtered_df[filtered_df["continent"] == continent]
        traces.append(
            dict(
                x=df_by_continent["gdpPercap"],
                y=df_by_continent["lifeExp"],
                text=df_by_continent["country"],
                mode="markers",
                opacity=0.7,
                marker={"size": 15, "line": {"width": 0.5, "color": "white"}},
                name=continent,
            )
        )

    figure_data = {
        "data": traces,
        "layout": dict(
            xaxis={
                "type": "log",
                "title": "GDP Per Capita",
                "range": [
                    math.log10(df.gdpPercap.min()),
                    math.log10(df.gdpPercap.max()),
                ],
            },
            yaxis={"title": "Life Expectancy", "range": [20, 90]},
            margin={"l": 40, "b": 40, "t": 10, "r": 10},
            legend={"x": 0, "y": 1},
            hovermode="closest",
            transition={"duration": 500},
        ),
    }
    return figure_data


@app.callback(
    [Output("table", "data"), Output("table", "columns")],
    [Input("year-slider", "value"), Input("continent-dropdown", "value")],
)
def update_figure_and_table(selected_year, continents):
    # pour trier le tableau exemple ici :
    # https://dash.plot.ly/datatable/callbacks
    if not isinstance(continents, list):
        # only 1 continent is selected
        continents = [continents]
    print(continents)

    table_data = df[df.continent.isin(continents)].to_dict("records")
    columns = [{"name": i, "id": i} for i in sorted(df.columns)]

    return table_data, columns


if __name__ == "__main__":
    app.run_server(debug=True)
