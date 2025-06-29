# CPU Stress
Spring Boot 3 echo application

Requirements:
- Python 3
- Docker

## Usage

```shell
python3 app.py -h
usage: app.py [-h] [-c C] [-l L]

CPU Stress

options:
  -h, --help  show this help message and exit
  -c C        CPU cores to load
  -l L        CPU load per core in percent 0...100

python3 app.py -c 2 -l 80
```

## Development

```shell
docker build -t codelev/cpu-stress:latest .
docker run --rm codelev/cpu-stress:latest -c 2 -l 75
# Starting CPU stress: 1 core(s) at 80% load each.
```
