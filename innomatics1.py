import pandas as pd
import os

folder_path = "C:\\Users\\Windows\\Desktop\\Property_data"
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

df_list = []

for file in csv_files:
    file_path = os.path.join(folder_path, file)
    try:
        
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
       
        df = pd.read_csv(file_path, encoding='ISO-8859-1')
    df_list.append(df)

merged_df = pd.concat(df_list, ignore_index=True)
merged_df.to_csv('merged_file.csv', index=False)
print("DONE MERGING")
print(merged_df.head())


