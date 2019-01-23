from datetime import date
import sqlite3
from pathlib import Path

class Entry:
    def __init__(self, pk, the_date, text):
        self.pk = pk  # primary key
        self.date = the_date
        self.text = text
        # TODO: Add creation_datetime ??

# Location of the file: DayOne.sqlite
DB_PATH = Path('~/Library/Group Containers/5U8NS4GX82.dayoneapp2/Data/Documents/DayOne.sqlite').expanduser()

# ---
# key: date
# value: entry_count, char_count
# daily_summary = dict()

daily_entry_count = dict()
daily_char_count = dict()

# -- SQLite
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

count = 100
itr = c.execute('SELECT Z_PK, ZGREGORIANYEAR, ZGREGORIANMONTH, ZGREGORIANDAY, ZMARKDOWNTEXT FROM ZENTRY ORDER BY ZCREATIONDATE DESC LIMIT ?', (count,))
for row in itr:
    pk,year,month,day,text = row
    entry = Entry(pk, date(year,month,day), text)
    # print(entry.pk, entry.date.isoformat(), entry.text[:5])

    # daily_summary[entry.date]
    d = entry.date
    daily_entry_count[d] = daily_entry_count.get(d, 0) + 1
    daily_char_count[d] = daily_char_count.get(d, 0) + len(entry.text)

conn.close()
# -- End of SQLite

# Show statistics
# TODO: sort keys from the latest
for d in daily_entry_count.keys():
    print(d.isoformat(), daily_entry_count[d], daily_char_count[d])
