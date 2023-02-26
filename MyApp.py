import streamlit as st
import pandas as pd
import plotly.express as px
import time
import numpy as np
import plotly.figure_factory as ff
from io import StringIO


  
#config
st.set_page_config(page_title="Unit 1 Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )  
  
#überschrift
st.header("Alle Wichtigen Zahlen")
st.subheader("Top Performer:")   

with st.sidebar:
    uploaded_file = st.file_uploader("Choose a file")
    print("sidebar")
col1,col2 = st.columns(2)

df=None
try:
    #st.sidebar()
    df = pd.read_excel(uploaded_file, engine='openpyxl',
                              sheet_name='Ranking',
                              skiprows=4,
                              usecols='C:M',
                              nrows=1000,
                              header=None)
    #st.write(dataframe)

    
    df_meetings = df.iloc[0:32,0:2]
    df_held = df.iloc[0:32,3:5]
    df_agreement = df.iloc[0:32,6:8]
    df_turnover = df.iloc[0:32,9:11]

#df1["PCS"],df1["Termine"] = df_meetings[2],df_meetings[3]
#print(df1)
#print(df_meetings)    
#print(df_held) 
#print(df_agreement)
#print(df_turnover) 
             
####streamlit code

#file upload


#state
    data_load_state = st.text("Data loading")
#data=load_data(10000) 
    data_load_state.text("loading data..done")   
                   
    #st.dataframe(df)
    #st.dataframe(df_meetings)

    #st.sidebar.header("Hier kann gefiltert werden")


    #site
    
    color="X_axis",
    termine = px.bar(df_meetings,
                   title="Gebuchte Meetings",
                   x=2,
                   y=3,
                   color=3,
                   orientation="v",
                   hover_name=2,
                   
                   )

    abgehalten = px.bar(df_held,
                   title="abgehaltene Termine",
                   x=5,
                   y=6,
                   color=6,
                   orientation="v",
                   hover_name=5
                   )

    vereinbarungen = px.bar(df_agreement,
                   title="Vereinbarungen",
                   x=8,
                   y=9,
                   color=9,
                   orientation="v",
                   hover_name=9            
                   )

    turnover = px.bar(df_turnover,
                   title="UMSATZ",
                   x=11,
                   y=12,
                   color=12,
                   orientation="v",
                   hover_name=12            
                   )


    st.plotly_chart(termine)
    st.plotly_chart(abgehalten)
    st.plotly_chart(vereinbarungen)
    st.plotly_chart(turnover)


except:
    print("bitte lade eine excel datei hoch")
    
#print(df)
#st.write(df)
#df_meetings = dataframe.iloc[0:32,0:2]

