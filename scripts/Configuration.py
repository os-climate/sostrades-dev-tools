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
Configuration.py is a script that initialise files and folders needed for sostrades :
- sostrades-dev-tools/platform/sostrades-webapi/sos_trades_api/configuration_template/configuration.json
- sostrades-dev-tools/platform/sostrades-webapi/.flaskenv
- sostrades-dev-tools/data/REFERENCES
- sostrades-dev-tools/data/RSA/private_key.pem
- sostrades-dev-tools/data/RSA/public_key.pem
'''
import json
import os

from constants import platform_path, flaskenv_file_path, model_path, data_path
from tooling import list_directory_paths


# Init platform/sostrades-webapi/sos_trades_api/configuration_template/configuration.json configuration file
configuration_path = f"{platform_path}/sostrades-webapi/sos_trades_api/configuration_template/configuration.json"
local_configuration_template_path = os.path.join(os.path.dirname(__file__), "local_configuration_template.json")

rsa_path = os.path.join(data_path, "RSA")
reference_path = os.path.join(data_path, "REFERENCE")

# Copy template file
if not os.path.exists(configuration_path):
    print("Local config file not found, creating one from template")
    with open(local_configuration_template_path, "r") as config_template_file:
        with open(configuration_path, 'w') as config_file:
            config_file.write(config_template_file.read())


# Updating sos_processes
def find_module_name(folder_path):
    module_name_parts = []
    current_dir = folder_path

    # Traverse upwards until we reach the root directory or encounter another '__init__.py'
    while os.path.isfile(os.path.join(current_dir, '__init__.py')):
        # Found '__init__.py', add the folder name to the module name parts
        module_name_parts.append(os.path.basename(current_dir))
        current_dir = os.path.dirname(current_dir)

    # Reverse the list and join to construct the module name
    return '.'.join(reversed(module_name_parts))

def list_modules_with_init_and_sos_processes(root_dir):
    result_folders = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if '__init__.py' in filenames and 'sos_processes' in dirnames:
            module_name = find_module_name(dirpath) + ".sos_processes"
            result_folders.append(module_name)
    return result_folders

all_platform_directory = list_directory_paths(platform_path)
all_model_directory = list_directory_paths(model_path)

sos_processes_modules = []
for folder in all_platform_directory + all_model_directory:
    sos_processes_modules += list_modules_with_init_and_sos_processes(folder)

print("Updating SOS_TRADES_PROCESS_REPOSITORY with local setup")
# Edit SOS_TRADES_PROCESS_REPOSITORY
with open(configuration_path, 'r') as config_file:
    configuration_data = json.load(config_file)

configuration_data["SOS_TRADES_PROCESS_REPOSITORY"] = sos_processes_modules
configuration_data["SQL_ALCHEMY_DATABASE"]["URI"] = f"sqlite:///{data_path}/sostrades-data.db"
configuration_data["LOGGING_DATABASE"]["URI"] = f"sqlite:///{data_path}/sostrades-logs.db"
configuration_data["SOS_TRADES_DATA"] = data_path
configuration_data["SOS_TRADES_REFERENCES"] = reference_path
configuration_data["SOS_TRADES_RSA"] = rsa_path

with open(configuration_path, 'w') as config_file:
    json.dump(configuration_data, config_file, indent=4)

# Define the values of .flaskenv
flask_env = {
    "FLASK_APP": "sos_trades_api/server/base_server.py",
    "FLASK_ENV": "development",
    "SOS_TRADES_SERVER_CONFIGURATION": f"{platform_path}/sostrades-webapi/sos_trades_api/configuration_template/configuration.json",
    #"SQL_ACCOUNT": "user",
    #"SQL_PASSWORD": "password",
    #"LOG_USER": "user",
    #"LOG_PASSWORD": "password",
    "SECRET_KEY": "ABCDEFGH12"
}

# Write the values to the file
with open(flaskenv_file_path, "w") as f:
    for key, value in flask_env.items():
        f.write(f"{key}={value}\n")

print(f"{flaskenv_file_path} has been successfully created.")

# Create repositories
os.makedirs(rsa_path, exist_ok=True)
os.makedirs(reference_path, exist_ok=True)

# Define the files path
private_key_path = os.path.join(rsa_path, "private_key.pem")
public_key_path = os.path.join(rsa_path, "public_key.pem")

# Create empty files
if not os.path.exists(private_key_path):
    with open(private_key_path, "w") as f:
        pass  # This just creates an empty file
    print(f"{private_key_path} have been created.")
else:
    print(f"{private_key_path} already created.")
if not os.path.exists(public_key_path):
    with open(public_key_path, "w") as f:
        pass  # This just creates an empty file
    print(f"{public_key_path} have been created.")
else:
    print(f"{public_key_path} already created.")
