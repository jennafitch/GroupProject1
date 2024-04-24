
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the datasets
baseball_group_df = pd.read_excel(r'C:\Users\jenfi\Downloads\BaseballGroup.xlsx')
teams_df = pd.read_excel(r'C:\Users\jenfi\OneDrive - University of Wisconsin-Whitewater\Teams.xlsx')

# Filter data for the year 2022
teams_df = teams_df[teams_df['yearID'] == 2022]

# Step 1: Calculate ballpark-specific statistics using Teams.xlsx

# Calculate Home Winning Percentage
teams_df['HomeWinPct'] = teams_df['Ghome'] / teams_df['G']

# Calculate Home Runs Scored and Allowed per Game
teams_df['HR_per_game'] = teams_df['HR'] / teams_df['Ghome']
teams_df['HRA_per_game'] = teams_df['HRA'] / teams_df['Ghome']

# Step 2: Analyze the impact of different ballparks using BaseballGroup.xlsx

# Merge BaseballGroup.xlsx with Teams.xlsx on the 'Tm' column
merged_df = pd.merge(baseball_group_df, teams_df, left_on='Tm', right_on='teamID', how='left')

# Calculate ballpark-specific statistics for each game
merged_df['HomeWinPct'] = merged_df['Ghome'] / merged_df['G']
merged_df['HR_per_game'] = merged_df['HR'] / merged_df['Ghome']
merged_df['HRA_per_game'] = merged_df['HRA'] / merged_df['Ghome']

# Step 3: Provide actionable insights and recommendations

# Example: Analyze the impact of ballpark on game outcomes
ballpark_impact = merged_df.groupby(['lgID', 'divID', 'park'])[['HomeWinPct', 'HR_per_game', 'HRA_per_game']].mean()

# Print the results
print("Ballpark Impact on Game Outcomes and Player Performances:")
print(ballpark_impact)

# Visualize Home Winning Percentage by Ballpark for AL teams
plt.figure(figsize=(18, 6))
sns.barplot(data=merged_df[merged_df['lgID'] == 'AL'], x='park', y='HomeWinPct', hue='divID', ci=None)
plt.title('Home Winning Percentage by Ballpark - AL Teams (2022)')
plt.xlabel('Ballpark')
plt.ylabel('Home Winning Percentage')
plt.xticks(rotation=45)
plt.legend(title='Division')
plt.show()

# Visualize Home Runs Scored per Game by Ballpark for AL teams
plt.figure(figsize=(18, 6))
sns.barplot(data=merged_df[merged_df['lgID'] == 'AL'], x='park', y='HR_per_game', hue='divID', ci=None)
plt.title('Home Runs Scored per Game by Ballpark - AL Teams (2022)')
plt.xlabel('Ballpark')
plt.ylabel('Home Runs Scored per Game')
plt.xticks(rotation=45)
plt.legend(title='Division')
plt.show()

# Visualize Home Runs Allowed per Game by Ballpark for AL teams
plt.figure(figsize=(18, 6))
sns.barplot(data=merged_df[merged_df['lgID'] == 'AL'], x='park', y='HRA_per_game', hue='divID', ci=None)
plt.title('Home Runs Allowed per Game by Ballpark - AL Teams (2022)')
plt.xlabel('Ballpark')
plt.ylabel('Home Runs Allowed per Game')
plt.xticks(rotation=45)
plt.legend(title='Division')
plt.show()

# Visualize Home Winning Percentage by Ballpark for NL teams
plt.figure(figsize=(18, 6))
sns.barplot(data=merged_df[merged_df['lgID'] == 'NL'], x='park', y='HomeWinPct', hue='divID', ci=None)
plt.title('Home Winning Percentage by Ballpark - NL Teams (2022)')
plt.xlabel('Ballpark')
plt.ylabel('Home Winning Percentage')
plt.xticks(rotation=45)
plt.legend(title='Division')
plt.show()

# Visualize Home Runs Scored per Game by Ballpark for NL teams
plt.figure(figsize=(18, 6))
sns.barplot(data=merged_df[merged_df['lgID'] == 'NL'], x='park', y='HR_per_game', hue='divID', ci=None)
plt.title('Home Runs Scored per Game by Ballpark - NL Teams (2022)')
plt.xlabel('Ballpark')
plt.ylabel('Home Runs Scored per Game')
plt.xticks(rotation=45)
plt.legend(title='Division')
plt.show()

# Visualize Home Runs Allowed per Game by Ballpark for NL teams
plt.figure(figsize=(18, 6))
sns.barplot(data=merged_df[merged_df['lgID'] == 'NL'], x='park', y='HRA_per_game', hue='divID', ci=None)
plt.title('Home Runs Allowed per Game by Ballpark - NL Teams (2022)')
plt.xlabel('Ballpark')
plt.ylabel('Home Runs Allowed per Game')
plt.xticks(rotation=45)
plt.legend(title='Division')
plt.show()
