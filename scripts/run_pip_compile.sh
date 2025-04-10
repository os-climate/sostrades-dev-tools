#!/bin/bash
# Get the directory of the current script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Change to the script's directory
cd "$SCRIPT_DIR/.."

mkdir -p ./platform_requirements

# # Initialize an empty string to collect all requirements.txt paths
# requirements_files=""

echo "Collecting requirements.txt files..."
model_reqs=""

for dir in models/*; do
    if [ -f "$dir/requirements.txt" ]; then
        echo "####################"
        echo "Found: $dir/requirements.txt"
        cat "$dir/requirements.txt"
        model_reqs+=" $dir/requirements.txt"
    fi
done

core_req="./platform/sostrades-core/requirements.txt"
webapi_req="./platform/sostrades-webapi/requirements.txt"
ontology_req="./platform/sostrades-ontology/requirements.txt"

if [ -f "$core_req" ] && [ -f "$webapi_req" ]; then

    echo "Compiling dev.requirements.txt..."
    all_reqs="$core_req $webapi_req"
    if [ -f "$ontology_req" ]; then
        all_reqs="$all_reqs $ontology_req"
    fi

    uv pip compile --resolver=backtracking \
        --output-file=./platform_requirements/dev.requirements.txt \
        $model_reqs $all_reqs --upgrade

    if [ -f "$ontology_req" ]; then
        echo "Compiling ontology.requirements.txt..."
        uv pip compile --resolver=backtracking \
            --output-file=./platform_requirements/ontology.requirements.txt \
            "$ontology_req" \
            -c ./platform_requirements/dev.requirements.txt --upgrade
    else
        echo "No ontology requirements.txt found, skipping."
    fi

    echo "Compiling api.requirements.txt..."
    uv pip compile --resolver=backtracking \
        --output-file=./platform_requirements/api.requirements.txt \
        $model_reqs $core_req $webapi_req \
        -c ./platform_requirements/dev.requirements.txt --upgrade

    echo "✅ All requirements compiled successfully."

else
    echo "❌ Core and/or WebAPI requirements.txt missing."
    exit 1
fi
