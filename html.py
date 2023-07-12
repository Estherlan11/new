import streamlit as st
import streamlit.components.v1 as components


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
<script>


    var map = L.map(
        "map",
        {
            center: [2.0, 32.0],
            crs: L.CRS.EPSG900913,
            zoom: 6,
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

    var url1 ="http://127.0.0.1:8080/geoserver/gwc/service/tms/1.0.0/mock1%3ATT_H_II@EPSG%3A900913@pbf/{z}/{x}/{y}.pbf"
   
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

    var url2 = "http://127.0.0.1:8080/geoserver/gwc/service/tms/1.0.0/mock1%3ATT_H_III@EPSG%3A900913@pbf/{z}/{x}/{y}.pbf"
    
    var vectorTileOptions2 = {
    interactive: true, 
    layerURL: url2, 
    tms: true,
    rendererFactory: L.canvas.tile,
    vectorTileLayerStyles: {'TT_H_III':
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

    var url3 = "http://127.0.0.1:8080/geoserver/gwc/service/tms/1.0.0/mock1%3AIV@EPSG%3A900913@pbf/{z}/{x}/{y}.pbf"
   
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
    width=700, height=800, scrolling=True
    
)
