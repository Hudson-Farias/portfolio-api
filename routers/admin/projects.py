from fastapi import Depends
from asyncio import gather
from routers.admin import router, partial_authenticated, has_authenticated

from database.projects import ProjectsORM

from models.admin.projects import *

from httpx import get
from typing import List

from env import GITHUB_ACCESS_TOKEN

GITHUB_API_URL = 'https://api.github.com/users/hudson-farias/repos?per_page=100'
GITHUB_API_URL_PRIVATE = 'https://api.github.com/user/repos?per_page=100'


async def get_project(project: dict):
    project_dto = Project(**project)
    project_dto.git_id = project['id']

    async with ProjectsORM() as orm:
        is_active = await orm.find_one(git_id = project_dto.git_id)
        project_dto.is_active = bool(is_active)

    return project_dto


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

    result = await gather(*[get_project(project) for project in projects])
    return result




@router.post('/projects/{git_id}', status_code = 204)
async def post_projects(git_id: int, is_auth: bool = Depends(has_authenticated)):
    async with ProjectsORM() as orm:
        project = await orm.find_one(git_id = git_id)

        await orm.create(git_id = git_id) if not project else await orm.delete(id = project.id) 
