import os
from data_shape import split_data
from dates_from_files_names import all_files_list

# Define the input directory
input_directory = r"D:\stock_data_csv"

# Get the list of file names in the directory
file_names = os.listdir(input_directory)

# Define the output directory
output_directory = r'D:\Processed_data_stock'

# Process each file
for file_name in file_names:
    # Create the full file path
    file_path = os.path.join(input_directory, file_name)
    # Call split_data with the current file path and output directory
    split_data(file_path, output_directory)
