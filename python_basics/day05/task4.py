# . Create a Python dictionary of 3 cities and their populations. Save it to 
# "cities.json"
#  Then load the JSON and print each city and its population.
# 2. Ask the user for a new city & its population  - update this info in the json 
# file

import json

# Create a dictionary of cities and their populations
cities = {
    "New York": 8419000,
    "Los Angeles": 3980000,
    "Chicago": 2716000
}

with open("cities.json", 'w') as file:
    json.dump(cities, file)

with open("cities.json", 'r') as file:
    loaded_cities = json.load(file)
    print("Cities and their populations:")
    for city, population in loaded_cities.items():
        print(f"{city}: {population}")

new_city = input("Enter a new city name: ")
new_population = int(input("Enter the population of the new city: "))

# Update the dictionary with the new city and population
cities[new_city] = new_population

# Save the updated dictionary to the JSON file
with open("cities.json", 'w') as file:
    json.dump(cities, file)
    print(f"{new_city} with population {new_population} has been added to cities.json")

    

