from block import Blockchain
from time import time


class TestBlockchain:

    def test_instance(self):
        b = Blockchain()
        assert type(b) is Blockchain

    def test_block_creation(self):
        b = Blockchain()
        assert len(b.chain) > 0

    def test_new_transaction(self):
        b = Blockchain()
        assert b.new_transaction('A', 'B', 2) == b.last_block['index'] + 1

    def test_hash(self):
        block = {
            'index': 1,
            'timestamp': time(),
            'transactions': [],
            'proof': 100,
            'previous_hash': 0,
        }
        assert Blockchain.hash(block) is not block

    def test_last_block(self):
        b = Blockchain()
        assert b.last_block == b.chain[-1]
