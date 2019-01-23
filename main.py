from datetime import date
import sqlite3
from pathlib import Path

# -- Constants
# Location of the file: DayOne.sqlite
DB_PATH = Path('~/Library/Group Containers/5U8NS4GX82.dayoneapp2/Data/Documents/DayOne.sqlite').expanduser()
# How many entries (from the latest) do you process?
# 処理対象とするエントリの数
COUNT = 200

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
# ignore the oldest day (because it may be wrong)
dates = sorted(list(daily_entry_count.keys()), reverse=True)[:-1]
for d in dates:
    print(d.isoformat(), daily_entry_count[d], daily_char_count[d])
