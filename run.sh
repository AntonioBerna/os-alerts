#!/bin/sh

set -xe

python src/main.py --env .env --urls urls.csv # --json db.json
