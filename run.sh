#!/bin/bash

echo -e "Starting Run Process... Please Wait..."

sleep 2

echo -e "Obtaining Root Directory..."
# get the root directory
root_dir=$(pwd)

echo -e "Root Dir: ${root_dir}"

# check if the dist and build folders exist.
# if not, build, else skip
if [ ! -d "${root_dir}/dist" ] && [ ! -d "${root_dir}/build"]; then
  # tell the user the folders don't exist and we're building them
  echo -e "'dist' and 'build' folders do not exist. Building Project... Please Wait..."

  # run the build command
  if [ ! python3 build.py ]; then
    echo -e "Build Failed. See output" >&2
    exit 1
  fi

  echo -e "Build Complete..."
fi

echo -e "Running PalinDrome... Please Wait..."

./dist/
