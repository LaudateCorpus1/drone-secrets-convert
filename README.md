# drone-secrets-convert
Converts pre Drone 1.0.0-rc6 YAML file with secrets to the new format

```bash
usage: convert.py [-h] [-c] file

positional arguments:
  file            path to file

optional arguments:
  -h, --help      show this help message and exit
  -c, --complete  Return the complete YAML, not just the secrets
```

# Run via Docker

```bash
$ docker pull viant/drone-secrets-convert:latest
$ docker run -v .drone.yml:/drone.yaml viant/drone-secrets-convert:latest
```

Or

```bash
$ docker run -v .drone.yml:/drone.yaml viant/drone-secrets-convert:latest convert -c
```
