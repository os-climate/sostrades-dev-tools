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
FROM registrysostrades.azurecr.io/ontology-builder:${SOSTRADES_VERSION} AS builder

# Install ontology requirements
COPY ./platform_requirements/dev.requirements.txt dev.requirements.txt

RUN sed -i '/petsc\|kubernetes\|numpy[[:blank:]]*=/d' dev.requirements.txt && \
    python -m uv pip install --no-cache-dir -r dev.requirements.txt debugpy numpy==${NUMPY_VERSION} kubernetes==${KUBERNETES_VERSION} && \
    python -m uv pip install --no-cache-dir --no-deps git+https://gitlab.com/gemseo/dev/gemseo-petsc@4f1f50baebec11c0ccf417c6ae8bf03b28a2c431

COPY ./models ./models

# Update PYTHONPATH & calcul ontology
RUN ls -d ${pwd}/platform/* | tr '\n' ':' > /tmp/pythonpath.txt && \ 
    ls -d ${pwd}/models/* | tr '\n' ':' >> /tmp/pythonpath.txt && \ 
    sed -i '$ s/.$//' /tmp/pythonpath.txt && \
    export PYTHONPATH=$(cat /tmp/pythonpath.txt) && \
    echo "PYTHONPATH=$PYTHONPATH" && \
    python -u platform/sostrades-ontology/sos_ontology/core/script/createSoSOntologyFromCode.py

#------------------------------------------------------------------------------

FROM ontology:${SOSTRADES_VERSION}

COPY --from=builder ./platform/sostrades-ontology/sos_ontology/data /usr/local/sostrades/sources/platform/sostrades-ontology/sos_ontology/data/

ENTRYPOINT ["/bin/bash", "/startup/commands.sh"]
