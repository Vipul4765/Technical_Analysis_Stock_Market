from dates_from_files_names import result_data
from next_date import generate_date_range
from all_sunday_dates import get_all_sundays

# Initialize an empty list to store holidays
holiday = []
all_sundays = get_all_sundays()

# Get the market open dates from the function
market_open_dates = result_data()

# Open the holiday file and read each line
with open('D:\\holiday.txt', 'r') as f:
    for line in f:
        if line.strip():
            holiday.append(line.strip())

# Define the start and end dates
start_date = '01012024'
end_date = '13082024'



# Generate all dates between start_date and end_date
all_dates = generate_date_range(start_date, end_date)

# Remove holiday dates from all_dates
for hol in holiday:
    if hol in all_dates:
        all_dates.remove(hol)

# Remove Sundays from all_dates
for sunday in all_sundays:
    if sunday in all_dates:
        all_dates.remove(sunday)

# Find dates in all_dates that are not in market_open_dates
missing_dates = [date for date in all_dates if date not in market_open_dates]

# Check if all dates are accounted for
if not missing_dates:
    print('All successful')
else:
    print('Missing dates:', missing_dates)
