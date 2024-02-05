country = input() # Add country name
visits = int(input()) # Number of visits

def process_cities_input(input_string):
    cities = input_string.split(',')
    cities = [city.strip().title() for city in cities]
    return cities

list_of_cities = process_cities_input(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(name, times_visited, cities_visited):
    new_country = {
        "country": name,
        "visits": int(times_visited),
        "cities": cities_visited
    }
    travel_log.append(new_country)

# Do not change the code below
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
print(travel_log)