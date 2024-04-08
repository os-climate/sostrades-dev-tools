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

# Variable with the path of sostrade-dev-tools
sostrades_dev_tools_path = os.path.dirname(os.path.dirname(__file__))
print(f"sostrades-dev-tools PATH : {sostrades_dev_tools_path}\n")

# Variable with the path of sostrades-venv
venv_path= f"{sostrades_dev_tools_path}\\sostrades-venv"
# Variable with the path of venv activate script
venv_script_activate_path= f"{venv_path}\\Scripts\\activate"

# Paths
platform_dir="platform"

# Run os.system command with interruption
def run_command(cmd):
 if os.system(cmd) != 0:
    raise Exception(f"Error to execute {cmd}")

if os.path.exists(venv_script_activate_path):
    if os.path.exists(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webapi"):
        print("sostrades-webapi is starting ...")
        # Change directory to sostrades-dev-tools\platform\sostrades-webapi
        os.chdir(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webapi")
        run_command(f"{venv_script_activate_path} && flask db upgrade")
        run_command(f"{venv_script_activate_path} && flask init_process")
        # Start sostrades-webapi servers with sostrades-venv
        run_command(f"{venv_script_activate_path} && start cmd /K python server_scripts\\split_mode\\launch_server_post_processing.py")
        run_command(f"{venv_script_activate_path} && start cmd /K python server_scripts\\split_mode\\launch_server_main.py")
        run_command(f"{venv_script_activate_path} && start cmd /K python server_scripts\\split_mode\\launch_server_data.py")
    else:
        print(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webapi repository not found")

    if os.path.exists(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-ontology"):
        print("sostrades-ontology is starting ...")
        # Change directory to sostrades-dev-tools\platform\sostrades-ontology
        os.chdir(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-ontology")
        # Start sostrades-ontology with sostrades-venv
        run_command(f"{venv_script_activate_path} && start cmd /K python sos_ontology\\rest_api\\api.py")
    else:
        print(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-ontology repository not found")

    os.chdir(sostrades_dev_tools_path)
else:
   print("Virtual environment (sostrades-venv) is not installed")


# Start sostrade-webgui
node_version="12.16.1"
nvs_home = os.environ.get('LOCALAPPDATA', '') + '\\nvs'
nvs_cmd_path = os.path.join(nvs_home, 'nvs.cmd')
if os.path.exists(nvs_cmd_path):
    print("sostrades-webgui is starting ...")
    # Change directory to sostrade-webgui
    if  os.path.exists(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webgui"):
        os.chdir(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webgui")
        run_command(f"{nvs_cmd_path} use {node_version} &&  start cmd /K npm start")
        os.chdir(sostrades_dev_tools_path)
    else:
        print(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webgui repository not found")
else:
    print("NVS is not installed")