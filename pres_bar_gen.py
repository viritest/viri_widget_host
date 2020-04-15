#!/usr/bin/env python
# coding: utf-8

"""This is a test/sandbox program to explore ways to get
relevant text to appear above bars in bar graphs.""";

import plotly.express as px
import numpy as np
import pandas as pd

# Constants
##     """These rates were obtained from con_ed
##    https://www.coned.com/en/save-money/energy-saving-programs/time-of-use"""

rates_dict = {
        "residential":
        {
             "summer":
            {
                "off":1.55/100, # 1.55 cents -> $0.0155
                "on":21.97/100  # 21.97 cents -> $0.2197
            },
            "non_summer":
            {
                "off":1.55/100, # 1.55 cents -> $0.0155
                "on":8.130/100  # 8.130 cents -> $0.08130
            }
        }
}
####################################

# Params per Our Presentation
## For our Presentation, User is "residential"
resid_rates = rates_dict["residential"]

## Finenness of Percentages to Display
resolution_percents = 10
rendered_perecents = np.linspace(0,100,resolution_percents) # Each Value Represents Percentage of On-Peak Usage
####################################

# Useful Helper Functions
def cost_calculate(amt,percent_on_peak,rate_plan,season):
    percent_on_peak*=0.1
    rate_on = rate_plan[season]["on"]
    cost_on = amt*percent_on_peak*rate_on

    rate_off = rate_plan[season]["off"]
    cost_off = amt*(1-percent_on_peak)*rate_off

    return cost_on + cost_off

def gen_bar_data_from_choice(choice):
    user_entered_consumption_text = int(choice)
    amt = user_entered_consumption_text

    #cost_calculate(amt,100,resid_rates,"non_summer") - I think this is unuseful, but need more testing

    summer_bars = [  (pct, cost_calculate(amt,pct,resid_rates,"summer") ) for pct in rendered_perecents]
    non_summer_bars = [  (pct, cost_calculate(amt,pct,resid_rates,"non_summer") ) for pct in rendered_perecents]
    return summer_bars,non_summer_bars
####################################
# These help generate the bar graph once given the data for the bars
## Helper Functions
### Generates percentage lists and cost lists for each bar
def pairs(bars):
    pct_list = [ bar[0]  for bar in bars ]
    cost_list = [ bar[1] for bar in bars]
    return pct_list, cost_list
### Generates dataframes from the input data that goes into each bar
def gen_frame(bars):
    return pd.DataFrame(list(zip(*pairs(bars))), # the * unpacks the tuple returned by "pairs()"
               columns =['% On-Peak', 'Cost $USD'])
## Main Graph Generator
### Generates visualization data for the bars and full graph ( title, labels, etc )
def gen_graph(df):
    fig = px.bar(
        df,
        x="% On-Peak",
        y="Cost $USD",
        text="Cost $USD",
        color="Cost $USD",
        height=800
    )
    fig.update_traces(texttemplate='$%{text:.5s}', textposition='outside')
    fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',title="Percentage of On-Peak Usage vs Cost USD")
    return fig

# In[5]:
def yield_figure(value):
    return gen_graph(gen_frame(gen_bar_data_from_choice(value)[1]  )  )

yield_figure(630).show()
