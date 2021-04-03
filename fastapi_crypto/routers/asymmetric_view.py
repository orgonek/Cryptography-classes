from fastapi import APIRouter
from utils.asymmetric_cryptography import Asymmetric

from models import KeysInfo, MessageSignature, MessageInfo

router = APIRouter(
    prefix='/api/asymmetric',
    tags=['asymmetric'],
    responses={404: {'description': 'Not found'}},
)


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
async def verify_message(data: MessageSignature):
    algorithm.verify_message(data.content, data.signature)


@router.post('/sign')
async def sign_message(data: MessageInfo):
    data.content = algorithm.sign_message(data.content)
    return data


@router.post('/encode')
async def encode_message(message: MessageInfo):
    message.content = algorithm.encode_message(message.content)
    return message


@router.post('/decode')
async def decode_message(message: MessageInfo):
    message.content = algorithm.decode_message(message.content)
    return message
