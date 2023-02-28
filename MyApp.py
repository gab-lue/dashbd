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

#global#data = None

# Define Streamlit app
def app():
   

    
    @st.cache_data
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
    #print(data)
    #if file is not None:
        # Read Excel file
        #read df and split it into 4 lists
    data = read_excel_file("Unit 1 - Ranking.xlsx")
    
    
       
    #if data is not None:
        #4 new dfs
    df_meetings = data.iloc[0:32,0:2]
    df_held = data.iloc[0:32,3:5]
    df_agreement = data.iloc[0:32,6:8]
    df_turnover = data.iloc[0:32,9:11]
    name_meeting,value_meeting = df_meetings.at[0,2],df_meetings.at[0,3]
    name_held,value_held = df_held.at[0,5],df_held.at[0,6]
    name_agree,value_agree = df_agreement.at[0,8],df_agreement.at[0,9]
    name_turn,value_turn = df_turnover.at[0,11],df_turnover.at[0,12]
  
    st.markdown('### Bestleistungen')
    col1,col2,col3,col4 = st.columns(4)
    col1.metric("gebuchte Termine:crown:",str(name_meeting),str(value_meeting))
    col2.metric("abgehaltene Termine:crown:",str(name_held),str(value_held))
    col3.metric("Vereinbarungen:crown:",str(name_agree),str(value_agree))
    col4.metric("Umsatz:crown:",str(name_turn),str(value_turn))  
         
         #make plots
 
    
    
        
        #st.write("file loading")
        

    abgehalten = px.bar(df_held,
                        title="abgehaltene Termine",
                        x=5,
                        y=6,
                        color=6,
                        orientation="v",
                        hover_name=6
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
    #rows data
    
    c1,c2 = st.columns((50,50))
    with c1:
        
        #st.write(print(name_meeting,value_meeting))
        #st.markdown('#### Termine gebucht')
        
        fig = px.bar(df_meetings, x=2, y=3,orientation="v",color=3,
                     title="gebuchte Termine",
                     opacity=0.8,
                     hover_name=3,
                     hover_data=(),
                     width=650,
                     
                     barmode="relative")
        
        st.write(fig)
        fig.update_layout(showlegend=False)
        #st.markdown('### abgehaltene Termine')
        st.plotly_chart(abgehalten,theme="streamlit")
    with c2:
        st.plotly_chart(vereinbarungen)
        st.plotly_chart(turnover)
   
        
            
    #else:
        # Add message to tell user to upload file
        #st.write("Please upload an Excel file.")
        
      
        


################################### script start#########################
#config
st.set_page_config(page_title="Unit 1 Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide",
                   initial_sidebar_state='collapsed'
                   )  
#css
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', 
                unsafe_allow_html=True)
st.header("Aktueller Stand der Zahlen - PCS Monat Februar")
     
st.sidebar.header('Dashboard `version1`')

#rows shortcuts



#überschrift

app()



