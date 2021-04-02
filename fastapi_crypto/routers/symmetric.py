from fastapi import APIRouter

router = APIRouter(
    prefix='/api/symmetric',
    tags=['symmetric'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/key')
async def get_key():
    pass


@router.post('/key')
async def set_key():
    pass


@router.post('/encode')
async def encode_message():
    pass


@router.post('/decode')
async def decode_message():
    pass
