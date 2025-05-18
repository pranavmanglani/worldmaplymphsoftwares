import streamlit as st
import plotly.express as px
import pandas as pd

# Sample data: Cities with their coordinates
data = {
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],
    'Latitude': [40.7128, 51.5074, 35.6762, 48.8566, -33.8688],
    'Longitude': [-74.0060, -0.1278, 139.6503, 2.3522, 151.2093]
}

df = pd.DataFrame(data)

# Create a map using Plotly
fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", hover_name="City", zoom=1)

# Use OpenStreetMap style for the map
fig.update_layout(mapbox_style="open-street-map")

# Display the map in Streamlit
st.plotly_chart(fig)
