'''
An app to publish the point data of health facilities distribution 
'''

#############################################################
#import necessary packages

import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd

#############################################################
#set the whole page layout and navigation bar
st.set_page_config(page_title="Uganda travel time",layout='wide')


def app():

    #set the layout and title 
    st.title("Health Centres")
    col1, col2 = st.columns([2.8, 1.2])

    #add a map viewer and set the paraments
    m = leafmap.Map(center=[1.5, 32], 
                    zoom=7, 
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True,
)
    
    #read the file
    df1 = pd.read_csv('/home/lrx0914/csv/national and regional hospital.csv',
                          usecols=['Facility name', 'Facility type', 'Latitude', 'Longitude'])

    df2 = pd.read_csv('/home/lrx0914/csv/hospital.csv',
                          usecols=['Facility name', 'Facility type', 'Latitude', 'Longitude'])

    df3 = pd.read_csv('/home/lrx0914/csv/hospital_II.csv',
                          usecols=['Facility name', 'Facility type', 'Latitude', 'Longitude'])

    df4 = pd.read_csv('/home/lrx0914/csv/h_III.csv',
                          usecols=['Facility name', 'Facility type', 'Latitude', 'Longitude'])

    df5 = pd.read_csv('/home/lrx0914/csv/h_IV.csv',
                          usecols=['Facility name', 'Facility type', 'Latitude', 'Longitude'])

    df6 = pd.read_csv('/home/lrx0914/csv/clinic.csv',
                          usecols=['Facility name', 'Facility type', 'Latitude', 'Longitude'])

    options = ['National and Regional Hospital', 'Hospital', 'Health Centre II',
                   'Health Centre III', 'Health Centre IV', 'Clinic']

    #set the selection box to switch layers
    empty_element = st.empty()

    with empty_element:
            
            selectbox = st.sidebar.multiselect("Select level of health center to display", options)

            if 'National and Regional Hospital' in selectbox: #add the point data to map 
                m.add_points_from_xy(df1,
                                     layer_name="National and Regional Hospital",
                                     x="Long",
                                     y="Lat",
                                     )

            if 'Hospital' in selectbox:
                m.add_points_from_xy(df2, layer_name="Hospital", x="Longitude", y="Latitude")

            if 'Health Centre II' in selectbox:
                m.add_points_from_xy(df3, layer_name="Health Centre II", x="Longitude", y="Latitude")

            if 'Health Centre III' in selectbox:
                m.add_points_from_xy(df4, layer_name="Health Centre III", x="Longitude", y="Latitude")

            if 'Health Centre IV' in selectbox:
                m.add_points_from_xy(df5, layer_name="Health Centre IV", x="Longitude", y="Latitude")

            if 'Clinic' in selectbox:
                m.add_points_from_xy(df6, layer_name="Clinic", x="Longitude", y="Latitude")
    
    #read the Uganda boundary file 
    boundry = '/home/lrx0914/boundry.geojson'

    #add the Uganda file to map
    m.add_geojson(boundry, layer_name="Boundary", info_mode=None)

    with col1:
        m.to_streamlit(height=700)
    
    #add introduction part in HTML
    with col2:
         st.markdown('''<li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    This map displays the spatial distribution of health facilities at different levels. </li> </br>
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    The data were categorized into six levels: National and Regional Hospitals,</br> Hospitals,</br> Level II Health Centers, </br>Level III Health Centers,</br> Level IV Health Centers, </br> Clinics.</li> </br> 
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    You can use the selection box on the left to add or remove layers.</li> </br> 
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    Click on points to access the detailed information of each health facility. </li>
                     ''',unsafe_allow_html=True)

#############################################################
if __name__ == '__main__':
    # Main block
    app()
