from fastapi import Depends
from routers.admin import router, partial_authenticated

from models.admin.projects import *

from httpx import get
from typing import List

from env import GITHUB_ACCESS_TOKEN

GITHUB_API_URL = 'https://api.github.com/users/hudson-farias/repos?per_page=100'
GITHUB_API_URL_PRIVATE = 'https://api.github.com/user/repos?per_page=100'


@router.get('/projects', status_code = 200, response_model = List[Project])
async def get_projects(is_auth: bool = Depends(partial_authenticated)):
    github_url = GITHUB_API_URL_PRIVATE if is_auth else GITHUB_API_URL

    headers = {
        'Accept': 'application/vnd.github+json',
        'X-GitHub-Api-Version': '2022-11-28'
    }

    if is_auth: headers['Authorization'] = f'Bearer {GITHUB_ACCESS_TOKEN}'

    response = get(github_url, headers = headers)
    projects = response.json()

    data = [Project(**project) for project in projects]
    return data
