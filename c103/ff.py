import pandas as pd
import plotly.express as px
ct = pd.read_csv("line_chart.csv")
fig = px.scatter(ct,x = "Country",y = "Per capita income",title = "Per capita income", color = "Country")
fig.show()