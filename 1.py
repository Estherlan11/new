import leafmap.foliumap as leafmap
import streamlit as st
import tempfile
from pathlib import Path
import geopandas as gpd
import pandas as pd
from zipfile import ZipFile
import time


st.set_page_config(page_title="Uganda travel time", layout="wide")


st.sidebar.markdown('Starting a long computation...')

# Add a placeholder
latest_iteration = st.sidebar.empty()
bar = st.sidebar.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

st.sidebar.markdown('...and now we\'re done!')

tab1, tab2 = st.tabs(["🎨Map","📈Chart"])

def gdf_to_shp(gdf, name):
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir, f"{name}.shp")
        gdf.to_file(path, driver="ESRI Shapefile")

        zip = Path(tmpdir, f"{name}_zip.zip")
        with ZipFile(zip, 'w') as zipObj:
            zipObj.write(f"{name}.shp",arcname = 'user_shapefiles.shp')
            zipObj.write(f"{name}.cpg",arcname = 'user_shapefiles.cpg')
            zipObj.write(f"{name}.dbf",arcname = 'user_shapefiles.dbf')
            zipObj.write(f"{name}.prj",arcname = 'user_shapefiles.prj')
            zipObj.write(f"{name}.shx",arcname = 'user_shapefiles.shx')
                
        return zip

def save_file():
   
        file_paths = [
            "Walking_only_travel_time",
            "IV_travel_time",
        ]
        ds_name = st.sidebar.selectbox(label="Select a dataset", options=file_paths)
        gdf = gpd.read_file("E:\\polygon_layer\\"+ds_name+".geojson")

        with tab2:
            col1, col2 = st.columns([2, 2])
            with col1:
                st.dataframe(pd.DataFrame(gdf.to_numpy(), columns=gdf.columns))
            with col2:
                st.pyplot(gdf.plot().figure)

        zip = gdf_to_shp(gdf, "E:\\"+ds_name+".geojson")

        with st.empty():
            with open(zip, "rb") as file:
                st.sidebar.download_button(
                    label="Download shapefile",
                    data=file,
                    file_name=f"{ds_name}.zip",
                    on_click=None 
            )


def app():
        
    m = leafmap.Map(center=[5,32], zoom=6)
        
    layer0 = 'E:\\layer0\\layer0.geojson' 
    
    style_dict = {
        "color": "yellow",
        "weight": 2,
        "opacity": 1,
        "fillOpacity": 0,
}

    m.add_geojson(layer0, 
                  layer_name="Walking_only_travel_time",
                  style=style_dict )
    
    layer1 = 'E:\\layer1\\layer1.geojson' 

    m.add_geojson(layer1, layer_name="IV_travel_time")
    
    save_file()
    
    with tab1:
        tab1.subheader('Vector Map')

    m.to_streamlit(height=700)
    


    m.save('map1.html')

if __name__ == "__main__":
    app()

