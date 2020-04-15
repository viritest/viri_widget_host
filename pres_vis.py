import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go # https://plotly.com/python/creating-and-updating-figures/#figures-as-graph-objects

import pres_bar_gen

# Step 1. Launch the application
app = dash.Dash()

# Step 2. Import the dataset
#filepath="anat_roots.csv"
#df = pd.read_csv(filepath)
#print(df.head(4))

# Step 2.b - Extra Python Code
## Static Input Incrementation Parameters
min= 50
max= 10000

## Prefabs - Just incase
### Tick Marks to Use w/ Slider
prefab_slider_marks={x:"{} kWh".format(x) for x in range(0,1000+1,100)}

# Step 3. Create a plotly figure
    # go.Scatter
    ## https://plotly.com/python/line-and-scatter/#scatter-and-line-plot-with-goscatter
    ## https://plotly.com/python/reference/#scatter

    # go.Layout
    ## https://plotly.com/python/creating-and-updating-figures/#the-layout-key
    ## title
    ### https://plotly.com/python/reference/#layout-title
    ## hovermode
    ### https://plotly.com/python/reference/#layout-hovermode

    #go.figure
    ## Beautiful Code structure where things fed into figure are defined separately and modularly


# Step 4. Create a Dash layout ( Overall Layout of Site )
    # app.layout

    # html components
    ## https://dash.plotly.com/dash-html-components

    # html.Div
    ## https://dash.plotly.com/dash-html-components/div

    # dcc - Dash Core Components
    ## https://dash.plotly.com/dash-core-components

    # dcc.Graph - Same syntax as plolty, but feeding arguments via Step 3 is good style
    ## https://dash.plotly.com/dash-core-components
app.layout = html.Div([

    # Adding a Header and a Paragraph
    html.Div([
        html.H1("This is first try w/ Dash"),
        html.P("Learning Dash is so interesting!!")
            ],
        style={"padding":"50px",
                "backgroundColor":"hsl(220,100%,65%)"}),
    # # Adding a Plot
    # dcc.Graph(id="plot_id",figure=fig),

    # # From Recipe
    # ## Adding Dropdown from Recipe
    # dcc.Dropdown(
    #     value=['a'],
    #     options=[{'label': i, 'value': i} for i in ['a', 'b', 'c', 'd']],
    #     multi=True,
    #     id='dropdown'
    # ),
    #
    # ## Adding Display of Dropdown Output
    # html.H1(id='output')

    html.Img(
        src="https://virimodo.com/img/phoenix.cb6e2e33.png"
        ),
    # Collect & Display Number Input
    # dcc.Input(
    #     id='input',
    #     type='number',
    #     min=min,
    #     max=max,
    #     ),
    dcc.Slider(
        id='my_slider',
        min=0,
        max=1000,
        step=10,
        marks=prefab_slider_marks,
        value=300
    ),

    dcc.Graph(id='pct_cost_bars')

])

# Step 5. Add callback functions

@app.callback(
    Output('pct_cost_bars', 'figure'),
    [Input('my_slider', 'value')])
def update_output(value):
    print (type(value))
    new_figure = pres_bar_gen.yield_figure(value)
    return new_figure


# Step 6. Add the server clause
if __name__ == "__main__":
    app.run_server(debug=True)
