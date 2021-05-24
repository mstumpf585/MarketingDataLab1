import plotly.graph_objects as go 
import pandas as pd 

data = pd.read_csv("AFC.csv")

fig = go.Figure()
fig.add_trace(go.Bar(x=data['educat'], y=data['income']))

fig.update_layout(title='Analysis', 
    xaxis_title = "Education",
    xaxis_dtick = 1, 
    yaxis_title = "Income",
    yaxis_dtick=1,)

fig.show()