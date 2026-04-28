import streamlit as st
import pandas as pd

st.set_page_config(page_title="Uber Rides Data", layout="wide")
st.title("Uber Rides Data Visualization")

with st.sidebar:
    st.header("About")
    st.write(
        """
        This app visualizes Uber rides data using Streamlit and Plotly.
        The data is sourced from a CSV file containing information about Uber rides, including pickup and dropoff locations, timestamps, and more.
        """
    )


@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df


df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df.head())

st.map(df.sample(100).rename(columns={"Lat": "lat", "Lon": "lon"}))
