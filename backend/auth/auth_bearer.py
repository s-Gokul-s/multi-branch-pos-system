from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from fastapi import Depends

from auth.auth_handler import verify_acess_token


auth_scheme = HTTPBearer()


def get_current_user(
        
        token: HTTPAuthorizationCredentials = Depends(auth_scheme)
):
    

    return verify_acess_token(token.credentials)
    
