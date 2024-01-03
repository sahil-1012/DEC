import pandas as pd

# Read the CSV file
df = pd.read_csv("./Book1.csv")

# Divide all values by 1000
df.iloc[:, 1:] /= 1000000000

# Save the modified DataFrame back to the original CSV file
df.to_csv("your_file.csv", index=False)
