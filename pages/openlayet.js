import MVT from 'ol/format/MVT.js';
import Map from 'ol/Map.js';
import VectorTileLayer from 'ol/layer/VectorTile.js';
import VectorTileSource from 'ol/source/VectorTile.js';
import View from 'ol/View.js';

const map = new Map({
  target: 'map',
  view: new View({
    center: [0, 0],
    zoom: 2,
  }),
  layers: [
    new VectorTileLayer({
      source: new VectorTileSource({
        format: new MVT(),
        url: 'http://localhost:8080/geoserver/gwc/service/tms/1.0.0/mock1:Walking_only_travel_time@EPSG:900913@pbf/{z}/{y}/{x}.pbf',
      }),
    }),
  ],
});

//map.on('pointermove', showInfo);

const info = document.getElementById('info');
function showInfo(event) {
  const features = map.getFeaturesAtPixel(event.pixel);
  if (features.length == 0) {
    info.innerText = '';
    info.style.opacity = 0;
    return;
  }
  const properties = features[0].getProperties();
  info.innerText = JSON.stringify(properties, null, 2);
  info.style.opacity = 1;
}