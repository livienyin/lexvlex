import json

with open('data/census_tracts.geojson') as a:
  tracts = json.load(a)

census_tracts = tracts['features']

for tract in census_tracts:
  total_acres = tract['properties']['total_park_acres']
  rounded_acres = round(total_acres, 3)
  tract['properties']['total_park_acres'] = rounded_acres

with open('data/census_tracts.geojson', 'w') as a:
  json.dump(tracts, a)
