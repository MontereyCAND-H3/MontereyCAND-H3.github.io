import argparse
import datetime
import os
import re
import textwrap
from typing import Tuple
import yaml

from dateutil.relativedelta import relativedelta, SA

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

def get_flags():
  parser = argparse.ArgumentParser()
  
  parser.add_argument("--num_to_add", type=int, default=6)
  parser.add_argument("--upcumming_dir", default="_upcumming-trails")
  
  flags = parser.parse_args()
  return flags


def parse_jekyll_front_matter(jekyll_input):
  # Split the Jekyll input into front matter and content
  if jekyll_input.startswith('---'):
    front_matter_end = jekyll_input.find('---', 3)
    if front_matter_end != -1:
      front_matter = jekyll_input[3:front_matter_end].strip()
      content = jekyll_input[front_matter_end + 3:].strip()
      # Parse the front matter as YAML
      front_matter_dict = yaml.safe_load(front_matter)
      return front_matter_dict, content
  return {}, jekyll_input

def second_saturday(year, month):
  # Find the first day of the month
  first_day = datetime.date(year, month, 1)
  # Find the first Saturday of the month
  first_saturday = first_day + relativedelta(weekday=SA(+1))
  # The second Saturday is one week after the first Saturday
  second_saturday = first_saturday + relativedelta(weeks=1)
  return second_saturday

def get_next_n_months(basis_date: datetime.datetime, number_to_generate: int):
  event_dates = []
  for i in range(number_to_generate):
    # Calculate the year and month
    year = basis_date.year + (basis_date.month + i - 1) // 12
    month = (basis_date.month + i - 1) % 12 + 1
    # Get the second Saturday of the month
    event_dates.append(second_saturday(year, month))
  return event_dates
    

def get_basis_event(working_dir) -> Tuple[int, str]:
  directory_contents = list(filter(
    lambda f: re.match("\d+\.md", f),
    os.listdir(working_dir)
  ))
  # This line assumes we are using file names that are run numbers, which works for my repo at least
  latest = max(directory_contents, key=(lambda f: int(f.split('.')[0])))
  return int(latest.split('.')[0]), os.path.join(working_dir, latest)

def get_date_from_event_file(path_to_event) -> datetime.datetime:
  with open(path_to_event) as fid:
    front_matter, _ = parse_jekyll_front_matter(''.join(fid.readlines()))
  
  return front_matter["date"]

def get_base_text(event_date: datetime.datetime):
  base_text = f"---\n"
  base_text += f"name: A trail!?!?!\n"
  base_text += f"hares: Maybe You?? (contact Jersey Lunchbox or current Hareraiser!)\n"
  base_text += f"location: TBD\n"
  base_text += f"date: {event_date.strftime('%Y-%m-%d')}\n"
  base_text += f"---\n"
  base_text += f"\n"
  base_text += f"(details to follow)\n"
  return base_text

def main():
  flags = get_flags()
  
  latest_event_number, latest = get_basis_event(flags.upcumming_dir)
  
  print(latest_event_number, latest)
  starting_date : datetime.datetime = get_date_from_event_file(latest)
  for event_number, event_date in enumerate(get_next_n_months(starting_date, flags.num_to_add), start=latest_event_number+1):
    log.info(f"Generating event #{event_number} for {event_date}")
    event_filename = os.path.join(flags.upcumming_dir, f"{event_number}.md")
    event_text = get_base_text(event_date)
    
    with open(event_filename, 'w') as fid:
      fid.write(event_text)
  
  
  
if __name__ == "__main__":
  main()