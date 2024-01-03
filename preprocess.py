import pandas as pd
import os
import math

def interpolate(df, start_value, end_value, curr_index, total_index):
    weight = curr_index / total_index
    interpolated_value = start_value + (end_value - start_value) * weight
    return round(interpolated_value, 2)

def interpolate_data(input_csv):
    # Read the input CSV
    df = pd.read_csv(input_csv, index_col="Country Name")

    # Extract the years for interpolation
    years = list(range(1990, 2021))

    # Create a new DataFrame with all years
    result = {"Country Name": list(df.index)}
    for year in years:
        result[str(year)] = []

    for country in result["Country Name"]:
        for index, year in enumerate(years):
            if year == 2020:
                result["2020"].append(df.loc[country, str(year)])
                break
            total_index = 10
            curr_index = index % total_index
            start_year = year - curr_index
            end_year = year + total_index - curr_index
            start_value = df.loc[country, str(start_year)]
            end_value = df.loc[country, str(end_year)]

            # Call the custom interpolation function
            value = interpolate(df, start_value, end_value, curr_index, total_index)
            result[str(year)].append(value)

    return result

# input_csv_path = "./hdi.csv"
# interpolated_data = interpolate_data(input_csv_path)
# interpolated_df = pd.DataFrame(interpolated_data)

# # Save the interpolated data to a new CSV file in the preprocess folder
# output_folder = "./preprocess"
# os.makedirs(output_folder, exist_ok=True)
# output_csv_path = os.path.join(output_folder, "hdi.csv")
# interpolated_df.to_csv(output_csv_path, index=False)
# print(f"Interpolated HDI data saved to {output_csv_path}")

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
def calculate_average_difference(values):
    # Calculate differences between consecutive elements
    differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]

    # Calculate the average difference
    average_difference = sum(differences) / len(differences)

    return average_difference

def interpolate_industrial_data(input_csv):
    # Read the input CSV
    df = pd.read_csv(input_csv, index_col="Country Name")

    # Extract the years for interpolation
    years = list(range(1990, 2020))

    # Create a new DataFrame with all years
    result = {"Country Name": list(df.index)}
    for year in years:
        result[str(year)] = []

    for country in result["Country Name"]:
        for index, year in enumerate(years):
            # Check if the value is missing
            if pd.isna(df.loc[country, str(year)]):
                # Get all the values of Country in Array to get average growth per year
                country_index = result["Country Name"].index(country)
                country_values_array = [
                    result[key][country_index]
                    for key in result
                    if key != "Country Name" and int(key) < year
                ]
                prev_value = result[str(year - 1)][country_index]
                avg_diff = calculate_average_difference(country_values_array)

                # print(avg_diff, prev_value, country, year)
                interpolated_value = prev_value + avg_diff
                value = round(interpolated_value, 2)
            else:
                value = round(df.loc[country, str(year)], 2)

            result[str(year)].append(value)

    return result

# # Example usage:
# input_csv_path = "./industrial_production.csv"
# interpolated_industrial_data = interpolate_industrial_data(input_csv_path)
# interpolated_industrial_pd = pd.DataFrame(interpolated_industrial_data)

# # Append the data to a CSV file in the preprocess folder with the same name
# output_csv_path = f"./preprocess/{input_csv_path.split('/')[-1]}"
# interpolated_industrial_pd.to_csv(output_csv_path, mode='w', index=False)

# ------------------------------------------------------------------------------------

def format_range_csv(input_csv_path):
    df = pd.read_csv(input_csv_path)

    # Filter columns for the years 1990 to 2020
    selected_years = [str(year) for year in range(1990, 2021)]
    df_selected_years = df[["Country Name"] + selected_years]

    # Define the output CSV path in the preprocess folder with the same name
    output_csv_path = f"./preprocess/{input_csv_path.split('/')[-1]}"

    df_selected_years.to_csv(output_csv_path, mode="w", index=False)

    return df_selected_years


input_csv_path = "./gdp.csv"
interpolated_industrial_data = format_range_csv(input_csv_path)
print(pd.DataFrame(interpolated_industrial_data))

input_csv_path = "./population.csv"
interpolated_industrial_data = format_range_csv(input_csv_path)
print(pd.DataFrame(interpolated_industrial_data))

input_csv_path = "./urbanization.csv"
interpolated_industrial_data = format_range_csv(input_csv_path)
print(pd.DataFrame(interpolated_industrial_data))