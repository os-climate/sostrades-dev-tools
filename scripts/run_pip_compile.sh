#!/bin/bash
# Get the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script's directory
cd "$SCRIPT_DIR"
cd ../

mkdir -p ./platform_requirements

# Initialize an empty string to collect all requirements.in paths
requirements_files=""

# echo palatform requirements
for dir in platform/*; do
    if [ -d "$dir" ]; then
        # Check if requirements.in exists in the directory
        if [ -f "$dir/requirements.in" ]; then
            echo "####################"
            echo "./$dir/requirements.in"
            cat "./$dir/requirements.in"
        fi
        if [ -f "$dir/requirements.txt" ]; then
            echo "####################"
            echo "./$dir/requirements.txt"
            cat "./$dir/requirements.txt"
        fi
    fi
done

# Loop through each directory in the models folder
for dir in models/*; do
    if [ -d "$dir" ]; then
        # Check if requirements.in exists in the directory
        if [ -f "$dir/requirements.in" ]; then
            echo "####################"
            # Add the path to the requirements_files string
            requirements_files="'./$dir/requirements.in' $requirements_files"
            echo "./$dir/requirements.in"
            cat "./$dir/requirements.in"
        fi
    fi
done

# Compile the 3 requirement files
echo "Attempting to compile all and ontology requirements"

core_req="./platform/sostrades-core/requirements.in"
webapi_req="./platform/sostrades-webapi/requirements.in"
ontology_req="./platform/sostrades-ontology/requirements.in"

if [ -f "$core_req" ] && [ -f "$webapi_req" ]; then

    # Construire la commande pour dev.requirements.txt
    all_reqs="$core_req $webapi_req"
    if [ -f "$ontology_req" ]; then
        all_reqs="$all_reqs $ontology_req"
    fi

    eval "uv pip compile --resolver=backtracking --output-file=./platform_requirements/dev.requirements.txt $requirements_files $all_reqs --upgrade"
    if [ $? -eq 0 ]; then
        echo "Compile all requirements passed"
    else
        echo "Compile all requirements failed"
        exit 1
    fi

    # Compiler ontology.requirements.txt uniquement si le fichier existe
    if [ -f "$ontology_req" ]; then
        eval "uv pip compile --resolver=backtracking --output-file=./platform_requirements/ontology.requirements.txt '$ontology_req' -c ./platform_requirements/dev.requirements.txt --upgrade"
        if [ $? -eq 0 ]; then
            echo "Compile ontology requirements passed"
        else
            echo "Compile ontology requirements failed"
            exit 1
        fi
    else
        echo "Ontology requirements.in not found, skipping ontology compilation"
    fi

    # Compiler api.requirements.txt
    eval "uv pip compile --resolver=backtracking --output-file=./platform_requirements/api.requirements.txt $requirements_files $core_req $webapi_req -c ./platform_requirements/dev.requirements.txt --upgrade"
    if [ $? -eq 0 ]; then
        echo "Compile api requirements passed"
    else
        echo "Compile api requirements failed"
        exit 1
    fi

else
    echo "Core and/or WebAPI requirements.in file(s) missing."
    exit 1
fi