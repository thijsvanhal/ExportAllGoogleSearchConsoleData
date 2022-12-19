## Import modules
import searchconsole
import pandas as pd
import os.path
from pathlib import Path
import time

## Make connection with the API using client_secrets.json. The script checks if credentials.json excists so you don't need to log in every time.
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./")
file_exists = os.path.exists('credentials.json')
if file_exists is False:
    account = searchconsole.authenticate(client_config='client_secrets.json', serialize='credentials.json')
else:
    account = searchconsole.authenticate(client_config='client_secrets.json', credentials='credentials.json')

## Use a for loop 
for acc in account:
    ## Check for the right permission, you cannot access unverified properties
    if acc.permission != 'siteUnverifiedUser':
        ## Wait 20 second before exporting, this way we prevent a temporary ban
        time.sleep(20)
        webproperty = acc
        ## Use the API to get the data. Change the date and add filters if you like (check SearchConsole module documentation)
        report = webproperty.query.range('2022-01-01', '2022-12-17').dimension('query','page').get().to_dataframe()
        ## Give each column a proper name
        report.columns=['keyword','page','clicks','impressions','ctr','position']
        ## Set the export path to the downloads folder
        export_path = r'~/Downloads/'
        ## Use the site name as file name
        file_name = str(acc.url) + '.csv'
        ## Find and replace a single slash to prevent an exporting error
        new_file_name = file_name.replace('/', '')
        ## Setup the full export path
        full_export_path = export_path + new_file_name
        ## Export to CSV with a | as seperator to the downloads folder on your computer
        report.to_csv(
            full_export_path,
            index=False,
            sep = '|')
        ## Print that the export is done
        print("The export of " + str(acc.url) + " is done!")
## Print that everything is exported, the script is done!
print("Everything is exported!")