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
NodeInstallation.py is a script that install NVS with a specific version of Node settable with the parameter {node_version}
The path of the installation is set in the parameter {nvs_home}
At the end of the script it also ask if you want to run the build of sostrades-webgui
'''
import os

from constants import node_version, platform_path, sostrades_dev_tools_path
from tooling import run_command


# Function to install NVS in the directory %LOCALAPPDATA%\nvs (Doc : https://github.com/jasongin/nvs/blob/master/doc/SETUP.md)
def install_nvs():
    nvs_home = os.environ.get("LOCALAPPDATA", "") + "/nvs"
    if not os.path.exists(nvs_home):
        os.makedirs(nvs_home)
        # Clone NVS repository
        clone_command = f'git clone https://github.com/jasongin/nvs "{nvs_home}"'
        run_command(clone_command)

    # Run nvs.cmd install
    nvs_cmd_path = os.path.join(nvs_home, "nvs.cmd")
    install_command = f'"{nvs_cmd_path}" install'
    run_command(install_command)

    print("NVS has been installed successfully.")


# Function to install and switch node version with nvs
def switch_node_version(node_version):
    # Get path to nvs.cmd
    nvs_home = os.environ.get("LOCALAPPDATA", "") + "/nvs"
    nvs_cmd_path = os.path.join(nvs_home, "nvs.cmd")

    # Check if Node.js version is already installed
    list_command = f'"{nvs_cmd_path}" list'
    installed_versions = os.popen(list_command).read()

    if node_version not in installed_versions:
        # If Node.js version is not installed, add it
        add_command = f'"{nvs_cmd_path}" add {node_version}'
        run_command(add_command)
        print(f"Node.js version {node_version} has been added.")
        run_command(f'"{nvs_cmd_path}" install')
    else:
        print(f"Node.js version {node_version} is already installed.")

    # Command to switch version
    switch_command = f'"{nvs_cmd_path}" use {node_version}'
    print(f"{switch_command}")
    run_command(switch_command)

    print(f"Switched to Node.js version {node_version}.")


# Ask if user want to install NVS
print(f"Installing NVS with Node v{node_version} ...")
# Install nvs
install_nvs()
# Install nodes.js
switch_node_version(node_version)

# Ask if we build the frontend now
print("This script will install requirements and build the frontend")
confirmation = input("Do you want to continue? (Yes/No): ").strip().lower()

if confirmation == "yes":
    nvs_home = os.environ.get("LOCALAPPDATA", "") + "/nvs"
    nvs_cmd_path = os.path.join(nvs_home, "nvs.cmd")
    # Change directory to sostrade-webgui
    if os.path.exists(f"{platform_path}\sostrades-webgui"):
        os.chdir(f"{platform_path}\sostrades-webgui")
        run_command(f"{nvs_cmd_path} use {node_version} && npm install -y")
        os.chdir(sostrades_dev_tools_path)
    else:
        print(f"{platform_path}\sostrades-webgui repository not found")
else:
    print("Do not forget to build the frontend later")
