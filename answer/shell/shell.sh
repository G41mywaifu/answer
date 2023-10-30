#!/bin/bash


if [ $# -ne 2 ]; then
    exit 1
fi

file=$1
search_string=$2
output_file="item.txt"

grep -n "$search_string" "$file" > "$output_file"

cat "$output_file"