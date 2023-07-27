import streamlit as st
import leafmap.foliumap as leafmap
import folium

st.set_page_config(page_title="Uganda travel time", layout='wide')


def app():

    st.title("Raster Datasets")
    col1, col2 = st.columns([4, 1])

    m = leafmap.Map(center=[1.5, 32], 
                    zoom=7, 
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True)


    layer1 = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                        layers = 'data:UGA_100_M',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    fg1 = folium.FeatureGroup(name='Any Health Facility', control=True)
    
    
    layer2 = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                        layers = 'data:hos_III',
                        transparent = True, 
                        control = True,
                        version = '1.0.0',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    
    fg2 = folium.FeatureGroup(name='Level III health centre', control=True)

    layer3 = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                        layers = 'data:h4',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    
    fg3 = folium.FeatureGroup(name='Level IV health centre', control=True)
    
    layer4 = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                        layers = 'data:h4h',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    fg4 = folium.FeatureGroup(name='Level IV health centre & Hospital', control=True)
    
    
    fg2.add_child(layer2).add_to(m)
    fg3.add_child(layer3).add_to(m)
    fg4.add_child(layer4).add_to(m)
    fg1.add_child(layer1).add_to(m)



    legend_dict1 = {
    '<= 39.45': '#d7191c',
    '39.45 - 59.76': '#e85b3b',
    '59.76 - 79.89': '#f99d59',
    '79.89 - 98.57': '#fec980',
    '98.57 - 118.48': '#ffedaa',
    '118.48 - 142.98': '#ecf7b9',
    '142.98 - 182.67': '#c7e8ad',
    '182.67 - 336.82': '#9fd6aa',
    '336.82 - 594.12': '#6dbac3',
    '> 594.12': '#3b9edc',
    }

    legend_dict2 = {
    '<= 4171.77': '#d7191c',
    '4171.77 - 6219.96': '#e85b3b',
    '6219.96 - 8259.70': '#f99d59',
    '8259.70 - 10406.69': '#fec980',
    '10406.69 - 13009.44': '#ffedaa',
    '13009.44 - 16443.83': '#ecf7b9',
    '16443.83 - 21929.96': '#c7e8ad',
    '21929.96 - 31877.73': '#9fd6aa',
    '31877.73 - 61049.99': '#6dbac3',
    '> 61049.99': '#3b9edc',
    }

    legend_dict3 = {
    '<= 9881.06': '#d7191c',
    '9881.06 - 14572.30': '#e85b3b',
    '14572.30 - 19120.42': '#f99d59',
    '19120.42 - 24200.95': '#fec980',
    '24200.95 - 29871.09': '#ffedaa',
    '29871.09 - 36437.09': '#ecf7b9',
    '36437.09 - 45209.22': '#c7e8ad',
    '45209.22 - 58869.04': '#9fd6aa',
    '58869.04 - 93513.95': '#6dbac3',
    '> 93513.95': '#3b9edc',
    }

    legend_dict4 = {
    '<= 8245.39': '#d7191c',
    '8245.39 - 12316.40': '#e85b3b',
    '12316.40 - 16169.24': '#f99d59',
    '16169.24 - 20317.24': '#fec980',
    '20317.24 - 25029.02': '#ffedaa',
    '25029.02 - 30218.67': '#ecf7b9',
    '30218.67 - 36635.56': '#c7e8ad',
    '36635.56 - 46791.85': '#9fd6aa',
    '46791.85 - 83103.22': '#6dbac3',
    '> 83103.22': '#3b9edc',
    }

    legend_list = [
            'Any Health Facility',
            'Level III health centre',
            'Level IV health centre',
            'Level IV health centre & Hospital',
        ]

    legend = st.sidebar.selectbox(label="Select a legend", options=legend_list, index=legend_list.index('Any Health Facility'))
    
    if legend == 'Any Health Facility':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict1)
    elif legend == 'Level III health centre':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict2)
    elif legend == 'Level IV health centre':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict3)
    elif legend == 'Level IV health centre & Hospital':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict4)
    
    with col1:
       m.to_streamlit(width=800, height=700)

    with col2:
        st.markdown('test')

def download():
    st.sidebar.markdown(" Select raster datasets you want to download 👉")
    
    url1 = 'https://datashare.ed.ac.uk/handle/10283/3956'
    url2 = 'https://datashare.ed.ac.uk/handle/10283/3957'
    url3 = 'https://datashare.ed.ac.uk/handle/10283/3950'  
    url4 = 'https://datashare.ed.ac.uk/handle/10283/3954'
    
    st.sidebar.markdown(f'''
                        <a href = {url1}><button style="background-color:#C6E5F2">Any Health Facility</button></a>
                        ''',
    unsafe_allow_html=True)


    st.sidebar.markdown(f'''

                        <a href={url2}><button style="background-color:#C6E5F2;">Level III Health centre</button></a>
        ''',
        unsafe_allow_html=True)
    
    st.sidebar.markdown(f'''

                            <a href={url3}><button style="background-color:#C6E5F2;">Level IV Health centre</button></a>
        ''',
        unsafe_allow_html=True)
    
    st.sidebar.markdown(f'''

                            <a href={url4}><button style="background-color:#C6E5F2;">Level IV Health centre & Hospital</button></a>
        ''',
        unsafe_allow_html=True)



if __name__ == '__main__':
    app()
    download()


