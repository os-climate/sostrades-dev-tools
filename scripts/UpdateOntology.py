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
UpdateOntology.py is a script that execute “python sos_ontology\core\script\createSoSOntologyFromCode.py” to update ontology
'''
import os

from constants import (
    venv_script_activate_path,
    sostrades_dev_tools_path,
    platform_path,
    model_path
)
from tooling import run_command, list_directory_paths

all_platform_directory = list_directory_paths(platform_path)
all_model_directory = list_directory_paths(model_path)

python_path=""
for source in all_model_directory:
    python_path+=source + os.pathsep
for source in all_platform_directory:
    python_path+=source + os.pathsep
   
print(f'PYTHONPATH={python_path}')

if os.path.exists(venv_script_activate_path):
    if os.path.exists(f"{platform_path}\\sostrades-ontology"):
        print("Updating ontology ...")
        # Change directory to sostrades-dev-tools\platform\sostrades-ontology
        os.chdir(f"{platform_path}\\sostrades-ontology")
        # Start sostrades-ontology with sostrades-venv
        run_command(
            f"{venv_script_activate_path} && set PYTHONPATH={python_path} && python sos_ontology\\core\\script\\createSoSOntologyFromCode.py"
        )
        print("Finished")
    else:
        print(f"{platform_path}\\sostrades-ontology repository not found")

    os.chdir(sostrades_dev_tools_path)
else:
    print("Virtual environment (sostrades-venv) is not installed")

