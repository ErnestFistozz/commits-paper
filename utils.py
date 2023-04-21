from datetime import timezone, datetime
import requests, 

def format_datetime(timestamp):
    formated_timestamp = datetime.fromisoformat(timestamp[:-1]).astimezone(timezone.utc)
    return formated_timestamp.strftime('%Y-%m-%d %H:%M:%S')


def get_commit_details( org: str, repo_name: str) -> str:
    branch, page, size = 'master', 1 , 1
    url = f'https://codecov.io/api/v2/gh/{org}/repos/{repo_name}/commits?branch={branch}&page={page}&page_size={size}'
    response = requests.get(url).json()['results'][0]
    date, hash, message = format_datetime(response['timestamp']), response['commitid'],  \
        response['message']
    return date, hash, message, len(response['message'])