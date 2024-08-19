import pandas as pd
import os


def process_stock_data(file_path):
    """
    This function processes stock data from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file containing stock data.

    Returns:
    pd.DataFrame: A DataFrame containing the filtered and formatted stock data.
    """
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Strip any leading or trailing spaces from column names
    df.columns = df.columns.str.strip()

    # Strip leading and trailing spaces from all string columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    # Filter the DataFrame to include only rows where 'SERIES' is 'EQ'
    df = df[df['SERIES'] == 'EQ']

    # Drop unnecessary columns
    df.drop(columns=['PREV_CLOSE', 'LAST_PRICE', 'AVG_PRICE', 'TTL_TRD_QNTY', 'TURNOVER_LACS', 'NO_OF_TRADES',
                     'DELIV_QTY', 'DELIV_PER'], inplace=True)

    # Rename columns for clarity
    df.rename(columns={
        'SYMBOL': 'Symbol',
        'SERIES': 'Series',
        'DATE1': 'Date',
        'OPEN_PRICE': 'Open',
        'HIGH_PRICE': 'High',
        'LOW_PRICE': 'Low',
        'CLOSE_PRICE': 'Close'
    }, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%Y')

    # Format the dates to 'DD-MM-YYYY'
    df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')

    return df


def split_data(file_path, output_dir):
    df = process_stock_data(file_path)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Group by 'Symbol'
    symbol_wise_group = df.groupby('Symbol')

    for symbol, group in symbol_wise_group:
        # Define the file path for the symbol
        file_name = f"{symbol}.csv"
        file_path = os.path.join(output_dir, file_name)

        # Check if file exists
        if os.path.exists(file_path):
            # Append data to existing file
            group.to_csv(file_path, mode='a', header=False, index=False)
        else:
            # Create new file and write data
            group.to_csv(file_path, mode='w', header=True, index=False)

    print("Data has been split and saved to individual files.")



