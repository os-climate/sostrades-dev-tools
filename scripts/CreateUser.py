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
a password is temporarely save in sostrades-dev-tools\platform\sostrades-webapi\sos_trades_api\secret\* it has to be delete.
After the user is created it gives some sostrade app rights to that user in de database.
The credential of your database have to be well set in sostrades-dev-tools\platform\sostrades-webapi\.flaskenv {SQL_ACCOUNT} and {SQL_PASSWORD}
'''
import os
import mysql.connector

# Variable with the path of sostrade-dev-tools
sostrades_dev_tools_path = os.path.dirname(os.path.dirname(__file__))
print(f"sostrades-dev-tools PATH : {sostrades_dev_tools_path}\n")

# Variable with the path of sostrades-venv
venv_path= f"{sostrades_dev_tools_path}\\sostrades-venv"
# Variable with the path of venv activate script
venv_script_activate_path= f"{venv_path}\\Scripts\\activate"

# Paths
platform_dir="platform"
flaskenv_file_path = f"{sostrades_dev_tools_path}\platform\sostrades-webapi\.flaskenv" 

# Run os.system command with interruption
def run_command(cmd):
 if os.system(cmd) != 0:
    raise Exception(f"Error to execute {cmd}")
 
# This function get SQL_ACCOUNT and SQL_PASSWORD value from path
def mysql_credentials_from_flaskenv_file(path):
    if os.path.exists(path):
        # Open the file in read mode
        with open( path, 'r') as f:
            # Initialize variables to store SQL_ACCOUNT and SQL_PASSWORD values
            sql_account = None
            sql_password = None
            # Read each line of the file
            for line in f:
                # Remove trailing whitespace and split the line into key and value
                key, value = line.strip().split('=')
                
                # Check if the key is SQL_ACCOUNT or SQL_PASSWORD
                if key == 'SQL_ACCOUNT':
                    sql_account = value
                elif key == 'SQL_PASSWORD':
                    sql_password = value

            return sql_account,sql_password
    else:
        print(f"{path} not found")

# Get SQL account and password
sql_account, sql_password = mysql_credentials_from_flaskenv_file(flaskenv_file_path)

if os.path.exists(venv_script_activate_path):
    if os.path.exists(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webapi"):
        # Change directory to sostrades-dev-tools\platform\sostrades-webapi
        os.chdir(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webapi")
        # Ask user informations to create 
        print("Sign up for SOSTRADES:")
        username=input("Enter username :")
        email=input("Enter email :")
        firstname=input("Enter firstname :")
        lastname=input("Enter lastname :")
        # Create user in the database with flask and save the password in sostrades-dev-tools\platform\sostrades-webapi\sos_trades_api\secret\*
        print(f"Creating user {username} ...")
        run_command(f"{venv_script_activate_path} && flask db upgrade")
        run_command(f"{venv_script_activate_path} && flask init_process")
        run_command(f"{venv_script_activate_path} && flask create_standard_user {username} {email} {firstname} {lastname} ")
    else:
        print(f"{sostrades_dev_tools_path}\\{platform_dir}\\sostrades-webapi repository not found")

    os.chdir(sostrades_dev_tools_path)
else:
   print("Virtual environment (sostrades-venv) is not installed")

# Connect to the database
db_connection = mysql.connector.connect(
    host="localhost",
    user=sql_account,
    password=sql_password,
    database="sostrades-data"
) 

if db_connection.is_connected():
    # Create a cursor to execute SQL queries
    cursor = db_connection.cursor()

    # Define the SELECT query with parameters
    query = f"SELECT id FROM `user` WHERE username = %s AND email = %s AND firstname = %s AND lastname = %s"

    # Execute the query with user-provided parameters
    cursor.execute(query, (username, email, firstname, lastname))

    # Fetch the query results
    result = cursor.fetchone()

    # Check if there are any results
    if result:
        user_id = result[0]
        insert_query = "INSERT INTO group_access_user (id, group_id, user_id, right_id) VALUES ( %s, %s, %s, %s)"
        
        # Execute the INSERT query to add the user to the group_access_user table
        cursor.execute(insert_query, ( None, 2, user_id, 5))
        db_connection.commit()

        print(f"User created successfully")
    else:
        print("No matching user found.")

    # Close the cursor and database connection
    cursor.close()
    db_connection.close()
else:
    print("Error connecting to the database.")




