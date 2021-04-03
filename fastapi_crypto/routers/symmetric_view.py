from fastapi import APIRouter, Form, HTTPException
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
    if not algorithm.set_key(item.value):
        raise HTTPException(status_code=422, detail='Incorrect value of key')
    return item


@router.post('/encode')
async def encode_message(message: MessageInfo):
    encrypted_message = algorithm.encode_message(message.content)
    if encrypted_message == message.content:
        raise HTTPException(status_code=422, detail='Entered data is incorrect')

    message.content = encrypted_message
    return message



@router.post('/decode')
async def decode_message(message: MessageInfo):
    decrypted_message = algorithm.decode_message(message.content)
    if decrypted_message == message.content:
        raise HTTPException(status_code=422, detail='Entered data is incorrect')

    message.content = decrypted_message
    return message


@router.post('/key/form')
async def form(key: str = Form(...)):
    algorithm.set_key(key)

    return {"The current value of the key": key}
