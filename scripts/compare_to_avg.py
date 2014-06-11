import json

def init():
  with open('data/census_tracts.geojson') as a, open('data/city_average.json') as b:
    tracts = json.load(a)
    averages = json.load(b)

  census_tracts = tracts['features']
  tracts['features'] = transform(census_tracts, averages)

  with open('data/census_tracts.geojson', 'w') as a:
    json.dump(tracts, a)

def compare_to_average(stat, average):
  if stat > average:
    return 'above'
  else:
    return 'below'

def transform(census_tracts, averages):
  for tract in census_tracts:
    properties = tract['properties']
    new_dict = {}
    for prop in properties:
      if prop == 'tract_name' or prop == 'GEOID10':
        break
      else:
        average = averages[prop]
        prop_status = prop + '_status'
        above_or_below = compare_to_average(properties[prop], average)
        new_dict.update({prop_status: above_or_below})
    properties.update(new_dict)
    tract['properties'] = properties
  return census_tracts

init()
