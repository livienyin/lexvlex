var statistics = {
  "activities": "Programming Activities",
  "picnic": "Picnic Areas",
  "playgrounds": "Parks with Playgrounds",
  "dog_parks": "Dog Parks",
  "tract_name": "Census Tract",
  "restrooms": "Parks with Restrooms",
  "trail": "Miles of Trails (in Parks)",
  "event_space": "Event Spaces (in Parks)",
  "number_of_parks": "Total Parks",
  "fields": "Sports Fields/Courts",
  "total_park_acres": "Total Park Acreage",
  "biggest_park": "Largest Park by Area",
  "gardens": "Commnity Gardens"
};

var map = L.map('map', {
  zoom: 11,
  center: [38.042, -84.515],
  maxZoom: 14,
  minZoom: 10
});

map.scrollWheelZoom.disable();

var basemapTiles = L.tileLayer('http://{s}.tiles.mapbox.com/v3/codeforamerica.i6fijbde/{z}/{x}/{y}.png').addTo(map);

function style(feature) {
  var tractColor = '#b2df8a';

  if (feature.properties.number_of_parks == 0) {
    tractColor = '#aaa';
  }

  return {
    fillColor: tractColor,
    weight: 1,
    opacity: 0.7,
    color: tractColor,
    fillOpacity: 0.6
  };
};

function popup(feature) {
  var tract = feature.properties;
  var popupText = '<strong>Tract Number ' + tract.tract_name + '</strong>';
/*  for (var amenity in tract) {
    popupText += '<br>' + tract.statistics[amenity] + ': ' + tract.amenity;
  }; */
  return popupText;
};

function onEachFeature(feature, layer) {
  layer.on('click', function(e) {
    map.fitBounds(e.target.getBounds());
  });
  layer.bindPopup(popup(feature));
};

$.getJSON('./data/census_tracts.geojson', function(data) {
  var census_tracts = L.geoJson(data, {
    style: style,
    onEachFeature: onEachFeature
  });
  census_tracts.addTo(map);
});
