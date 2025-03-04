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

# Numpy version
ARG NUMPY_VERSION="1.24.4"

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

# Change workdir to run test on ontology image
WORKDIR /usr/local/sostrades/sources/

ENTRYPOINT ["/bin/bash", "/startup/commands.sh"]
