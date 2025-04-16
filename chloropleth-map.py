# Exercise: 
# make a dash app with the following plotly chart ,

# put it on github. 

from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Polotical candidate voting pool analysis'),
    html.P("Select a candidate:"),
    dcc.RadioItems(
        id='candidate',
        options=["Joly", "Coderre", "Bergeron"],
        value="Coderre",
        inline=True
    ),
    dcc.Graph(id="graph"),
])

@app.callback(
    Output("graph", "figure"),
    Input("candidate", "value"))
def display_choropleth(candidate):
    df = px.data.election() # replace with your own data source
    geojson = px.data.election_geojson()

    fig = px.choropleth(df, geojson=geojson, color=candidate,
        locations="district", featureidkey="properties.district",
        projection="mercator"
    )

    # make map centered to locations in our 
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(
    margin={"r":0,"t":0,"l":0,"b":0})

    return fig

if __name__ == '__main__':
    app.run(port=5007, debug=True)
