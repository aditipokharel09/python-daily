from collections import Counter

# 1. THE DATA (Since the external file is missing, we define it here)
countries_data = [
    {"name": "Afghanistan", "capital": "Kabul", "languages": ["Pashto", "Uzbek"], "population": 27657145},
    {"name": "Estonia", "capital": "Tallinn", "languages": ["Estonian"], "population": 1323290},
    {"name": "Finland", "capital": "Helsinki", "languages": ["Finnish", "Swedish"], "population": 5530719},
    {"name": "United States", "capital": "Washington D.C.", "languages": ["English"], "population": 331002651},
    {"name": "Brazil", "capital": "Brasília", "languages": ["Portuguese"], "population": 212559417},
    {"name": "Japan", "capital": "Tokyo", "languages": ["Japanese"], "population": 126476461},
    {"name": "Germany", "capital": "Berlin", "languages": ["German"], "population": 83783942},
    {"name": "Nigeria", "capital": "Abuja", "languages": ["English", "Hausa", "Yoruba", "Igbo"], "population": 206139589},
    {"name": "India", "capital": "New Delhi", "languages": ["Hindi", "English"], "population": 1380004385},
    {"name": "China", "capital": "Beijing", "languages": ["Chinese"], "population": 1439323776},
    {"name": "Norway", "capital": "Oslo", "languages": ["Norwegian"], "population": 5378857}
]

# --- 2. SORTING LOGIC ---

# Sort by name
sorted_by_name = sorted(countries_data, key=lambda x: x['name'])

# Sort by capital
sorted_by_capital = sorted(countries_data, key=lambda x: x['capital'])

# Sort by population (Largest to Smallest)
sorted_by_pop = sorted(countries_data, key=lambda x: x['population'], reverse=True)

# --- 3. EXERCISE ANSWERS ---

# I. Ten most populated countries
top_10_populated = sorted_by_pop[:10]

# II. Ten most spoken languages
all_languages = []
for country in countries_data:
    all_languages.extend(country['languages'])

# We use Counter to find the 10 most frequent languages
most_spoken_langs = Counter(all_languages).most_common(10)

# --- 4. PRINTING THE RESULTS ---

print("--- TOP 10 MOST POPULATED COUNTRIES ---")
for country in top_10_populated:
    print(f"{country['name']}: {country['population']:,}")

print("\n--- TOP 10 MOST SPOKEN LANGUAGES ---")
for lang, count in most_spoken_langs:
    print(f"{lang}: Used in {count} countries")

print("\n--- FIRST 3 COUNTRIES SORTED BY NAME ---")
for country in sorted_by_name[:3]:
    print(country['name'])