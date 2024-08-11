import pandas as pd

# Read the CSV files
file1 = pd.read_csv('file1.csv')
file2 = pd.read_csv('file2.csv')

# Sort file2 by Time
file2 = file2.sort_values(by='Time')

# Calculate the required sum of scores from file1
required_sum = file1['Score'].dropna().sum()

# Initialize variables
current_sum = 0
output_rows = []
file1_index = 0

# Iterate over each row in file2
for _, row in file2.iterrows():
    # If we've exhausted file1, stop processing
    if file1_index >= len(file1):
        break

    file1_row = file1.iloc[file1_index]

    # Skip file1 rows with NaN Score
    if pd.isna(file1_row['Score']):
        file1_index += 1
        continue

    # Match Time and Score between file2 and file1
    if row['Time'] == file1_row['Time'] and row['Score'] == file1_row['Score']:
        if current_sum + row['Score'] <= required_sum:
            output_rows.append(row)
            current_sum += row['Score']
            file1_index += 1

    # Stop if the required sum is reached
    if current_sum == required_sum:
        break

# Ensure no additional rows from file2 are added that would exceed the sum
if current_sum < required_sum:
    for _, row in file2.iterrows():
        # Skip rows that exceed the sum or are duplicates by Time
        if current_sum + row['Score'] > required_sum or row['Time'] in [r['Time'] for r in output_rows]:
            continue

        output_rows.append(row)
        current_sum += row['Score']

        # Stop if the required sum is reached
        if current_sum == required_sum:
            break

# Create a DataFrame for the output
output_df = pd.DataFrame(output_rows).sort_values(by='Time')

# Save the result to a new CSV file
output_df.to_csv('results.csv', index=False)

print(f"Results saved to 'results.csv' with a total score of {current_sum}")

# Verify the results and tell the difference(s) if any
if current_sum > required_sum:
    print(f"{current_sum-required_sum} higher than the Required Sum ({required_sum})")
elif current_sum < required_sum:
    print(f"{required_sum-current_sum} lesser than the Required Sum ({required_sum})")
else: print("Perfect matched!")
