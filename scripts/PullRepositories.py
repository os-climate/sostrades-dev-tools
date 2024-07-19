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

import os
import subprocess
from constants import (sostrades_dev_tools_path,
                       model_dir_name,
                       platform_dir_name)


def pull_repositories(folder_path):
    # Navigate through the specified folder
    for root, dirs, files in os.walk(folder_path):
        # Check if it's a git repository
        if '.git' in dirs:
            print(f'Pull repository {root}')
            os.chdir(root)
            command = ["git", "pull"]
            subprocess.run(command)
            os.chdir(sostrades_dev_tools_path)


pull_repositories(model_dir_name)
pull_repositories(platform_dir_name)
