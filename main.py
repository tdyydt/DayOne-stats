import sqlite3
from pathlib import Path

# Location of the file: DayOne.sqlite
DB_PATH = Path('~/Library/Group Containers/5U8NS4GX82.dayoneapp2/Data/Documents/DayOne.sqlite').expanduser()
print(DB_PATH)
# SELECT ZGREGORIANYEAR, ZGREGORIANMONTH, ZGREGORIANDAY, ZMARKDOWNTEXT FROM ZENTRY ORDER BY ZCREATIONDATE DESC LIMIT 1;

# class Entry:
#     year = None
#     month = None
#     day = None
#     # date = None
#     markdown_text = None

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

count = 100
itr = c.execute('SELECT ZGREGORIANYEAR, ZGREGORIANMONTH, ZGREGORIANDAY, ZMARKDOWNTEXT FROM ZENTRY ORDER BY ZCREATIONDATE DESC LIMIT ?', (count,))
for row in itr:
    year,month,day,text = row
    print(bool(text), text[:10])
    # print(year,month,day,len(text))

conn.close()


# def main():
#     pass

# if __name__ == '__main__':
#     main()
