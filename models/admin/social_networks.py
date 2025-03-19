from pydantic import BaseModel

class SocialNetworkDTO(BaseModel):
    url: str
    icon: str
    show_header: bool
    show_footer: bool


class SocialNetwork(SocialNetworkDTO):
    id: int
