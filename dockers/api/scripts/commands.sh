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
echo "/petsc-install/lib" >> /tmp/pythonpath.txt
# Temporary special PYTHONPATH for gemseo
echo '/usr/local/sostrades/sources/platform/gemseo/src' >> /tmp/pythonpath.txt
cat /tmp/pythonpath.txt
export PYTHONPATH=$(cat /tmp/pythonpath.txt)

pip install importlib-metadata==4.13.0

python /startup/check_database_is_ready.py

cd /usr/local/sostrades/sources/platform/sostrades-webapi
flask db upgrade
flask init_process

python /startup/create_initial_account.py

gunicorn sos_trades_api.server.split_mode.post_processing_server:app --bind 0.0.0.0:8003 --limit-request-line 0 --timeout 300 -D --enable-stdio-inheritance
gunicorn --worker-class eventlet sos_trades_api.server.message_server:app --bind 0.0.0.0:8002 --limit-request-line 0 --timeout 300 -D --enable-stdio-inheritance
gunicorn sos_trades_api.server.split_mode.data_server:app --bind 0.0.0.0:8001 --limit-request-line 0 --timeout 300 -D  --enable-stdio-inheritance
gunicorn sos_trades_api.server.split_mode.main_server:app --bind 0.0.0.0:8000 --limit-request-line 0 --timeout 300 --threads 5