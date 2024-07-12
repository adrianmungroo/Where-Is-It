import streamlit as st
import geopandas as gpd
from geopandas.tools import geocode
from streamlit_folium import folium_static
import folium

def showPlace(name):
    geo_info = geocode(name)
    y = geo_info['geometry'][0].y
    x = geo_info['geometry'][0].x
    m = folium.Map(location=[y, x], zoom_start=8, tiles='OpenStreetMap')

    folium.Marker(
        location=[y, x],
    ).add_to(m)

    folium.LayerControl().add_to(m)
    
    return m, geo_info

location = st.sidebar.text_input('Where do you want to go?')

if location:
    m, geoinfo = showPlace(location)
    st.title(geoinfo.address[0])
    folium_static(m)