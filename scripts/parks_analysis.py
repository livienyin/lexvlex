import json

def number_of_parks(parks):
  return len(parks)

def total_park_acres(parks):
  acres = 0
  for park in parks:
    acres += park['properties']['ACRES']
  rounded_acres = round(acres, 3)
  return rounded_acres

def biggest_park(parks):
  biggest_park = ''
  park_acres = 0
  for park in parks:
    if park['properties']['ACRES'] > park_acres:
      park_acres = park['properties']['ACRES']
      biggest_park = park['properties']['PARK_NAME']
  return biggest_park

def number_of_playgrounds(parks):
  playgrounds = 0
  for park in parks:
    if park['properties']['PLAYGROUND'] == 'Yes':
      playgrounds += 1
  return playgrounds

def miles_of_trail(parks):
  miles = 0
  for park in parks:
    miles += park['properties']['PAVED_TRAI']
    miles += park['properties']['UNPVD_TRLS']
  return miles

def number_of_fields(parks):
  fields = 0
  for park in parks:
    properties = park['properties']
    park_fields = properties['BASKETBALL'] + properties['HARDCOURT'] + properties['TENNIS_COU'] + properties['VOLLEYBALL'] + properties['BALLFIELD'] + properties['FOOTBALLS']
    fields += park_fields
  return fields

def number_of_parks_with_gardens(parks):
  garden_parks = 0
  for park in parks:
    if park['properties']['GARDENS'] == 'Yes':
      garden_parks += 1
  return garden_parks

def number_of_parks_with_event_spaces(parks):
  event_parks = 0
  for park in parks:
    properties = park['properties']
    if properties['AMPHITHEAT'] == 'Yes' or properties['SPECIAL_EV'] == 'Yes' or properties['CC_YOUTH'] == 'Yes' or properties['CC_SENIOR'] == 'Yes' or properties['NGHBRBLDGS'] == 'Yes':
      event_parks += 1
  return event_parks

def number_of_parks_with_activities(parks):
  activity_parks = 0
  for park in parks:
    properties = park['properties']
    if properties['DAY_CAMP'] == 'Yes' or properties['NAT_PRGMS'] == 'Yes' or properties['SWIMMING'] == 'Yes':
      activity_parks += 1
  return activity_parks

def number_of_dog_parks(parks):
  dog_parks = 0
  for park in parks:
    if park['properties']['DOG_PARKS'] == 'Yes':
      dog_parks += 1
  return dog_parks

def number_of_picnic_areas(parks):
  picnic_areas = 0
  for park in parks:
    picnic_areas += park['properties']['PICNICTBLS']
  return picnic_areas

def number_of_restrooms(parks):
  restrooms = 0
  for park in parks:
    if park['properties']['RESTROOMS'] == 'Y':
      restrooms += 1
  return restrooms

def make_parks_array(parks, tract):
  parks_array = []
  for park in parks:
    if park['properties']['NAME10'] == tract['properties']['NAME10']:
      parks_array.append(park)
  return parks_array

def transform(parks, census_tracts):
  for tract in census_tracts:

    tract_name = tract['properties']['NAME10']
    GEOID10 = tract['properties']['GEOID10']
    tract_parks = make_parks_array(parks, tract)

    number = number_of_parks(tract_parks)
    acres = total_park_acres(tract_parks)
    largest_park = biggest_park(tract_parks)
    playgrounds = number_of_playgrounds(tract_parks)
    trail = miles_of_trail(tract_parks)
    fields = number_of_fields(tract_parks)
    garden_parks = number_of_parks_with_gardens(tract_parks)
    event_space = number_of_parks_with_event_spaces(tract_parks)
    activities = number_of_parks_with_activities(tract_parks)
    dog_parks = number_of_dog_parks(tract_parks)
    picnic = number_of_picnic_areas(tract_parks)
    restrooms = number_of_restrooms(tract_parks)

    new_dict = { 'tract_name': tract_name, 'GEOID10': GEOID10, 'number_of_parks': number, 'total_park_acres': acres, 'biggest_park': largest_park, 'playgrounds': playgrounds, 'trail': trail, 'fields': fields, 'gardens': garden_parks, 'event_space': event_space, 'activities': activities, 'dog_parks': dog_parks, 'picnic': picnic, 'restrooms': restrooms }

    tract['properties'] = new_dict

  return census_tracts

def init():
  with open('data/lexington_parks.geojson') as a, open('data/census_tracts.geojson') as b:
    lex_parks = json.load(a)
    tracts = json.load(b)

  parks = lex_parks['features']
  census_tracts = tracts['features']

  tracts['features'] = transform(parks, census_tracts)

  with open('data/census_tracts.geojson', 'w') as c:
    json.dump(tracts, c)

init()
