from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    username: str
    email: str
    # Add other fields as needed
