import streamlit as st
import pandas as pd
import numpy as np

# Sample data: Cities with their coordinates
data = {
    'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],
    'Latitude': [40.7128, 51.5074, 35.6762, 48.8566, -33.8688],
    'Longitude': [-74.0060, -0.1278, 139.6503, 2.3522, 151.2093]
}

df = pd.DataFrame(data)

# Display the map
st.map(df[['Latitude', 'Longitude']])
