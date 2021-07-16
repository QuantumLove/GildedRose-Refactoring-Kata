#!/bin/bash
set -euf -o pipefail

docker-compose run --rm gilded-rose $@ 