'''
An app to publish the point data of settlements distribution 
'''

#############################################################
#import necessary packages

import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd

#############################################################
#set the whole page layout

st.set_page_config(page_title="Uganda travel time",layout="wide")

#cache the data
@st.cache_data

def app():

    #set the layout
    st.title("Village Distribution")
    col1, col2 = st.columns([2.8, 1.2])
    
    #add a map window and set the paraments

    m = leafmap.Map(center=[1.5,32], 
                    zoom=7,
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True)

    #read the file
    df = pd.read_csv('/home/lrx0914/csv/villages.csv', 
                            usecols=['FULL_NAME', 'POINT_X', 'POINT_Y'])
            
    #add the data to map
    m.add_points_from_xy(df, x="POINT_X", y="POINT_Y")

    #read the Uganda boundary file 
    boundry = '/home/lrx0914/boundry.geojson' 

    #add the Uganda file to map
    m.add_geojson(boundry, layer_name="Boundary",info_mode=None)
    
    with col1:
        m.to_streamlit(height=700)

    #add introduction part
    with col2:
        st.markdown('''<li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    This section presents the spatial distribution of primary villages in Uganda.</li></br>
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    You can adjust the view area using the zoom buttons in the top left corner or the mouse scroll wheel. </li></br>
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    Click on points to access the detailed information of each village. </li> 
        ''',unsafe_allow_html=True)

#############################################################
if __name__ == "__main__":
    # Main block
    app()
