from fastapi import APIRouter, Form, HTTPException, Request
from utils.symmetric_cryptography import Symmetric
from models import KeyInfo, MessageInfo
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix='/api/symmetric',
    tags=['symmetric'],
    responses={404: {'description': 'Not found'}},
)

algorithm = Symmetric()
templates = Jinja2Templates(directory='templates')


@router.get('/key')
async def get_random_key():
    return {"generated key": algorithm.create_key()}


@router.post('/key/set')
async def set_key(key: str = Form(...)):
    if not algorithm.set_key(key):
        raise HTTPException(status_code=422, detail='Incorrect value of key')
    return {"Actual key value": key}


@router.get('/key/set')
async def set_key(request: Request):
    return templates.TemplateResponse('form_key.html', context={'request': request})


@router.post('/encode')
async def encode_message(message: str = Form(...)):
    encrypted_message = algorithm.encode_message(message)
    if encrypted_message == message:
        raise HTTPException(status_code=422, detail='Entered data is incorrect')

    return {"Encrypted message": encrypted_message}


@router.get('/encode')
async def encode_message(request: Request):
    return templates.TemplateResponse('form_symmetric.html', context={'request': request, 'path': '/api/symmetric/encode'})


@router.post('/decode')
async def decode_message(message: str = Form(...)):
    decrypted_message = algorithm.decode_message(message)
    if decrypted_message == message:
        raise HTTPException(status_code=422, detail='Entered data is incorrect')

    return {"Decrypted message": decrypted_message}


@router.get('/decode')
async def decode_message(request: Request):
    return templates.TemplateResponse('form_symmetric.html', context={'request': request, 'path': '/api/symmetric/decode/'})

