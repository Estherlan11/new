'''
An app to publish the point adat of settlements distribution 
'''

#############################################################
#import necessary packages

import streamlit as st
import folium
import leafmap.foliumap as leafmap

#############################################################
#set the whole page layout and navigation bar
st.set_page_config(page_title="Uganda travel time",layout='wide')

def app():
    
    #set the layout and title
    st.title("Raster Split Map")

    col1, col2 = st.columns([2.8, 1.2])
    
    #add a map viewer and set the paraments
    m = leafmap.Map(center=[1.5, 32], 
                    zoom=7,
                    draw_control=False,
                    measure_control=False,
                    attribution_control=True)

    #call the left_layer WMS request from GeoServer
    left_layer = folium.WmsTileLayer(url = 'http://34.147.148.225:8080/geoserver/wms?',
                            layers = 'data:pryamid',
                            transparent = True, 
                            control = True,
                            version = '1.1.1',
                            fmt="image/png",
                            name = 'Resolution: 100m',
                            overlay = True,
                            show = True,
                            )
    #call the left_layer WMS request from GeoServer
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

    #add the two layers on the map viewer
    m.split_map(left_layer, right_layer)

    legend_dict1 = {                    #add the legend information of layers
    '<= 44.49': '#d7191c',
    '44.49-65.98': '#e85b3b',
    '65.98-87.71': '#f99d59',
    '87.71-111.82': '#fec980',
    '111.82-148.29': '#ffedaa',
    '148.29-197.14': '#ecf7b9',
    '197.14-248.34': '#c7e8ad',
    '248.34-416.46': '#9fd6aa',
    '416.46-794.02': '#6dbac3',
    '> 794.02': '#3b9edc',
    }

    legend_dict2 = {
    '<= 22.00': '#d7191c',
    '22.00-31.01': '#e85b3b',
    '31.01-42.01': '#f99d59',
    '42.01-55.00': '#fec980',
    '55.00-70.00': '#ffedaa',
    '70.00-91.00': '#ecf7b9',
    '91.00-124.00': '#c7e8ad',
    '124.00-193.99': '#9fd6aa',
    '193.99-444.99': '#6dbac3',
    '> 444.99': '#3b9edc',
    }

    legend_list = [
            '20m Resolution',
            '1000m Resolution',
        ]
    #design a selection box in sidebar to choose the legends
    legend = st.sidebar.selectbox(label="Select a legend", 
                                  options=legend_list, 
                                  index=legend_list.index('20m Resolution'))
    
    #add the movable legends into the map viewer
    if legend == '20m Resolution':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict1)
    elif legend == '1000m Resolution':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict2)
    
    #display the map window in the platform
    with col1:
        m.to_streamlit(height=700)
    
    #add introduction part in HTML
    with col2:
         st.markdown('''
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    This section features a split map for comparing the same dataset at different resolutions.</li> </br> 
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    The left layer displays Uganda Travel Time to any health facility Map Output at 20-meter resolution, while the right layer presents the data at 1000-meter resolution.</li> </br>  
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    The extent of both layers can be adjusted by moving the center axis. </li> </br>
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    The legend corresponding to each layer can be selected in the left function area.It is movable in the map window.</li> </br>  
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    The travel time is measured in minutes. </li> 
        ''',unsafe_allow_html=True)
    
    
#############################################################

if __name__ == '__main__':
    # Main block
    app()
