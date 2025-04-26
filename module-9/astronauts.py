import requests
import json

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def get_astronauts():
    url = "http://api.open-notify.org/astros.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Pretty-print the entire JSON response
        jprint(data)
        
        print(f"\n There are {data['number']} astronauts in space right now:\n")
        for person in data['people']:
            print(f"Astronaut: {person['name']} | Craft: {person['craft']}")
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching data:", e)

get_astronauts()
