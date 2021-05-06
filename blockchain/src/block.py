from time import time
import hashlib
import json


class Blockchain:
    def __init__(self):
        self.current_transactions = []
        self.chain = []
        self.new_block(proof=1000, previous_hash='First here')

    def new_block(self, proof: int, previous_hash: str = None) -> dict:
        """
        Creates a new block in the Blockchain

        Args:
            proof: Received from proof of work algorithm
            previous_hash: Hash of previous block

        Returns:
            block: Created block
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.chain.append(block)
        self.current_transactions = []
        return block

    def new_transaction(self, sender: str, recipient: str, amount) -> int:
        """
        Creates a transaction to be included in the next mined block

        Args:
            sender: Address of sender
            recipient: Address of recipient
            amount: Amount sent in transaction

        Returns:
              index: Index of block which will contain this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block: dict) -> str:
        """
        Creates SHA-256 hash of block

        Args:
            block: Block to be hashed
        """

        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """
        Returns: Last block in chain
        """
        return self.chain[-1]

    def proof_of_work(self, block) -> int:
        """
        Proof of work algorithm implementation
        """

        last_proof = block['proof']
        proof = 0

        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates if hash contain 4 zeros on the beginning
        Args:
            last_proof: Previous proof
            proof: Current proof
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == '0000'



