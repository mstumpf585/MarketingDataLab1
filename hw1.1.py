import plotly.express as px
import numpy as np 

t = np.arange(100)

fig = px.line(x=t, y=120-(3/5)*t, title="test")

# minimum phones sold 
fig.add_hline(y=25)
fig.show()