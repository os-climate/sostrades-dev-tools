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
FROM python:3.9 AS builder

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

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

# Copy platform repos for standalone image if needed

# Install ontology requirements
COPY ./platform/sostrades-core/dev.requirements.txt dev.requirements.txt

RUN sed -i '/petsc\|numpy/d' dev.requirements.txt && \
    pip install --no-cache-dir -r dev.requirements.txt debugpy

COPY ./platform/gemseo ./platform/gemseo
COPY ./platform/sostrades-ontology ./platform/sostrades-ontology
COPY ./platform/sostrades-core ./platform/sostrades-core
COPY ./platform/sostrades-webapi ./platform/sostrades-webapi
COPY ./models ./models

## SET PYTHONPATH
RUN ls -d platform/* | tr '\n' ':' > /tmp/pythonpath.txt && \
    ls -d models/* | tr '\n' ':' >> /tmp/pythonpath.txt && \
    sed -i "s|gemseo|gemseo/src|g" /tmp/pythonpath.txt && \
    truncate -s-1 /tmp/pythonpath.txt

# export pythonpath with all repo and launch script to generate .owl
RUN export PYTHONPATH=$(cat /tmp/pythonpath.txt) && \
    echo $PYTHONPATH && \
    python platform/sostrades-ontology/sos_ontology/core/script/createSoSOntologyFromCode.py

#------------------------------------------------------------------------------

FROM python:3.9

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

# Install path for sostrades
RUN mkdir -p /usr/local/sostrades/sources

# startup path for ontology
RUN mkdir /startup

# Install ontology requirements
COPY ./platform/sostrades-ontology/ontology.requirements.txt ontology.requirements.txt
RUN pip install --no-cache-dir -r ontology.requirements.txt gunicorn

WORKDIR /usr/local/sostrades/sources/sostrades-ontology
COPY ./platform/sostrades-ontology .

# Copy startup files for ontology
ADD ./dockers/ontology/scripts /startup

COPY --from=builder ./platform/sostrades-ontology/sos_ontology/data /usr/local/sostrades/sources/sostrades-ontology/sos_ontology/data/

ENTRYPOINT ["/bin/bash", "/startup/commands.sh"]