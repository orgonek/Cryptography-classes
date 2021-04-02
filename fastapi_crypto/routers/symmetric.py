from fastapi import APIRouter
from pydantic.main import BaseModel
from utils.symmetric_cryptography import Symmetric
from typing import Optional

router = APIRouter(
    prefix='/api/symmetric',
    tags=['symmetric'],
    responses={404: {'description': 'Not found'}},
)

algorithm = Symmetric()


class KeyInfo(BaseModel):
    value: str
    description: Optional[str] = None


class MessageInfo(BaseModel):
    value: str
    description: Optional[str] = None


@router.get('/key')
async def get_random_key():
    return {"generated key": algorithm.create_key()}


@router.post('/key')
async def set_key(item: KeyInfo):
    algorithm.set_key(item.value)
    return item


@router.post('/encode')
async def encode_message(message: MessageInfo):
    message.value = algorithm.encode_message(message.value)
    return message


@router.post('/decode')
async def decode_message(message: MessageInfo):
    message.value = algorithm.decode_message(message.value)
    return message
