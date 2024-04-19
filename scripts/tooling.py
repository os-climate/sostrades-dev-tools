"""
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
"""

import os


# Run os.system command with interruption
def run_command(cmd):
    if os.system(cmd) != 0:
        raise Exception(f"Error to execute {cmd}")

# Function to get all directories within a directory
def list_directory_paths(directory):
    # Check if the path is a directory
    if not os.path.isdir(directory):
        raise Exception(f"{directory} is not a directory.")

    # Initialize an array to store directory paths
    directory_paths = []

    # Iterate through the directories in the given directory
    for folder_name in os.listdir(directory):
        # Construct the absolute path
        absolute_path = os.path.join(directory, folder_name)
        # Check if it's a directory
        if os.path.isdir(absolute_path):
            # Check if the directory is gemseo then add \src to the path
            if os.path.basename(absolute_path) == "gemseo":
                directory_paths.append(os.path.join(absolute_path, "src"))
            # Add the absolute path to the array
            else:
                directory_paths.append(absolute_path)

    return directory_paths
