#!/bin/bash
# Get the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script's directory
cd "$SCRIPT_DIR"
cd ../

mkdir -p ./platform_requirements

# Initialize an empty string to collect all requirements.in paths
requirements_files=""

# Loop through each directory in the models folder
for dir in models/*; do
    if [ -d "$dir" ]; then
        # Check if requirements.in exists in the directory
        if [ -f "$dir/requirements.in" ]; then
            # Add the path to the requirements_files string
            requirements_files="'./$dir/requirements.in' $requirements_files"
            echo "./$dir/requirements.in"
            cat "./$dir/requirements.in"
        fi
    fi
done

# Compile the 3 requirement files
echo "Attempting to compile all and ontology requirements"
if [ -f "./platform/sostrades-ontology/requirements.in" ] && [ -f "./platform/gemseo/requirements.txt" ] && [ -f "./platform/sostrades-core/requirements.in" ] && [ -f "./platform/sostrades-webapi/requirements.in" ]; then
    eval "pip-compile --resolver=backtracking --output-file=./platform_requirements/dev.requirements.txt $requirements_files './platform/gemseo/requirements.txt' './platform/sostrades-core/requirements.in' './platform/sostrades-webapi/requirements.in' './platform/sostrades-ontology/requirements.in' --upgrade"
    
    if [ $? -eq 0 ]; then
        echo "Compile all requirements passed"
    else
        echo "Compile all requirements failed"
        exit 1
    fi

    eval "pip-compile --resolver=backtracking --output-file=./platform_requirements/ontology.requirements.txt './platform/sostrades-ontology/requirements.in' --upgrade"
    if [ $? -eq 0 ]; then
        echo "Compile ontology requirements passed"
    else
        echo "Compile ontology requirements failed"
        exit 1
    fi
else
    echo "One or more required files do not exist."
    exit 1
fi

echo "Attempting to compile api requirements"
if [ -f "./platform/gemseo/requirements.txt" ] && [ -f "./platform/sostrades-core/requirements.in" ] && [ -f "./platform/sostrades-webapi/requirements.in" ]; then
    eval "pip-compile --resolver=backtracking --output-file=./platform_requirements/api.requirements.txt $requirements_files './platform/gemseo/requirements.txt' './platform/sostrades-core/requirements.in' './platform/sostrades-webapi/requirements.in' --upgrade"
    if [ $? -eq 0 ]; then
        echo "Compile api requirements passed"
    else
        echo "Compile api requirements failed"
        exit 1
    fi
else
    echo "One or more required files do not exist."
    exit 1
fi
