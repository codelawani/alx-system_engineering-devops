#!/usr/bin/env bash
read -r file position <<< "$(tail -n +2 output.txt | head -n 1 | awk '{print $1, $2}')"

echo "$file"
echo "$position"
