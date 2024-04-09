# Windows installation

It is possible to run SoSTrades on windows without installing docker by running some scripts. It is recommended to follow step by step the installation bellow, because if you skip a script the next could not working. All script will be found in the folder `sostrades-dev-tools\script\`

## 1. Prerequisites

sostrades-dev-tool need : 
> - Python version 3.9 : https://www.python.org/downloads/release/python-3913/  
> - Git : https://git-scm.com/download/win  
> - Python module "mysql.connector" : `pip install mysql-connector-python`

## 2. Scripts explaination 

> - PrepareDevEnv.py : script to download all platform and model repository from model_repositories.json and platform_repositories.json file with git clone command. And the repository is clonned in sostrades-dev-tool\model and sostrades-dev-tool\platform. Ans the script also create a sostrades-dev-tool\.vscode\setting.json file with the value of python.analysis.extraPaths according to the reository cloned

> - PrepareVenv.py: script to install a venv in the folder `sostrades-dev-tools\sostrades-venv\` with the python 3.9 and install all requirements of sostrades

> - Configuration.py: script to create files and folders needed by SoSTrades
>> - sostrades-dev-tools\platform\sostrades-webapi\sos_trades_api\configuration_template\configuration.json
>> - sostrades-dev-tools\platform\sostrades-webapi\.flaskenv
>> - C:\TEMP\SOSTRADES\
>> - C:\TEMP\SOSTRADES\REFERENCES\
>> - C:\TEMP\SOSTRADES\RSA\
>> - C:\TEMP\SOSTRADES\RSA\private_key.pem
>> - C:\TEMP\SOSTRADES\RSA\public_key.pem

> - NodeInstallation.py: script to install a NVS and also install a version of Node with nvs. In addition it is possible to build sostrades-webgui 

> - EditFlaskenv.py: script to modify the values SQL_ACCOUNT, SQL_PASSWORD, LOG_USER, LOG_PASSWORD in the file sostrades-dev-tools\platform\sostrades-webapi\.flaskenv 

> - CreateDatabases.py : script that create sostrades-data and sostrades-log tables in database.

> - CreateUser.py : script that create an user in sostrades with the command "flask create_standard_user" when the user is created 
a password is temporarely save in sostrades-dev-tools\platform\sostrades-webapi\sos_trades_api\secret\* it has to be delete. After the user is created it gives some sostrade app rights to that user in de database.

> - StartSOSTrades.py : script that run api server, ontology server, and webgui server with venv and node

## 3. Install Mysql

SoSTrades need a database with 2 tables "sostrades-data" and "sostrades-log". No script is written to install MYSQL yet, so it has to be install manually. First download [mysql-installer-community](https://dev.mysql.com/get/archives/mysql-installer/mysql-installer-community-8.0.32.0.msi). Launch "mysql-installer-community-8.0.32.0.msi" from the previous file downloaded. If you have the following screen it means you already have some product of mysql, just cancel this first windows and confirm.
![](images/Mysql_Cancel.png) 
You will get this screen. Click on Add button and select **MySQL Server 5.7.44 - x 64** you can also add MySQL WorkBench if wanted
![](images/Mysql_add.png) 
![](images/Mysql_5.7.png)
Once the MySQL Server is selected click on Next then exectute on the next screen. Let everything by default until to get the screend asking you to enter the password. Enter you password twice and click next to complete all the installation of MySQL.
![](images/Mysql_credential.png)
Keep the password of root user. It will be asking again later in the sostrades installation.

## 4. Run scripts

Clone the repository sostrades-dev-tools to get the installation scripts
```
git clone https://github.com/os-climate/sostrades-dev-tools.git
```
Then run PrepareDevEnv.py from `sostrades-dev-tools` folder to clone all models and platform repository needed:
```
python scripts\PrepareDevEnv.py
```
Then run PrepareVenv.py to install venv named sostrades-venv:
```
python scripts\PrepareVenv.py
```
Then run Configuration.py to create folder and files needed to run SoSTrades:
```
python scripts\Configuration.py
```
Then run NodeInstallation.py to install NVS with the good version of Node at the end of the script it will ask you if you want to build the webgui:
```
python scripts\NodeInstallation.py 
```
Then run script is EditFlaskenv.py to modify the .flaskenv file with your SQL credentials (user=root and the password is the same in the MySQL installation section):
```
python scripts\EditFlaskenv.py
```
To create "sostrades-data" and "sostrades-log" tables run CreateDatabases.py:
```
python scripts\CreateDatabases.py
```
To create an user to access to SoSTrades platform run CreateUser.py:
```
python scripts\CreateUser.py
```
Finally run the script StartSOSTrades.py to launch SoSTrades :
```
python scripts\CreatStartSOSTradeseUser.py
```
When the last script is running you can go to [http://127.0.0.1:4200](http://127.0.0.1:4200) with your web browser and connect with your credentials just created before.

## 5. Run venv

To run sostrades-venv with all requierements installed run the following command from you `sostrade-dev-tools` folder:
```
sostrades-venv\Scripts\activate
```
