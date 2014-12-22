import argparse
import re

parser = argparse.ArgumentParser(description='Convert *.asciitab guitar tabs to .vextab.')
parser.add_argument('infile', type=argparse.FileType('r'))

args = parser.parse_args()

lines = map(lambda line: line.rstrip(), args.infile.readlines())

BAR_REGEX = r'^[HP/\d\\\-]+$'
TAB_LINE_REGEX = r'^[HPABCDEFG=/\d\\\-\|]+$'

tab_line_regex = re.compile(TAB_LINE_REGEX, re.IGNORECASE)
bar_regex = re.compile(BAR_REGEX, re.IGNORECASE)

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

def parse_bars_from_stave(stave):
  bars = zip(*[line.split('|') for line in stave])
  # make sure every line in the bar has the same length
  bars = filter(lambda bar: all([len(line) == len(bar[0]) for line in bar]), bars)
  # filter out empty strings
  bars = filter(lambda bar: len(bar[0]) > 0, bars)
  # filter out sections that contain characters that aren't part of the bar
  bars = filter(lambda bar: all([bar_regex.match(line) for line in bar]), bars)
  return bars

staves = parse_staves_from_lines(lines)

for stave in staves:
  for bar in parse_bars_from_stave(stave):
    print '#######################################'
    for line in bar:
      print line
