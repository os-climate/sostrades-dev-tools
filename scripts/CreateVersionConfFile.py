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
from constants import (platform_path, model_path, git_commits_info_file_path)
import git
from datetime import datetime

def get_git_info(repo_name:str, repo_git_path:str)-> dict:
    '''
    Get git info from folder
    '''
    try:
        repo = git.Repo(repo_git_path)

        # get last commit sha
        last_commit = repo.head.commit
        last_commit_hash = last_commit.hexsha

        # get last commit date
        last_commit_date = datetime.fromtimestamp(last_commit.committed_date).strftime('%Y-%m-%d %H:%M:%S')

        # get last commit URL
        last_commit_url = None
        if repo.remotes:
            remote_url = repo.remotes.origin.url
            if remote_url.endswith('.git'):
                remote_url = remote_url[:-4]  # Remove the .git suffix for the URL construction

            # Construire l'URL du dernier commit
            last_commit_url = f"{remote_url}/commit/{last_commit_hash}"

        # get branch or tag
        branch_or_tag = ""
        if repo.head.is_detached:
            tags = [tag.name for tag in repo.tags if tag.commit == last_commit and tag.name.startswith('v')]
            if len(tags)>0:
                branch_or_tag = tags[0]
        else:
            branch_or_tag = repo.active_branch.name

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
all_repo_info.extend(build_commits_info_dict(model_path))
#write it in json file
if len(all_repo_info) > 0:
    save_to_json(all_repo_info, git_commits_info_file_path)
    
