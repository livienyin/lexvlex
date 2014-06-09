import json

def init():
  with open('data/census_tracts.geojson') as a:
    tracts = json.load(a)

  census_tracts = tracts['features']
  data = transform(census_tracts)

  with open('data/city_average.json', 'w') as b:
    json.dump(data, b)

def transform(census_tracts):
  number = get_average(census_tracts, 'number_of_parks')
  acres = get_average(census_tracts, 'total_park_acres')
  largest_park = 'Not Applicable'
  playgrounds = get_average(census_tracts, 'playgrounds')
  trail = get_average(census_tracts, 'trail')
  fields = get_average(census_tracts, 'fields')
  garden_parks = get_average(census_tracts, 'gardens')
  event_space = get_average(census_tracts, 'event_space')
  activities = get_average(census_tracts, 'activities')
  dog_parks = get_average(census_tracts, 'dog_parks')
  picnic = get_average(census_tracts, 'picnic')
  restrooms = get_average(census_tracts, 'restrooms')

  return { 'number_of_parks': number, 'total_park_acres': acres, 'biggest_park': largest_park, 'playgrounds': playgrounds, 'trail': trail, 'fields': fields, 'gardens': garden_parks, 'event_space': event_space, 'activities': activities, 'dog_parks': dog_parks, 'picnic': picnic, 'restrooms': restrooms }

def get_average(census_tracts, stat_field):
  total_tracts = len(census_tracts)
  total = 0.0
  for tract in census_tracts:
    total += tract['properties'][stat_field]
  average = total / total_tracts
  rounded_average = round(average, 3)
  return rounded_average

init()
