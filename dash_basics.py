import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc 

airline_data = pd.read_csv('course_8 for Pr/airline_data.csv')
airline_data.head()  


# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup', title='Distance group proportion by flights')

# Create a dash application
app = dash.Dash(__name__)

 
app.layout = html.Div(children=[html.H1('Airline Dashboard', style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
                                html.P('Proportion of distance group (250 mile distance interval group) by flights.', style={'textAlign':'center', 'color': '#F57241'}),
                                dcc.Graph(figure=fig),
                    ])

# Run the application                   
if __name__ == '__main__':
     app.run_server(host='127.0.0.1', port='8050', debug=True)