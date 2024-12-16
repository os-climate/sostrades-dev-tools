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
import platform
import subprocess

from constants import node_version, platform_path, sostrades_dev_tools_path
from tooling import run_command

# Function to get the NVS path depending on the operating system
def get_nvs_home():
    if platform.system() == "Windows":
        return os.environ.get("LOCALAPPDATA", "") + "/nvs"
    else:  # For Linux
        return os.path.expanduser("~/.nvs")

# Function to install NVS only on Windows
def install_nvs():
    if platform.system() == "Windows":
        nvs_home = get_nvs_home()
        if not os.path.exists(nvs_home):
            os.makedirs(nvs_home)
            # Clone the NVS repository
            clone_command = f"git clone https://github.com/jasongin/nvs {nvs_home}"
            run_command(clone_command)
            print("NVS has been installed successfully.")
        else:
            print("NVS is already installed.")
    else:
        print("NVS installation is skipped on Linux. Checking for installation...")

# Function to install and switch the Node version using NVS
def switch_node_version(node_version):
    if platform.system() == "Windows":
        nvs_home = get_nvs_home()
        nvs_cmd_path = os.path.join(nvs_home, "nvs.cmd")
        nvs_use_command = f'"{nvs_cmd_path}" use {node_version}'
        nvs_add_command = f'"{nvs_cmd_path}" add {node_version}'
        list_command = f'"{nvs_cmd_path}" list'
    else:  # For Linux
        nvs_home = get_nvs_home()
        nvs_script_path = os.path.join(nvs_home, "nvs.sh")
        nvs_use_command = f". {nvs_script_path} && nvs use {node_version}"
        nvs_add_command = f". {nvs_script_path} && nvs add {node_version}"
        list_command = f". {nvs_script_path} && nvs list"

    # Check if the Node.js version is already installed
    print(f"Checking installed versions of Node.js...")
    installed_versions = subprocess.getoutput(list_command)

    if node_version not in installed_versions:
        # If the Node.js version is not installed, add it
        run_command(nvs_add_command)
        print(f"Node.js version {node_version} has been added.")
    
    # Command to switch the Node.js version
    print(f"Switching Node.js version to {node_version}...")
    run_command(nvs_use_command)
    print(f"Switched to Node.js version {node_version}.")

# Install NVS on Windows or check for its existence on Linux
print(f"Installing NVS with Node v{node_version} ...")
install_nvs()

# Install Node.js and switch to the required version
switch_node_version(node_version)

# Prompt the user to confirm building the frontend
print("This script will install requirements and build the frontend")
confirmation = input("Do you want to continue? (Yes/No): ").strip().lower()

if confirmation == "yes":
    # Change directory to sostrade-webgui
    if os.path.exists(f"{platform_path}/sostrades-webgui"):
        os.chdir(f"{platform_path}/sostrades-webgui")
        if platform.system() == "Windows":
            nvs_home = get_nvs_home()
            nvs_cmd_path = os.path.join(nvs_home, "nvs.cmd")
            run_command(f'"{nvs_cmd_path}" use {node_version} && npm install -y')
        else:  # For Linux
            nvs_home = get_nvs_home()
            nvs_script_path = os.path.join(nvs_home, "nvs.sh")
            run_command(f". {nvs_script_path} && nvs use {node_version} && npm install")
        
        os.chdir(sostrades_dev_tools_path)
    else:
        print(f"{platform_path}/sostrades-webgui repository not found")
else:
    print("Do not forget to build the frontend later")
