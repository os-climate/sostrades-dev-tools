# SoSTrades Platform Installation

This section is dedicated to installing the SoSTrades platform locally.

> You can contribute to this documentation, give feedback, and raise a [GitHub issue](https://github.com/os-climate/sostrades-dev-tools/issues).

Please note that supported operating systems are standard Linux-based systems, macOS systems, and Windows.

It contains script facilities to clone repositories and create a virtual environment for the SoSTrades project.

The expected folder organization is the following:

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

You are then free to change branches, pull changes, clone new model repositories, and use scripts at your convenience.
Please follow the [add a new repository](add-repository.md) page to add new repositories.

## 1. Choose Your Installation

Two installations are available. This page documents the "standard" way of installation.
* [Common Setup](#2-common-setup) covers prerequisites for installation.
* [Local Model Development Environment Installation](#3-local-model-development-environment-installation) covers the installation of SoSTrades as a library enabling model development.
* [Local Platform Installation](#4-local-platform) covers local platform installation to have a working local platform for GUI interaction and visualization.

If needed, you may install a docker running platform by following the [Common Setup section](#2-common-setup) and then [Docker installation](docker_installation.md).

## 2. Common Setup

This section outlines how to organize your environment and folders for installation.

### 2.1 Setup Prerequisites
If a prior SoSTrades installation relying on `PYTHONPATH` exists, it must be disabled to avoid conflicts. To do this:

- Open the Windows Control Panel and delete the `PYTHONPATH` environment variable.

#### 2.1.1 Common Prerequisites

> - 10 GB of disk space.
> - Any version of Python installed
> - pip module
> - Git.
> - NVS on Linux

Verify prerequisites:

```bash
python --version
python -m pip --version
git --version
```

#### 2.1.2 Linux Packages Installation

Install Git and additional prerequisites:

1. Update the package list:
    ```bash
    apt update
    ```

2. Install Git:
    ```bash
    apt install -y git
    ```

3. Install additional prerequisites. Use your package manager to install them (example with apt):
    ```bash
    sudo apt install -y pkg-config libmysqlclient-dev libsqlite3-dev build-essential libldap2-dev libsasl2-dev python-dev-is-python3 libssl-dev curl tmux
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

All development environments are built from a dedicated directory initiated with this repository. This directory will be used as root and will contain all the other necessary repositories from OS-Climate. This root directory contains VSCode tasks and launch docker-compose files. This allows launching SoSTrades in docker containers and debugging webapi servers directly from the container in VS Code. From the repository, a script is available to clone all the repositories to prepare the development environment.

1. Clone this repository in the root directory
```bash
git clone https://github.com/os-climate/sostrades-dev-tools
(For SSH: git clone git@github.com:os-climate/sostrades-dev-tools.git)

cd sostrades-dev-tools
```

Ensure the root directory:

- Has no spaces in its name.
- Is writable by the scripts.

If conditions are unmet, the `PrepareVenv` script may fail.

2. If needed, configure model repositories:
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
This script clones the repositories and creates configuration files for VS Code.

```bash
python scripts/PrepareDevEnv.py
```

## 3. Local Model Development Environment Installation

This setup enables local development with a pre-configured virtual environment and VS Code workspace.

### 3.1 Prerequisites

Follow the [Common Setup section](#2-common-setup).

### 3.2 Prepare Virtual Environment
```bash
python scripts/PrepareVenv.py
```

Some usage tips for Visual Studio Code and venv are available in [Visual Studio Code and Venv Tips](vs_code_venv_tips.md) and are recommended if you plan to develop models.
If you encounter an issue with the "uv" command, make sure your PATH variable includes the "Scripts" folder of your python installation. Typically, you should add `C:\Users\<username>\AppData\Local\Programs\Python\Python<your_python_version>\Scripts` to your PATH environment variable.

## 4. Local Platform

SoSTrades can run without Docker by following these steps. Every script is stored in the folder `sostrades-dev-tools/scripts/`

### 4.1 Prerequisites

Follow:
- [Common Setup](#2-common-setup)
- [Local Model Development Environment Installation](#3-local-model-development-environment-installation)

### 4.2 Run Installation Scripts

1. Run `Configuration.py`:
    ```bash
    python scripts/Configuration.py
    ```

2. Run `NodeInstallation.py` to install NVS and Node. At the end of the script, it will ask you if you want to build the webgui:
    ```bash
    python scripts/NodeInstallation.py
    ```

3. Create a user with `CreateUser.py`:
    ```bash
    python scripts/CreateUser.py
    ```
Important: the `CreateUser.py` script will ask you to input some information (user, name, last name, and e-mail). Leaving any of these fields empty will result in the script crashing; at least a character is required. 

4. (optional) Update Ontology. This script could take more than 15 minutes; it depends on the number of repositories you have:
    ```bash
    python scripts/UpdateOntology.py
    ```

### 4.3 Start SoSTrades Platform

#### Windows
```bash
python scripts/StartSOSTrades.py
```

#### Linux
```bash
bash scripts/Linux-StartSOSTrades.sh
```

Instructions for the user:
- Navigate between panes using `Ctrl-b` and arrow keys (Up, Down, Left, Right).
- Close a single pane by typing `exit` in it.
- Detach from the session without closing it: `Ctrl-b d`.
- Close the entire session: `Ctrl-b :` and type `kill-session`.

#### Connecting
When the last script is running, you can go to [http://localhost:4200](http://localhost:4200) with your web browser and connect with your credentials just created before. Make sure opened terminals show no obvious errors.

The user is the one entered previously, and the password is temporarily saved in `sostrades-dev-tools/platform/sostrades-webapi/sos_trades_api/secret/*`.

### 4.4 Pull Repositories

If you need to pull all your repositories (both platform and models), you can execute the script `PullRepositories.py`: 

```bash
python scripts/PullRepositories.py
```

## 5. Troubleshooting

### Common Issues

#### Issue: `PYTHONPATH` Conflicts
If a prior SoSTrades installation relying on `PYTHONPATH` exists, it must be disabled to avoid conflicts. To do this:
- Open the Windows Control Panel and delete the `PYTHONPATH` environment variable.

#### Issue: Virtual Environment Setup Fails
Ensure the root directory:
- Has no spaces in its name.
- Is writable by the scripts.

If conditions are unmet, the `PrepareVenv` script may fail.

### Additional Help
For further assistance, please raise a [GitHub issue](https://github.com/os-climate/sostrades-dev-tools/issues).

## 6. Script Descriptions
- `PrepareDevEnv.py`: script to download all model repositories from `model_repositories.json` and platform repositories from `platform_repositories.json` with the `git clone` command. Repositories are cloned in `sostrades-dev-tool/models` and `sostrades-dev-tool/platform`. The script also creates a `sostrades-dev-tools/.vscode/setting.json` file with extraPaths according to the repository cloned.
- `PrepareVenv.py`: script to install a venv in the folder `sostrades-dev-tools/.venv` with Python 3.12 and install all requirements of SoSTrades.
- `Configuration.py`: script to create files and folders needed by SoSTrades:
  - `sostrades-dev-tools/platform/sostrades-webapi/sos_trades_api/configuration_template/configuration.json`
  - `sostrades-dev-tools/platform/sostrades-webapi/.flaskenv`
  - `sostrades-dev-tools/data/REFERENCES/`
  - `sostrades-dev-tools/data/RSA/private_key.pem`
  - `sostrades-dev-tools/data/RSA/public_key.pem`
- `NodeInstallation.py`: script to install NVS (Node Version Switcher) and also install a version of Node with NVS. In addition, it is possible to build `sostrades-webgui`.
- `CreateUser.py`: script that creates a user in SoSTrades with the command `flask create_standard_user`. When the user is created, a password is temporarily saved in `sostrades-dev-tools/platform/sostrades-webapi/sos_trades_api/secret/*`. Once stored, the password has to be deleted. Some SoSTrades app rights are granted in the database with the `flask` command.
- `UpdateOntology.py`: script will execute with your `.venv` the command `python sos_ontology/core/script/createSoSOntologyFromCode.py` in the `sostrades-ontology` folder to update ontology with all your repositories.
- `StartSOSTrades.py`: script that runs the API server, ontology server, and webgui server with venv and node.
- `Linux-StartSOSTrades.py`: same as before - use tmux to split the screen.
- `FullInstall.py`: script for a direct full install. Execute like `python scripts/FullInstall.py`.
