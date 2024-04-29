'''
Copyright 2024 Capgemini
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

import subprocess
from os.path import dirname, join

scripts_list = ['PrepareDevEnv', 'PrepareVEnv', 'Configuration', 'NodeInstallation', 'EditFlaskenv', 'CreateDatabases',
                'CreateUser', 'UpdateOntology']
for script in scripts_list:
    print(f'---------------------------------------------')
    print(f'Starting {script} script')
    print(f'---------------------------------------------')
    subprocess.run(["python", join(dirname(__file__), f"{script}.py")])
    print(f'---------------------------------------------')
    print(f'End of {script} script')
    print(f'---------------------------------------------')
