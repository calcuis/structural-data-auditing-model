import pandas as pd

def model5(vendor,dataset,output):
    file1 = pd.read_csv(f'{vendor}.csv')
    file2 = pd.read_csv(f'{dataset}.csv')

    required_sum = file1['Score'].dropna().sum()
    current_sum = 0
    output_rows = []
    file1_index = 0

    for _, row in file2.iterrows():
        if file1_index < len(file1):
            file1_row = file1.iloc[file1_index]

            if not pd.isna(file1_row['Score']):
                if current_sum + row['Score'] <= required_sum:
                    output_rows.append(row)
                    current_sum += row['Score']
                    file1_index += 1

                if current_sum == required_sum:
                    break
            else:
                file1_index += 1

    output_df = pd.DataFrame(output_rows)
    output_df.to_csv(f'{output}.csv', index=False)

    print(f"Results saved to '{output}.csv' with a total score of {current_sum}")

    if current_sum > required_sum:
        print(f"{current_sum-required_sum} higher than the Required Sum ({required_sum})")
    elif current_sum < required_sum:
        print(f"{required_sum-current_sum} lesser than the Required Sum ({required_sum})")
    else: print("Perfect matched!")

for x in range(1, 32):
  model5(f"./1/{x}",f"./2/{x}",f"./3/{x}")
