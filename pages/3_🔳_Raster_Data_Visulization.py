import streamlit as st
import leafmap.foliumap as leafmap
import folium

st.set_page_config(page_title="Uganda travel time", layout='wide')

@st.cache_data
def app():

    st.title("Raster Datasets")
    col1, col2 = st.columns([4, 1])

    m = leafmap.Map(center=[1.5, 32], 
                    zoom=7, 
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True)
   
    fg1 = folium.FeatureGroup(name='Walking only travel time', control=True)


    layer1 = folium.WmsTileLayer(url = 'http://localhost:8080/geoserver/wms?',
                        layers = 'mock1:Uganda_100_tra',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    fg2 = folium.FeatureGroup(name='Health centre & Hospital', control=True)
    
    layer2 = folium.WmsTileLayer(url = 'http://localhost:8080/geoserver/wms?',
                        layers = 'mock1:hos',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    fg3 = folium.FeatureGroup(name='Level II health centre & Hospital', control=True)
    
    layer3 = folium.WmsTileLayer(url = 'http://localhost:8080/geoserver/wms?',
                        layers = 'mock1:hos_II',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    
    fg4 = folium.FeatureGroup(name='Level III health centre & Hospital', control=True)

    layer4 = folium.WmsTileLayer(url = 'http://localhost:8080/geoserver/wms?',
                        layers = 'mock1:hos_III',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    
    fg5 = folium.FeatureGroup(name='Level IV health centre & Hospital', control=True)
    
    layer5 = folium.WmsTileLayer(url = 'http://localhost:8080/geoserver/wms?',
                        layers = 'mock1:hos_IV',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    
    fg1.add_child(layer1).add_to(m)
    fg2.add_child(layer2).add_to(m)
    fg3.add_child(layer3).add_to(m)
    fg4.add_child(layer4).add_to(m)
    fg5.add_child(layer5).add_to(m)

    with col1:
       m.to_streamlit(width=800, height=700)

    st.sidebar.markdown(" Select raster datasets you want to download 👉")
    
    url1 = 'https://data.malariaatlas.org/maps'
    url2 = 'https://stackoverflow.com'
    url3 = 'https://datashare.ed.ac.uk/handle/10283/3957'
    url4 = 'https://datashare.ed.ac.uk/handle/10283/3950'

    st.sidebar.markdown(f'''
                        <a href = {url1}><button style="background-color:#C6E5F2">Walking only travel time</button></a>
                        ''',
    unsafe_allow_html=True)


    st.sidebar.markdown(f'''

                        <a href={url2}><button style="background-color:#C6E5F2;">Health centre & Hospital</button></a>
    ''',
    unsafe_allow_html=True)

    st.sidebar.markdown(f'''

                        <a href={url2}><button style="background-color:#C6E5F2;">Level II Health centre & Hospital</button></a>
    ''',
    unsafe_allow_html=True)

    st.sidebar.markdown(f'''

                        <a href={url3}><button style="background-color:#C6E5F2;">Level III Health centre & Hospital</button></a>
        ''',
        unsafe_allow_html=True)

    st.sidebar.markdown(f'''

                            <a href={url4}><button style="background-color:#C6E5F2;">Level IV Health centre & Hospital</button></a>
        ''',
        unsafe_allow_html=True)


    with col2:
        st.markdown()

if __name__ == '__main__':
    app()



