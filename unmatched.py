import os
import pandas as pd

def find_unmatched():
    result = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                try:
                    df = pd.read_csv(file_path, usecols=[0, 1, 4, 5, 6])
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")
                    continue
                df.columns = ['Session', 'Timestamp', 'Sender', 'Receiver', 'Receiver_ID']
                df.dropna(inplace=True)
                df['Source'] = file
                df = df[['Source', 'Session', 'Timestamp', 'Sender', 'Receiver', 'Receiver_ID']]
                result.append(df)
    if result:
        combined_df = pd.concat(result)
        duplicates = combined_df.duplicated(subset=['Session', 'Timestamp', 'Sender', 'Receiver', 'Receiver_ID'], keep=False)
        unique_df = combined_df[~duplicates]
        unique_df.to_csv('output.csv', index=False)
    else:
        print("No csv files found or no data to process.")

find_unmatched()
