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

# open models and platform repositories, read commits, write info in file
import json
from os import listdir
from os.path import(join, isdir, exists)
from datetime import datetime
import subprocess

git_commits_info_file_path = f"./platform/sostrades-webapi/sos_trades_api/git_commits_info.json"
platform_path = "./platform"
models_path = "./models"


def get_git_info(repo_name:str, repo_git_path:str)-> dict:
    '''
    Get git info from folder
    '''

    def run_git_command(command):
        result = subprocess.run(command, cwd=repo_git_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise Exception(f"Git command failed: {result.stderr}")
        return result.stdout.strip()

    try:
        # get last commit hash
        last_commit_hash = run_git_command(['git', 'rev-parse', 'HEAD'])

        # Récupérer la branche ou le tag courant
        branch_or_tag = run_git_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        if branch_or_tag == 'HEAD':
            all_tags = run_git_command(['git', 'tag', '--contains', last_commit_hash])
            tags = [tag for tag in all_tags.split('\n') if tag.startswith('v')]
            if len(tags)>0:
                branch_or_tag = tags[0]
        
        # get last commit date
        last_commit_date = run_git_command(['git', 'log', '-1', '--format=%cd'])
    

        # get repo url
        last_commit_url = run_git_command(['git', 'remote', 'get-url', 'origin'])

        return {
            'name':repo_name,
            'commit': last_commit_hash,
            'url': last_commit_url,
            'committed_date': last_commit_date,
            'branch': branch_or_tag
        }
    except Exception as e:
        raise Exception(f"Error while getting repository {repo_git_path} git info: {e}")


def build_commits_info_dict(folder_path:str)-> dict:
    '''
    Loop on each repo in the folder, if it is a git repo, get the last commit name, branch and date
    '''
    repo_info = []
    for repo in listdir(folder_path):
        repo_path = join(folder_path, repo)
        if isdir(repo_path):
            try:
                # Check that the repository is a git folder
                if exists(join(repo_path, '.git')):
                    repo_info.append(get_git_info(repo, repo_path))
            except Exception as e:
                print(e)
    return repo_info


def save_to_json(data, json_path):
    try:
        with open(json_path, 'w+') as json_file:
            json.dump(data, json_file)
        print(f"Data successfully written to {json_path}")
    except Exception as e:
        print(f"Failed to write data to JSON file: {e}")
        

# get repositories commits info in a dict 
all_repo_info = build_commits_info_dict(platform_path)
all_repo_info.extend(build_commits_info_dict(models_path))
#write it in json file
if len(all_repo_info) > 0:
    save_to_json(all_repo_info, git_commits_info_file_path)
    
