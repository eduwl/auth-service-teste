from typing import Union
from pydantic import BaseModel

class User(BaseModel):
    username: Union[str, None]
    role: Union[str, None]
    password: Union[str, None]
