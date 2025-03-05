from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from typing import Optional
from httpx import get

from env import AUTH_APP_URL


router = APIRouter(prefix = '/admin')


async def partial_authenticated(request: Request, auth: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error = False))):
    token = auth.credentials if auth else request.cookies.get('HOST_OWNER_TOKEN')

    response = get(f'{AUTH_APP_URL}/verify?token={token}')
    if response.status_code != 204: return False
    return True


async def has_authenticated(request: Request, auth: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer(auto_error = False))):
    is_auth = await partial_authenticated(request, auth)
    if not is_auth: raise HTTPException(status_code = 498, detail = 'Token invalid')
    return True
