import argparse
import re

parser = argparse.ArgumentParser(description='Convert *.asciitab guitar tabs to .vextab.')
parser.add_argument('infile', type=argparse.FileType('r'))

args = parser.parse_args()

lines = args.infile.readlines()

TAB_LINE_REGEX = r'^[HPABCDEFG=/\d\\\-\|]+$'

tab_line_regex = re.compile(TAB_LINE_REGEX, re.IGNORECASE)

def is_stave(lines):
  return len(lines) == 6 and all([tab_line_regex.match(line.strip()) for line in lines])

def parse_staves_from_lines(lines):
  staves = []
  i = 0
  while i < len(lines):
    stave = lines[i:i+6]
    if is_stave(stave):
      staves.append(stave)
      i += 5
    else:
      i += 1
  return staves
    
staves = parse_staves_from_lines(lines)

for stave in staves:
  print '#######################################'
  for line in stave:
    print line,
