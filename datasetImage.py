import pandas as pd
import numpy as np
import plotly.graph_objects as go
from warpdrive import WarpDrive

wd = WarpDrive()

# Define the size of the DataFrame
num_rows = 1000  # Number of rows
num_cols = 5     # Number of columns

# Sample data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]
 
# Create a bar trace
trace = go.Bar(x=categories, y=values)
 
# Create the layout
layout = go.Layout(title='Bar Chart Example', xaxis=dict(title='Categories'), yaxis=dict(title='Values'))
 
# Create the figure
fig = go.Figure(data=[trace], layout=layout)
 
# Display the figure
fig.show()
# Generate random data
data = np.random.rand(num_rows, num_cols)

# Define column names
columns = ['Column_' + str(i+1) for i in range(num_cols)]

# Create DataFrame
df = pd.DataFrame(data, columns=columns)

# Save DataFrame to a CSV file
df.to_csv('random_data.csv', index=False)

# Display the DataFrame
print(df)
