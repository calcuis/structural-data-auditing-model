import pandas as pd

# Load the CSV files
file1 = pd.read_csv('file1.csv')
file2 = pd.read_csv('file2.csv')

# Merge the two files based on 'Time' and 'Score' columns
merged = pd.merge(file1, file2, on=['Time', 'Score'], how='left', indicator=True)

# Create 'Coexist' column based on the indicator
merged['Coexist'] = merged['_merge'].apply(lambda x: 1 if x == 'both' else '')

# Drop the merge indicator column
merged = merged.drop(columns=['_merge'])

# Save the result to a new CSV file
merged.to_csv('results.csv', index=False)

print("Results saved to 'results.csv'")
