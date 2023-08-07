'''
An app to publish the vector data 
'''

#############################################################
#import necesary packges

import leafmap.foliumap as leafmap
import streamlit as st
import tempfile
from pathlib import Path
import geopandas as gpd
import pandas as pd
from zipfile import ZipFile
import time
import streamlit.components.v1 as components

#############################################################
#set the whole page layout and navigation bar

st.set_page_config(page_title="Uganda travel time", layout='wide')
st.title("Vector Map")

# Add a placeholder animation
st.sidebar.markdown('Starting a long loading time please wait for a moment...')
latest_iteration = st.sidebar.empty()
# set the start time
bar = st.sidebar.progress(0)

# set a loop and update the progress bar with each iteration
for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

# Add the remindering word
st.sidebar.markdown('...and now we\'re done!')

#insert containers with different elements separated into tabs on the top of the page
tab1, tab2 = st.tabs(["🎨Map","📈Chart"])

#############################################################

# write a function to transform the data from Geodataframe to Shapefile


def gdf_to_shp(gdf, name):
    #set a temporary directory to store the shapefiles
    with tempfile.TemporaryDirectory() as tmpdir:
        path = Path(tmpdir, f"{name}.shp")
        gdf.to_file(path, driver="ESRI Shapefile")
        
        #use zip package to compress all the files into a zip format
        zip = Path(tmpdir, f"{name}_zip.zip")
        with ZipFile(zip, 'w') as zipObj:
            zipObj.write(f"{name}.shp",arcname = 'user_shapefiles.shp')
            zipObj.write(f"{name}.cpg",arcname = 'user_shapefiles.cpg')
            zipObj.write(f"{name}.dbf",arcname = 'user_shapefiles.dbf')
            zipObj.write(f"{name}.prj",arcname = 'user_shapefiles.prj')
            zipObj.write(f"{name}.shx",arcname = 'user_shapefiles.shx')
                
        return zip

#############################################################

# write a function to download files

def save_file():
    #insert the file paths
        file_paths = [
            "Travel Time to Any Health Facility",
            "Travel Time to Level III Health centre",
            "Travel Time to Level IV Health centre",
            "Travel Time to Level IV Health centre & Hospital"
        ]
        #add a selection box for users to choose the target download file
        ds_name = st.sidebar.selectbox(label="Select a dataset to dowload", options=file_paths)
        gdf = gpd.read_file("/home/lrx0914/geojsonfile/"+ds_name+".geojson")

        #design a page to preview the downloading data attribute table and map image
        with tab2:
            col1, col2 = st.columns([3, 2])
            with col1:
                st.dataframe(pd.DataFrame(gdf.to_numpy(), columns=gdf.columns),height=420)
            with col2:
                st.pyplot(gdf.plot().figure)

        #input all the download data sources in geojson format
        zip = gdf_to_shp(gdf, "/home/lrx0914/"+ds_name+".geojson")
        #read the data sources according to the file name
        with st.empty():
            with open(zip, "rb") as file:
                st.sidebar.download_button(
                    label="Download shapefile",
                    data=file,
                    file_name=f"{ds_name}.zip",
                    on_click=None 
            )
#############################################################

# write a function to add the vector layers using WMTS
 
