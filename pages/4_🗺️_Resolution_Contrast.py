import streamlit as st
import folium
import leafmap.foliumap as leafmap

st.set_page_config(page_title="Uganda travel time",layout='wide')

def app():

    col1, col2 = st.columns([4, 1])
    

    m = leafmap.Map(center=[1.5,32], 
                    zoom=7,
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True)
    
    left_layer = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                            layers = 'data:Uganda_100_tra',
                            transparent = True, 
                            control = True,
                            version = '1.1.1',
                            fmt="image/png",
                            name = 'Resolution: 100m',
                            overlay = True,
                            show = True,
                            )

    right_layer = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                            layers = 'data:Uganda_1km_tra',
                            transparent = True, 
                            control = True,
                            version = '1.1.0',
                            fmt="image/png",
                            name = 'Resolution: 1000m',
                            overlay = True,
                            show = True,
                            )

    m.split_map(left_layer, right_layer)
    
    with col1:
        m.to_streamlit(width=700, height=650)
    
    with col2:
        st.markdown('test')
  

    
if __name__ == "__main__":
    app()
