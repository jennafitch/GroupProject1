
import pandas as pd

# Load data from BaseballGroup.xlsx
baseball_file = r'C:\Users\jenfi\Downloads\BaseballGroup.xlsx'
baseball_df = pd.read_excel(baseball_file)

# Filter data for home and away games
home_games = baseball_df[baseball_df['H/A'] != '@']
away_games = baseball_df[baseball_df['H/A'] == '@']

# Calculate total runs scored and allowed at home
home_runs_scored = home_games.groupby('Tm')['R'].sum()
home_runs_allowed = home_games.groupby('Tm')['RA'].sum()

# Calculate total runs scored and allowed away
away_runs_scored = away_games.groupby('Tm')['R'].sum()
away_runs_allowed = away_games.groupby('Tm')['RA'].sum()

# Create a DataFrame to store the results
results = pd.DataFrame({
    'Home Runs Scored': home_runs_scored,
    'Away Runs Scored': away_runs_scored,
    'Home Runs Allowed': home_runs_allowed,
    'Away Runs Allowed': away_runs_allowed
})

# Fill missing values with 0
results = results.fillna(0)

# Calculate the differences between home and away
results['Runs Scored Difference'] = results['Home Runs Scored'] - results['Away Runs Scored']
results['Runs Allowed Difference'] = results['Home Runs Allowed'] - results['Away Runs Allowed']

# Print the results
print(results)
