from pydantic import BaseModel
from typing import List


class SocialNetwork(BaseModel):
    id: int
    url: str
    icon: str


class SocialNetworks(BaseModel):
    social_networks_header: List[SocialNetwork] = []
    social_networks_footer: List[SocialNetwork] = []
