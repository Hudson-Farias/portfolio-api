from fastapi import Depends
from routers.admin import router, has_authenticated

from database.experiences import ExperiencesORM

from models.admin.experiences import *

from typing import List


async def response_data() -> List[Experience]:
    async with ExperiencesORM() as orm: experiences = await orm.find_many()
    data = [Experience(**experience.dict()) for experience in experiences]

    return data




@router.get('/experiences', status_code = 200, response_model = List[Experience])
async def get_experiences():
    return await response_data()


@router.post('/experiences', status_code = 201, response_model = List[Experience])
async def post_experience(params: ExperienceDTO, _: bool = Depends(has_authenticated)):
    async with ExperiencesORM() as orm: await orm.create(**params.dict())
    return await response_data()


@router.put('/experiences/{experience_id}', status_code = 201, response_model = List[Experience])
async def put_experience(experience_id: int, params: ExperienceDTO, _: bool = Depends(has_authenticated)):
    async with ExperiencesORM() as orm: await orm.update(id = experience_id, **params.dict())
    return await response_data()



@router.delete('/experiences/{experience_id}', status_code = 201, response_model = List[Experience])
async def delete_experience(experience_id: int, _: bool = Depends(has_authenticated)):
    async with ExperiencesORM() as orm: await orm.delete(id = experience_id)
    return await response_data()
