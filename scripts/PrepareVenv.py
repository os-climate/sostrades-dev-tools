'''
Copyright 2024 Capgemini
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
'''
PrepareVenv.py is a script that installs venv in the path sostrades-dev-tools/.venv only if you have a python version 3.12 or higher.
After the environment is created it will install all requirements of platform, model, and in addition python_ldap.
At the end of the script, a file sostrades-dev-tools/.venv/lib/site-packages/sostrades.pth is created with all paths of the different repositories.
Then it is possible to run the .venv with the command sostrades-dev-tools/.venv/Scripts/activate
'''
import os
import sys

from constants import (
    platform_path,
    model_path,
    sostrades_dev_tools_path,
    venv_script_activate_path,
    venv_script_activate_command,
    venv_path,
    venv_lib_site_package_path,
)
from tooling import run_command, list_directory_paths


# Function to write a file from array
def write_array_to_file(array, file_path):
    # Open the file in write mode
    with open(file_path, "w") as f:
        # Write each element of the array on a separate line
        for item in array:
            f.write(f"{item}\n")
    print(f"Array written to {file_path} successfully.")


# Display Python version
python_version = sys.version.split()[0]
print(f"Python version : {python_version}")

# Check Python version
required_python_major_version = 3
required_python_minor_version = 12

if sys.version_info.major < required_python_major_version or (
    sys.version_info.major == required_python_major_version
    and sys.version_info.minor < required_python_minor_version
):
    raise Exception(
        f"Python version {python_version} detected, but Python v{required_python_major_version}.{required_python_minor_version}+ is required"
    )

# Create a venv with the good python version inside sostrades-dev-tools/.venv
if os.path.exists(venv_script_activate_path):
    print(f"Virtual environment already exists at {venv_path}. Recreating it with --clear flag.")
    create_venv_command = f"{sys.executable} -m venv --clear {venv_path}"
else:
    print(f"Creating new virtual environment at {venv_path}")
    create_venv_command = f"{sys.executable} -m venv {venv_path}"

run_command(create_venv_command)

# Verify the venv was created successfully
if not os.path.exists(venv_script_activate_path):
    raise Exception(
        f"Virtual environment creation failed. Activation script not found at: {venv_script_activate_path}"
    )

print(f"Venv created successfully in: {venv_path}")

# Helper function to find requirements file (prefers .in, falls back to .txt, then pyproject.toml)
def find_requirements_file(repo_path):
    # Check if the repository directory exists
    if not os.path.isdir(repo_path):
        return None

    if os.path.exists(f"{repo_path}/requirements.in"):
        return f"-r {repo_path}/requirements.in"
    elif os.path.exists(f"{repo_path}/requirements.txt"):
        return f"-r {repo_path}/requirements.txt"
    elif os.path.exists(f"{repo_path}/pyproject.toml"):
        return f"-e {repo_path}"
    return None

# Collect platform requirements
platform_requirements = []
for repo_name in ["sostrades-core", "sostrades-ontology", "sostrades-webapi"]:
    repo_path = f"{platform_path}/{repo_name}"
    req_file = find_requirements_file(repo_path)
    if req_file:
        platform_requirements.append(req_file)
    else:
        print(f"Warning: No requirements file found for {repo_name}")

# Collect model requirements
requirements_models = []
if os.path.exists(model_path):
    for model_folder in os.listdir(model_path):
        model_repo_path = f"{model_path}/{model_folder}"
        if os.path.isdir(model_repo_path):
            req_file = find_requirements_file(model_repo_path)
            if req_file:
                requirements_models.append(req_file)

# Combine all requirements
all_requirements = " ".join(platform_requirements + requirements_models)

# Validate that we have requirements to install
if not all_requirements.strip():
    raise Exception(
        "No requirements files found in platform or model repositories. "
        "Please ensure repositories contain requirements.in, requirements.txt, or pyproject.toml files."
    )

# Install all requirements
install_command = f"{venv_script_activate_command} && pip list && \
    python -m pip install --no-cache-dir wheel && \
    python -m pip install --no-cache-dir {all_requirements} && \
    pip list"

run_command(install_command)

#  Create sostrades.pth inside the .venv
sostrades_pth_path = f"{venv_lib_site_package_path}/sostrades.pth"
if not os.path.exists(venv_lib_site_package_path):
    raise Exception(
        "Virtual environment (venv) is not well installed so the requirements cannot be installed"
    )

# Call the function to get directory paths
all_platform_directory = list_directory_paths(platform_path)
all_model_directory = list_directory_paths(model_path)

# Create the sostrades.pth for the Python environment
write_array_to_file(all_platform_directory + all_model_directory, sostrades_pth_path)
