# Using a plain source file containing nothing but the first
# and last names on each line of Attendees.txt
from pathlib import Path
import csv
import pprint
import os
import sys
source = Path(r"C:\Users\Bruce\Google Drive\____WTF2020\Attendees.txt")
label_width = 335
label_height = 230

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
    width:{label_width}px;
    height:{label_height}px;
    border-bottom:1px solid #000000;
  }}
  h1, h3 {{
    font-family: Sans-Serif;
    line-height: 100%;
    padding-left: 10px;
    padding-top: 0;
    margin: 0;
    text-align: left;
  }}
  h1 {{
    font-size: 4.5em;
    margin-bottom: 5px;
  }}
  h3 {{
  }}
  img {{
    vertical-align: top;
    height: 70px;
    width: 100%;
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
        <img src="WinterTechForumBanner.png">
        <h1>{first}</h1><h3>{last}</h3></td>
        <td>
        <img src="WinterTechForumBanner.png">
        <h1>{first}</h1><h3>{last}</h3></td>
      </tr>
    <tbody>
  </table>

  """

name_tags_table_end = """
  <tbody>
</table>
"""

input = ''.join([i if ord(i) < 128 else '' for i in source.read_text(encoding="utf8")])
lines = input.strip().splitlines()
pprint.pprint(lines)
# sys.exit()

with open("NameTags.html", 'w') as name_tags:
    name_tags.write(f"{name_tags_table_begin}")
    for n, rec in enumerate(lines):
        first, last = rec.split(' ', maxsplit=1)
        full_name = f"{first} {last}"
        name_tags.write(f"{name_tag_row(first, last)}")
        if (n+1) % 4 == 0:
            name_tags.write('<div class = "pageBreak">\n')
    name_tags.write(f"{name_tags_table_end}")

os.system("subl NameTags.html")
os.system("call start NameTags.html")
