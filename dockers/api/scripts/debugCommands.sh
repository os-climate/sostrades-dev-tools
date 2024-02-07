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

# Build python path regarding all sub folder in sostrades source folder
ls -d /usr/local/sostrades/sources/platform/*/ | tr '\n' ':' > /tmp/pythonpath.txt
ls -d /usr/local/sostrades/sources/models/*/ | tr '\n' ':' >> /tmp/pythonpath.txt
echo -n "/petsc-install/lib:" >> /tmp/pythonpath.txt
# Temporary special PYTHONPATH for gemseo
echo -n '/usr/local/sostrades/sources/platform/gemseo/src' >> /tmp/pythonpath.txt
cat /tmp/pythonpath.txt
export PYTHONPATH=$(cat /tmp/pythonpath.txt)

python /startup/check_database_is_ready.py

cd /usr/local/sostrades/sources/platform/sostrades-webapi
flask db upgrade
flask init_process

python /startup/create_initial_account.py

python -m debugpy --wait-for-client --listen 0.0.0.0:5678 /usr/local/sostrades/sources/platform/sostrades-webapi/server_scripts/split_mode/launch_server_main.py & 
python -m debugpy --wait-for-client --listen 0.0.0.0:5681 /usr/local/sostrades/sources/platform/sostrades-webapi/server_scripts/split_mode/launch_server_post_processing.py & 
python -m debugpy --wait-for-client --listen 0.0.0.0:5679 /usr/local/sostrades/sources/platform/sostrades-webapi/server_scripts/split_mode/launch_server_data.py & 
python -m debugpy --wait-for-client --listen 0.0.0.0:5680 /usr/local/sostrades/sources/platform/sostrades-webapi/server_scripts/launch_server_message.py


