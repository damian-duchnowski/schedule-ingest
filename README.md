# schedule-ingest
Short script for automating the ingestion of my work schedule into my to-do application TickTick.

Input is the month number and a file containing shift codes, which is then parsed into dates and using an unofficial API sent to the application's servers.


On top of that, the script checks passed in data:
- if all needed entries for the month are included i.e. shift or rest for all days in a given month
- if all calculated dates actually exist
