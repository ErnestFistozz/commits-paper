import requests, csv
from pydriller import Repository
import pandas as pd
from utils import format_datetime, get_commit_details

headers = [ 'CommitHash', 'Date', 'CommitMessage', 'CommitMessageSize', 'CommitLines', 
    'IsMergeRequest', 'NumberFilesChanged']

projects = [{}]

for repo in projects:
    with open(rf'./{repo.proj}CommitsDist.csv', 'a+', encoding='utf-8', newline=',') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([header for header in headers])
        try:
            gh_repo = f'../commits/{repo}'
            date, hash, message, commit_msg_size = get_commit_details(repo.org, repo.proj)
            for commit in Repository(path_to_repo=gh_repo, only_in_branch='origin/master').traverse_commits():
                lines = commit.lines
                is_merge_commit = 'Yes' if commit.merge else 'No'
                no_of_files_modified = commit.files
                print(hash, date, message, commit_msg_size, lines, is_merge_commit, no_of_files_modified )
        except:
            print('I am here')
            continue
            
