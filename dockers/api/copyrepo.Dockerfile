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
FROM registrysostrades.azurecr.io/sostrades-api:${SOSTRADES_VERSION}


# Copy models and platform repos for standalone image if needed
COPY ./platform/sostrades-webapi ./platform/sostrades-webapi
COPY ./platform/sostrades-core ./platform/sostrades-core
COPY ./models ./models

RUN if [ -e ./platform/sostrades-webapi/sos_trades_api/version.info ] ; then echo Version.info file provided ; else TZ="UTC" date > ./platform/sostrades-webapi/sos_trades_api/version.info ; fi

# Update PYTHONPATH
RUN ls -d ${SOS_TRADES_SOURCES}/platform/* | tr '\n' ':' > /tmp/pythonpath.txt && \ 
    ls -d ${SOS_TRADES_SOURCES}/models/* | tr '\n' ':' >> /tmp/pythonpath.txt && \ 
    sed -i '$ s/.$//' /tmp/pythonpath.txt && \
    echo "export PYTHONPATH=$(cat /tmp/pythonpath.txt)" >> /etc/environment && \
    echo '. /etc/environment' >> /etc/bash.bashrc

ENV ENV=/etc/environment

ENTRYPOINT ["/bin/bash", "/startup/commands.sh"]
