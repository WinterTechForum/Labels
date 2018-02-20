from pathlib import Path
import csv
import pprint
import os

raw = [line for line in
        next(Path().glob("*.csv")).read_text().splitlines()
        if "Unique Ticket URL" not in line]
records = { f"{row[6]}|{row[5]}" for row in csv.reader(raw) }
with open("Attendees.txt", 'w') as attendees:
    for n, rec in enumerate(sorted(records)):
        last, first = rec.split('|')
        attendees.write(f"{n + 1} {first} {last}\n")

name_tags_table_begin = """
<style>
  .nameTags {
    border-collapse:collapse;
    padding:5px;
  }
  .nameTags td {
    padding:5px;
  }
  .oneTag {
    border-spacing:10px;
  }
  .oneTag td {
    width:250px;
    height:150px;
    background-image: url(WinterTechForumBanner.png);
    background-size: 100% 35%;
    background-repeat: no-repeat;
    background-position: 0px 0px;
    border:1px solid #000000;
  }
  h1, h3 {
    font-family: Sans-Serif;
    text-align: center;
    padding: 0;
    margin: 0;
  }
  h1 {
    padding-top: 40px;
    font-size: 3em;
  }
</style>
<table class="nameTags">
  <tbody>
"""

def name_tag_row(first, last):
  return f"""
  <table class="oneTag">
    <tbody>
      <tr>
        <td><h1>{first}</h1><h3>{last}</h3></td>
        <td><h1>{first}</h1><h3>{last}</h3></td>
      </tr>
    <tbody>
  </table>

  """

name_tags_table_end = """
  <tbody>
</table>
"""

with open("NameTags.html", 'w') as name_tags:
    name_tags.write(f"{name_tags_table_begin}")
    for n, rec in enumerate(sorted(records)):
        last, first = rec.split('|')
        name_tags.write(f"{name_tag_row(first, last)}")
    name_tags.write(f"{name_tags_table_end}")

os.system("subl NameTags.html")
# os.system("subl Attendees.txt")
os.system("subl NameTags.py")
os.system("call start NameTags.html")
