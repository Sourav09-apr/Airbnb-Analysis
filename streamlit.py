import streamlit as st
import geopandas as gpd
from shapely.geometry import Point

def create_geospatial_dataframe(df):
    df['coordinates'] = df['location'].apply(lambda loc: Point(loc['coordinates'][0], loc['coordinates'][1]))
    gdf = gpd.GeoDataFrame(df, geometry='coordinates')
    return gdf

def visualize_geospatial_data(gdf):
    st.title("Airbnb Listings Geospatial Visualization")
    st.map(gdf)

# Streamlit application
st.set_page_config(layout="wide")
gdf = create_geospatial_dataframe(cleaned_data)
visualize_geospatial_data(gdf)

import matplotlib.pyplot as plt
import seaborn as sns

def price_analysis(df):
    plt.figure(figsize=(12, 6))
    sns.histplot(df['price'], bins=50, kde=True)
    plt.title('Distribution of Airbnb Listing Prices')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.show()

price_analysis(cleaned_data)
def availability_analysis(df):
    df['availability.month'] = df['availability.start_date'].dt.month
    monthly_availability = df.groupby('availability.month').size()
    
    plt.figure(figsize=(12, 6))
    monthly_availability.plot(kind='bar')
    plt.title('Monthly Availability of Airbnb Listings')
    plt.xlabel('Month')
    plt.ylabel('Number of Available Listings')
    plt.show()

availability_analysis(cleaned_data)
def location_based_insights(df, neighborhood):
    neighborhood_data = df[df['neighbourhood'] == neighborhood]
    
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='neighbourhood', y='price', data=neighborhood_data)
    plt.title(f'Price Distribution in {neighborhood}')
    plt.xlabel('Neighborhood')
    plt.ylabel('Price')
    plt.show()

# Example usage for a specific neighborhood
location_based_insights(cleaned_data, 'Downtown')
def interactive_visualizations(df):
    st.sidebar.title("Filter Options")
    neighborhood = st.sidebar.selectbox("Select Neighborhood", df['neighbourhood'].unique())
    filtered_data = df[df['neighbourhood'] == neighborhood]
    
    st.write(f"Price Distribution in {neighborhood}")
    sns.boxplot(x='neighbourhood', y='price', data=filtered_data)
    st.pyplot()

# Add to Streamlit application
interactive_visualizations(cleaned_data)
