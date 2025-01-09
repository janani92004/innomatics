
import pandas as pd

# Load the two CSV files
df1 = pd.read_csv("C:\\Users\\Windows\\Desktop\\hsr.csv")  # Replace with your actual file paths
df2 = pd.read_csv("C:\\Users\\Windows\\Desktop\\merged_file.csv")

# Merge the two DataFrames on a common column (e.g., 'property_id')
merged_df = pd.merge(df1, df2, on='property_id', how='inner')  # 'inner' can be changed to 'left', 'right', or 'outer'

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('NEW_merged_file.csv', index=False)

# Print the merged DataFrame
print(merged_df)
print("DONE")
