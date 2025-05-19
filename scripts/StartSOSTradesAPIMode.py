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
StartSOSTradesAPIMode.py is a script that run api v0 server, ontology server
'''
import os

from constants import (
    venv_script_activate_path,
    venv_script_activate_command,
    sostrades_dev_tools_path,
    platform_path,
)
from tooling import run_command


if not os.path.exists(venv_script_activate_path):
    raise Exception("Virtual environment (.venv) is not installed")
if not os.path.exists(f"{platform_path}/sostrades-webapi"):
    raise Exception(f"{platform_path}/sostrades-webapi repository not found")
if not os.path.exists(f"{platform_path}/sostrades-ontology"):
    raise Exception(f"{platform_path}/sostrades-ontology repository not found")

run_command(f"{venv_script_activate_command} && python ./scripts/CreateVersionConfFile.py")

print("sostrades-webapi is starting ...")
# Change directory to sostrades-dev-tools/platform/sostrades-webapi
os.chdir(f"{platform_path}/sostrades-webapi")
run_command(f"{venv_script_activate_command} && flask db upgrade")
run_command(f"{venv_script_activate_command} && flask init_process")
# Start sostrades-webapi servers with .venv
run_command(
    f'{venv_script_activate_command} && start cmd /K \"title API V0 && python server_scripts/api_mode/launch_server_api_v0.py\"'
)

print("sostrades-ontology is starting ...")
# Change directory to sostrades-dev-tools/platform/sostrades-ontology
os.chdir(f"{platform_path}/sostrades-ontology")
# Start sostrades-ontology with .venv
run_command(
    f'{venv_script_activate_command} && start cmd /K \"title API ONTOLOGY && python sos_ontology/rest_api/api.py\"'
)

os.chdir(sostrades_dev_tools_path)
