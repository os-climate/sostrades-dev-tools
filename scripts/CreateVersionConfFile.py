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
import re

git_commits_info_file_path = f"./platform/sostrades-webapi/sos_trades_api/git_commits_info.json"
gitignore_file_path = f"./platform/sostrades-webapi/.gitignore"
platform_path = "./platform"
models_path = "./models"

def get_git_info(repo_name:str, repo_git_path:str)-> dict:
    '''
    Get git info from folder
    :param repo_name: name of the repo to check
    :type repo_name: str
    :param repo_git_path: path of the repo to check
    :type repo_git_path: str
    :return: dict with git last commit info with format:
    [
        {
        'name':str,
        'commit': str,
        'url': str,
        'committed_date': str,
        'branch': str
        }
    ]
    '''

    def run_git_command(command):
        result = subprocess.run(command, cwd=repo_git_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            raise Exception(f"Git command failed: {result.stderr}")
        return result.stdout.strip()

    try:
        # get last commit hash
        last_commit_hash = run_git_command(['git', 'rev-parse', 'HEAD'])

        # get current branch or version tag
        branch_or_tag = run_git_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        if branch_or_tag == 'HEAD':
            all_tags = run_git_command(['git', 'tag', '--contains', last_commit_hash])
            tags = [tag for tag in all_tags.split('\n') if tag.startswith('v')]
            if len(tags)>0:
                def convert_version(version:str)->list[int]:
                    return [int(part) for part in version.strip('v').split('.')]

                # sort versions
                sorted_tags = sorted(tags, key=convert_version)
                
                branch_or_tag = sorted_tags[-1]
        
        # get last commit date
        last_commit_date = run_git_command(['git', 'log', '-1', '--format=%cd'])
        # change the format of the last committed date
        try:
            # the format in input is: Thu Jul 11 13:00:09 2024 +0000
            input_format = '%a %b %d %H:%M:%S %Y %z'
            # parse format into datetime
            commit_date = datetime.strptime(last_commit_date, input_format)

            # define output format:  Thu Jul 11 2024 13:00
            output_format = '%Y-%m-%d %H:%M'
            # format output date in str
            last_commit_date = commit_date.strftime(output_format)
        except:
            print(f"error while converting last commit date {last_commit_date} into datetime")

        # get repo url
        INFO_REGEXP = ':\/\/.*@'
        INFO_REPLACE = '://'
        last_commit_url = run_git_command(['git', 'remote', 'get-url', 'origin'])
        last_commit_url = re.sub(INFO_REGEXP, INFO_REPLACE, last_commit_url)
        
        # Post-process url to remove .git
        if last_commit_url.endswith(".git"):
            last_commit_url = last_commit_url[:-4]
            # Verify if we are dealing with ssh remote repository and replace by https://
        SSH_REGEX =  r'^[a-zA-Z]+@[a-zA-Z0-9.-]+:'
        SSH_REGEX_TO_REPLACE = r'^.*@'
        SSH_REGEX_REPLACE = 'https://'
        if bool(re.match(SSH_REGEX, last_commit_url)):
            last_commit_url = last_commit_url.replace(":", "/")
            last_commit_url = re.sub(SSH_REGEX_TO_REPLACE, SSH_REGEX_REPLACE, last_commit_url)

        return {
            'name':repo_name,
            'commit': last_commit_hash,
            'url': last_commit_url,
            'committed_date': last_commit_date,
            'branch': branch_or_tag
        }
    except Exception as e:
        raise Exception(f"Error while getting repository {repo_git_path} git info: {e}") from e


def build_commits_info_dict(folder_path:str)-> list[dict]:
    '''
    Loop on each repo in the folder, if it is a git repo, get the last commit name, branch and date
    :param folder_path: folder to iterate through sub folder to get git info
    :type folder_path: str
    :return: list of dict with git last commits info with format:
    [
        {
        'name':str,
        'commit': str,
        'url': str,
        'committed_date': str,
        'branch': str
        }
    ]
    '''
    repo_info = []
    for repo in listdir(folder_path):
        repo_path = join(folder_path, repo)
        if isdir(repo_path):
            try:
                # Check that the repository is a git folder
                if exists(join(repo_path, '.git')):
                    print(f"getting git info of {repo}")
                    git_repo_info = get_git_info(repo, repo_path)
                    repo_info.append(git_repo_info)
            except Exception as e:
                print(e)
    return repo_info


def save_to_json(data, json_path):
    """
    save json data into file in json_path (create file if not exists)
    :param data: json data to save
    :type data: dict
    :param json_path: file path where to save
    :type json_path: str
    """
    try:
        with open(json_path, 'w+') as json_file:
            json.dump(data, json_file)
        print(f"Data successfully written to {json_path}")
    except Exception as e:
        print(f"Failed to write data to JSON file: {e}")
        

def check_git_commit_file_in_git_ignore()->bool:
    """
    Check if the file name is in the sostrades_webapi .gitignore file 
    so that there is no merge conflict on automerge

    :return: if the file name "sos_trades_api/git_commits_info.json" is present in .gitignore file
    """
    is_ignored = False
    if exists(gitignore_file_path):
        with open(gitignore_file_path, 'r') as git_file:
            content = git_file.readlines()
            if "sos_trades_api/git_commits_info.json\n" in content:
                is_ignored = True

    return is_ignored

#check that the file is ignored in git folder, else do not create it to avoid merging issues
if check_git_commit_file_in_git_ignore():
    # get repositories commits info in a dict 
    all_repo_info = build_commits_info_dict(platform_path)
    all_repo_info.extend(build_commits_info_dict(models_path))
    platform_app_info = {
        "repositories":all_repo_info,
        "version":"version",
        "build_date":datetime.now().strftime("%d %b %Y")
    }
    # get the version of platform from sostrades-core branch or tag
    for repo in all_repo_info:
        if repo["name"].lower() == "sostrades-core":
            platform_app_info['version'] = repo['branch']

    #write it in json file
    if len(all_repo_info) > 0:
        save_to_json(platform_app_info, git_commits_info_file_path)
