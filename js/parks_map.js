var map = L.map('map', {
  zoom: 11,
  center: [38.042, -84.515],
  maxZoom: 14,
  minZoom: 10
});

var basemapTiles = L.tileLayer('http://{s}.tiles.mapbox.com/v3/codeforamerica.i6fijbde/{z}/{x}/{y}.png').addTo(map);
