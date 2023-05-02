import math
import pickle
import pathlib
import numpy as np
import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output, State, callback  # pip install dash (version 2.0.0 or higher)
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import dash

prediction_layout = html.Div(
    [
        dbc.Row(
            [
                dbc.Row(
                    [
                        html.Div([
                            html.P("Please fill your personal health information.",style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'1.5em',}),
                        ])
                        
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Label("Name: "),
                                dbc.Input(id="input_name", placeholder="Type Name", type="text"),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Label("BMI: "),
                                        dbc.Input(id="input_bmi", placeholder="Type BMI", type="text", value=""),
                                        dbc.FormText("Please input number"),
                                        dbc.FormFeedback("Valid", type="valid"),
                                        dbc.FormFeedback("Sorry, it's not a number",type="invalid",),
                                    ]
                                ),

                                html.Br(),
                                html.Div(
                                    [
                                        html.Label("SleepTime: "),
                                        dbc.Input(id="input_sleeptime", placeholder="Type SleepTime", type="text", value=""),
                                        dbc.FormText("Please make sure number range within 0 ~ 24"),
                                        dbc.FormFeedback("Valid", type="valid"),
                                        dbc.FormFeedback("Sorry, number range outside 0 ~ 24",type="invalid",),
                                    ]
                                ),
                                html.Br(),
                                html.Label("Sex: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Male", "value": "Male"},
                                        {"label": "Female", "value": "Female"},
                                    ],
                                    id="radio_sex",
                                    inline=True,
                                ),
                                html.Br(),
                                html.Label("Smoking: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes", "value": "Yes"},
                                        {"label": "No", "value": "No"},
                                    ],
                                    id="radio_smoking",
                                    inline=True,
                                ),
                                html.Br(),
                                html.Label("AlcoholDrinking: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes", "value": "Yes"},
                                        {"label": "No", "value": "No"},
                                    ],
                                    id="radio_ad",
                                    inline=True,
                                ),
                                html.Br(),
                                html.Label("Stroke: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes", "value": "Yes"},
                                        {"label": "No", "value": "No"},
                                    ],
                                    id="radio_stroke",
                                    inline=True,
                                ),
                                html.Br(),
                                html.Label("Difficult Walking: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes", "value": "Yes"},
                                        {"label": "No", "value": "No"},
                                    ],
                                    id="radio_dw",
                                    inline=True,
                                ),
                                html.Br(),
                                dbc.Tooltip(
                                    "Body Mass Index (BMI)",
                                    target="input_bmi",
                                ),
                                dbc.Tooltip(
                                    "On average, how many hours of sleep do you get in a 24-hour period?",
                                    target="input_sleeptime",
                                ),
                                dbc.Tooltip(
                                    "Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]",
                                    target="radio_smoking",
                                ),
                                dbc.Tooltip(
                                    "Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week",
                                    target="radio_ad",
                                ),
                                dbc.Tooltip(
                                    "(Ever told) (you had) a stroke?",
                                    target="radio_stroke",
                                ),
                                dbc.Tooltip(
                                    "Do you have serious difficulty walking or climbing stairs?",
                                    target="radio_dw",
                                ),                                                                
                            ],
                            width = 6,
                        ),
                        dbc.Col(
                            [
                                html.Label("Age: "),
                                dbc.Input(id="input_age", placeholder="Type Age", type="text", value=""),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Label("PhysicalHealth: "),
                                        dbc.Input(id="input_ph", placeholder="Type PhysicalHealth", type="text", value=""),
                                        dbc.FormText("Please make sure number range within 0 ~ 30"),
                                        dbc.FormFeedback("Valid", type="valid"),
                                        dbc.FormFeedback("Sorry, number range outside 0 ~ 30", type="invalid",),
                                    ]
                                ),
                                html.Br(),
                                html.Div(
                                    [
                                        html.Label("MentalHealth: "),
                                        dbc.Input(id="input_mh", placeholder="Type MentalHealth", type="text", value=""),
                                        dbc.FormText("Please make sure number range within 0 ~ 30"),
                                        dbc.FormFeedback("Valid", type="valid"),
                                        dbc.FormFeedback("Sorry, number range outside 0 ~ 30",type="invalid",),
                                    ]
                                ),
                                html.Br(),
                                html.Label("Diabetic: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes", "value": "Yes"},
                                        {"label": "No", "value": "No"},
                                    ],
                                    id="radio_diabetic",
                                    inline=True,
                                ),
                                html.Br(),
                                html.Label("PhysicalActivity: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes", "value": "Yes"},
                                        {"label": "No", "value": "No"},
                                    ],
                                    id="radio_pa",
                                    inline=True,
                                ),
                                html.Br(),
                                html.Label("Asthma: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes", "value": "Yes"},
                                        {"label": "No", "value": "No"},
                                    ],
                                    id="radio_asthma",
                                    inline=True,
                                ),
                                html.Br(),
                                html.Label("KidneyDisease: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes", "value": "Yes"},
                                        {"label": "No", "value": "No"},
                                    ],
                                    id="radio_kd",
                                    inline=True,
                                ),
                                html.Br(),
                                html.Label("SkinCancer: "),
                                dbc.RadioItems(
                                    options=[
                                        {"label": "Yes", "value": "Yes"},
                                        {"label": "No", "value": "No"},
                                    ],
                                    id="radio_sc",
                                    inline=True,
                                ),
                                html.Br(),
                                dbc.Tooltip(
                                    "(Ever told) (you had) diabetes?",
                                    target="radio_diabetic",
                                ),
                                dbc.Tooltip(
                                    "Adults who reported doing physical activity or exercise during the past 30 days other than their regular job",
                                    target="radio_pa",
                                ),
                                dbc.Tooltip(
                                    "(Ever told) (you had) asthma?",
                                    target="radio_asthma",
                                ),
                                dbc.Tooltip(
                                    "Not including kidney stones, bladder infection or incontinence, were you ever told you had kidney disease?",
                                    target="radio_kd",
                                ),
                                dbc.Tooltip(
                                    "(Ever told) (you had) skin cancer?",
                                    target="radio_sc",
                                ),
                                dbc.Tooltip(
                                    "Now thinking about your physical health, which includes physical illness and injury, for how many days during the past 30",
                                    target="input_ph",
                                ),
                                dbc.Tooltip(
                                    "Thinking about your mental health, for how many days during the past 30 days was your mental health not good?",
                                    target="input_mh",
                                ),
                            ],   
                            width = 6,
                        )
                    ]
                ),
                dbc.Row(
                    [
                        html.Label("GenHealth: "),
                        dbc.RadioItems(
                            options=[
                                {"label": "Excellent", "value": "Excellent"},
                                {"label": "Very Good", "value": "Very Good"},
                                {"label": "Good", "value": "Good"},
                                {"label": "Fair", "value": "Fair"},
                                {"label": "Poor", "value": "Poor"},
                            ],
                            id="radio_genhealth",
                            inline=True,
                        ),
                        html.Br(),
                        html.Br(),
                        html.Label("Race: "),
                        dbc.RadioItems(
                            options=[
                                {"label": "US Native", "value": "US Native"},
                                {"label": "Asian", "value": "Asian"},
                                {"label": "Black", "value": "Black"},
                                {"label": "Hispanic", "value": "Hispanic"},
                                {"label": "White", "value": "White"},
                                {"label": "Other", "value": "Other"},
                            ],
                            id="radio_race",
                            inline=True,
                        ),
                        dbc.Tooltip(
                            "Would you say that in general your health is...?",
                            target="radio_genhealth",
                        ),                     
                    ]
    
                ),
            ],
            className="mt-4",
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row(
            [
                dbc.Row(
                    [
                        html.P("Health Report", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2.5em', 'text-align':'center'})
                    ]
                ),
                dbc.Row(
                    [
                        html.Hr(style={"borderWidth": "0.7vh", "width": "100%", "borderColor": "gray","opacity": "unset",})
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div([
                                    html.P("Name:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanName", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px", "color":"#7B8FA1"}),
                                ])
                            ]
                        ),
                        dbc.Col(
                            [
                                html.Div([
                                    html.P("Age:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanAge", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px", "color":"#7B8FA1"}),
                                ])
                            ]
                        ),
                        dbc.Col(
                            [
                                html.Div([
                                    html.P("Sex:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanSex", style={'font':'Monospace', 'font-size':'1.5em',  'display': 'inline-block', "margin-left": "15px", "color":"#7B8FA1"}),
                                ])
                            ]
                        ),
                        dbc.Col(
                            [
                                html.Div([
                                    html.P("Race:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanRace", style={'font':'Monospace', 'font-size':'1.5em',  'display': 'inline-block', "margin-left": "15px", "color":"#7B8FA1"}),
                                ])
                            ]
                        ),

                    ]
                ),

                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div([
                                    html.P("Diabetic:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanDiabetic", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px"}),
                                ]),
                                html.Div([
                                    html.P("Smoking:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanSmoking", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px"}),
                                ]),
                                    html.Div([
                                    html.P("Alcohol Drinking:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanAd", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px"}),
                                ]),
                                html.Div([
                                    html.P("Stroke:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanStroke", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px"}),
                                ]),
                                    html.Div([
                                    html.P("Difficult Walking:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanDw", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px"}),
                                ]),
                            ]
                        ),
                        dbc.Col(
                            [
                                html.Div([
                                    html.P("Physical Activity:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanPa", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px"}),
                                ]),
                                html.Div([
                                    html.P("Asthma:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanAsthma", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px"}),
                                ]),
                                    html.Div([
                                    html.P("Kindey Disease:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanKd", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px"}),
                                ]),
                                html.Div([
                                    html.P("Skin Cancer:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanSc", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px"}),
                                ]),
                                html.Div([
                                    html.P("General Health:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    html.Span(id="spanGenHealth", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px", "color": "#5dacbd"}),
                                ]),
                            ]
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        html.Hr(style={"borderWidth": "0.7vh", "width": "100%", "borderColor": "gray","opacity": "unset",})
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P("BMI:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    ], width = 4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        dbc.Progress(id="bar_bmi"),
                                        
                                    ], width = 8
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P("Sleep Time:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    ], width = 4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        dbc.Progress(id="bar_sleep"),
                                        
                                    ], width = 8
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P("Physical Health:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    ], width = 4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        dbc.Progress(id="bar_ph"),
                                        
                                    ], width = 8
                                )
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    [
                                        html.P("Mental Health:", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                    ], width = 4
                                ),
                                dbc.Col(
                                    [
                                        html.Br(),
                                        dbc.Progress(id="bar_mh"),
                                        
                                    ], width = 8
                                )
                            ]
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        html.Hr(style={"borderWidth": "0.7vh", "width": "100%", "borderColor": "gray","opacity": "unset",})
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Row(
                            [
                                html.Div([
                                html.P("Cardiovascular Risk :", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                ]), 
                            ]
                        ),
                        dbc.Row(
                            [
                                # html.P("HIGH", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'3.5em', 'text-align':'center', "color":"#F48484"}),
                                html.Span(id="hd_risk", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'3.5em', 'text-align':'center', "margin-left": "15px"}),
                                # dbc.Col(
                                #     [
                                #         html.P("HIGH", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'3.5em', 'text-align':'center', "color":"#F48484"})
                                #     ], width = 4
                                # ),
                                # dbc.Col(
                                #     [
            
                                #     ], width = 8
                                # )
                            ]
                        ),
                        dbc.Row(
                            [
                                html.Div([
                                html.P("What you can do :", style={'font':'Monospace', 'font-weight': 'bold', 'font-size':'2em', 'display': 'inline-block'}),
                                ]),
                                html.Span(id="advice", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px", "color": "#5dacbd"}),
                                # html.Span("Please reduce the time for smoking.",id="ageRange", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px", "color":"#AACB73"}),
                                # html.Span("Please reduce the amount of alcohol.",id="ageRange", style={'font':'Monospace', 'font-size':'1.5em', 'display': 'inline-block', "margin-left": "15px", "color":"#AACB73"}), 
                            ]
                        ),
                    ]
                ),
                
            ],
            style={"border":"5px solid", "border-radius" : "25px", "padding":'30px', "margin-left":"150px", "margin-right":"150px"}, className='mb-4'
        ),
        dcc.Store(id='pre_res', data=[], storage_type='memory'),
    ]
)

# 檢測數字有沒有在range內
@callback(
    [Output("input_ph", "valid"), Output("input_ph", "invalid")],
    [Input("input_ph", "value")],
)
def check_validity(text):
    if len(text) != 0 and (int(text) <= 30 and int(text) >=0):
        return True, False
    elif len(text) != 0 and (int(text) > 30 or int(text) < 0):
        return False, True
    return False, False

@callback(
    [Output("input_mh", "valid"), Output("input_mh", "invalid")],
    [Input("input_mh", "value")],
)
def check_validity(text):
    if len(text) != 0 and (int(text) <= 30 and int(text) >=0):
        return True, False
    elif len(text) != 0 and (int(text) > 30 or int(text) < 0):
        return False, True
    return False, False

@callback(
    [Output("input_bmi", "valid"), Output("input_bmi", "invalid")],
    [Input("input_bmi", "value")],
)
def check_validity(text):
    if len(text) != 0 and text.isnumeric():
        return True, False
    elif len(text) != 0 and not text.isnumeric():
        return False, True
    return False, False

@callback(
    [Output("input_sleeptime", "valid"), Output("input_sleeptime", "invalid")],
    [Input("input_sleeptime", "value")],
)
def check_validity(text):
    if len(text) != 0 and (int(text) <= 24 and int(text) >=0):
        return True, False
    elif len(text) != 0 and (int(text) > 24 or int(text) < 0):
        return False, True
    return False, False

pass_out_components=["spanName", "spanAge", "spanSex", "spanRace", "spanGenHealth"]
pass_in_components=["input_name", "input_age", "radio_sex", "radio_race", "radio_genhealth"]
for i, out_component in enumerate(pass_out_components):
    @callback(
        Output(component_id=out_component, component_property="children"),
        Input(component_id=pass_in_components[i], component_property="value"),  
    )
    def passValue(text):
        return text

# 多加一個css style在原有的css上
# @callback(
#     Output(component_id="spanSmoking", component_property="children"),
#     Output(component_id="spanSmoking", component_property="style"),
#     Input(component_id="radio_smoking", component_property="value"),
#     State("spanSmoking", "style"),  
# )
# def passSmoking(text, current_style):
#     if text == "Yes":
#         new_style={'color': '#F48484'}
#         update_style={**current_style, **new_style}
#         return "Yes", update_style
#     elif text == "No":
#         new_style={'color': '#AACB73'}
#         update_style={**current_style, **new_style}
#         return "No", update_style
#     else:
#         return "",current_style

component_ids = ["spanSmoking", "spanDiabetic", "spanAd", "spanStroke", "spanDw", "spanPa", "spanAsthma", "spanKd", "spanSc"]
input_ids = ["radio_smoking", "radio_diabetic", "radio_ad", "radio_stroke", "radio_dw", "radio_pa", "radio_asthma", "radio_kd", "radio_sc"]
color_map = {"Yes": "#F48484", "No": "#AACB73"}

for i, component_id in enumerate(component_ids):
    @callback(
        Output(component_id=component_id, component_property="children"),
        Output(component_id=component_id, component_property="style"),
        Input(component_id=input_ids[i], component_property="value"),
        State(component_id, "style"),  
    )
    def update_text_and_style(text, current_style):
        if text in color_map:
            new_style = {'color': color_map[text]}
            update_style = {**current_style, **new_style}
            return text, update_style
        else:
            return "", current_style


@callback(
    Output(component_id="bar_bmi", component_property="label"),
    Output(component_id="bar_bmi", component_property="value"),
    Input(component_id="input_bmi", component_property="value"),  
)
def generate_bar_bmi(input_1):
    if len(input_1) == 0:
        return input_1, 0
    else:
        return input_1, int(input_1)/50*100

@callback(
    Output(component_id="bar_sleep", component_property="label"),
    Output(component_id="bar_sleep", component_property="value"),
    Input(component_id="input_sleeptime", component_property="value"),  
)
def generate_bar_sleep(input_1):
    if len(input_1) == 0:
        return input_1, 0
    else:
        return input_1, int(input_1)/24*100
    
@callback(
    Output(component_id="bar_ph", component_property="label"),
    Output(component_id="bar_ph", component_property="value"),
    Input(component_id="input_ph", component_property="value"),  
)
def generate_bar_ph(input_1):
    if len(input_1) == 0:
        return input_1, 0
    else:
        return input_1, int(input_1)/30*100

@callback(
    Output(component_id="bar_mh", component_property="label"),
    Output(component_id="bar_mh", component_property="value"),
    Input(component_id="input_mh", component_property="value"),  
)
def generate_bar_mh(input_1):
    if len(input_1) == 0:
        return input_1, 0
    else:
        return input_1, int(input_1)/30*100


@callback(
    Output(component_id="pre_res", component_property="data"),
    Input(component_id="radio_smoking", component_property="value"),
    Input(component_id="radio_ad", component_property="value"),  
    Input(component_id="radio_stroke", component_property="value"),  
    Input(component_id="radio_dw", component_property="value"),  
    Input(component_id="radio_pa", component_property="value"), 
    Input(component_id="radio_asthma", component_property="value"),
    Input(component_id="radio_kd", component_property="value"),
    Input(component_id="radio_sc", component_property="value"), 
    Input(component_id="radio_sex", component_property="value"),  
    Input(component_id="radio_diabetic", component_property="value"),  
    Input(component_id="radio_genhealth", component_property="value"),    
    Input(component_id="input_bmi", component_property="value"),  
    Input(component_id="input_ph", component_property="value"),  
    Input(component_id="input_mh", component_property="value"),  
    Input(component_id="input_sleeptime", component_property="value"),
    Input(component_id="input_age", component_property="value"),    
)
def prediction(input1, input2, input3, input4, input5, input6, input7, input8,
               input9, input10, input11, input12, input13, input14, input15, input16):
    para = [input1, input2, input3, input4, input5, input6, input7, input8, input9, input10, input11, input12, input13, input14, input15, input16]
    for i in range(0, 8):
        if para[i] != None and para[i] == "Yes":
            para[i] = 1
        else:
            para[i] = 0

    if para[8] != None and para[8] == "Female":
        para[8] = 0
    else:
        para[8] = 1

    if para[9] != None and para[9] == "Yes":
        para[9] = 3
    else:
        para[9] = 0

    genHealth = {'Poor':0, 'Fair':1, 'Good':2, 'Very Good':3, 'Excellent':4}
    if para[10] == None:
        para[10] = 4
    elif para[10] in genHealth:
        para[10] = genHealth[para[10]]
    
    if len(para[-1]) == 0:
        para[-1] = 0
    elif int(para[-1]) <= 24:
        para[-1] = 0
    elif int(para[-1]) >= 80:
        para[-1] = 12
    else:
        para[-1] = ((int(para[-1]) - 25) / 5) + 1
    
    for i in range(11,15):
        if len(para[i]) == 0:
            para[i] = 0
        else:
            para[i] = int(para[i])
    res = np.array([para[11], para[0], para[1], para[2], para[12], para[13], para[3], para[8], para[-1], para[9], para[4], para[10], para[14], para[5], para[6], para[7]]).reshape(1, -1)

    with open('GBCModel.pkl', 'rb') as f:
        model = pickle.load(f)
        prediction = model.predict(res)

    if prediction == 1:
        return "HIGH"
    else:
        return "LOW"

color_prediction = {"HIGH": "#F48484", "LOW": "#AACB73"}  
@callback(
    Output(component_id="hd_risk", component_property="children"),
    Output(component_id="hd_risk", component_property="style"),
    Input(component_id="pre_res", component_property="data"),
    State("hd_risk", "style"),  
)
def update_text_and_style(text, current_style):
    if text in color_prediction:
        new_style = {'color': color_prediction[text]}
        update_style = {**current_style, **new_style}
        return text, update_style
    else:
        return "", current_style


input_list = ["radio_smoking", "radio_ad", "radio_stroke", "radio_dw", "radio_pa", "radio_asthma", "radio_kd",
              "radio_sc", "radio_diabetic", "input_bmi", "input_sleeptime"]
suggestions = ["Please reduce amount of smoking.",
               "Please reduce amount of alcohol drinking.",
               "Please do exercise regularly and contact your doctor to control stroke.",
               "Please try to regularly participate in rehabilitation.",
               "Please do exercise regularly.",
               "Please contact your doctor to eliminate the chance of asthma.",
               "Please ensure that you eat a light meal.",
               "Please wear sun protection lotion frequently.",
               "Please make sure to maintain a balanced and moderate diet.",
               "Your BMI is too high, please do exercise regularly and keep healthy dietary.",
               "Please have more sleeptime, average over 8 hours a day."]

@callback(
    Output(component_id="advice", component_property="children"),
    [Input(component_id=input, component_property="value") for input in input_list]
)
def update_span_text(*input_values):
    spans = []
    for index, input_value in enumerate(input_values):
        if index == 4:
            if input_value == "No":
                spans.append(html.Span(suggestions[index]))
                spans.append(html.Br())
            else:
                 spans.append(html.Span())
        elif index == 9:
            if len(input_value) != 0 and int(input_value) >= 40:
                spans.append(html.Span(suggestions[index]))
                spans.append(html.Br())
            else:
                 spans.append(html.Span())
        elif index == 10:
            if len(input_value) != 0 and int(input_value) < 8:
                spans.append(html.Span(suggestions[index]))
                spans.append(html.Br())
            else:
                 spans.append(html.Span())
        else:                                         
            if input_value == "Yes":
                spans.append(html.Span(suggestions[index]))
                spans.append(html.Br())
            else:
                spans.append(html.Span())
    return spans
