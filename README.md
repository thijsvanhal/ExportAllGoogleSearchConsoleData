# Export Google Search Console Data For All Verified Properties

Ever wanted to export Google Search Console data for all of your verified properties? With this Python script you can do it without manually exporting anything!
##How it works
This script uses the amazing [SearchConsole module](https://github.com/joshcarty/google-searchconsole) for Python. Once logged in with the credentials we make a call to get all verified properties in Google Search Console.

Using a for loop we make a call to the API and export data for each verified property. To export it to a CSV we need to edit the name so we remove a single slash before exporting it to the downloads folder on your computer.

Simple script but does the job!
## How can you use this script?
1. Download the script or clone this project
  Go to [Google Cloud Console](https://console.cloud.google.com/)
  Make a new project
  Enable the Google Search Console API
  Make an OAuth consent screen
  Create Credentials > OAuth client ID
  Save credentials as .json
  Rename file to client_secrets.json and put it in the same folder as the script
2. Run the script!
3. Analyze your data 🙂

P.S. I don’t know the exact limits of the API so the script waits 20 seconds before every call, you can remove or lower it but you can get banned (temporarily).
