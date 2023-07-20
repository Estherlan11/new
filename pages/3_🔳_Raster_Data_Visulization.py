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
   
    fg1 = folium.FeatureGroup(name='Walking only travel time', control=True)


    layer1 = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                        layers = 'data:Uganda_100_tra',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    fg2 = folium.FeatureGroup(name='Health centre & Hospital', control=True)
    
    layer2 = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                        layers = 'data:hos',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    fg3 = folium.FeatureGroup(name='Level II health centre & Hospital', control=True)
    
    layer3 = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                        layers = 'data:hos_II',
                        transparent = True, 
                        control = True,
                        version = '1.0.0',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    
    fg4 = folium.FeatureGroup(name='Level III health centre & Hospital', control=True)

    layer4 = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                        layers = 'data:hos_III',
                        transparent = True, 
                        control = True,
                        version = '1.1.1',
                        fmt="image/png",
                        name = 'raster',
                        overlay = True,
                        show = True,
                        )
    
    fg5 = folium.FeatureGroup(name='Level IV health centre & Hospital', control=True)
    
    layer5 = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                        layers = 'data:hos_IV',
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



    legend_dict1 = {
    '<= 12026.40': '#d7191c',
    '12026.40-18344.96': '#e85b3b',
    '18344.96-24200.21': '#f99d59',
    '24200.21-30106.90': '#fec980',
    '30106.90-36445.49': '#ffedaa',
    '36445.49-43745.91': '#ecf7b9',
    '43745.91-52346.50': '#c7e8ad',
    '52346.50-64005.56': '#9fd6aa',
    '64005.56-97798.92': '#6dbac3',
    '> 97798.92': '#3b9edc',
    }

    legend_dict3 = {
    '<=3445.39': '#d7191c',
    '3445.39-5198.84': '#e85b3b',
    '5198.84-6856.00': '#f99d59',
    '6856.00-8639.95': '#fec980',
    '8639.95-10735.26': '#ffedaa',
    '10735.26-13484.62': '#ecf7b9',
    '13484.62-17784.66': '#c7e8ad',
    '17784.66-25662.77': '#9fd6aa',
    '25662.77-51056.97': '#6dbac3',
    '>51056.97': '#3b9edc',
    }

    legend_dict2 = {
    '<=2646.71': '#d7191c',
    '2646.71-4048.04': '#e85b3b',
    '4048.04-5390.93': '#f99d59',
    '5390.93-6856.16': '#fec980',
    '6856.16-8631.11': '#ffedaa',
    '8631.11-11061.79': '#ecf7b9',
    '11061.79-14825.25': '#c7e8ad',
    '14825.25-21897.99': '#9fd6aa',
    '21897.99-45514.67': '#6dbac3',
    '> 45514.67': '#3b9edc',
    }

    legend_dict4 = {
    '<= 8375.26': '#d7191c',
    '8375.26-12518.90': '#e85b3b',
    '12518.90-16529.46': '#f99d59',
    '16529.46-20867.87': '#fec980',
    '20867.87-25753.24': '#ffedaa',
    '25753.24-31350.49': '#ecf7b9',
    '31350.49-38933.38': '#c7e8ad',
    '38933.38-51014.38': '#9fd6aa',
    '51014.38-80834.01': '#6dbac3',
    '> 80834.01': '#3b9edc',
    }

    legend_list = [
            'Walking_only_travel_time',
            'Health centre & Hospital',
            'Level II health centre & Hospital',
            'Level III health centre & Hospital',
            'Level IV health centre & Hospital',
        ]

    legend = st.sidebar.selectbox(label="Select a legend", options=legend_list, index=legend_list.index('Walking_only_travel_time'))
    
    if legend == 'Walking_only_travel_time':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict1)
    elif legend == 'Health centre & Hospital':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict1)
    elif legend == 'Level II health centre & Hospital':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict2)
    elif legend == 'Level III health centre & Hospital':
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



if __name__ == '__main__':
    app()
    download()


