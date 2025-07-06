
import requests
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")  # Replace with your actual token
HEADERS = {'X-Auth-Token': API_TOKEN}

# Leagues and seasons to fetch
competitions = ['PL', 'BL1', 'SA']  # Premier League, Bundesliga, Serie A
seasons = [2023, 2022, 2021]

all_matches = []

for comp in competitions:
    for season in seasons:
        url = f'https://api.football-data.org/v4/competitions/{comp}/matches?season={season}'
        print(f"Fetching {comp} {season}...")
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            matches = data.get('matches', [])
            for match in matches:
                match['competition'] = comp
                match['season'] = season
            all_matches.extend(matches)
        else:
            print(f"Failed to fetch {comp} {season}: {response.status_code}")

# Normalize and save
df = pd.json_normalize(all_matches)
os.makedirs('data', exist_ok=True)
df.to_csv('data/raw_matches.csv', index=False)
print(f"Total matches fetched: {len(df)}")

