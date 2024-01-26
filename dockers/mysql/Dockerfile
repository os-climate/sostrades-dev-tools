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
FROM mysql:8.0.33

RUN chmod 1777 /tmp

ADD ./mysql/scripts/init_sostrades_databases.sql.template /tmp
RUN chmod +x /tmp/init_sostrades_databases.sql.template

ADD ./env/sostrades-database-credentials.env /tmp
#ADD ./resources/ocdb.sql /tmp
RUN export $(cat /tmp/sostrades-database-credentials.env | xargs) && /tmp/init_sostrades_databases.sql.template > /docker-entrypoint-initdb.d/init_sostrades.sql 


RUN rm /etc/my.cnf
RUN rm /tmp/sostrades-database-credentials.env

EXPOSE 3306

