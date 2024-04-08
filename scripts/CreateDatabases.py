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
CreateDatabases.py is a script that create sostrades-data and sostrades-log tables in your own database.
SQL_ACCOUNT and SQL_PASSWORD have to be defined with your own database credentials
in the file sostrades-dev-tools\platform\sostrades-webapi\.flaskenv
'''
import os
import mysql.connector

# Variable with the path of sostrade-dev-tools
sostrades_dev_tools_path = os.path.dirname(os.path.dirname(__file__))
print(f"sostrades-dev-tools PATH : {sostrades_dev_tools_path}\n")
# .flaskenv path
flaskenv_file_path = f"{sostrades_dev_tools_path}\platform\sostrades-webapi\.flaskenv" 

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

def create_database(host, user, password, database_name):
    # Connect to MySQL server
    conn = mysql.connector.connect(
        host=host,
        user=sql_account,
        password=sql_password
    )

    # Create a cursor to execute SQL queries
    cursor = conn.cursor()

    # Create the database
    cursor.execute("CREATE DATABASE IF NOT EXISTS `{}`".format(database_name))

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Get SQL account and password
sql_account, sql_password = mysql_credentials_from_flaskenv_file(flaskenv_file_path)

print("Creating sostrades-data and sostrades-log databases if not exist ...")
create_database("127.0.0.1", f"{sql_account}", f"{sql_password}", "sostrades-data" )
create_database("127.0.0.1", f"{sql_account}", f"{sql_password}", "sostrades-log" )
print("FINISH")

