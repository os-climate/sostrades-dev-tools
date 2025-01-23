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
PrepareVenv.py is a script that install venv in the path sostrades-dev-tools/.venv only if you have a python version in v3.9.
After the environement is created it will install all requirements of platform, model, and in addition python_ldap. 
At the end of the script, a file sostrades-dev-tools/.venv/lib/site-packages/sostrades.pth with is created with all path of the different repositories.
Then is is possible to run the .venv with the commande sostrades-dev-tools/.venv/Scripts/activate
'''
import os
import sys

from constants import (
    platform_path,
    model_path,
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
accepted_python_major_version = 3
accepted_python_minor_version = 9

if (
    sys.version_info.major != accepted_python_major_version
    or sys.version_info.minor != accepted_python_minor_version
):
    raise Exception(
        f"Python version : {python_version} but python v{accepted_python_major_version}.{accepted_python_minor_version} is required"
    )

# Create a venv with the good python version inside sostrades-dev-tools/.venv
create_venv_command = f"{sys.executable} -m venv '{venv_path}'"
run_command(create_venv_command)
print(f"Venv created in the folling path : '{venv_path}'")

# Install platform and model requirements
if not os.path.exists(venv_script_activate_path):
    raise Exception(
        "Virtual environment (venv) is not well installed so the requierements cannot be installed"
    )

requirements_models = []
for model_folder in os.listdir(model_path):
    requirements_path = f"{model_path}/{model_folder}/requirements.in"
    if os.path.exists(requirements_path):
        requirements_models.append(f"-r '{model_path}/{model_folder}/requirements.in'")
requirements_model_command = " ".join(requirements_models)
run_command(
    f"{venv_script_activate_command} && python -m pip list && \
            python -m pip install --no-cache-dir wheel && \
            python -m pip install --no-cache-dir \
            -r '{platform_path}/sostrades-core/requirements.in' \
            -r '{platform_path}/sostrades-ontology/requirements.in' \
            -r '{platform_path}/sostrades-webapi/requirements.in' \
            {requirements_model_command}\
            && python -m pip list"
)

#  Create sostrades.pth inside the .venv
sostrades_pth_path = f"{venv_lib_site_package_path}/sostrades.pth"
if not os.path.exists(venv_lib_site_package_path):
    raise Exception(
        "Virtual environment (venv) is not well installed so the requierements cannot be installed"
    )

# Call the function to get directory paths
all_platform_directory = list_directory_paths(platform_path)
all_model_directory = list_directory_paths(model_path)

# Create the sostrades.pth for the Python environment
write_array_to_file(all_platform_directory + all_model_directory, sostrades_pth_path)