def app():
    #set the layout
    with tab1:
        
        col1, col2 = st.columns([2.8, 1.2])
    
    #using 'components.html' function to add the layers with HTML language
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

        <!-- insert javascript packages to set the style  -->

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
                height: 700.0px;
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

    <!-- add the map window -->
    <script>

        //add the map window
        
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


        //input the base map
        var basemap = L.tileLayer(
            "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            ).addTo(map);
    
    <!-- layer1 -->
        //store the layer1 into the layer group 
        var layer1 = L.featureGroup(
                    {}
                ).addTo(map);

        //call the WMTS request
        var url1 ="http://34.147.148.225:8080/geoserver/gwc/service/tms/1.0.0/data%3Aallh@EPSG%3A900913@pbf/{z}/{x}/{y}.pbf"
        

        <!-- use VectorGrid API to achieve interactive function -->
        //set the style of the first vector layer
        var vectorTileOptions1 = {
        interactive: true, 
        layerURL: url1, 
        tms: true,
        rendererFactory: L.canvas.tile,
        vectorTileLayerStyles: {'allh':
                    {
                    color: '#2C99FC',
                    width: 1,
                }
                }, 

        //get the detail information of each polygon in layer1
        getFeatureId: function(f) {
        return f.properties.osm_id;
        }
    };
        //use VectorGrid to add the layer to the map
        var tile_layer_1 = L.vectorGrid.protobuf(
                url1, vectorTileOptions1)
                .addTo(layer1);
        
        // add the popup window by mouse hovering and clicking
        tile_layer_1.on("mouseover", e => {

    var properties = e.layer.properties;
        L.popup()
        .setContent("<b>Town_name:</b> &nbsp"+properties.NAME_3+"<br>"+ "<b>Tavel Time:</b>&nbsp"+properties.MEAN)
        .setLatLng(e.latlng)
        .openOn(map);
    });

    <!-- layer2 -->
    //store the layer2 into the layer group 
    var layer2 = L.featureGroup(
                    {}
                ).addTo(map);

        //call the WMTS request of layer2
        var url2 = "http://34.147.148.225:8080/geoserver/gwc/service/tms/1.0.0/data%3ATT_H_IIIV@EPSG%3A900913@pbf /{z}/{x}/{y}.pbf"
        
        <!-- use VectorGrid API to achieve interactive function -->
        //set the style of the second vector layer  
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
        //get the detail information of each polygon in layer2
        getFeatureId: function(f) {
        return f.properties.osm_id;
        }
    };
        
    //use VectorGrid to add the layer to the map
    var tile_layer_2 = L.vectorGrid.protobuf(
                url2, vectorTileOptions2)
                .addTo(layer2);
    
        // add the popup window by mouse hovering and clicking
        //select the target field
        tile_layer_2.on("mouseover", e => {
    
    var properties = e.layer.properties;
        L.popup()
        .setContent("<b>Town_name:</b> &nbsp"+properties.NAME_3+"<br>"+ "<b>Tavel Time:</b>&nbsp"+properties.MEAN)
        .setLatLng(e.latlng)
        .openOn(map);
    });


    <!-- layer3 -->
    var layer3 = L.featureGroup(
                    {}
                ).addTo(map);

        //call the WMTS request of layer3
        var url3 = "http://34.147.148.225:8080/geoserver/gwc/service/tms/1.0.0/data%3AIV@EPSG%3A900913@pbf/{z}/{x}/{y}.pbf"
       
        <!-- use VectorGrid API to achieve interactive function -->
        //set the style of the 3rd vector layer  
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

        //get the detail information of each polygon in layer3
        getFeatureId: function(f) {
        return f.properties.osm_id;
        }
    };
        //use VectorGrid to add the layer to the map
        var tile_layer_3 = L.vectorGrid.protobuf(
                url3, vectorTileOptions3)
                .addTo(layer3);

    
        // add the popup window by mouse hovering and clicking
        //select the target field
        tile_layer_3.on("mouseover", e => {

    var properties = e.layer.properties;
        L.popup()
        .setContent("<b>Town_name:</b> &nbsp"+properties.NAME_3+"<br>"+ "<b>Tavel Time:</b>&nbsp"+properties.MEAN)
        .setLatLng(e.latlng)
        .openOn(map);
    });



    <!-- layer4 -->
    //store the layer into layer group
    var layer4 = L.featureGroup(
                    {}
                ).addTo(map);

        //call the WMTS request of layer4
        var url4 = "http://34.147.148.225:8080/geoserver/gwc/service/tms/1.0.0/data%3Ah4_h@EPSG%3A900913@pbf/{z}/{x}/{y}.pbf"
        
        <!-- use VectorGrid API to achieve interactive function -->
        //set the style of the 4th vector layer  
        var vectorTileOptions4 = {
        interactive: true, 
        layerURL: url4, 
        tms: true,
        rendererFactory: L.canvas.tile,
        vectorTileLayerStyles: {'h4_h':
                    {
                    color: 'yellow',
                    width: 1,
                }
                },        

        //get the detail information of each polygon in layer4
        getFeatureId: function(f) {
        return f.properties.osm_id;
        }
    };
            
    //use VectorGrid to add the layer to the map
    var tile_layer_4 = L.vectorGrid.protobuf(
                url4, vectorTileOptions4)
                .addTo(layer4);

        // add the popup window by mouse hovering and clicking
        //select the target field
        tile_layer_4.on("mouseover", e => {

    var properties = e.layer.properties;
        L.popup()
        .setContent("<b>Town_name:</b> &nbsp"+properties.NAME_3+"<br>"+ "<b>Tavel Time:</b>&nbsp"+properties.MEAN)
        .setLatLng(e.latlng)
        .openOn(map);
    });

    //display all the layers stored in the group and add them into the layer controller
    var outlayer = {
                    base_layers : {
                        "openstreetmap" : basemap,
                    },
                    overlays :  {
                        "Any Health Facility" : layer1,
                        "Health Centre III" : layer2,
                        "Health Center IV" : layer3,
                        "Health Center IV and Hospital" : layer4,
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

        #set the map window size and display it in the platform
        height=700, scrolling=True
        
    )
        #add introduction part in HTML
        with col2:
             st.markdown('''
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    In this section, the travel time to the nearest health facility maps is displayed at diffrent map outputs.</li> </br> 
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    The travel time values are shown for level 3 administrative boundaries of Uganda. </li> </br> 
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    You can hover over a target district to obtain the average travel time to the nearest health facility in that area.</li></br>  
                    <li style="font-family:sans-serif; color:#3b3a37; font-size: 18px; text-align:justify;">
                    You can select the required data to download through the selection box in the side bar. </br>
                    Additionally, the attribute table of the selected dataset can be previewed through the chart section.</li> </br> 
                    ''',unsafe_allow_html=True)


#############################################################

if __name__ == '__main__':

    # Main block
    # run the functions
    app()
    save_file()


