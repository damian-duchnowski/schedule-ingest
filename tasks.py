from datetime import datetime
from auth import client
from parse import parse_working_hours

entries = parse_working_hours()
for i, entry in enumerate(entries):
    # Extracting elements from entry
    date, shift, start, end = entry.split('\t')

    # Processing variables for readability
    year = int(date.split('-')[0])
    month = int(date.split('-')[1])
    day = int(date.split('-')[2])

    start_hour = int(start.split(':')[0])
    start_minute = int(start.split(':')[1])

    end_hour = int(end.split(':')[0])
    end_minute = int(end.split(':')[1])

    # Defining variables for task builder
    title = 'Praca'

    start_time = datetime(year, month, day, start_hour, start_minute)

    # Check if night shift
    if shift == 'S1':
        # Check if last day of the month
        if i == len(entries) - 1:
            # Check if December
            if month == 12:
                end_time = datetime(year + 1, 1, 1, end_hour, end_minute)
            else:
                end_time = datetime(year, month + 1, 1, end_hour, end_minute)
        else:
            end_time = datetime(year, month, day + 1, end_hour, end_minute)
    else:
        end_time = datetime(year, month, day, end_hour, end_minute)

    # Building and creating task
    builded_task = client.task.builder(
        title,
        startDate=start_time,
        dueDate=end_time,
        projectId=client.state['projects'][2]['id'])
    task = client.task.create(builded_task)

    # Printing to console for progress tracking
    print("Added task: " + date, shift, start, end)
