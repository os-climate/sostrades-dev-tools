#!/bin/bash
# Copyright 2023 Capgemini

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Function to read an array from a JSON file
read_array_from_json() {
    local file="$1"
    local array_name="$2"
    
    # Read the JSON file into the array
    IFS=$'\n' read -d '' -r -a "$array_name" < <(jq -r '.[] | .url + "," + .branch' "$file")
}

# Define the names of the JSON files for platform and model repositories
platform_file="platform_repositories.json"
model_file="model_repositories.json"

# Read platform and model repositories from JSON files
read_array_from_json "$platform_file" platform_repositories
read_array_from_json "$model_file" model_repositories

# Paths
platform_dir="./platform"
model_dir="./models"
vscode_dir="./.vscode"

# Function to clone repositories
# Usage: clone_repositories destination_directory "${repositories[@]}"
clone_repositories() {
    local destination="$1"
    shift
    local repositories=("$@")
    echo $repositories
    mkdir -p "$destination"
    cd "$destination"

    for repo in "${repositories[@]}"; do
        IFS="," read -ra parts <<< "$repo"
        repo_url="${parts[0]}"
        branch="${parts[1]}"
        git clone "$repo_url" -b "$branch"
    done

    cd ..
}

# Clone platform repositories
clone_repositories "$platform_dir" "${platform_repositories[@]}"

# Clone model repositories
clone_repositories "$model_dir" "${model_repositories[@]}"

# Generate Visual Studio Code Python extension configuration
# Create .vscode directory if it doesn't exist
mkdir -p "$vscode_dir"
python_analysis_extraPaths=()

# Add platform repositories to the configuration
for repo in "${platform_repositories[@]}"; do
    IFS="," read -ra parts <<< "$repo"
    repo_url="${parts[0]}"
    repo_name=$(basename "$repo_url" .git)
    if [ "$repo_name" == "gemseo" ]; then
        python_analysis_extraPaths+=("$platform_dir/gemseo/src")
    else
        python_analysis_extraPaths+=("$platform_dir/$repo_name")
    fi
done

# Add model repositories to the configuration
for repo in "${model_repositories[@]}"; do
    IFS="," read -ra parts <<< "$repo"
    repo_url="${parts[0]}"
    repo_name=$(basename "$repo_url" .git)
    python_analysis_extraPaths+=("$model_dir/$repo_name")
done

# Generate .vscode/settings.json
echo '{' > "$vscode_dir/settings.json"
echo '    "python.analysis.extraPaths": [' >> "$vscode_dir/settings.json"
for path in "${python_analysis_extraPaths[@]}"; do
    echo "        \"$path\"," >> "$vscode_dir/settings.json"
done
echo '    ],' >> "$vscode_dir/settings.json"
echo "    \"git.autoRepositoryDetection\": \"subFolders\"," >> "$vscode_dir/settings.json"
echo "    \"git.openRepositoryInParentFolders\": \"always\"," >> "$vscode_dir/settings.json"
echo "    \"git.repositoryScanMaxDepth\": 2" >> "$vscode_dir/settings.json"
echo '}' >> "$vscode_dir/settings.json"
