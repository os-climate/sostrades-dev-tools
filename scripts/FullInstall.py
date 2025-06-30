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

from tooling import run_command
from constants import (
    run_prefix_system,
)

scripts_list = ['PrepareDevEnv', 'PrepareVenv', 'Configuration', 'NodeInstallation', 'CreateUser', 'UpdateOntology']
for script in scripts_list:
    print(f'---------------------------------------------')
    print(f'Starting {script} script')
    print(f'---------------------------------------------')
    run_command(f'{run_prefix_system}"{sys.executable}" {join(dirname(__file__), script+".py")}')
    print(f'---------------------------------------------')
    print(f'End of {script} script')
    print(f'---------------------------------------------')
