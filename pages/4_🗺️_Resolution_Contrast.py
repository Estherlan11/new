import streamlit as st
import folium
import leafmap.foliumap as leafmap

st.set_page_config(page_title="Uganda travel time",layout='wide')

def app():

    st.title("Raster Split Map")

    col1, col2 = st.columns([3.8, 1.5])
    
    m = leafmap.Map(center=[1.5, 32], 
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
    legend = st.sidebar.selectbox(label="Select a legend", 
                                  options=legend_list, 
                                  index=legend_list.index('20m Resolution'))
    
    if legend == '20m Resolution':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict1)
    elif legend == '1000m Resolution':
        m.add_legend(title="Travel Time", 
                     legend_dict=legend_dict2)
    
    with col1:
        m.to_streamlit(width=720, height=650)
    
    with col2:
         st.markdown('''
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                    This section features a split map for comparing the same dataset at different resolutions.</li> </br> 
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                    The left layer displays Uganda Travel Time to any health facility Map Output at 20-meter resolution, while the right layer presents the data at 1000-meter resolution.</li> </br>  
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                    The extent of both layers can be adjusted by moving the center axis. </li> </br>
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                    The legend corresponding to each layer can be selected in the left function area.It is movable in the map window.</li> </br>  
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 17px; text-align:justify;">
                    The travel time is measured in minutes. </li> 
        ''',unsafe_allow_html=True)
    


    
if __name__ == "__main__":
    app()
