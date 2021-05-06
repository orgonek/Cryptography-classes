from fastapi import FastAPI
from block import Blockchain
from uuid import uuid4
from fastapi.responses import JSONResponse

app = FastAPI()

blockchain = Blockchain()

# Global unique address
GLOBAL_RECIPIENT = str(uuid4()).replace('-', '')
BLOCK_REWARD = 10


@app.get('/api/status')
def get_status():
    if blockchain:
        return {'Status': 'Blockchain working correctly'}

    return {'Status': 'Not working'}


@app.get('/api/mine')
def mine():
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block)
    blockchain.new_transaction(
        sender='Block Reward',
        recipient=GLOBAL_RECIPIENT,
        amount=BLOCK_REWARD
    )

    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    context = {
        'message': 'New block created',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],

    }
    return JSONResponse(content=context)


@app.get('/api/chain')
def chain():
    context = {
        'Length of chain': len(blockchain.chain),
        'Chain content': blockchain.chain,
    }

    return JSONResponse(content=context)

