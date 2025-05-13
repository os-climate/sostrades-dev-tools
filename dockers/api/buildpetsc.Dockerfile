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
FROM python:3.12

RUN chmod 1777 /tmp

# Installation de PETSc et de ses dépendances
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y \
    wget g++ gcc make gfortran bzip2 git vim xmlsec1 \
    libxmlsec1-dev pkg-config default-libmysqlclient-dev \
    build-essential libsasl2-dev python3-dev libldap2-dev \
    libssl-dev procps mpi mpich unixodbc-dev unixodbc \
    coinor-libcbc-dev cron && apt clean

# Numpy version
ARG NUMPY_VERSION="1.26.4"

# Upgrade pip and install uv
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir uv && \
    python -m uv pip install --no-cache-dir setuptools numpy==${NUMPY_VERSION}

# PETSC version and directory
ARG PETSC_VERSION="3.21.6"
ARG PETSC_BUILD_DIR="/petsc-build"
ARG PETSC_INSTALL_DIR="/petsc-install"
ENV PYTHON_SITE_PACKAGE_DIR="/usr/local/lib/python3.12/site-packages"

# Fix petsc4py incompatibility with cython 3.1.0
RUN pip install --no-cache-dir cython==3.0.12

# Download and install PETSc
RUN git clone --branch v${PETSC_VERSION} --depth 1 https://gitlab.com/petsc/petsc.git ${PETSC_BUILD_DIR} && \
    cd ${PETSC_BUILD_DIR} &&\
    export PETSC_ARCH=arch-linux-c-debug && \
    export PETSC_DIR=${PETSC_BUILD_DIR} && \
    mkdir ${PETSC_INSTALL_DIR} && \
    ./configure --with-cc=gcc --with-cxx=g++ --with-fc=gfortran --with-petsc4py=yes --download-petsc4py=yes --with-shared-libraries --download-mpich --download-fblaslapack --prefix=${PETSC_INSTALL_DIR}&& \
    make all install check && \
    cd ../ && \
    rm -rf ${PETSC_BUILD_DIR} && \
    echo "${PETSC_INSTALL_DIR}/lib" > "${PYTHON_SITE_PACKAGE_DIR}/petsc4py.pth"

# Update env with PETSC install
ENV PATH=${PETSC_INSTALL_DIR}/bin:${PATH}
ENV PETSC_DIR=${PETSC_INSTALL_DIR}
ENV USE_PETSC="True"

# Allow flask to work withtout .flaskenv file in git repository
ENV FLASK_APP=sos_trades_api/server/base_server.py

# Install path for sostrades
ENV SOS_TRADES_SOURCES="/usr/local/sostrades/sources"
RUN mkdir -p ${SOS_TRADES_SOURCES} /usr/local/sostrades/conf/ /startup
WORKDIR ${SOS_TRADES_SOURCES}

ARG KUBERNETES_VERSION="29.0.0"

ENTRYPOINT ["/bin/bash", "/startup/commands.sh"]
