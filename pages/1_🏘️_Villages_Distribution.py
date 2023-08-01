import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Uganda travel time",layout="wide")

@st.cache_data

def app():

    st.title("Village Distribution")
    col1, col2 = st.columns([4, 1])
    

    m = leafmap.Map(center=[1.5,32], 
                    zoom=7,
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True)

    df = pd.read_csv('/home/lrx0914/csv/villages.csv', 
                            usecols=['FULL_NAME', 'POINT_X', 'POINT_Y'])
            
    m.add_points_from_xy(df, x="POINT_X", y="POINT_Y")

    boundry = '/home/lrx0914/boundry.geojson' 

    m.add_geojson(boundry, layer_name="Boundary",info_mode=None)
    
    with col1:
        m.to_streamlit(width=700, height=650)

    with col2:
        st.markdown('''<p style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    This section presents the spatial distribution of primary villages in Uganda.</br>
                    You can adjust the view area using the zoom buttons in the top left corner or the mouse scroll wheel. </br>
                    Click on points to access the detailed information of each village. </p> 
        ''',unsafe_allow_html=True)

    
if __name__ == "__main__":
    app()
