import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Uganda travel time",layout='wide')


def app():

    col1, col2 = st.columns([4, 1])


    m = leafmap.Map(center=[1.5, 32], 
                    zoom=7, 
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True,
)
    

    df1 = pd.read_csv('E:\\health_center\\national and regional hospital.csv',
                          usecols=['Facility name', 'Facility type', 'Lat', 'Long'])

    df2 = pd.read_csv('E:\\health_center\\hospital.csv',
                          usecols=['Facility name', 'Facility type', 'Lat', 'Long'])

    df3 = pd.read_csv('E:\\health_center\\hospital_II.csv',
                          usecols=['Facility name', 'Facility type', 'Lat', 'Long'])

    df4 = pd.read_csv('E:\\health_center\\h_III.csv',
                          usecols=['Facility name', 'Facility type', 'Lat', 'Long'])

    df5 = pd.read_csv('E:\\health_center\\h_IV.csv',
                          usecols=['Facility name', 'Facility type', 'Lat', 'Long'])

    df6 = pd.read_csv('E:\\health_center\\clinic.csv',
                          usecols=['Facility name', 'Facility type', 'Lat', 'Long'])

    options = ['National and Regional Hospital', 'Hospital', 'Health Centre II',
                   'Health Centre III', 'Health Centre IV', 'Clinic']

    # icon1 = 'https://em-content.zobj.net/thumbs/160/google/350/black-circle_26ab.png'

    empty_element = st.empty()

    with empty_element:
            
            selectbox = st.sidebar.multiselect("Select level of health center to display", options)

            if 'National and Regional Hospital' in selectbox:
                m.add_points_from_xy(df1,
                                     layer_name="National and Regional Hospital",
                                     x="Long",
                                     y="Lat",
                                    #  marker_colors=['black'],icon_names=['info'],icon_colors=['black']
                                    )

            if 'Hospital' in selectbox:
                m.add_points_from_xy(df2, layer_name="Hospital", x="Long", y="Lat")

            if 'Health Centre II' in selectbox:
                m.add_points_from_xy(df3, layer_name="Health Centre II", x="Long", y="Lat")

            if 'Health Centre III' in selectbox:
                m.add_points_from_xy(df4, layer_name="Health Centre III", x="Long", y="Lat")

            if 'Health Centre IV' in selectbox:
                m.add_points_from_xy(df5, layer_name="Health Centre IV", x="Long", y="Lat")

            if 'Clinic' in selectbox:
                m.add_points_from_xy(df6, layer_name="Clinic", x="Long", y="Lat")

    boundry = 'E:\\boundry.geojson'

    m.add_geojson(boundry, layer_name="Boundary")

    with col1:
        m.to_streamlit(width=700, height=650)
    
    with col2:
        st.markdown()

if __name__ == '__main__':
    app()
