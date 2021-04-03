from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.templating import Jinja2Templates

from utils.asymmetric_cryptography import Asymmetric

router = APIRouter(
    prefix='/api/asymmetric',
    tags=['asymmetric'],
    responses={404: {'description': 'Not found'}},
)

algorithm = Asymmetric()
templates = Jinja2Templates(directory='templates')


@router.get('/keys')
async def get_keys():
    return algorithm.create_keys()


@router.get('/keys/ssh')
async def get_keys_ssh():
    return algorithm.create_ssh_keys()


@router.post('/keys/set')
async def set_keys(public_key: str = Form(...), private_key: str = Form(...)):
    if not algorithm.set_keys(public_key, private_key):
        raise HTTPException(status_code=422, detail='Incorrect keys data')

    return {"current public key": public_key, "Current private key": private_key}


@router.get('/keys/set', include_in_schema=False)
async def set_keys(request: Request):
    return templates.TemplateResponse('form_keys_asymmetric.html', context={'request': request})


@router.post('/verify')
async def verify_message(message: str = Form(...), signature: str = Form(...)):
    if not algorithm.verify_message(message, signature):
        raise HTTPException(status_code=422, detail='Incorrect data provided')

    return {'Message signature': 'verified'}


@router.get('/verify', include_in_schema=False)
async def verify_message(request: Request):
    return templates.TemplateResponse('form_verify.html', context={'request': request})


@router.post('/sign')
async def sign_message(message: str = Form(...)):
    signature = algorithm.sign_message(message)
    if message == signature:
        raise HTTPException(status_code=422, detail='Incorrect data provided')

    return {'Signature ': signature}


@router.get('/sign', include_in_schema=False)
async def sign_message(request: Request):
    return templates.TemplateResponse('form_data.html', context={'request': request, 'path': '/api/asymmetric/sign'})


@router.post('/encode')
async def encode_message(message: str = Form(...)):
    encrypted_message = algorithm.encode_message(message)

    if message == encrypted_message:
        raise HTTPException(status_code=422, detail='Incorrect data provided')

    return {'Encrypted message': encrypted_message}


@router.get('/encode',include_in_schema=False)
async def encode_message(request: Request):
    return templates.TemplateResponse('form_data.html', context={'request': request, 'path': '/api/asymmetric/encode'})


@router.post('/decode')
async def decode_message(message: str = Form(...)):
    decrypted_message = algorithm.decode_message(message)

    if message == decrypted_message:
        raise HTTPException(status_code=422, detail='Incorrect data provided')

    return {'Decrypted message': decrypted_message}


@router.get('/decode', include_in_schema=False)
async def decode_message(request: Request):
    return templates.TemplateResponse('form_data.html', context={'request': request, 'path': '/api/asymmetric/decode'})