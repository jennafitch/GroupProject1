
import pandas as pd
import statsmodels.api as sm

# Load data from Teams with only 2022 data.xlsx
teams_file = r'C:\Users\jenfi\OneDrive - University of Wisconsin-Whitewater\Teams with just 2022 data.xlsx'
teams_df = pd.read_excel(teams_file)

# Filter data for the year 2022
teams_2022 = teams_df[teams_df['yearID'] == 2022]

# Load data from Baseball (1).xlsx
baseball_file = r'C:\Users\jenfi\Downloads\BaseballGroup.xlsx'
baseball_df = pd.read_excel(baseball_file)

# Merge data from both spreadsheets
merged_df = pd.merge(teams_2022, baseball_df, how='inner', left_on='teamID', right_on='Tm')

# Prepare data for multiple regression
X = merged_df[['BPF', 'PPF']]
Y = merged_df.iloc[:, 5]  # Assuming runs scored (R) is in the 6th column (index 5)

# Add constant to independent variables
X = sm.add_constant(X)

# Fit multiple regression model
model = sm.OLS(Y, X).fit()

# Print model summary
print(model.summary())
