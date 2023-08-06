'''
An app to publish the raster data layers 
'''

#############################################################
#import necesary packges

import streamlit as st
import leafmap.foliumap as leafmap
import folium

#############################################################
#set the whole page layout and navigation bar
st.set_page_config(page_title="Uganda travel time", layout='wide')


def app():

    #set the layout and title
    st.title("Raster Datasets")
    col1, col2 = st.columns([2.8, 1.2])

    #add a map viewer and set the paraments
    m = leafmap.Map(center=[1.5, 33], 
                    zoom=7, 
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True)

    #call the layer1 WMS request from GeoServer
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
    
    #call the layer2 WMS request from GeoServer and store to the layer controller
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

    #call the layer3 WMS request from GeoServer and store to the layer controller
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
    
    #call the layer4 WMS request from GeoServer and store to the layer controller
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
    
     
    #add the layers to controller
    fg2.add_child(layer2).add_to(m)
    fg3.add_child(layer3).add_to(m)
    fg4.add_child(layer4).add_to(m)
    fg1.add_child(layer1).add_to(m)


    #set the legend of each layer
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
    '<= 69.53': '#d7191c',
    '69.53-103.67': '#e85b3b',
    '103.67-137.66': '#f99d59',
    '137.66-183.44': '#fec980',
    '183.44-216.82': '#ffedaa',
    '216.82-290.73': '#ecf7b9',
    '290.73-365.50': '#c7e8ad',
    '365.50-531.30': '#9fd6aa',
    '531.30-1018.50': '#6dbac3',
    '> 1018.50': '#3b9edc',
    }

    legend_dict3 = {
    '<= 164.08': '#d7191c',
    '164.08-242.87': '#e85b3b',
    '242.87-318.67': '#f99d59',
    '318.67-403.35': '#fec980',
    '403.35-497.85': '#ffedaa',
    '497.85-607.28': '#ecf7b9',
    '607.28-753.49': '#c7e8ad',
    '753.49-981.15': '#9fd6aa',
    '981.15-1558.57': '#6dbac3',
    '> 1558.57': '#3b9edc',
    }

    legend_dict4 = {
    '<= 137.42': '#d7191c',
    '137.42-205.29': '#e85b3b',
    '205.29-286.32': '#f99d59',
    '286.32-338.62': '#fec980',
    '338.62-418.15': '#ffedaa',
    '418.15-503.64': '#ecf7b9',
    '503.64-610.59': '#c7e8ad',
    '610.59-779.86': '#9fd6aa',
    '779.86-1385.05': '#6dbac3',
    '> 1385.05': '#3b9edc',
    }

    legend_list = [
            'Any Health Facility',
            'Level III health centre',
            'Level IV health centre',
            'Level IV health centre & Hospital',
        ]

    #add the legend selection box in the side bar
    legend = st.sidebar.selectbox(label="Select a legend", 
                                  options=legend_list, 
                                  index=legend_list.index('Any Health Facility'))
    
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
   
    #display the map window in the platform
    with col1:
       m.to_streamlit(height=650)

    #add introduction part in HTML
    with col2:
        st.markdown('''
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    This module presents the 100-metre resolution maps in raster format of travel time to the nearest health facility at 4 levels.</li> 
                    </br>
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    The layer controller is located in the top right corner of the map window. </li></br>
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    The legend corresponding to each layer can be selected in the left function area.It is movable in the map window .</li></br>  
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    The travel time is measured in minutes. </li></br>
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    You can quickly access and download the original data through the buttons on the left side of the page. </li> 
        ''',unsafe_allow_html=True)

#############################################################
'''
write a function to achieve datasets download
'''

def download():
    st.sidebar.markdown(" Select raster datasets you want to download 👉")
    
    url1 = 'https://datashare.ed.ac.uk/handle/10283/3956'
    url2 = 'https://datashare.ed.ac.uk/handle/10283/3957'
    url3 = 'https://datashare.ed.ac.uk/handle/10283/3950'  
    url4 = 'https://datashare.ed.ac.uk/handle/10283/3954'
    
    #add download buttons to skip to the corresponding pages
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


#############################################################

if __name__ == '__main__':
    '''Main block'''
    #run the functions
    app()
    download()


