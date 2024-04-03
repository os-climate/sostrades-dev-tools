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
import mysql.connector

# Variable with the path of sostrade-dev-tools
sostrades_dev_tools_path = os.path.dirname(os.path.dirname(__file__))
print(f"sostrades-dev-tools PATH : {sostrades_dev_tools_path}\n")

# Paths
platform_dir="platform"
model_dir="models"

# Run os.system command with interruption
def run_command(cmd):
 if os.system(cmd) != 0:
    raise Exception(f"Error to execute {cmd}")

# Function to install NVS in the directory %LOCALAPPDATA%\nvs (Doc : https://github.com/jasongin/nvs/blob/master/doc/SETUP.md)
def install_nvs():
    nvs_home = os.environ.get('LOCALAPPDATA', '') + '\\nvs'
    if not os.path.exists(nvs_home):
        os.makedirs(nvs_home)
        # Clone NVS repository
        clone_command = f'git clone https://github.com/jasongin/nvs "{nvs_home}"'
        run_command(clone_command)
    
    # Run nvs.cmd install
    nvs_cmd_path = os.path.join(nvs_home, 'nvs.cmd')
    install_command = f'"{nvs_cmd_path}" install'
    run_command(install_command)

    print("NVS has been installed successfully.")

# Function to install and switch node version with nvs 
def switch_node_version(node_version):
    # Get path to nvs.cmd
    nvs_home = os.environ.get('LOCALAPPDATA', '') + '\\nvs'
    nvs_cmd_path = os.path.join(nvs_home, 'nvs.cmd')
    
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

# This function will ask user and password of mysql
def get_mysql_credentials():
    confirmed = False
    while not confirmed:
        mysql_user = input("Enter the user root of mysql: ")
        mysql_password = input("Enter the user root password of mysql: ")
        print(f"Mysql user root: {mysql_user}")
        print(f"Mysql user root password: {mysql_password}")
        confirm = input("Your credentials are correct ? (Yes/No): ").strip().lower()
        
        if confirm == "yes":
            confirmed = True
            print("Credentials confirmed.")
    
    return mysql_user,mysql_password

# Ask if user want to install NVS 
print("This script will install NVS on your system.")
confirmation = input("Do you want to continue? (Yes/No): ").strip().lower()

node_version="12.16.1"
if confirmation == "yes":
    # Install nvs
    install_nvs()
    # Install nodes.js v12.16.1
    switch_node_version(node_version)
else:
    print(f"NVS installation canceled. Be careful you need node.js version {node_version} installed on your computer to run the frontend")


# Ask if we build the frontend now 
print("This script will install requirements and build the fronted")
confirmation = input("Do you want to continue? (Yes/No): ").strip().lower()

if confirmation == "yes":
    nvs_home = os.environ.get('LOCALAPPDATA', '') + '\\nvs'
    nvs_cmd_path = os.path.join(nvs_home, 'nvs.cmd')
    # Change directory to sostrade-webgui
    if  os.path.exists(f"{sostrades_dev_tools_path}\platform\sostrades-webgui"):
        os.chdir(f"{sostrades_dev_tools_path}\platform\sostrades-webgui")
        run_command(f"{nvs_cmd_path} use {node_version} && npm install -y")
        os.chdir(sostrades_dev_tools_path)
    else:
        print(f"{sostrades_dev_tools_path}\platform\sostrades-webgui repository not found")
else:
    print("Do not forget to build the frontend later")

# Ask mysql user and password credentials
mysql_user, mysql_password = get_mysql_credentials()

# Init platform\sostrades-webapi\sos_trades_api\configuration_template\configuration.json configuration file
configuration={
    "ENVIRONMENT": "DEVELOPMENT", 
    "SQL_ALCHEMY_DATABASE": { 
        "HOST" : "127.0.0.1", 
        "PORT" : 3306, 
        "USER_ENV_VAR":f"{mysql_user}", 
        "PASSWORD_ENV_VAR":f"{mysql_password}", 
        "DATABASE_NAME": "sostrades-data", 
        "SSL": False 
    }, 
    "SQLALCHEMY_TRACK_MODIFICATIONS": False, 
    "LOGGING_DATABASE": { 
        "HOST": "127.0.0.1", 
        "PORT": 3306, 
        "USER_ENV_VAR":f"{mysql_user}", 
        "PASSWORD_ENV_VAR":f"{mysql_password}", 
        "DATABASE_NAME": "sostrades-log", 
        "SSL": False 
    }, 
    "SECRET_KEY_ENV_VAR": "SECRET_KEY", 
    "JWT_TOKEN_LOCATION": "headers", 
    "JWT_ACCESS_TOKEN_EXPIRES": 18000, 
    "JWT_REFRESH_TOKEN_EXPIRES": 36000, 
    "DEFAULT_GROUP_MANAGER_ACCOUNT": "All users", 
    "CREATE_STANDARD_USER_ACCOUNT": False, 
    "LDAP_SERVER" : "", 
    "LDAP_BASE_DN" : "", 
    "LDAP_FILTER" : "", 
    "LDAP_USERNAME" : "", 
    "SMTP_SERVER" : "", 
    "SMTP_SOS_TRADES_ADDR" : "", 
    "SOS_TRADES_ENVIRONMENT" : "Local", 
    "SOS_TRADES_K8S_DNS": "", 
    "SOS_TRADES_FRONT_END_DNS": "", 
    "SOS_TRADES_ONTOLOGY_ENDPOINT": "http://127.0.0.1:5555/api/ontology", 
    "SOS_TRADES_PROCESS_REPOSITORY": ["sostrades_core.sos_processes.test"], 
    "INTERNAL_SSL_CERTIFICATE": "", 
    "SOS_TRADES_EXECUTION_STRATEGY": "subprocess", 
    "SOS_TRADES_SERVER_MODE": "mono", 
    "SOS_TRADES_DATA": "C:\\TEMP\\SOSTRADES", 
    "SOS_TRADES_REFERENCES": "C:\\TEMP\\SOSTRADES\\REFERENCES", 
    "EEB_PATH": "", 
    "SOS_TRADES_RSA": "C:\\TEMP\\SOSTRADES\\RSA", 
    "SAML_V2_METADATA_FOLDER": "" 
}

