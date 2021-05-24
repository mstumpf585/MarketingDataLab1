import plotly.graph_objects as go 
import pandas as pd 

data = pd.read_csv("AFC.csv")

fig = go.Figure()
fig.add_trace(go.Histogram(x=data["age"], name="Age"))
fig.add_trace(go.Histogram(x=data["educat"], name="Education"))
fig.add_trace(go.Histogram(x=data["status"], name="Status"))

fig.update_layout(
    barmode='overlay',
    yaxis2 = dict (
        title="Age"
    ))

fig.update_traces(opacity=.75)
fig.show()
