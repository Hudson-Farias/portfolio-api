from pydantic import BaseModel
from typing import List, Optional


class Skill(BaseModel):
    id: int
    name: str
    icon: str


class Skills(BaseModel):
    title: str
    skills: List[Skill] = []


class Experience(BaseModel):
    id: int
    company: str
    period: str
    role: str
    description: str


class Project(BaseModel):
    id: int
    name: str
    description: Optional[str] = ''
    image_url: Optional[str] = None
    homepage: Optional[str] = None
    html_url: Optional[str] = None


class ModelResponse(BaseModel):
    skills: List[Skills] = []
    experiences: List[Experience] = []
    projects: List[Project] = []
