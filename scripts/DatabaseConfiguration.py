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

import os
import mysql.connector

# Variable with the path of sostrade-dev-tools
sostrades_dev_tools_path = os.path.dirname(os.path.dirname(__file__))
print(f"sostrades-dev-tools PATH : {sostrades_dev_tools_path}\n")

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


# Ask mysql user and password credentials
mysql_user, mysql_password = get_mysql_credentials()

print("Creating sostrades-data and sostrades-log databases if not exist ...")
create_database("127.0.0.1", f"{mysql_user}", f"{mysql_password}", "sostrades-data" )
create_database("127.0.0.1", f"{mysql_user}", f"{mysql_password}", "sostrades-log" )
print("FINISH")

