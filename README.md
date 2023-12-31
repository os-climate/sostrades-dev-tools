# sostrades-dev-tools : Setup SoStrades platform

This repository contains files for local platform deployment, and local for virtual environment venv creation. It also contains default vscode workspace configuration files.

## 1. Choose your environment

Depending on your needs, two different environment installations are proposed. A common setup is mandatory whatever the installation you need to perform.

Follow the diagram below to know what you need to install: 


![](doc_images/choose_your_env.png) 


## 2. Common Setup

The objective is to have all folders properly organized on your local computer. Admin rights on your computer are mandatory to ensure a smooth installation process.  


### 2.1 WSL and/or Ubuntu install + Conda

1. Install WSL2 if using Windows
```
wsl --install --web-download
```

2. Install Ubuntu 22.04 LTS 

On Windows with WSL2
```
wsl --install -d Ubuntu-22.04
```

As an alternative
You may use directly Ubuntu 22.04 LTS or an equivalent, in this case you may have to make some changes on you own.

4. Launch Ubuntu

![](doc_images/ubuntu_installed.png) 


5. Conda installation
Check conda installation with 
`conda info`, if not installed do 
```
pip install conda
```
or 
```
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
chmod +x Anaconda3-2023.09-0-Linux-x86_64.sh
./Anaconda3-2023.09-0-Linux-x86_64.sh
# => Accept licence and follow instructions
# Restart terminal for env variables update
```

6. Install jq
```
$ sudo apt  install jq           #For Debian/Ubuntu
$ sudo yum install jq            #For Fedora/CentOS/RHEL
$ sudo pacman -Syu jq            #For Arch
```


### 2.3 Clone code and tools

All development environments are built from a dedicated directory initiated with this repository. This directory will be used as root and will contains all the others necessary repositories from OS-Climate. This root directory contains VSCode tasks and launch docker-compose files. This allows to launch SoStrades in docker containers and to debug webapi servers directly from thus container in VS Code. From the repository a script is available to clone all the repositories to prepare the development environment.

1. Clone this repository in root directory
```
git clone https://github.com/os-climate/sostrades-dev-tools
(For SSH : git clone git@github.com:os-climate/sostrades-dev-tools.git)
 
cd sostrades-dev-tools
```
2. If needed configure model repositories : Edit the model_repositories.json and platform_repositories.json according to what repositories you want.

```
[
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
3. Launch the PrepareDevEnv.sh
```
./PrepareDevEnv.sh  (if necessary sudo chmod +x PrepareDevEnv.sh to allow execution rights)

```

## 3. Local Docker Env Installation

You are a developer and need a local working platform.

### 3.1 Prerequisites

Follow common setup paragraph :

- WSL2 + Ubuntu 22.04 LTS or directly an Ubuntu equivalent

You will need also:

- Docker 24.0.4 installed and running with your account (on Ubuntu)
- Docker compose 2.17.2 installed (on Ubuntu)


1. Try running  "docker" and  "docker compose" to see if command is recognized
```
docker --version
docker compose --version 

docker ps 
```
 
 If this commands are not working fix docker and docker-compose installation before to continue 

### 3.2 Visual Studio Code (VSCode) installation 
VSCode settings have been written in dedicated files during execution of PrepareDevEnv.sh (in a previous step).

The following command can be run to install VSCode :
```
sudo snap install --classic code
```

In order to benefit from VSCode settings, type the following command in the "sostrades-dev-tools" directory, at the same level than the "./vscode" (hidden) folder (or models/ and platform/ visible directories) :
```
code . &
```

### 3.3 Prepare development environment with docker

All the commands below need to be done from the root directory. 

1. Build all docker images
```
docker compose build
```

### 3.4 Start and play with your SoSTrades GUI

Here all commands needed to play with the image built are listed : 

- First start of your local GUI instance 
```
docker compose up
```

Wait some minutes

Go to [127.0.0.1:1080](127.0.0.1:1080 '127.0.0.1:1080') with your web browser and connect with the following credentials :

login : user

password : mdp

- Stop the instance 
```
docker compose stop
```
- Restart the instance 
```
docker compose start
```
- Clean the instance (if errors)
```
docker compose down
```

- Start the application with debug mode 
```
docker compose -f docker-compose.debug.yml up
```
If using VSCode you will find  4 debug profiles : 

- Remote attach main
- Remote attach message
- Remote attach post processing
- Remote attach data

![](doc_images/vscode_debug_mode.png) 

After having launched each debug profile your application should be available on 127.0.0.1:1080 and you will be able to debug it directly running in the container and from VSCode. All debug profiles must be started since flask api are waiting for debug connection to continue. Then without debug connections platform won't be responding.

### 3.5 Useful links

https://code.visualstudio.com/docs/containers/docker-compose

https://code.visualstudio.com/docs/containers/debug-common 

## 4. Local Model Development Env Installation
The objective is to have a working local dev environment based on a conda venv, with pre-configured VS-CODE workspace to be able to run code and debug. Other IDE may be used but should be configured properly.

### 4.1 Prerequisites

Follow 2. common setup paragraph :

- WSL2 + Ubuntu 22.04 LTS or directly an Ubuntu equivalent
- Conda installed

### 4.2 Prepare Conda environment
```
./PrepareCondaEnv.sh  (if necessary sudo chmod +x PrepareCondaEnv.sh to allow execution rights)
```

### 4.3 Visual Studio Code (VSCode) installation 
VSCode settings have been written in dedicated files during execution of PrepareDevEnv.sh (in a previous step).

The following command can be run to install VSCode :
```
sudo snap install --classic code
```

In order to benefit from VSCode settings, type the following command in the "sostrades-dev-tools" directory, at the same level than the "./vscode" (hidden) folder (or models/ and platform/ visible directories) :
```
code . &
```

### 4.4 Use conda env in VS code

Use keys windows + shift + p to open command panel, search for "Python: Select Interpreter"

![](doc_images/select_interpreter.png) 

Select "Python 3.9.x ("SOSTradesEnv")

![](doc_images/select_python.png) 

Now you can launch any SoSTrades code from VSCode.


