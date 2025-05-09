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
FROM python:3.12 AS builder

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

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

ARG KUBERNETES_VERSION="29.0.0"

# Install ontology requirements
COPY ./platform_requirements/dev.requirements.txt dev.requirements.txt

RUN sed -i '/petsc\|kubernetes\|numpy[[:blank:]]*=/d' dev.requirements.txt && \
    python -m uv pip install --no-cache-dir -r dev.requirements.txt debugpy numpy==${NUMPY_VERSION} kubernetes==${KUBERNETES_VERSION} && \
    python -m uv pip install --no-cache-dir --no-deps git+https://gitlab.com/gemseo/dev/gemseo-petsc@4f1f50baebec11c0ccf417c6ae8bf03b28a2c431

COPY ./platform/sostrades-ontology ./platform/sostrades-ontology
COPY ./platform/sostrades-core ./platform/sostrades-core
COPY ./models ./models

# Update PYTHONPATH
RUN ls -d ${pwd}/platform/* | tr '\n' ':' > /tmp/pythonpath.txt && \ 
    ls -d ${pwd}/models/* | tr '\n' ':' >> /tmp/pythonpath.txt && \ 
    sed -i '$ s/.$//' /tmp/pythonpath.txt && \
    export PYTHONPATH=$(cat /tmp/pythonpath.txt) && \
    echo "PYTHONPATH=$PYTHONPATH" && \
    python -u platform/sostrades-ontology/sos_ontology/core/script/createSoSOntologyFromCode.py

#------------------------------------------------------------------------------

FROM python:3.12

# Numpy version
ARG NUMPY_VERSION="1.26.4"

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install path for sostrades
RUN mkdir -p /usr/local/sostrades/sources

# startup path for ontology
RUN mkdir /startup

# Install ontology requirements
COPY ./platform_requirements/ontology.requirements.txt ontology.requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip && \
    python -m pip install --no-cache-dir uv && \
    python -m uv pip install --no-cache-dir -r ontology.requirements.txt pylint gunicorn debugpy numpy==${NUMPY_VERSION}
COPY ./platform/sostrades-ontology /usr/local/sostrades/sources/platform/sostrades-ontology

# Add repositories needed to pass test on ontology image
COPY ./platform/sostrades-core/sostrades_core /usr/local/sostrades/sources/platform/sostrades-core/sostrades_core

# Update PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/usr/local/sostrades/sources/platform/sostrades-ontology:/usr/local/sostrades/sources/platform/sostrades-core"

# Copy startup files for ontology
ADD ./dockers/ontology/scripts /startup

COPY --from=builder ./platform/sostrades-ontology/sos_ontology/data /usr/local/sostrades/sources/platform/sostrades-ontology/sos_ontology/data/

# Change workdir to run test on ontology image
WORKDIR /usr/local/sostrades/sources/

ENTRYPOINT ["/bin/bash", "/startup/commands.sh"]
