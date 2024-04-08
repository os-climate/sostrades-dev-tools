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
Configuration.py is a script that initialise files and folders needed for sostrades :
- sostrades-dev-tools\platform\sostrades-webapi\sos_trades_api\configuration_template\configuration.json
- sostrades-dev-tools\platform\sostrades-webapi\.flaskenv
- C:\TEMP\SOSTRADES\
- C:\TEMP\SOSTRADES\REFERENCES\
- C:\TEMP\SOSTRADES\RSA\
- C:\TEMP\SOSTRADES\RSA\private_key.pem
- C:\TEMP\SOSTRADES\RSA\public_key.pem
'''
import json
import os

# Variable with the path of sostrade-dev-tools
sostrades_dev_tools_path = os.path.dirname(os.path.dirname(__file__))
print(f"sostrades-dev-tools PATH : {sostrades_dev_tools_path}\n")

# Paths
platform_dir="platform"

# Init platform\sostrades-webapi\sos_trades_api\configuration_template\configuration.json configuration file
configuration={
    "ENVIRONMENT": "DEVELOPMENT", 
    "SQL_ALCHEMY_DATABASE": { 
        "HOST" : "127.0.0.1", 
        "PORT" : 3306, 
        "USER_ENV_VAR":"SQL_ACCOUNT", 
        "PASSWORD_ENV_VAR":"SQL_PASSWORD", 
        "DATABASE_NAME": "sostrades-data", 
        "SSL": False 
    }, 
    "SQLALCHEMY_TRACK_MODIFICATIONS": False, 
    "LOGGING_DATABASE": { 
        "HOST": "127.0.0.1", 
        "PORT": 3306, 
        "USER_ENV_VAR":"LOG_USER", 
        "PASSWORD_ENV_VAR":"LOG_PASSWORD",
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
    "SQL_ACCOUNT":"user",
    "SQL_PASSWORD":"password",
    "LOG_USER":"user",
    "LOG_PASSWORD":"password", 
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