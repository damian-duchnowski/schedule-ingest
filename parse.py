import sys
from calendar import monthrange
from datetime import datetime


def check_date(year, month, day):
    """Checks if date exists in calendar."""
    correctDate = None
    try:
        correctDate = datetime(year, month, day)
        correctDate = True
    except ValueError:
        correctDate = False
    return correctDate


def check_days(year, month):
    """Checks if number of entries matches amount of days in passed month."""
    num_lines = sum(1 for line in open(sys.argv[1], 'r'))
    num_days = monthrange(int(year), int(month))[1]

    if num_days == num_lines:
        return True
    else:
        return False


def parse_dates():
    dates = []
    if check_days(datetime.today().year, sys.argv[2]):
        with open(sys.argv[1], 'r') as f:
            for i, line in enumerate(f):
                today = datetime.today()
                date = datetime(today.year, int(sys.argv[2]), i + 1).date()
                if check_date(date.year, date.month, date.day):
                    dates.append(date.strftime('%Y-%m-%d'))
                else:
                    break
        return dates
    else:
        sys.exit("Entries don't match days in the month.")


def parse_working_hours():
    """Parse entries into text file with date and times."""
    entries = []
    with open(sys.argv[1], 'r') as f:
        for i, line in enumerate(f):
            line = line.rstrip()
            if line == 'S1':
                start_time = '22:30'
                end_time = '6:30'
                entries.append(parse_dates()[i] + '\t' + line + '\t' +
                               start_time + '\t' + end_time)
            elif line == 'S2':
                start_time = '6:30'
                end_time = '14:30'
                entries.append(parse_dates()[i] + '\t' + line + '\t' +
                               start_time + '\t' + end_time)
            elif line == 'S3':
                start_time = '14:30'
                end_time = '22:30'
                entries.append(parse_dates()[i] + '\t' + line + '\t' +
                               start_time + '\t' + end_time)
            else:
                pass
    return entries
