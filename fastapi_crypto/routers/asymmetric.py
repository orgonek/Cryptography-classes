from fastapi import APIRouter
from utils.asymmetric_cryptography import Asymmetric
from pydantic.main import BaseModel
from typing import Optional

router = APIRouter(
    prefix='/api/asymmetric',
    tags=['asymmetric'],
    responses={404: {'description': 'Not found'}},
)


class KeysInfo(BaseModel):
    public_key: str
    private_key: str
    description: Optional[str]


class MessageInfo(BaseModel):
    value: str
    description: Optional[str]


algorithm = Asymmetric()


@router.get('/key')
async def get_keys():
    return algorithm.create_keys()


@router.get('/key/ssh')
async def get_keys_ssh():
    return algorithm.create_ssh_keys()


@router.post('/key')
async def set_keys(items: KeysInfo):
    algorithm.set_keys(items.public_key, items.private_key)
    return items


@router.post('/verify')
async def verify_message():
    pass


@router.post('/sign')
async def sign_message(message: MessageInfo):
    message.value = algorithm.sign_message(message.value)
    return message


@router.post('/encode')
async def encode_message(message: MessageInfo):
    message.value = algorithm.encode_message(message.value)
    return message


@router.post('/decode')
async def decode_message(message: MessageInfo):
    message.value = algorithm.decode_message(message.value)
    return message
