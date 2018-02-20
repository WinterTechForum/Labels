from pathlib import Path
import csv
import pprint
import os
label_width = "335px"
label_height = "230px"

raw = [line for line in
        next(Path().glob("*.csv")).read_text().splitlines()
        if "Unique Ticket URL" not in line]
records = { f"{row[6]}|{row[5]}" for row in csv.reader(raw) }
with open("Attendees.txt", 'w') as attendees:
    for n, rec in enumerate(sorted(records)):
        last, first = rec.split('|')
        attendees.write(f"{n + 1} {first} {last}\n")

name_tags_table_begin = f"""
<style>
  .nameTags {{
    border-collapse:collapse;
    padding:5px;
  }}
  .nameTags td {{
    padding:5px;
  }}
  .oneTag {{
    border-spacing:0;
    margin-bottom:5px;
  }}
  .oneTag td {{
    width:{label_width};
    height:{label_height};
    border-bottom:1px solid #000000;
  }}
  h1, h3 {{
    font-family: Sans-Serif;
    text-align: center;
    padding: 0;
    margin: 0;
  }}
  h1 {{
    padding-top: 0;
    font-size: 4.5em;
  }}
  .pageBreak {{
      page-break-before: always;
  }}
</style>
<table class="nameTags">
  <tbody>
"""

def name_tag_row(first, last):
  return f"""
  <table class="oneTag">
    <tbody>
      <tr>
        <td>
        <img src="WinterTechForumBanner.png" align="top" width="{label_width}">
        <h1>{first}</h1><h3>{last}</h3></td>
        <td>
        <img src="WinterTechForumBanner.png" align="top" width="{label_width}">
        <h1>{first}</h1><h3>{last}</h3></td>
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
        if (n+1) % 4 == 0:
            name_tags.write('<div class = "pageBreak">\n')
    name_tags.write(f"{name_tags_table_end}")

os.system("subl NameTags.html")
# os.system("subl Attendees.txt")
os.system("subl NameTags.py")
os.system("call start NameTags.html")
