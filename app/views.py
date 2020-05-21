from app import app
from flask import render_template
import dash
import pandas as pd
import numpy as np
# import plotly.express as px
import plotly.graph_objects as go
import plotly
# from plotly.subplots import make_subplots
import json

def create_graph(y1, y2):
	trace = go.Bar(
    	    x=['clayton', 'leighton'],
        	y=[y1,y2],
    	)
	data = [trace]
	graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)
	return graphJSON

fig = create_graph(1,2)
fig2 = create_graph(2,1)
name = 'Clayton'

@app.route("/")
def index():
    return render_template("index.html",value=name,graphJSON=fig,graphJSON2=fig2)

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """