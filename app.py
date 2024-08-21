import pandas as pd 
import plotly.express as px 
import streamlit as st 

car_data =pd.read_csv('vehicles_us.csv')

hist_button = st.button('Construir histograma')
scatter_plot_button = st.button ('Consturir grafico de dispersion')

if hist_button:
    
    st.write('Creacion de un histograma para el conjunto de datos')
    
    fig = px.histogram(car_data, x = 'odometer', title= 'Histograma')
    
    st.plotly_chart(fig, use_container_width = True)
    
if scatter_plot_button: 
    
    st.write ('Creacion de un grafico de dispersion para el conjunto de datos')
    
    fig1 = px.scatter (car_data,x='odometer', title= 'Diagrama de dispersion')
    
    st.plotly_chart(fig1, use_container_width = True)
    

