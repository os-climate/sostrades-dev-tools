# SoSTrades platform installation

This section is dedicated to install locally either SoSTrades platform or SoSTrades as a library. 

> Feedback is a gift: please note that these installation procedures are still in beta phase. You can contribute to this documentation, give feedbacks and raise a [github issue](https://github.com/os-climate/sostrades-dev-tools/issues).

Please note that supported operating systems are standard Linux-based systems, macOS systems

It contains script facilities to clone repositories, and create virtual environments for sostrades project.

The scripts clone the repositories in the correct folder for the rest of the scripts to work properly, as explained in Installation section.
The expected folder organisation is the following :

```
├── sostrades-dev-tools
│   ├── dockers
│   │   └── docker related files
│   ├── models
│   │   ├── sostrades-optimization-plugins
│   │   ├── witness-core
│   │   ├── witness-energy
│   │   └── Other model repositories
│   ├── platform
│   │   ├── sostrades-core
│   │   ├── sostrades-webapi
│   │   ├── sostrades-webgui
│   │   └── sostrades-ontology
└── other files...
```


You are then free to change branches, pull changes, clone new model repositories and use scripts at your convenience.

## 1. Choose your installation

Depending on your needs, different environment installations are proposed. A common setup is mandatory whatever the installation you need to perform.

Please consult the diagram below to determine which paragraph you should read.

![](images/choose_your_env.png) 


## 2. Common Setup

The objective of this section is to get the environment and all folders properly organized on your local computer to start the installation.

### 2.2 Setup prerequisites

#### 2.2.1 Common prerequisites

python version 3.9.x

git

*Note1:* if you have a more recent version of python installed, the `python` command is probably bound to it, resulting in a version issue with the installation scripts. If you installed python 3.9 on top, then you need to use the command `python3.9` hereafter.
Make sure the requirements are properly installed with `python3.9 -m pip install mysql mysql-connector-python==8.3.0`. If the issue persists, you can replace the `python3.9` command by the full path to the correct python executable (3.9.x) in your filesystem.

You can verify the installed version with
```bash
python3 --version
python3.9 --version
git --version
```

To install python and git you can run this following commands :

1. Update the package list: 
    ```bash
    apt update
    ```
    
2. Install Python 3.9 and essential tools:  
    ```bash
    apt install -y software-properties-common
    add-apt-repository -y ppa:deadsnakes/ppa
    apt update
    apt install -y python3.9 python3.9-venv python3.9-distutils python3-pip python3.9-dev
    python3.9 --version
    ``` 
3. Install git:
    ```bash
    apt install -y git
    ```

#### 2.2.2 Linux packages Installation

Some specific pre-requisites are needed:
```bash
apt install -y libmysqlclient-dev build-essential libldap2-dev libsasl2-dev python-dev-is-python3 libssl-dev vim curl tmux
apt install -y pkg-config libmysqlclient-dev
```

#### 2.2.3 Mac OS Installation

Please note that install has not been tested on personal Mac OS laptops, but could be different depending on the MacOS version used. Do not hesitate to contribute to this documentation, give feedbacks and raise an [ github issue](https://github.com/os-climate/sostrades-dev-tools/issues).

If you want to be sure of having a working installation without OS version problems, use docker 

### 2.3 Clone code and tools

1. Clone this repository in root directory and position to last version
```bash
git clone https://github.com/os-climate/sostrades-dev-tools
(For SSH : git clone git@github.com:os-climate/sostrades-dev-tools.git)
 
cd sostrades-dev-tools
# Position to latest tag (ex if v4.1.3 is the latest version)
git checkout v4.1.3
```

*Important:* the root directory name should not contain spaces, and it should be stored in a location where the scripts can write new files (beware of installation in remote filesystems). 
If these conditions are not met, the `PrepareVenv` script might fail and a custom installation of the SoSTrades requirements might be necessary. Try installing in a local filesystem location without spaces.

2. If needed configure model repositories : edit the `model_repositories.json` and `platform_repositories.json` according to what repositories you want. The provided `model_repositories.json` file includes the WITNESS model repositories, as well as the optimization plugins repository required to run WITNESS optimizations :

```json
[
    {
        "url": "https://github.com/os-climate/sostrades-optimization-plugins.git",
        "branch": "validation"
    },{
        "url": "https://github.com/os-climate/witness-core.git",
        "branch": "validation"
    },
    {
        "url": "https://github.com/os-climate/witness-energy.git",
        "branch": "validation"
    }
]
```
3. Launch the `PrepareDevEnv` script
This script will prepare the local working directory as follow :

```
├── sostrades-dev-tools
│   ├── dockers
│   │   └── docker related files
│   ├── docs
│   ├── scripts
│   ├── models
│   │   ├── sostrades-optimization-plugins
│   │   ├── witness-core
│   │   ├── witness-energy
│   │   └── Other model repositories
│   ├── platform
│   │   ├── gemseo
│   │   ├── sostrades-core
│   │   ├── sostrades-webapi
│   │   ├── sostrades-webgui
│   │   └── sostrades-ontology
└── other files...
```

```bash
python3.9 scripts/PrepareDevEnv.py
```

## 3. Local Model Development Env Installation

The objective is to have a working local dev environment based on a venv.

### 3.1 Prerequisites

Follow [common setup section](#2-common-setup)

### 3.2 Prepare venv
```bash
python3.9 scripts/PrepareVenv.py
```


### 3.3 Run venv

To run .venv with all requirements installed, run the following command from your `sostrade-dev-tools` folder:

```bash
source /sostrades-dev-tools/.venv/bin/activate
```

## 4. Local platform Linux

It is recommended to follow step by step the installation below, because if you skip a script the next one may not work properly. Every script is stored in the folder `sostrades-dev-tools\scripts\`

### 5.1 Prerequisites

The repository sostrades-dev-tools and all scripts need the following prerequisites:
> - Follow [common setup section](#2-common-setup)
> - Follow [local model development env installation section](#3-local-model-development-env-installation)

### 5.2 Run install scripts


First you need to run `Configuration.py` to create folder and files needed to run SoSTrades:

```bash
python3.9 scripts/Configuration.py
```

Before run `NodeInstallation.py`, you need to install NVS witch allow to manage Node and its versions
```bash
git clone https://github.com/jasongin/nvs ~/.nvs
echo 'export NVS_HOME="$HOME/.nvs"' >> ~/.bashrc
echo '[ -s "$NVS_HOME/nvs.sh" ] && . "$NVS_HOME/nvs.sh"' >> ~/.bashrc
source ~/.bashrc
```

Then run `NodeInstallation.py` to install the good version of Node and at the end of the script it will ask you if you want to build the webgui:

```bash
python3.9 scripts/NodeInstallation.py
```

To create an user to access to SoSTrades platform run `CreateUser.py`:

```bash
python3.9 scripts/CreateUser.py
```
Important: the `CreateUser.py` script will ask you to input some information (user, name, last name and e-mail). Leaving any of these fields empty will result in the script crashing, at least a character is required. 

<!-- If you want to update Ontology execute the script `UpdateOntology.py`. This script could take more than 15mn it depends on the number of repository you have.

```bash
python3.9 scripts/UpdateOntology.py
``` -->

### 5.3 Start SoSTrades platform 

Finally run the script `Linux-StartSOSTrades.py` to launch SoSTrades :

```bash
python3.9 scripts/Linux-StartSOSTrades.py
```

When the last script is running you can go to [http://localhost:4200](http://localhost:4200) with your web browser and connect with your credentials just created before.


Instructions for user:
- Navigate between panes using `Ctrl-b` and arrow keys (Up, Down, Left, Right).
- Close a single pane by typing `exit` in it.
- Detach from the session without closing it: `Ctrl-b d`.
- Close the entire session: `Ctrl-b :` and type `kill-session`.

### 5.4 Pull repositories

If you need to pull all your repositories (both platform and models) you can execute the script `PullRepositories.py` : 

```
python scripts\PullRepositories.py
```

## 6. Scripts explanation
> - PrepareDevEnv.py : script to download all model repositories from model_repositories.json and platform repositories from platform_repositories.json with git clone command. Repositories are cloned in sostrades-dev-tool\models and sostrades-dev-tool\platform. The script also creates a `sostrades-dev-tools\.vscode\setting.json` file with extraPaths according to the repository cloned,

> - PrepareVenv.py: script to install a venv in the folder `sostrades-dev-tools\.venv\` with the python 3.9 and install all requirements of SoSTrades,

> - Configuration.py: script to create files and folders needed by SoSTrades
>> - `sostrades-dev-tools\platform\sostrades-webapi\sos_trades_api\configuration_template\configuration.json`
>> - `sostrades-dev-tools\platform\sostrades-webapi\.flaskenv`
>> - `sostrades-dev-tools\data\REFERENCES\`
>> - `sostrades-dev-tools\data\RSA\private_key.pem`
>> - `sostrades-dev-tools\data\RSA\public_key.pem`

> - `NodeInstallation.py`: script to install a NVS (Node Version Switcher) and also install a version of Node with NVS. In addition it is possible to build sostrades-webgui

> - `CreateUser.py` : script that creates an user in SoSTrades with the command `flask create_standard_user`. When the user is created, a password is temporarily saved in `sostrades-dev-tools\platform\sostrades-webapi\sos_trades_api\secret\*`. Once stored, the password has to be deleted. Some SoSTrades app rights are granted in the database with flask command.

> - `UpdateOntology.py` script will execute with your `.venv` the command `python sos_ontology\core\script\createSoSOntologyFromCode.py`in `sostrades-ontology` folder to update ontology with all your repositories

> - `StartSOSTrades.py` : script that run api server, ontology server, and webgui server with venv and node
> - `Linux-StartSOSTrades.py` : same as before - use tmux to slip screen

> - `FullInstall.py` : script for a direct full install. Execute like `python scripts\FullInstall.py`
