#!/usr/bin/env sh

# Remove comment lines from for ex. a conf file, and pipe output to a new copy
grep -o '^[^#]*' file config.conf > updated_config.conf
