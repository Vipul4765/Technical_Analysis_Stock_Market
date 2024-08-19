import os
import pandas as pd
from data_shape import split_data
from dates_from_files_names import all_files_list

# Define the input and output directories
input_directory = r"D:\Processed_data_stock"
output_directory = r"D:\Sorted_data_stock_data"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Get the list of file names in the input directory
file_names = os.listdir(input_directory)

# Process each file
for file_name in file_names:
    # Create the full file path for input and output
    input_file_path = os.path.join(input_directory, file_name)
    output_file_path = os.path.join(output_directory, file_name)

    # Read the CSV file into a DataFrame
    df = pd.read_csv(input_file_path)

    # Convert 'Date' column to datetime format
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    # Sort the DataFrame by 'Date'
    df.sort_values(by='Date', inplace=True)

    # Drop duplicate rows based on all columns or specify subset
    df.drop_duplicates(inplace=True)

    # Optionally convert 'Date' column back to string format if needed
    # df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')

    # Write the processed DataFrame to the output directory
    df.to_csv(output_file_path, index=False)

    print(f"Processed and s0aved: {output_file_path}")
