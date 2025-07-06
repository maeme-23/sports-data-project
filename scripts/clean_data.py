
# scripts/clean_data.py
import pandas as pd

def clean_data():
    df = pd.read_csv('data/raw_matches.csv')
    df.drop_duplicates(inplace=True)
    df.dropna(subset=['homeTeam.name', 'awayTeam.name', 'score.fullTime.home', 'score.fullTime.away'], inplace=True)
    df['match_date'] = pd.to_datetime(df['utcDate'])
    df = df[['match_date', 'homeTeam.name', 'awayTeam.name', 'score.fullTime.home', 'score.fullTime.away']]
    df.columns = ['date', 'home_team', 'away_team', 'home_score', 'away_score']
    df.sort_values(by='date', inplace=True)
    df.to_csv('data/cleaned_matches.csv', index=False)
    print(f"Cleaned data saved with {len(df)} records.")

if __name__ == "__main__":
    clean_data()
