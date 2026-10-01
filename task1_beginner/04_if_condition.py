"""ShadowFox Python Internship - Task 1: If Condition"""

# 1. BMI category.
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)

if bmi >= 30:
    category = "Obesity"
elif bmi >= 25:
    category = "Overweight"
elif bmi >= 18.5:
    category = "Normal"
else:
    category = "Underweight"

print(f"BMI: {bmi:.2f}")
print("Category:", category)

# 2 and 3. City-country mapping and same-country check.
countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"],
}

city_to_country = {
    city.lower(): country
    for country, cities in countries.items()
    for city in cities
}

city = input("Enter a city name: ").strip()
country = city_to_country.get(city.lower())
if country:
    print(f"{city} is in {country}")
else:
    print("City not found in the given list.")

first_city = input("Enter the first city: ").strip()
second_city = input("Enter the second city: ").strip()

first_country = city_to_country.get(first_city.lower())
second_country = city_to_country.get(second_city.lower())

if first_country and second_country and first_country == second_country:
    print(f"Both cities are in {first_country}")
else:
    print("They don't belong to the same country")
