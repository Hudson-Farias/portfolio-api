from pydantic import BaseModel
from typing import Optional


class Project(BaseModel):
    name: str
    html_url: str
    homepage: Optional[str] = None
    private: bool
