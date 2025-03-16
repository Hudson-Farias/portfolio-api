from pydantic import BaseModel
from typing import Optional, List


class Project(BaseModel):
    git_id: int
    name: str
    html_url: str
    homepage: Optional[str] = None


class Projects(BaseModel):
    visible: List[Project] = []
    options: List[Project] = []
