from uuid import UUID

import pydantic


# class User(pydantic.BaseModel, extra="allow"):
#     id: UUID
#     email: pydantic.EmailStr
#     first_name: str
#     last_name: str
#     created_at: pydantic.PastDatetime
