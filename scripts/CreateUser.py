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
CreateUser.py is a script that create an user in sostrades with the command "flask create_standard_user" when the user is created 
a password is temporarely save in sostrades-dev-tools/platform/sostrades-webapi/sos_trades_api/secret/* it has to be delete.
After the user is created it gives some sostrade app rights to that user in de database.
The credential of your database have to be well set in sostrades-dev-tools/platform/sostrades-webapi/.flaskenv {SQL_ACCOUNT} and {SQL_PASSWORD}
'''
import os

from constants import (
    platform_path,
    venv_script_activate_path,
    venv_script_activate_command,
    sostrades_dev_tools_path,
)
from tooling import run_command

if not os.path.exists(venv_script_activate_path):
    raise Exception("Virtual environment (.venv) is not installed")

if not os.path.exists(f"{platform_path}/sostrades-webapi"):
    raise Exception(f"{platform_path}/sostrades-webapi repository not found")

# Change directory to sostrades-dev-tools/platform/sostrades-webapi
os.chdir(f"{platform_path}/sostrades-webapi")
# Ask user informations to create
print("Sign up for SOSTRADES:")
username = input("Enter username :")
email = input("Enter email :")
firstname = input("Enter firstname :")
lastname = input("Enter lastname :")

if len(email) == 0:
    raise Exception("Can't use empty email")

# Create user in the database with flask and save the password in sostrades-dev-tools/platform/sostrades-webapi/sos_trades_api/secret/*
print(f"Creating user {username} ...")
run_command(f"{venv_script_activate_command} && flask db upgrade")
run_command(f"{venv_script_activate_command} && flask init_process")
run_command(
    f"{venv_script_activate_command} && flask create_standard_user {username} {email} {firstname} {lastname} \
    && flask set_user_access_group {username} SoSTrades_Dev && flask change_user_profile {username} -p \"Study manager\""
)
print(f"User created successfully")

os.chdir(sostrades_dev_tools_path)
