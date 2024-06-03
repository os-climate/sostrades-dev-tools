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
EditFlaskenv.py is a script that ask the SQL_ACCOUNT and SQL_PASSWORD and modify it 
in sostrades-dev-tools/platform/sostrades-webapi/.flaskenv
'''
import os

from constants import sostrades_dev_tools_path

# File path to edit
flaskenv_file_path = f"{sostrades_dev_tools_path}/platform/sostrades-webapi/.flaskenv"


def modify_flaskenv_file(flaskenv_file):
    # Initialise temp .flaskenv file
    temp_file = []
    # Ask SQL account and SQL password
    sql_account = input("Please provide your SQL account: ")
    sql_password = input("Please provide your SQL password: ")
    # Modify the values with the sql account and password provided
    with open(flaskenv_file, "r") as f:
        for line in f:
            # Remove trailing whitespace and split the line into key and value
            key, value = line.strip().split("=")
            # Check each line of the file to modify
            if key == "SQL_ACCOUNT":
                temp_file += [f"{key}={sql_account}"]
            elif key == "SQL_PASSWORD":
                temp_file += [f"{key}={sql_password}"]
            elif key == "LOG_USER":
                temp_file += [f"{key}={sql_account}"]
            elif key == "LOG_PASSWORD":
                temp_file += [f"{key}={sql_password}"]
            else:
                temp_file += [f"{key}={value}"]
    print("Modified values of .flaskenv file :")
    for line in temp_file:
        print(line)
    return temp_file


# Check if .flaskenv exist
if not os.path.exists(flaskenv_file_path):
    raise (f"{flaskenv_file_path} not found")

# Read the file {flaskenv_file_path}
with open(flaskenv_file_path, "r") as f:
    # Print current value of .flaskenv file
    print("Current values of .flaskenv file :")
    for line in f:
        print(line.strip())

# Ask new values to change in .flaskenv file
confirmed = False
while not confirmed:
    file = modify_flaskenv_file(flaskenv_file_path)
    confirm = input("Your credentials are correct ? (Yes/No): ").strip().lower()
    if confirm == "yes":
        confirmed = True
        print("Credentials confirmed.")

# Replace the new values of .flaskenv with {file}
with open(flaskenv_file_path, "w") as f:
    for element in file:
        f.write(str(element + "\n"))

print(f"{flaskenv_file_path} modified.")
