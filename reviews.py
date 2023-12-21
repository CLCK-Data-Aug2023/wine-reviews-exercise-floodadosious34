# add your code here
import pandas as pd
import zipfile

# Specify the path to your ZIP file
zip_file_path = './data/winemag-data-130k-v2.csv.zip'

# Specify the name of the CSV file within the ZIP archive
csv_file_name = 'winemag-data-130k-v2.csv'

# Open the ZIP file and read the CSV using pandas
with zipfile.ZipFile(zip_file_path, 'r') as z:
    with z.open(csv_file_name) as f:
        df = pd.read_csv(f)
#See what original csv looks like
df.to_csv('data/review-per-country.csv')

#Create ne df grouped by country and use agg method to take points of each country and get a count and mean
data_summary = df.groupby('country').agg({'points': ['count', 'mean']})
print(data_summary)
#rename colums for count and mean, to count and points.
data_summary.columns = ['count', 'points']
print(data_summary)
#Select the points column and use the round method to get the numbers to 1 decimal point
data_summary['points'] = data_summary['points'].round(1)
print(data_summary)
#send new df to csv in the data folder
data_summary.to_csv('data/reviews-per-country.csv', index=True)
print(data_summary)

