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

import json
import subprocess
import os

from constants import (
    sostrades_dev_tools_path,
    model_dir_name,
    platform_dir_name,
    vscode_dir,
    venv_path,
)


# Function to read the JSON file
def read_json_file(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


# Function to clone repositories from URLs
def git_clone(url, branch, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    os.chdir(directory)
    command = ["git", "clone", "-b", branch, url]
    subprocess.run(command)
    os.chdir(sostrades_dev_tools_path)


def clone_all_repos_in_folder(items: list[dict[str:str]], directory: str):
    for item in items:
        url = item.get("url")
        branch = item.get("branch")
        repo_name = extract_repo_name(url)
        if not os.path.exists(f"{directory}/{repo_name}"):
            print(f"Cloning {url} (branch: {branch}) into directory {directory}...")
            git_clone(url, branch, directory)
        else:
            print(f"{repo_name} already cloned")


# Function to extract the name of the project from github url
def extract_repo_name(git_url):
    # Split the URL by slashes "/"
    parts = git_url.split("/")
    # Extract the last element
    repo_name = parts[-1]
    # Remove ".git" from the end of the link if present
    repo_name = repo_name.replace(".git", "")

    return repo_name


# Path to the first JSON file (model_repositories.json)
model_file_path = "model_repositories.json"
# Path to the second JSON file (platform_repositories.json)
platform_file_path = "platform_repositories.json"

# Read the first JSON file (model_repositories.json)
model_data = read_json_file(model_file_path)
# Read the second JSON file (platform_repositories.json)
platform_data = read_json_file(platform_file_path)

# Git clone for URLs in model_repositories.json
print("Cloning repositories from model_repositories.json:")
clone_all_repos_in_folder(model_data, model_dir_name)

# Git clone for URLs in platform_repositories.json
print("\nCloning repositories from platform_repositories.json:")
clone_all_repos_in_folder(platform_data, platform_dir_name)

# Generate Visual Studio Code Python extension configuration
python_analysis_extraPaths = []
# Add platform repositories to the configuration
for repo_url in platform_data:
    url = repo_url.get("url")
    repo_name = extract_repo_name(url)
    if repo_name == "gemseo":
        python_analysis_extraPaths += [platform_dir_name + "/" + "gemseo/src"]
    else:
        python_analysis_extraPaths += [platform_dir_name + "/" + repo_name]
# Add model repositories to the configuration
for repo_url in model_data:
    url = repo_url.get("url")
    repo_name = extract_repo_name(url)
    python_analysis_extraPaths += [platform_dir_name + "/" + repo_name]

print("\npython_analysis_extraPaths=", python_analysis_extraPaths)

# Prepare .vscode/settings.json file
settings_json_path = f"{vscode_dir}/settings.json"
settings = {}

# Create .vscode directory if it doesn't exist
os.makedirs(vscode_dir, exist_ok=True)

# Read existing json file if exists
if os.path.exists(settings_json_path):
    try:
        with open(settings_json_path, "r") as f:
            settings = json.load(f)
    except:
        pass

settings["python.analysis.extraPaths"] = python_analysis_extraPaths
settings["git.autoRepositoryDetection"] = "subFolders"
settings["git.openRepositoryInParentFolders"] = "always"
settings["git.repositoryScanMaxDepth"] = 2
settings["python.defaultInterpreterPath"] = f"{venv_path}/bin/python"

# Generate .vscode/settings.json
with open(settings_json_path, "w") as f:
    json.dump(settings, f, indent=4)
