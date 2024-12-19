import os

from constants import venv_script_activate_path, venv_script_activate_command, sostrades_dev_tools_path, platform_path, model_path
from tooling import run_command, list_directory_paths
import platform

all_platform_directory = list_directory_paths(platform_path)
all_model_directory = list_directory_paths(model_path)

python_path=""
for source in all_model_directory:
    python_path+=source + os.pathsep
for source in all_platform_directory:
    python_path+=source + os.pathsep

if platform.system() == "Windows":
    python_path=python_path.replace("/","\\")


print(f'PYTHONPATH={python_path}')

if os.path.exists(venv_script_activate_path):
    if os.path.exists(f"{platform_path}/sostrades-ontology"):
        print("Updating ontology ...")
        # Change directory to sostrades-dev-tools/platform/sostrades-ontology
        os.chdir(f"{platform_path}/sostrades-ontology")
        # Start sostrades-ontology with .venv
        if platform.system() == "Windows":
            run_command(
                f"{venv_script_activate_command} && set PYTHONPATH={python_path} && python sos_ontology/core/script/createSoSOntologyFromCode.py"
            )
        else:  # For Linux
            run_command(
                f"{venv_script_activate_command} && export PYTHONPATH={python_path} && python sos_ontology/core/script/createSoSOntologyFromCode.py"
            )
        print("Finished")
    else:
        print(f"{platform_path}/sostrades-ontology repository not found")

    os.chdir(sostrades_dev_tools_path)
else:
    print("Virtual environment (.venv) is not installed")

