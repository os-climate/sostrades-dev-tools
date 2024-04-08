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

# Run os.system command with interruption
def run_command(cmd):
 if os.system(cmd) != 0:
    raise Exception(f"Error to execute {cmd}")

# Function to get all directories within a directory
def list_directory_paths(directory):
    # Check if the path is a directory
    if not os.path.isdir(directory):
        print(f"{directory} is not a directory.")
        return []

    # Initialize an array to store directory paths
    directory_paths = []

    # Iterate through the directories in the given directory
    for folder_name in os.listdir(directory):
        # Construct the absolute path
        absolute_path = os.path.join(directory, folder_name)
        # Check if it's a directory
        if os.path.isdir(absolute_path):
            # Check if the directory is gemseo then add \src to the path 
            if os.path.basename(absolute_path)=="gemseo":
                directory_paths.append(os.path.join(absolute_path, "src"))
            # Add the absolute path to the array
            else:
                directory_paths.append(absolute_path)

    return directory_paths

# Function to write a file from array
def write_array_to_file(array, file_path):
    try:
        # Open the file in write mode
        with open(file_path, 'w') as f:
            # Write each element of the array on a separate line
            for item in array:
                f.write(str(item) + '\n')
        print(f"Array written to {file_path} successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Path
platform_dir="platform"
model_dir="models"

# Variable with the path of sostrade-dev-tools
sostrades_dev_tools_path = os.path.dirname(os.path.dirname(__file__))
print(f"sostrades-dev-tools PATH : {sostrades_dev_tools_path}")

# Display Python version
python_version=sys.version.split()[0] 
print(f"Python version : {python_version}")

# Check Python version
accepted_python_major_version=3
accepted_python_minor_version=9
check_python_version=False
if accepted_python_major_version==sys.version_info.major and accepted_python_minor_version==sys.version_info.minor: #Check python version = v3.9.x
    check_python_version=True
else:
    print(f"Python version : {python_version} but python v{accepted_python_major_version}.{accepted_python_minor_version} is required")

# Create .\venv directory
venv_path= f"{sostrades_dev_tools_path}\\sostrades-venv"
if not os.path.exists(venv_path) and check_python_version==True:
    os.makedirs(venv_path)
    print(f"{venv_path} created")

# Create a venv with the good python version inside sostrades-dev-tools\sostrades-venv
if not os.path.exists(venv_path) and check_python_version==True: 
   create_venv_command=f"python -m venv {venv_path}"
   run_command(create_venv_command)
   print (f"Venv created in the folling path : {venv_path}")
else:
   print("Cannot create a virtual environment (venv) because you do not have a compatible version of Python")

# Install platform and model requirements 
venv_script_activate_path= f"{venv_path}\\Scripts\\activate"
if os.path.exists(venv_script_activate_path) and check_python_version==True:
    run_command(f"{venv_script_activate_path} && pip list && \
                python -m pip install --no-cache-dir \
                https://download.lfd.uci.edu/pythonlibs/archived/python_ldap-3.4.0-cp39-cp39-win_amd64.whl \
                -r {sostrades_dev_tools_path}\\{platform_dir}\\gemseo\\requirements.txt \
                -r {sostrades_dev_tools_path}\\{platform_dir}\\sostrades-core\\requirements.in \
                -r {sostrades_dev_tools_path}\\{platform_dir}\\sostrades-ontology\\requirements.in \
                -r {sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webapi\\requirements.in \
                -r {sostrades_dev_tools_path}\\{model_dir}\\\witness-energy\\requirements.in \
                -r {sostrades_dev_tools_path}\\{model_dir}\\witness-core\\requirements.in \
                && pip list")
else:
   print("Virtual environment (venv) is not well installed so the requierements cannot be installed")

#  Create sostrades.pth inside the sostrades-venv
venv_lib_site_package_path= f"{venv_path}\\lib\\site-packages"
sostrades_pth_path= f"{venv_lib_site_package_path}\\sostrades.pth"
if os.path.exists(venv_lib_site_package_path) and check_python_version==True:
    # Directory path to traverse
    platform_path = f"{sostrades_dev_tools_path}\\{platform_dir}"
    model_path = f"{sostrades_dev_tools_path}\\{model_dir}"

    # Call the function to get directory paths
    all_platform_directory = list_directory_paths(platform_path)
    all_model_directory=list_directory_paths(model_path)
    platform_model_directory=all_platform_directory
    platform_model_directory.extend(all_model_directory)

    # Print the directory paths
    for path in platform_model_directory:
        print(path)

    # Create the sostrades.pth for the Python environment
    write_array_to_file(platform_model_directory, sostrades_pth_path)
else:
   print("Virtual environment (venv) is not well installed so the requierements cannot be installed")