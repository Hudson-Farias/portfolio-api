from fastapi import Depends
from routers.admin import router, has_authenticated

from database.social_networks import SocialNetworksORM

from models.admin.social_networks import *

from typing import List


async def response_data() -> List[SocialNetwork]:
    async with SocialNetworksORM() as orm: social_networks = await orm.find_many()
    data = [SocialNetwork(**social_network.dict()) for social_network in social_networks]

    return data


@router.get('/social_networks', status_code = 200, response_model = List[SocialNetwork])
async def get():
    return await response_data()


@router.post('/social_networks', status_code = 201, response_model = List[SocialNetwork])
async def post(params: SocialNetworkDTO, _: bool = Depends(has_authenticated)):
    async with SocialNetworksORM() as orm: await orm.create(**params.dict())
    return await response_data()


@router.put('/social_networks/{social_network_id}', status_code = 201, response_model = List[SocialNetwork])
async def put(social_network_id: int, params: SocialNetworkDTO, _: bool = Depends(has_authenticated)):
    async with SocialNetworksORM() as orm: await orm.update(id = social_network_id, **params.dict())
    return await response_data()



@router.delete('/social_networks/{social_network_id}', status_code = 201, response_model = List[SocialNetwork])
async def delete(social_network_id: int, _: bool = Depends(has_authenticated)):
    async with SocialNetworksORM() as orm: await orm.delete(id = social_network_id)
    return await response_data()
