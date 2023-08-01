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
        m.to_streamlit(width=700, height=650)
    
    with col2:
        st.markdown('test')
    


    
if __name__ == "__main__":
    app()
