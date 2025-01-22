# SoSTrades Platform Installation

This section is dedicated to install SoSTrades platform locally.

> You can contribute to this documentation, give feedbacks and raise a [github issue](https://github.com/os-climate/sostrades-dev-tools/issues).

Please note that supported operating systems are standard Linux-based systems, macOS systems, and Windows.

It contains script facilities to clone repositories, and create virtual environment for SoSTrades project.

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
Please follow [add a new repository](add-repository.md) page to add new repositories.

## 1. Choose your installation

Two installation are available. This page documents the "standard" way of installation.
* [common setup](#2-common-setup) Covers prerequisites for installation
* [Local Model Development Environment Installation](#3-local-model-development-environment-installation) covers installation of SoSTrades as a library enabling model development
* [Local Platform Installation](#4-local-platform) covers local platform installation to have a working local platform for GUI interaction and visualization

If needed, you may install a docker running platform, by following [common setup section](#2-common-setup) and then [Docker installation](docker_installation.md).

## 2. Common Setup

This section outlines how to organize your environment and folders for installation.

### 2.1 Setup Prerequisites
If a prior SoSTrades installation relying on `PYTHONPATH` exists, it must be disabled to avoid conflicts. To do this:

- Open the Windows Control Panel and delete the `PYTHONPATH` environment variable.

#### 2.1.1 Common Prerequisites

> - 10 GB of disk space.
> - Python version 3.9.x (latest pre-built [here](https://www.python.org/downloads/release/python-3913/)).
> - Git.
> - NVS on Linux

*Note:* If a different Python version is installed, the `python` command is probably bound to it, resulting in a version conflict. Use the full path to the Python 3.9 executable (3.9.x) in your filesystem to call the various scripts.
On Windows installation, python is typically installed in `C:/Users/<User>/AppData/Local/Programs/Python/Python39/python.exe`


Verify versions:

```bash
<path_to_python_3.9_executable> --version
git --version
```

#### 2.1.2 Linux Packages Installation

Install Python and Git with:

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

3. Install Git:
    ```bash
    apt install -y git
    ```

Install additional prerequisites. Use your package manager to install them (example with apt):
```bash
sudo apt install -y pkg-config libmysqlclient-dev build-essential libldap2-dev libsasl2-dev python-dev-is-python3 libssl-dev curl tmux
```

Install Node Version Switcher (NVS):
```bash
git clone https://github.com/jasongin/nvs ~/.nvs
echo 'export NVS_HOME="$HOME/.nvs"' >> ~/.bashrc
echo '[ -s "$NVS_HOME/nvs.sh" ] && . "$NVS_HOME/nvs.sh"' >> ~/.bashrc
source ~/.bashrc
```

#### 2.1.3 macOS Installation

While untested on personal macOS laptops, the installation process should follow Linux instructions. Contributions to improve this documentation are welcome via [GitHub issues](https://github.com/os-climate/sostrades-dev-tools/issues).

### 2.2 Clone Code and Tools

All development environments are built from a dedicated directory initiated with this repository. This directory will be used as root and will contains all the others necessary repositories from OS-Climate. This root directory contains VSCode tasks and launch docker-compose files. This allows to launch SoSTrades in docker containers and to debug webapi servers directly from thus container in VS Code. From the repository a script is available to clone all the repositories to prepare the development environment.

1. Clone this repository in root directory
```bash
git clone https://github.com/os-climate/sostrades-dev-tools
(For SSH: git clone git@github.com:os-climate/sostrades-dev-tools.git)

cd sostrades-dev-tools
```

Ensure the root directory:

- Has no spaces in its name.
- Is writable by the scripts.

If conditions are unmet, the `PrepareVenv` script may fail.

2. If needed configure model repositories:
Edit `model_repositories.json` and `platform_repositories.json` to specify repositories. Example:

```json
[
    {
        "url": "https://github.com/os-climate/sostrades-optimization-plugins.git",
        "branch": "validation"
    },
    {
        "url": "https://github.com/os-climate/witness-core.git",
        "branch": "validation"
    },
    {
        "url": "https://github.com/os-climate/witness-energy.git",
        "branch": "validation"
    }
]
```

3. Launch `PrepareDevEnv`:
This scripts clones the repositories and creates configuration files for VS Code.

```bash
<path_to_python_3.9_executable> scripts/PrepareDevEnv.py
```

## 3. Local Model Development Environment Installation

This setup enables local development with a pre-configured virtual environment and VS Code workspace.

### 3.1 Prerequisites

Follow the [Common Setup section](#2-common-setup).

### 3.2 Prepare Virtual Environment
```bash
<path_to_python_3.9_executable> scripts/PrepareVenv.py
```

Some usage tips for Visual Studio code and venv are available in [visual studio code and venv tips](vs_code_venv_tips.md) and are recommended if you plan to develop models.

## 4. Local Platform

SoSTrades can run without Docker by following these steps. Every script is stored in the folder `sostrades-dev-tools/scripts/`

### 4.1 Prerequisites

Follow:
- [Common Setup](#2-common-setup)
- [Local Model Development Environment Installation](#3-local-model-development-environment-installation)

### 4.2 Run Installation Scripts

1. Run `Configuration.py`:
    ```bash
    <path_to_python_3.9_executable> scripts/Configuration.py
    ```

2. Run `NodeInstallation.py` to install NVS and Node. At the end of the script it will ask you if you want to build the webgui:
    ```bash
    <path_to_python_3.9_executable> scripts/NodeInstallation.py
    ```

3. Create a user with `CreateUser.py`:
    ```bash
    <path_to_python_3.9_executable> scripts/CreateUser.py
    ```
Important: the `CreateUser.py` script will ask you to input some information (user, name, last name and e-mail). Leaving any of these fields empty will result in the script crashing, at least a character is required. 

4. (optional) Update Ontology. This script could take more than 15mn it depends on the number of repository you have:
    ```bash
    <path_to_python_3.9_executable> scripts/UpdateOntology.py
    ```

### 4.3 Start SoSTrades Platform

#### Windows
```bash
<path_to_python_3.9_executable> scripts/StartSOSTrades.py
```

#### Linux
```bash
bash scripts/Linux-StartSOSTrades.sh
```

Instructions for user:
- Navigate between panes using `Ctrl-b` and arrow keys (Up, Down, Left, Right).
- Close a single pane by typing `exit` in it.
- Detach from the session without closing it: `Ctrl-b d`.
- Close the entire session: `Ctrl-b :` and type `kill-session`.

#### Connecting
When the last script is running you can go to [http://localhost:4200](http://localhost:4200) with your web browser and connect with your credentials just created before. Make sure opened terminals show no obvious errors.

The user is the one entered previously and the password is temporarily saved in `sostrades-dev-tools/platform/sostrades-webapi/sos_trades_api/secret/*`.


### 4.4 Pull repositories

If you need to pull all your repositories (both platform and models) you can execute the script `PullRepositories.py` : 

```bash
<path_to_python_3.9_executable> scripts/PullRepositories.py
```

## 5. Script Descriptions
- PrepareDevEnv.py : script to download all model repositories from model_repositories.json and platform repositories from platform_repositories.json with git clone command. Repositories are cloned in sostrades-dev-tool/models and sostrades-dev-tool/platform. The script also creates a `sostrades-dev-tools/.vscode/setting.json` file with extraPaths according to the repository cloned,
- PrepareVenv.py: script to install a venv in the folder `sostrades-dev-tools/.venv` with the python 3.9 and install all requirements of SoSTrades,
- Configuration.py: script to create files and folders needed by SoSTrades
> - `sostrades-dev-tools/platform/sostrades-webapi/sos_trades_api/configuration_template/configuration.json`
> - `sostrades-dev-tools/platform/sostrades-webapi/.flaskenv`
> - `sostrades-dev-tools/data/REFERENCES/`
> - `sostrades-dev-tools/data/RSA/private_key.pem`
> - `sostrades-dev-tools/data/RSA/public_key.pem`
- `NodeInstallation.py`: script to install a NVS (Node Version Switcher) and also install a version of Node with NVS. In addition it is possible to build sostrades-webgui
- `CreateUser.py` : script that creates an user in SoSTrades with the command `flask create_standard_user`. When the user is created, a password is temporarily saved in `sostrades-dev-tools/platform/sostrades-webapi/sos_trades_api/secret/*`. Once stored, the password has to be deleted. Some SoSTrades app rights are granted in the database with flask command.
- `UpdateOntology.py` script will execute with your `.venv` the command `python sos_ontology/core/script/createSoSOntologyFromCode.py`in `sostrades-ontology` folder to update ontology with all your repositories
- `StartSOSTrades.py` : script that run api server, ontology server, and webgui server with venv and node
- `Linux-StartSOSTrades.py` : same as before - use tmux to split screen
- `FullInstall.py` : script for a direct full install. Execute like `python scripts/FullInstall.py`
