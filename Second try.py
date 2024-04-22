
import pandas as pd
import matplotlib.pyplot as plt

# Load the first spreadsheet (Teams with only 2022 data.xlsx)
teams_file = r'C:\Users\jenfi\OneDrive - University of Wisconsin-Whitewater\Teams with just 2022 data.xlsx'
teams_df = pd.read_excel(teams_file)

# Filter data for the year 2022
teams_2022 = teams_df[teams_df['yearID'] == 2022]

# Load the second spreadsheet (BaseballGroup.xlsx)
baseball_file = r'C:\Users\jenfi\Downloads\BaseballFilter.xlsx'
baseball_df = pd.read_excel(baseball_file)

# Merge data from both spreadsheets on the teamID/Tm column
merged_df = pd.merge(teams_2022, baseball_df, how='inner', left_on='teamID', right_on='Tm')

# Calculate correlation coefficients between BPF/PPF and performance metrics (R and RA)
correlation_bpf_r = merged_df['BPF'].corr(merged_df['R'])
correlation_ppf_r = merged_df['PPF'].corr(merged_df['R'])
correlation_bpf_ra = merged_df['BPF'].corr(merged_df['RA'])
correlation_ppf_ra = merged_df['PPF'].corr(merged_df['RA'])

print("Correlation coefficient between BPF and R:", correlation_bpf_r)
print("Correlation coefficient between PPF and R:", correlation_ppf_r)
print("Correlation coefficient between BPF and RA:", correlation_bpf_ra)
print("Correlation coefficient between PPF and RA:", correlation_ppf_ra)

# Create scatter plots to visualize the relationship between BPF/PPF and R/RA
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(merged_df['BPF'], merged_df['R'])
plt.title('BPF vs R')
plt.xlabel('BPF')
plt.ylabel('Runs Scored (R)')

plt.subplot(1, 2, 2)
plt.scatter(merged_df['PPF'], merged_df['R'])
plt.title('PPF vs R')
plt.xlabel('PPF')
plt.ylabel('Runs Scored (R)')

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(merged_df['BPF'], merged_df['RA'])
plt.title('BPF vs RA')
plt.xlabel('BPF')
plt.ylabel('Runs Allowed (RA)')

plt.subplot(1, 2, 2)
plt.scatter(merged_df['PPF'], merged_df['RA'])
plt.title('PPF vs RA')
plt.xlabel('PPF')
plt.ylabel('Runs Allowed (RA)')

plt.tight_layout()
plt.show()
