# Copyright 2023 Capgemini

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM python:3.9

# Installation de PETSc et de ses dépendances
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y \
    wget g++ gcc make gfortran bzip2 git vim xmlsec1 \
    libxmlsec1-dev pkg-config default-libmysqlclient-dev \
    build-essential libsasl2-dev python3-dev libldap2-dev \
    libssl-dev procps mpi mpich unixodbc-dev unixodbc \
    coinor-libcbc-dev && apt clean

# Upgrade pip
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy==1.24.3

# Download and install PETSc
RUN wget https://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.19.4.tar.gz && \ 
    tar -xzf petsc-3.19.4.tar.gz && \
    cd petsc-3.19.4 && \
    ./configure --with-cc=gcc --with-petsc4py=1 --with-cxx=g++ --with-fc=gfortran --download-mpich --download-fblaslapack && \
    make PETSC_DIR=/petsc-3.19.4 PETSC_ARCH=arch-linux-c-debug all check && \
    cp -r arch-linux-c-debug/lib/* /usr/local/lib/python3.9/site-packages/ && \
    cd ../ && \
    rm -rf petsc-3.19.4.tar.gz petsc-3.19.4

# Install path for sostrades 
RUN mkdir -p /usr/local/sostrades/sources /usr/local/sostrades/conf/ /startup
WORKDIR /usr/local/sostrades/sources

# Copy Python requirements and install them
COPY ./../platform/sostrades-webapi/api.requirements.txt api.requirements.txt
RUN sed -i '/petsc\|numpy/d' api.requirements.txt && \
    pip install --no-cache-dir -r api.requirements.txt pylint gunicorn debugpy

# Set all needed environment variables
ENV FLASK_APP=sos_trades_api/server/base_server.py
ENV FLASK_ENV=production
ENV SOS_TRADES_SERVER_CONFIGURATION='/usr/local/sostrades/conf/sostrades_configuration.json'

# Copy configuration files for sostrades 
ADD ./../dockers/api/conf /usr/local/sostrades/conf

# Copy startup files for sostrades 
ADD ./../dockers/api/scripts /startup

# Copy utility scripts
#COPY ./../dockers/api/scripts/for_all.sh /usr/local/sostrades
#RUN chmod +x /usr/local/sostrades/for_all.sh

# Copy models and platform repos for standalone image if needed
COPY ./../platform/sostrades-webapi ./platform/sostrades-webapi
COPY ./../platform/sostrades-core ./platform/sostrades-core
COPY ./../platform/gemseo ./platform/gemseo
COPY ./../models ./models

#ENTRYPOINT ["/bin/bash", "/startup/commands.sh"]
