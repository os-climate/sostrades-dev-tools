import os

from constants import venv_script_activate_path, venv_script_activate_command, sostrades_dev_tools_path, platform_path, model_path
from tooling import run_command, list_directory_paths

# Get all the directories in the platform and model directories
all_platform_directory = list_directory_paths(platform_path)
all_model_directory = list_directory_paths(model_path)

# Create Pythonpath with all the models and platform depends on the system environment
python_path=""
for source in all_model_directory:
    python_path+= source + os.pathsep
for source in all_platform_directory:
    python_path+= source + os.pathsep

# Set PYTHONPATH environment variable with the path of all the models and platform
os.environ['PYTHONPATH']= f'{python_path}'
print(f"PYTHONPATH={os.environ.get('PYTHONPATH')}")

if not os.path.exists(venv_script_activate_path):
    raise Exception("Virtual environment (.venv) is not installed")
if not os.path.exists(f"{platform_path}/sostrades-ontology"):
    raise Exception(f"{platform_path}/sostrades-ontology repository not found")

print("Updating ontology ...")
# Change directory to sostrades-dev-tools/platform/sostrades-ontology
os.chdir(f"{platform_path}/sostrades-ontology")
# Start sostrades-ontology with .venv
run_command(
    f'{venv_script_activate_command} && python sos_ontology/core/script/createSoSOntologyFromCode.py'
)
print("Finished")

os.chdir(sostrades_dev_tools_path)