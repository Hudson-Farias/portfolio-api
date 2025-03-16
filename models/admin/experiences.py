from pydantic import BaseModel


class ExperienceDTO(BaseModel):
    company: str
    period: str
    role: str
    description: str


class Experience(ExperienceDTO):
    id: int
