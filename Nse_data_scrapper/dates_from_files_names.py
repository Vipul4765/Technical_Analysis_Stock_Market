import os
def result_data():
    # Define the directory path
    directory = "D:\\stock_data_csv"
    # List all files and directories in the specified path
    files = os.listdir(directory)
    # Print the list of files
    all_data = []
    for file in files:
        if file.endswith(".csv"):
            date_data = file[-12:-4]
            all_data.append(date_data)
    return all_data


def all_files_list():
    # Define the directory path
    directory = "D:\\stock_data_csv"
    # List all files and directories in the specified path
    files = os.listdir(directory)
    # Print the list of files
    all_data = []
    for file in files:
        if file.endswith(".csv"):
            all_data.append(file)
    return all_data


