import argparse

parser = argparse.ArgumentParser(description='Convert *.asciitab guitar tabs to .vextab.')
parser.add_argument('infile', type=argparse.FileType('r'))

args = parser.parse_args()

lines = args.infile.readlines()

for line in lines:
  print line,
