from pathlib import Path
import csv
import pprint

raw = [line for line in
        next(Path().glob("*.csv")).read_text().splitlines()
        if "Unique Ticket URL" not in line]
records = { f"{row[6]}|{row[5]}" for row in csv.reader(raw) }
for n, rec in enumerate(sorted(records)):
    last, first = rec.split('|')
    print(n + 1, first, last)
