from routers.admin import router

from models.admin.projects import *

from httpx import get
from typing import List

GITHUB_API_URL = 'https://api.github.com/users/hudson-farias/repos'

@router.get('/projects', status_code = 200, response_model = List[Project])
async def get_projects():
    response = get(GITHUB_API_URL)
    projects = response.json()

    data = [Project(**project) for project in projects]
    return data
