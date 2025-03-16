from pydantic import BaseModel
from typing import Optional


class Project(BaseModel):
    git_id: Optional[int] = 0
    name: str
    html_url: str
    homepage: Optional[str] = None
    private: bool
    is_active: Optional[bool] = False
