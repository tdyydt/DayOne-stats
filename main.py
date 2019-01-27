import argparse
from datetime import date
import sqlite3
from pathlib import Path

# -- Constants
# Location of the file: DayOne.sqlite
DB_PATH = Path('~/Library/Group Containers/5U8NS4GX82.dayoneapp2/Data/Documents/DayOne.sqlite').expanduser()
# The number of entries (from the latest one) to be processed.
COUNT = 200

# -- command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument(
    '--daily-char',
    action='store_true',
    help='show the total number of characters in a day',
    )
parser.add_argument(
    '--daily-entry',
    action='store_true',
    help='show the number of entries in a day',
    )
args = parser.parse_args()

# If no options were specified, ...
if not args.daily_entry and not args.daily_char:
    args.daily_char = True

# ---
class Entry:
    def __init__(self, pk, the_date, text):
        self.pk = pk  # primary key
        self.date = the_date
        self.text = text
        # TODO: Add creation_datetime ??

# -- Dictionaries for summary
daily_entry_count = dict()
daily_char_count = dict()

# -- SQLite
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

count = COUNT
itr = c.execute('SELECT Z_PK, ZGREGORIANYEAR, ZGREGORIANMONTH, ZGREGORIANDAY, ZMARKDOWNTEXT FROM ZENTRY ORDER BY ZCREATIONDATE DESC LIMIT ?', (count,))
for row in itr:
    pk,year,month,day,text = row
    entry = Entry(pk, date(year,month,day), text)
    # print(entry.pk, entry.date.isoformat(), entry.text[:5])

    d = entry.date
    daily_entry_count[d] = daily_entry_count.get(d, 0) + 1
    daily_char_count[d] = daily_char_count.get(d, 0) + len(entry.text)

conn.close()
# -- End of SQLite

# ---
# Show statistics

# Sort dates from the latest;
# Ignore the oldest day (because it may be wrong)
dates = sorted(list(daily_entry_count.keys()), reverse=True)[:-1]
for d in dates:
    print(
        d.isoformat(),
        daily_entry_count[d] if args.daily_entry else '',
        daily_char_count[d] if args.daily_char else '',
        )
