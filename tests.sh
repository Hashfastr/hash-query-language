#!/bin/bash

# Vibe coded script

# Set the root directory to search; defaults to current directory if none provided
ROOT_DIR="./examples"

# Placeholder command to run on each file (replace this with your actual command)
# Use "$file" to reference the file in the command
run_command() {
    # Example: just cat the file (replace with real logic)
    python3 -m Hql -f "$1" > /dev/null 2> /dev/null
}

total=0
failed=0

# Loop through each regular file found under the root directory
find "$ROOT_DIR" -type f | while IFS= read -r file; do
    ((total++))
    echo -n "."

    
    if ! run_command "$file"; then
      echo
      echo "Hql test failed here: $file"
      ((failed++))
    fi
done
echo ""

echo "$failed/$total Failed"
