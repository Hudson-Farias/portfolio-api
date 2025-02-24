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
    title: str
    description: str
    image_url: Optional[str] = None
    live_url: str
    repo_url: str


class SocialNetwork(BaseModel):
    id: int
    url: str
    icon: str



class ModelResponse(BaseModel):
    skills: List[Skills] = []
    experiences: List[Experience] = []
    projects: List[Project] = []
    social_networks: List[SocialNetwork] = []
