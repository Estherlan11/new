import leafmap.foliumap as leafmap
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Uganda travel time",layout="wide")

@st.cache_data

def app():
    
    col1, col2 = st.columns([4, 1])
    

    m = leafmap.Map(center=[1.5,32], 
                    zoom=7,
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True)

    df = pd.read_csv('E:\\villages.csv', 
                            usecols=['FULL_NAME', 'POINT_X', 'POINT_Y'])
            
    m.add_points_from_xy(df, x="POINT_X", y="POINT_Y")

    boundry = 'E:\\boundry.geojson' 

    m.add_geojson(boundry, layer_name="Boundary")
    
    with col1:
        m.to_streamlit(width=700, height=650)

    with col2:
        st.markdown('this is an introduction')

    
if __name__ == "__main__":
    app()
