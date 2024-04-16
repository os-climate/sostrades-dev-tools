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
PrepareVenv.py is a script that install venv in the path sostrades-dev-tools\sostrades-venv only if you have a python version in v3.9.
After the environement is created it will install all requirements of platform, model, and in addition python_ldap. 
At the end of the script, a file sostrades-dev-tools\sostrades-venv\lib\site-packages\sostrades.pth with is created with all path of the different repositories.
Then is is possible to run the sostrades-venv with the commande sostrades-dev-tools\sostrades-venv\Scripts\activate
'''
import os
import sys

from constants import sostrades_dev_tools_path, platform_path, model_path
from tooling import run_command


# Function to get all directories within a directory
def list_directory_paths(directory):
    # Check if the path is a directory
    if not os.path.isdir(directory):
        raise Exception(f"{directory} is not a directory.")

    # Initialize an array to store directory paths
    directory_paths = []

    # Iterate through the directories in the given directory
    for folder_name in os.listdir(directory):
        # Construct the absolute path
        absolute_path = os.path.join(directory, folder_name)
        # Check if it's a directory
        if os.path.isdir(absolute_path):
            # Check if the directory is gemseo then add \src to the path
            if os.path.basename(absolute_path) == "gemseo":
                directory_paths.append(os.path.join(absolute_path, "src"))
            # Add the absolute path to the array
            else:
                directory_paths.append(absolute_path)

    return directory_paths


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
accepted_python_major_version = 3
accepted_python_minor_version = 9

if (
    sys.version_info.major != accepted_python_major_version
    or sys.version_info.minor != accepted_python_minor_version
):
    raise Exception(
        f"Python version : {python_version} but python v{accepted_python_major_version}.{accepted_python_minor_version} is required"
    )

# Create .\venv directory
venv_path = f"{sostrades_dev_tools_path}\\sostrades-venv"

# Create a venv with the good python version inside sostrades-dev-tools\sostrades-venv
create_venv_command = f"python -m venv {venv_path}"
run_command(create_venv_command)
print(f"Venv created in the folling path : {venv_path}")

# Install platform and model requirements
venv_script_activate_path = f"{venv_path}\\Scripts\\activate"
if os.path.exists(venv_script_activate_path):
    run_command(
        f"{venv_script_activate_path} && pip list && \
                python -m pip install --no-cache-dir \
                https://download.lfd.uci.edu/pythonlibs/archived/python_ldap-3.4.0-cp39-cp39-win_amd64.whl \
                -r {platform_path}\\gemseo\\requirements.txt \
                -r {platform_path}\\sostrades-core\\requirements.in \
                -r {platform_path}\\sostrades-ontology\\requirements.in \
                -r {platform_path}\\sostrades-webapi\\requirements.in \
                -r {model_path}\\\witness-energy\\requirements.in \
                -r {model_path}\\witness-core\\requirements.in \
                && pip list"
    )
else:
    print(
        "Virtual environment (venv) is not well installed so the requierements cannot be installed"
    )

#  Create sostrades.pth inside the sostrades-venv
venv_lib_site_package_path = f"{venv_path}\\lib\\site-packages"
sostrades_pth_path = f"{venv_lib_site_package_path}\\sostrades.pth"
if os.path.exists(venv_lib_site_package_path):
    # Call the function to get directory paths
    all_platform_directory = list_directory_paths(platform_path)
    all_model_directory = list_directory_paths(model_path)

    # Create the sostrades.pth for the Python environment
    write_array_to_file(
        all_platform_directory + all_model_directory, sostrades_pth_path
    )
else:
    print(
        "Virtual environment (venv) is not well installed so the requierements cannot be installed"
    )
