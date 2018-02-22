from pathlib import Path
import csv
import pprint
import os
label_width = 335
label_height = 230

raw = [line for line in
        next(Path().glob("tito-*.csv")).read_text().splitlines()
        if "Unique Ticket URL" not in line]
records = { f"{row[6]}|{row[5]}" for row in csv.reader(raw) }
with open("Attendees.txt", 'w') as attendees:
    for n, rec in enumerate(sorted(records)):
        last, first = rec.split('|')
        attendees.write(f"{n + 1} {first} {last}\n")

raw_interests = [
  line for line in Path("Interests.csv").read_text().splitlines()
]
interests = { row[0]: row[1] for row in csv.reader(raw_interests) }
# pprint.pprint(interests)


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

def name_tag_row(first, last, interests):
  return f"""
  <table class="oneTag">
    <tbody>
      <tr>
        <td>
        <img src="WinterTechForumBanner.png">
        <h1>{first}</h1><h3>{last}. {interests}</h3></td>
        <td>
        <img src="WinterTechForumBanner.png">
        <h1>{first}</h1><h3>{last}. {interests}</h3></td>
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
        full_name = f"{first} {last}"
        # attendee_interests = ""
        # if full_name not in interests:
        #     print(f"{full_name} not in interests")
        # if interests[full_name]:
        #     print(f"{full_name}: {interests[full_name]}")
            # attendee_interests = interests[full_name]
        name_tags.write(f"{name_tag_row(first, last, interests[f'{first} {last}'])}")
        if (n+1) % 4 == 0:
            name_tags.write('<div class = "pageBreak">\n')
    name_tags.write(f"{name_tags_table_end}")

os.system("subl NameTags.html")
# os.system("subl Attendees.txt")
os.system("subl NameTags.py")
os.system("call start NameTags.html")
