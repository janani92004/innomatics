#THIS CODE IS TO MERGE MY CLEANED HSR FILE WITH MY MAIN MERGED FILE
import pandas as pd


df1 = pd.read_csv("C:\\Users\\Windows\\Desktop\\hsr.csv")
df2 = pd.read_csv("C:\\Users\\Windows\\Desktop\\merged_file.csv")


merged_df = pd.merge(df1, df2, on='property_id', how='inner')  


merged_df.to_csv('NEW_merged_file.csv', index=False)


print(merged_df)
print("DONE")
