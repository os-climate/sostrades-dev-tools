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
StartSOSTrades.py is a script that run api server, ontology server, and webgui server with venv and node
'''
import os

from constants import (
    venv_script_activate_path,
    venv_script_activate_command,
    sostrades_dev_tools_path,
    platform_path,
    nvs_cmd_path,
    node_version,
)
from tooling import run_command


if os.path.exists(venv_script_activate_path):
    run_command(f"{venv_script_activate_command} && python ./scripts/CreateVersionConfFile.py")
    if os.path.exists(f"{platform_path}/sostrades-webapi"):
        print("sostrades-webapi is starting ...")
        # Change directory to sostrades-dev-tools/platform/sostrades-webapi
        os.chdir(f"{platform_path}/sostrades-webapi")
        run_command(f"{venv_script_activate_command} && flask db upgrade")
        run_command(f"{venv_script_activate_command} && flask init_process")
        # Start sostrades-webapi servers with .venv
        run_command(
            f"{venv_script_activate_command} && start cmd /K \"title API POST PROCESSING && python server_scripts/split_mode/launch_server_post_processing.py\""
        )
        run_command(
            f"{venv_script_activate_command} && start cmd /K \"title API MAIN && python server_scripts/split_mode/launch_server_main.py\""
        )
        run_command(
            f"{venv_script_activate_command} && start cmd /K \"title API DATA && python server_scripts/split_mode/launch_server_data.py\""
        )
        run_command(
            f"{venv_script_activate_command} && start cmd /K \"title API MESSAGE && python server_scripts/launch_server_message.py\""
        )

    else:
        print(f"{platform_path}/sostrades-webapi repository not found")

    if os.path.exists(f"{platform_path}/sostrades-ontology"):
        print("sostrades-ontology is starting ...")
        # Change directory to sostrades-dev-tools/platform/sostrades-ontology
        os.chdir(f"{platform_path}/sostrades-ontology")
        # Start sostrades-ontology with .venv
        run_command(
            f"{venv_script_activate_command} && start cmd /K \"title API ONTOLOGY && python sos_ontology/rest_api/api.py\""
        )
    else:
        print(f"{platform_path}/sostrades-ontology repository not found")

    os.chdir(sostrades_dev_tools_path)
else:
    print("Virtual environment (.venv) is not installed")

if os.path.exists(nvs_cmd_path):
    print("sostrades-webgui is starting ...")
    # Change directory to sostrade-webgui
    if os.path.exists(f"{platform_path}/sostrades-webgui"):
        os.chdir(f"{platform_path}/sostrades-webgui")
        run_command(f"{nvs_cmd_path} use {node_version} && start cmd /K npm start")
        os.chdir(sostrades_dev_tools_path)
    else:
        print(f"{platform_path}/sostrades-webgui repository not found")
else:
    print("NVS is not installed")
