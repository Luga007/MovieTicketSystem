from pydantic import BaseModel

class RoleCreate(BaseModel):
    name: str

class RoleOut(BaseModel):
    role_id: int
    name: str

    class Config:
        from_attributes = True