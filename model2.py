import pandas as pd

# Read the CSV files
file1 = pd.read_csv('file1.csv')
file2 = pd.read_csv('file2.csv')

# Calculate the required sum of scores from file1
required_sum = file1['Score'].sum()

# Initialize variables
current_sum = 0
output_rows = []

# Loop through file2 to select rows until the required sum is reached
for _, row in file2.iterrows():
    if current_sum + row['Score'] <= required_sum:
        output_rows.append(row)
        current_sum += row['Score']
    if current_sum == required_sum:
        break

# Create the output DataFrame
output_df = pd.DataFrame(output_rows)

# Save the result to a new CSV file
output_df.to_csv('results.csv', index=False)

print(f"Results saved to 'results.csv' with a total score of {current_sum}")

# Give feedback if anything differ(s)
if current_sum > required_sum:
    print(f"{current_sum-required_sum} higher than the Required Sum ({required_sum})")
elif current_sum < required_sum:
    print(f"{required_sum-current_sum} lesser than Required Sum ({required_sum})")
