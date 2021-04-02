from fastapi import APIRouter

router = APIRouter(
    prefix='/api/asymmetric',
    tags=['asymmetric'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/key')
async def get_keys():
    pass


@router.get('/key/ssh')
async def get_keys_ssh():
    pass


@router.post('/key')
async def set_keys():
    pass


@router.post('/verify')
async def verify_message():
    pass


@router.post('/sign')
async def sign_message():
    pass


@router.post('/encode')
async def encode_message():
    pass


@router.post('/decode')
async def decode_message():
    pass
