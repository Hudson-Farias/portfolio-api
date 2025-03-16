from fastapi import Depends
from routers.admin import router, partial_authenticated, has_authenticated

from database.projects import ProjectsORM

from models.admin.projects import *

from services.github import github


async def response_data(is_auth: bool) -> Projects:
    async with ProjectsORM() as orm: projects = await orm.find_many()
    projects_ids = [project.git_id for project in projects]

    projects = github(is_auth)

    data = Projects()

    for project in projects:
        project['git_id'] = project['id']
        project_dto = Project(**project)

        if project['id'] in projects_ids: data.visible.append(project_dto)
        else: data.options.append(project_dto)

    return data


@router.get('/projects', status_code = 200, response_model = Projects)
async def get_projects(is_auth: bool = Depends(partial_authenticated)):
    return await response_data(is_auth)



@router.post('/projects/{git_id}', status_code = 201)
async def post_projects(git_id: int, is_auth: bool = Depends(has_authenticated)):
    async with ProjectsORM() as orm: await orm.create(git_id = git_id)

    return await response_data(is_auth)



@router.delete('/projects/{git_id}', status_code = 201)
async def delete_project(git_id: int, is_auth: bool = Depends(has_authenticated)):
    async with ProjectsORM() as orm: await orm.delete(git_id = git_id)
    return await response_data(is_auth)
