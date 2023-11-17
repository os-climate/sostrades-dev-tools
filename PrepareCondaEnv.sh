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

# Define the environment name
environment_name="SOSTradesEnv"

# Update conda and create a new environment
echo "Preparing conda env"
conda update -y -n base conda
conda config --set channel_priority flexible
conda remove -y --name "$environment_name" --all
conda create -y -n "$environment_name" python=3.9.16

# Activate the new environment
echo "Activating conda env"
source activate "$environment_name"

# Install and upgrade pip
echo "Installing requirements in conda env"
python -m pip install --upgrade pip

# Install packages from requirements file, excluding some problematic packages
grep -vE 'petsc|mysqlclient|python-ldap|python3-saml|xmlsec' platform/sostrades-webapi/api.requirements.txt | python -m pip install -r /dev/stdin --no-cache-dir

# Set up PYTHONPATH
echo "Setting up PYTHONPATH"
conda deactivate
conda_path="$(conda info --envs | awk -v env="$environment_name" '$0 ~ env {print $2}')/lib/python3.9/site-packages/conda.pth"

# Find and add subfolders to PYTHONPATH
echo "$PWD/platform/gemseo/src" > "$conda_path"
for path in "$PWD/platform"/*; do
    if [ -d "$path" ] && [ "$(basename "$path")" != "gemseo" ]; then
        echo "$path" >> "$conda_path"
    fi
done
for path in "$PWD/models"/*; do
    if [ -d "$path" ]; then
        echo "$path" >> "$conda_path"
    fi
done

echo "Done"
