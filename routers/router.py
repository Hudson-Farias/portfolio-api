from fastapi import APIRouter

from database.skills_categories import SkillsCategoriesORM
from database.skills import SkillsORM
from database.experiences import ExperiencesORM
from database.projects import ProjectsORM
from database.social_networks import SocialNetworksORM
from models.model import *

router = APIRouter()

@router.get('/', status_code = 200, response_model = ModelResponse)
async def get():
    data = ModelResponse()

    async with SkillsCategoriesORM() as orm: skills_categories = await orm.find_many()
    async with SkillsORM() as orm:
        for category in skills_categories:
            skills = await orm.find_many(skill_category_id = category.id)

            skill_data = Skills(title = category.title)
            skill_data.skills = [Skill(**skill.dict()) for skill in skills]

            data.skills.append(skill_data)

    async with ExperiencesORM() as orm: experiences = await orm.find_many()
    data.experiences = [Experience(**experience.dict()) for experience in experiences]

    async with ProjectsORM() as orm: projects = await orm.find_many()
    data.projects = [Project(**project.dict()) for project in projects]

    async with SocialNetworksORM() as orm: social_networks = await orm.find_many()
    data.social_networks = [SocialNetwork(**social_network.dict()) for social_network in social_networks]

    return data
