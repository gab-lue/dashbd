import streamlit as st
import pandas as pd
import plotly.express as px
import time
import numpy as np
import plotly.figure_factory as ff
from io import StringIO
import os.path
import time


# Define function to read Excel file




# Define Streamlit app
def app():
    @st.cache(allow_output_mutation=True)
    def read_excel_file(filename):
        df = pd.read_excel(filename, engine='openpyxl',
                                   sheet_name='Ranking',
                                   skiprows=4,
                                   usecols='C:M',
                                   nrows=1000,
                                   header=None)
        return df   
    # Add file uploader widget
    with st.sidebar:
        file = st.file_uploader("Upload Excel file", type=["xlsx"])
    
    
    # Check if file is uploaded
    if file is not None:
        # Read Excel file
        file_contents = file.getvalue()        
        
    
        #read df and split it into 4 lists
        df = read_excel_file(file_contents)
        
        #4 new dfs
        df_meetings = df.iloc[0:32,0:2]
        df_held = df.iloc[0:32,3:5]
        df_agreement = df.iloc[0:32,6:8]
        df_turnover = df.iloc[0:32,9:11]
         
         #make plots
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
        
        #show plots
        
        st.plotly_chart(termine)
        st.plotly_chart(abgehalten)
        st.plotly_chart(vereinbarungen)
        st.plotly_chart(turnover)
    else:
        # Add message to tell user to upload file
        st.write("Please upload an Excel file.")
        
        
        


### script start###
#config
st.set_page_config(page_title="Unit 1 Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide"
                   )  
  
#überschrift
st.header("Alle Wichtigen Zahlen")
st.subheader("Top Performer:")   

app()

