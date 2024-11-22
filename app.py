# Streamlit app code for visualizing Price (Amount) variations with Plotly
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

df = pd.read_csv("Cleaned_data.csv")

st.title("Price Analysis Dashboard")
st.markdown("Explore the variation of Price with other Columns in the dataset.")
#st.balloons()
#st.snow()
#st.sidebar.selectbox("Select a column to compare",['Cpu','Gpu','IPS','Touchscreen'])

#sidebar
cat_cols = ['Company','TypeName','Cpu','Gpu','OpSys']
num_cols = ['Ram','Weight','Touchscreen','IPS','ppi']

all_cols = cat_cols + num_cols

selected_col = st.sidebar.selectbox("select a column to compare",all_cols)

#plotting
if selected_col:
    if selected_col in cat_cols:
        #bar chart
        fig = px.box(df , x = selected_col , y = 'Price' , title = f'Price Variation {selected_col}')
        st.snow()
    else:
        #scatter plot
        fig = px.scatter(df , x = selected_col , y = 'Price' , title = f'Price Vs  {selected_col}', trendline = "ols")
        st.balloons()
    st.plotly_chart(fig)
    