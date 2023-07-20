import leafmap.foliumap as leafmap
import streamlit as st
import tempfile
from pathlib import Path
import geopandas as gpd
import pandas as pd
from zipfile import ZipFile
import time
import streamlit.components.v1 as components


st.set_page_config(page_title="Uganda travel time", layout='wide')

st.sidebar.markdown('Starting a long loading time cause the big data volume...')

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
            "Travel Time to Hospital",
            "Travel Time to Level II Health centre & Hospital",
            "Travel Time to Level III Health centre & Hospital",
            "Travel Time to Level IV Health centre & Hospital"
        ]
        ds_name = st.sidebar.selectbox(label="Select a dataset", options=file_paths)
        gdf = gpd.read_file("/home/lrx0914/geojsonfile/"+ds_name+".geojson")

        with tab2:
            col1, col2 = st.columns([3, 2])
            with col1:
                st.dataframe(pd.DataFrame(gdf.to_numpy(), columns=gdf.columns),height=420)
            with col2:
                st.pyplot(gdf.plot().figure)

        zip = gdf_to_shp(gdf, "/home/s2283650/Downloads/"+ds_name+".geojson")

        with st.empty():
            with open(zip, "rb") as file:
                st.sidebar.download_button(
                    label="Download shapefile",
                    data=file,
                    file_name=f"{ds_name}.zip",
                    on_click=None 
            )

def app():
    with tab1:
        
        col1, col2 = st.columns([4, 1])
    
        with col1:
            components.html('''
    
                    <html>

    <head>

        <meta http-equiv="content-type" content="text/html; charset=UTF-8" />

        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>

        <style>
            html,
            body {
                width: 100%;
                height: 100%;
                margin: 0;
                padding: 0;
            }
        </style>
        <style>
            #map {
                position: absolute;
                top: 0;
                bottom: 0;
                right: 0;
                left: 0;
            }
        </style>
        <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
        <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
        <script
            src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" />
        <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap.min.css" />
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css" />
        <link rel="stylesheet"
            href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css" />
        <link rel="stylesheet"
            href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css" />

        <meta name="viewport" content="width=device-width,
                    initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
        <style>
            #map {
                position: relative;
                width: 700.0px;
                height: 650.0px;
                left: 0.0%;
                top: 0.0%;
            }
            

            .leaflet-container {
                font-size: 1rem;
            }
        </style>

        <script src="https://unpkg.com/leaflet.vectorgrid@latest/dist/Leaflet.VectorGrid.bundled.js"></script>
    </head>

    <body>


        <div class="folium-map" id="map"></div>

    </body>
    <script>


        var map = L.map(
            "map",
            {
                center: [1.5, 32.0],
                crs: L.CRS.EPSG900913,
                zoom: 7,
                zoomControl: true,
                preferCanvas: false,
            }
        );



        var basemap = L.tileLayer(
            "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            ).addTo(map);
    

        var layer1 = L.featureGroup(
                    {}
                ).addTo(map);

        var url1 ="http://34.147.148.225:8080/geoserver/gwc/service/tms/1.0.0/data%3ATT_H_II@EPSG%3A900913@pbf/{z}/{x}/{y}.pbf"
    
        var vectorTileOptions1 = {
        interactive: true, 
        layerURL: url1, 
        tms: true,
        rendererFactory: L.canvas.tile,
        vectorTileLayerStyles: {'TT_H_II':
                    {
                    color: '#2C99FC',
                    width: 1,
                }
                },        

        getFeatureId: function(f) {
        return f.properties.osm_id;
        }
    };
        
        var tile_layer_1 = L.vectorGrid.protobuf(
                url1, vectorTileOptions1)
                .addTo(layer1);

        tile_layer_1.on("mouseover", e => {

    var properties = e.layer.properties;
        L.popup()
        .setContent("<b>Town_name:</b> &nbsp"+properties.NAME_3+"<br>"+ "<b>Tavel Time:</b>&nbsp"+properties.MEAN)
        .setLatLng(e.latlng)
        .openOn(map);
    });


    var layer2 = L.featureGroup(
                    {}
                ).addTo(map);

        var url2 = "http://34.147.148.225:8080/geoserver/gwc/service/tms/1.0.0/data%3ATT_H_IIIV@EPSG%3A900913@pbf /{z}/{x}/{y}.pbf"
        
        var vectorTileOptions2 = {
        interactive: true, 
        layerURL: url2, 
        tms: true,
        rendererFactory: L.canvas.tile,
        vectorTileLayerStyles: {'TT_H_IIIV':
                    {
                    color: 'green',
                    width: 1,
                }
                },        

        getFeatureId: function(f) {
        return f.properties.osm_id;
        }
    };
            
            
    var tile_layer_2 = L.vectorGrid.protobuf(
                url2, vectorTileOptions2)
                .addTo(layer2);

        tile_layer_2.on("mouseover", e => {

    var properties = e.layer.properties;
        L.popup()
        .setContent("<b>Town_name:</b> &nbsp"+properties.NAME_3+"<br>"+ "<b>Tavel Time:</b>&nbsp"+properties.MEAN)
        .setLatLng(e.latlng)
        .openOn(map);
    });


    var layer3 = L.featureGroup(
                    {}
                ).addTo(map);

        var url3 = "http://34.147.148.225:8080/geoserver/gwc/service/tms/1.0.0/data%3AIV@EPSG%3A900913@pbf/{z}/{x}/{y}.pbf"
    
        var vectorTileOptions3 = {
        interactive: true, 
        layerURL: url3, 
        tms: true,
        rendererFactory: L.canvas.tile,
        vectorTileLayerStyles: {'IV':
                    {
                    color: ' #CC99FC',
                    width: 1,
                }
                },        

        getFeatureId: function(f) {
        return f.properties.osm_id;
        }
    };
        
        var tile_layer_3 = L.vectorGrid.protobuf(
                url3, vectorTileOptions3)
                .addTo(layer3);

        tile_layer_3.on("mouseover", e => {

    var properties = e.layer.properties;
        L.popup()
        .setContent("<b>Town_name:</b> &nbsp"+properties.NAME_3+"<br>"+ "<b>Tavel Time:</b>&nbsp"+properties.MEAN)
        .setLatLng(e.latlng)
        .openOn(map);
    });



    var outlayer = {
                    base_layers : {
                        "openstreetmap" : basemap,
                    },
                    overlays :  {
                        "Hostipal II" : layer1,
                        "Hostipal III" : layer2,
                        "Hostipal IV" : layer3
                    },
                };
                L.control.layers(
                    outlayer.base_layers,
                    outlayer.overlays,
                    {"autoZIndex": true, "collapsed": true, "position": "topright"}
                ).addTo(map);
            

    </script>

    </html>
                    ''',
        width=700, height=650, scrolling=True
        
    )
        with col2:
            st.markdown('test')

if __name__ == "__main__":
    app()
    save_file()


