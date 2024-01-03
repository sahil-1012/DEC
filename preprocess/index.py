import pandas as pd
from sklearn.model_selection import train_test_split

# Load GDP data
gdp_data = pd.read_csv("./preprocess/gdp.csv")
gdp_data.set_index("Country Name", inplace=True)

# Load HDI data
hdi_data = pd.read_csv("./preprocess/hdi.csv")
hdi_data.set_index("Country Name", inplace=True)

# Load population data
population_data = pd.read_csv("./preprocess/population.csv")
population_data.set_index("Country Name", inplace=True)

# Load industrial production data
industrial_data = pd.read_csv("./preprocess/industrial_production.csv")
industrial_data.set_index("Country Name", inplace=True)

# Load urbanization data
urbanization_data = pd.read_csv("./preprocess/urbanization.csv")
urbanization_data.set_index("Country Name", inplace=True)


# Merge dataframes with custom suffixes
merged_data = pd.merge(
    gdp_data, hdi_data, left_index=True, right_index=True, suffixes=("_gdp", "_hdi")
)
merged_data = pd.merge(
    merged_data,
    population_data,
    left_index=True,
    right_index=True,
    suffixes=("_merged", "_population"),
)
merged_data = pd.merge(
    merged_data,
    industrial_data,
    left_index=True,
    right_index=True,
    suffixes=("_merged", "_industrial"),
)
merged_data = pd.merge(
    merged_data,
    urbanization_data,
    left_index=True,
    right_index=True,
    suffixes=("_merged", "_urbanization"),
)

# Reset the index
merged_data.reset_index(inplace=True)

# Display the columns in the merged data
print("Columns in merged data:", merged_data.columns)

# Save the clean, processed data to a CSV file
merged_data.to_csv("./preprocess/clean_data.csv", index=False)