# Create configuration.json file for WebAPI
if os.path.exists(f"{sostrades_dev_tools_path}\{platform_dir}\sostrades-webapi\sos_trades_api\configuration_template"):
    if not os.path.exists(f"{sostrades_dev_tools_path}\{platform_dir}\sostrades-webapi\sos_trades_api\configuration_template\configuration.json"):
        print ("Creating configuration.json ...")
        with open(f"{sostrades_dev_tools_path}\{platform_dir}\\sostrades-webapi\sos_trades_api\configuration_template\configuration.json", "w") as f:
            json.dump(configuration, f, indent=4)
            print(f"{sostrades_dev_tools_path}\{platform_dir}\sostrades-webapi\sos_trades_api\configuration_template\configuration.json created")
    else:
        print (f"{sostrades_dev_tools_path}\{platform_dir}\sostrades-webapi\sos_trades_api\configuration_template\configuration.json already created")
else:
    print (f"{sostrades_dev_tools_path}\{platform_dir}\sostrades-webapi\sos_trades_api\configuration_template not found")

# Define the values of .flaskenv 
flask_env = {
    "FLASK_APP":"sos_trades_api/server/base_server.py",
    "FLASK_ENV":"development",
    "SOS_TRADES_SERVER_CONFIGURATION":f"{sostrades_dev_tools_path}\\platform\\sostrades-webapi\\sos_trades_api\\configuration_template\\configuration.json",
    "SOS_TRADES_REFERENCES":"C:\\Temp\\SoSTrades_persistance\\reference",
    "SOS_TRADES_DATA":"C:\\Temp\\SoSTrades_persistance",
    "EEB_PATH":"C:\\Temp\\SoSTrades_persistance\\eeb.yaml",
    "SOS_TRADES_RSA":"C:\\Temp\\SoSTrades_persistance\\rsa",
    "SQL_ACCOUNT":f"{mysql_user}",
    "SQL_PASSWORD":f"{mysql_password}", 
    "LOG_USER":f"{mysql_user}",
    "LOG_PASSWORD":f"{mysql_password}", 
    "SECRET_KEY":"ABCDEFGH12 ",
    "SAML_V2_METADATA_FOLDER":"sos_trades_api\\configuration\\saml"
    }

# File path to create
flaskenv_file_path = f"{sostrades_dev_tools_path}\platform\sostrades-webapi\.flaskenv"

# Write the values to the file
with open(flaskenv_file_path, "w") as f:
    for key, value in flask_env.items():
        f.write(f"{key}={value}\n")

print(f"{flaskenv_file_path} has been successfully created.")

# Create repository C:\TEMP\SOSTRADES,C:\TEMP\SOSTRADES\RSA, C:\TEMP\SOSTRADES\REFERENCE
if not os.path.exists("C:\\TEMP\\SOSTRADES"):
    os.makedirs("C:\\TEMP\\SOSTRADES")
    print("C:\TEMP\SOSTRADES directory created.")

if not os.path.exists("C:\\TEMP\\SOSTRADES\\RSA"):
    os.makedirs("C:\\TEMP\\SOSTRADES\\RSA")
    print("C:\TEMP\SOSTRADES\RSA directory created.")
    
if not os.path.exists("C:\\TEMP\\SOSTRADES\\REFERENCES"):
    os.makedirs("C:\\TEMP\\SOSTRADES\\REFERENCES")
    print("C:\TEMP\SOSTRADES\REFERENCES directory created.")

# Define the directory path
directory_path = "C:TEMP\SOSTRADES\RSA"

# Define the files path
private_key_path = "C:\TEMP\SOSTRADES\RSA\private_key.pem"
public_key_path = "C:\TEMP\SOSTRADES\RSA\public_key.pem"

# Create empty files
if not os.path.exists(private_key_path):
    with open(private_key_path, "w") as f:
        pass  # This just creates an empty file
    print(f"{private_key_path} have been created.")
else:
    print(f"{private_key_path} already created.")
if not os.path.exists(public_key_path):
    with open(public_key_path, "w") as f:
        pass  # This just creates an empty file
    print(f"{public_key_path} have been created.")
else:
    print(f"{public_key_path} already created.")



def create_database(host, user, password, database_name):
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password
    )

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS `{}`".format(database_name))

    # Close the cursor and connection
    cursor.close()
    conn.close()

print("Creating sostrades-data and sostrades-log databases if not exist ...")
create_database("127.0.0.1", f"{mysql_user}", f"{mysql_password}", "sostrades-data" )
create_database("127.0.0.1", f"{mysql_user}", f"{mysql_password}", "sostrades-log" )
print("FINISH")

