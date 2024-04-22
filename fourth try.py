
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data from the spreadsheet
baseball_file = r'C:\Users\jenfi\Downloads\BaseballGroup.xlsx'
baseball_df = pd.read_excel(baseball_file)

# Filter home games
home_games = baseball_df[baseball_df['H/A'] != '@']

# Group by team and calculate average performance metrics for home and away games
team_performance = home_games.groupby('Tm')[['R', 'RA']].mean().reset_index()
team_performance.columns = ['Tm', 'Avg_R_Home', 'Avg_RA_Home']

# Group by team and calculate average performance metrics for away games
away_games = baseball_df[baseball_df['H/A'] == '@']
away_performance = away_games.groupby('Tm')[['R', 'RA']].mean().reset_index()
away_performance.columns = ['Tm', 'Avg_R_Away', 'Avg_RA_Away']

# Merge home and away performance metrics
team_performance = pd.merge(team_performance, away_performance, on='Tm')

# Calculate correlation between home and away performance
correlation_R = team_performance['Avg_R_Home'].corr(team_performance['Avg_R_Away'])
correlation_RA = team_performance['Avg_RA_Home'].corr(team_performance['Avg_RA_Away'])

print("Correlation coefficient for runs scored (R):", correlation_R)
print("Correlation coefficient for runs allowed (RA):", correlation_RA)

# Visualize the correlation between home and away performance
plt.figure(figsize=(12, 6))

# Plot for runs scored (R)
plt.subplot(1, 2, 1)
plt.scatter(team_performance['Avg_R_Home'], team_performance['Avg_R_Away'])
plt.title('Runs Scored at Home vs Away')
plt.xlabel('Average Runs Scored at Home')
plt.ylabel('Average Runs Scored Away')

plt.text(0.95, 0.05, f'Correlation = {correlation_R:.2f}', transform=plt.gca().transAxes, fontsize=12,
         verticalalignment='bottom', horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

# Plot for runs allowed (RA)
plt.subplot(1, 2, 2)
plt.scatter(team_performance['Avg_RA_Home'], team_performance['Avg_RA_Away'])
plt.title('Runs Allowed at Home vs Away')
plt.xlabel('Average Runs Allowed at Home')
plt.ylabel('Average Runs Allowed Away')

plt.text(0.95, 0.05, f'Correlation = {correlation_RA:.2f}', transform=plt.gca().transAxes, fontsize=12,
         verticalalignment='bottom', horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

plt.tight_layout()
plt.show()
