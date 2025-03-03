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
FROM registrysostrades.azurecr.io/python-petsc-${DEV_TOOLS_BRANCH}:3.9

# Numpy version
ARG NUMPY_VERSION="1.24.4"

ARG KUBERNETES_VERSION="29.0.0"

# Copy Python requirements and install them
COPY ./platform_requirements/api.requirements.txt api.requirements.txt
RUN sed -i '/petsc\|kubernetes\|numpy[[:blank:]]*=/d' api.requirements.txt && \
    python -m uv pip install --no-cache-dir -r api.requirements.txt pylint gunicorn debugpy numpy==${NUMPY_VERSION} kubernetes==${KUBERNETES_VERSION} && \
    python -m uv pip install --no-cache-dir --no-deps git+https://gitlab.com/gemseo/dev/gemseo-petsc@4f1f50baebec11c0ccf417c6ae8bf03b28a2c431

COPY ./platform/sostrades-webapi ./platform/sostrades-webapi
COPY ./platform/sostrades-core ./platform/sostrades-core
    
RUN pip list

ENV ENV=/etc/environment

ENTRYPOINT ["/bin/bash", "/startup/commands.sh"]
