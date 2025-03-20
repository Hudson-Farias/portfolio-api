from pydantic import BaseModel
from typing import List


class SkillDTO(BaseModel):
    name: str
    icon: str
    skill_category_id: int


class Skill(SkillDTO):
    id: int
    skill_category_name: str


class SkillCategory(BaseModel):
    id: int
    title: str


class SkillsResponse(BaseModel):
    skills: List[Skill] = []
    categories: List[SkillCategory] = []
