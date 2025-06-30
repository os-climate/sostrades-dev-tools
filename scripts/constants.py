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
import os
import platform

# Paths
platform_dir_name="platform"
model_dir_name="models"
data_dir_name="data"

# Variable with the path of sostrade-dev-tools
sostrades_dev_tools_path = os.path.dirname(os.path.dirname(__file__))
platform_path = f"{sostrades_dev_tools_path}/{platform_dir_name}"
model_path = f"{sostrades_dev_tools_path}/{model_dir_name}"
data_path = f"{sostrades_dev_tools_path}/{data_dir_name}".replace("\\", "/")

# Python version to install
python_version_to_install = "3.12.9"

# Variable with the path of .venv
venv_path = f"{sostrades_dev_tools_path}/.venv"

# Check if the platform is Windows
if platform.system() == 'Windows':
    # Define the variable with a Windows-specific path
    venv_script_activate_path = f"{venv_path}/Scripts/activate"
    venv_script_activate_command = f'call "{venv_path}/Scripts/activate"'
    venv_lib_site_package_path = f"{venv_path}/lib/site-packages"
    run_prefix_system = "start \b "
else:
    # Define the variable with a generic path for other platforms
    venv_script_activate_path = f"{venv_path}/bin/activate"
    venv_script_activate_command = f". '{venv_path}/bin/activate'"
    venv_lib_site_package_path = f"{venv_path}/lib/python3.12/site-packages"
    run_prefix_system = ""

vscode_dir = ".vscode"

# Start sostrade-webgui
node_version = "18.10.0"
nvs_home = os.environ.get('LOCALAPPDATA', '') + '/nvs'
nvs_cmd_path = os.path.join(nvs_home, 'nvs.cmd')

flaskenv_file_path = f"{sostrades_dev_tools_path}/platform/sostrades-webapi/.flaskenv"
