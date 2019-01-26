# DayOne-stats

Show statistics of your [Day One](http://dayoneapp.com/) journal.

The statistics include...
- the number of entries in a day (temporaly disabled)
- the total number of characters in a day

Please note that this project is still under development.

## Usage

```
python3 main.py
```

You can use [termgraph](https://github.com/mkaz/termgraph) to visualize the statistics.

```
python3 main.py | head -30 | termgraph --format "{:.0f}"
```
