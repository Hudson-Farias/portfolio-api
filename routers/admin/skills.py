from fastapi import Depends
from routers.admin import router, has_authenticated

from database.skills_categories import SkillsCategoriesORM
from database.skills import SkillsORM

from models.admin.skills import *


async def response_data():
    async with SkillsORM() as orm: skills = await orm.find_many()
    async with SkillsCategoriesORM() as orm: skills_categories = await orm.find_many()

    data = SkillsResponse()

    categories_hash = {cat.id: cat.title for cat in skills_categories}

    data.skills = [Skill(**skill.dict(), skill_category_name = categories_hash[skill.skill_category_id]) for skill in skills]
    data.categories = [SkillCategory(**cat.dict()) for cat in skills_categories]

    return data


@router.get('/skills', status_code = 200, response_model = SkillsResponse)
async def get():
    return await response_data()


@router.post('/skills', status_code = 201, response_model = SkillsResponse)
async def post(params: SkillDTO, _: bool = Depends(has_authenticated)):
    async with SkillsORM() as orm: await orm.create(**params.dict())
    return await response_data()


@router.put('/skills/{skill_id}', status_code = 201, response_model = SkillsResponse)
async def put(skill_id: int, params: SkillDTO, _: bool = Depends(has_authenticated)):
    async with SkillsORM() as orm: await orm.update(id = skill_id, **params.dict())
    return await response_data()


@router.delete('/skills/{skill_id}', status_code = 201, response_model = SkillsResponse)
async def delete(skill_id: int, _: bool = Depends(has_authenticated)):
    async with SkillsORM() as orm: await orm.delete(id = skill_id)
    return await response_data()
