from fastapi import APIRouter
from utils.symmetric_cryptography import Symmetric
from models import KeyInfo, MessageInfo

router = APIRouter(
    prefix='/api/symmetric',
    tags=['symmetric'],
    responses={404: {'description': 'Not found'}},
)

algorithm = Symmetric()


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
