from pydantic.main import BaseModel
from typing import Optional


class KeyInfo(BaseModel):
    value: str
    description: Optional[str] = None


class KeysInfo(BaseModel):
    public_key: str
    private_key: str
    description: Optional[str]


class MessageInfo(BaseModel):
    content: str
    description: Optional[str]


class MessageSignature(MessageInfo):
    signature: str


