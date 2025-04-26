import requests

# Step 1: Fetch strawberry data from Fruityvice API
url = "https://www.fruityvice.com/api/fruit/strawberry"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully connected to Fruityvice API.")
else:
    print(f"Failed to connect to Fruityvice API. Status code: {response.status_code}")
    exit()

# Step 2: Print raw JSON response
print("\nRaw JSON response:")
print(response.text)

# Step 3: Format and print the strawberry facts
data = response.json()
print("\nFormatted strawberry facts:")
print(f"Name: {data['name']}")
print(f"Family: {data['family']}")
print(f"Order: {data['order']}")
print(f"Genus: {data['genus']}")
print(f"Family: {data['family']}")
print(f"Nutrition per 100g:")
print(f"  - Calories: {data['nutritions']['calories']}")
print(f"  - Carbohydrates: {data['nutritions']['carbohydrates']}g")
print(f"  - Protein: {data['nutritions']['protein']}g")
print(f"  - Fat: {data['nutritions']['fat']}g")
print(f"  - Sugar: {data['nutritions']['sugar']}g")
