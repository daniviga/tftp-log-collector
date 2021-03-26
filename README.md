# tftp-log-collector

## Installation

Setup a python venv

```bash
python3 -m venv venv
source venv/bin/activate
```

## Getting started

```bash
./log_collector.py -h

usage: log_collector.py [-h] [--ext EXT] [--delay DELAY] csv_file

positional arguments:
  csv_file              CSV file to be parsed

optional arguments:
  -h, --help            show this help message and exit
  --ext EXT, -e EXT     File extension to be used (default: log)
  --delay DELAY, -d DELAY
                        Delay between collections in hrs (default: 12)

```
