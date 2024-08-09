import pandas as pd

# Read the CSV files
file1 = pd.read_csv('file1.csv')
file2 = pd.read_csv('file2.csv')

# Calculate the required sum of scores from file1
required_sum = file1['Score'].dropna().sum()

# Initialize variables
current_sum = 0
output_rows = []
file1_index = 0

# Loop through file2 to select rows until the required sum is reached
for _, row in file2.iterrows():
    if file1_index < len(file1):
        file1_row = file1.iloc[file1_index]
        # If the current row's score in file2 matches a non-null score in file1
        if not pd.isna(file1_row['Score']):
            if current_sum + row['Score'] <= required_sum:
                output_rows.append(row)
                current_sum += row['Score']
                file1_index += 1
            # If the exact required sum is reached, stop processing
            if current_sum == required_sum:
                break
        else:
            # Skip missing Score entries in file1 and continue
            file1_index += 1

# Create the output DataFrame
output_df = pd.DataFrame(output_rows)

# Save the result to a new CSV file
output_df.to_csv('results.csv', index=False)

print(f"Results saved to 'results.csv' with a total score of {current_sum}")

# Verify the results and tell the difference(s) if any
if current_sum > required_sum:
    print(f"{current_sum-required_sum} higher than the Required Sum ({required_sum})")
elif current_sum < required_sum:
    print(f"{required_sum-current_sum} lesser than the Required Sum ({required_sum})")
else: print("Perfect matched!")
