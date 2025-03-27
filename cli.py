#!/usr/bin/env python3
"""Command-line interface for csv-merge-cli."""
import argparse
import json
import sys
from csv_merge_cli import analyze

def main(argv=None):
    parser = argparse.ArgumentParser(description='Merge repeated CSV sections and union their columns without data loss')
    parser.add_argument('path', help='Input data file')
    args = parser.parse_args(argv)
    with open(args.path, encoding='utf-8') as f:
        data = f.read()
    print(json.dumps(analyze(data), sort_keys=True))
    return 0

if __name__ == '__main__':
    sys.exit(main())
