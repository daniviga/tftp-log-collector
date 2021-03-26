# tftp-log-collector

## System-wide installation

```bash
$> pip install .

$> log_collector.py -h

usage: log_collector.py [-h] [--ext EXT] [--delay DELAY] csv_file

positional arguments:
  csv_file              CSV file to be parsed

optional arguments:
  -h, --help            show this help message and exit
  --ext EXT, -e EXT     File extension to be used (default: log)
  --delay DELAY, -d DELAY
                        Delay between collections in hrs (default: 12)
```


## Dev installation

Setup a python venv

```bash
$> python3 -m venv venv
$> source venv/bin/activate
$> pip install -r requirements.txt
$> ./log_collector.py -h
```
