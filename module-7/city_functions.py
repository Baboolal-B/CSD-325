# city_functions.py

def format_city_country(city, country, language=None, population=None):
    """Return a formatted string like 'City, Country - population xxx, Language'."""
    if population and language:
        return f"{city}, {country} - population {population}, {language}"
    elif population:
        return f"{city}, {country} - population {population}"
    elif language:
        return f"{city}, {country}, {language}"
    else:
        return f"{city}, {country}"

# Sample calls with different parameters
print(format_city_country("Santiago", "Chile"))
print(format_city_country("Tokyo", "Japan", population=14000000))
print(format_city_country("Toronto", "Canada", population=3000000, language="English"))
