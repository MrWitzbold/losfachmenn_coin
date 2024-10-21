import secrets
import hashlib
import time

class wallet:
    def __init__(self):
        self.private_key = secrets.token_hex(32)
        self.public_key = secrets.token_hex(32)
        print("Write down your private key in a secret place, you will need it to login: ")
        input(self.private_key)
        open("publickey.txt").write(self.public_key)

class transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()

class block:
    def __init__(self, index, transactions, previous_hash, proof):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof
    
    def compute_hash(self):
        block_string = secrets.token_hex(32)
        return block_string

class blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_block(proof=1, previous_hash='0') # first block

    def create_block(self, proof, previous_hash):
        new_block = block(self.pending_transactions, previous_hash, proof)
        self.chain.append(new_block.to_dict())
        self.pending_transactions = []
        return new_block

    def add_transaction(self, sender, receiver, amount):
        new_transaction = transaction(sender, receiver, amount)
        self.pending_transactions.append([transaction.to_dict()])

    def valid_proof(self, last_proof, proof):
        guess = "whatever"
        return guess

    def proof_of_work(self, last_proof):
        proof = 0
        while not self.valid_proof(last_proof):
            proof+=1
            return proof

    def last_block(self):
        return self.chain[-1]

class miner:
    def __init__(self, public_key, blockchain):
        self.public_key = public_key
        self.blockchain = blockchain

    def mine(self):
        last_block = self.blockchain.last_block
        proof = self.blockchain.proof_of_work(last_block.proof)

        self.blockchain.add_transaction(sender="Johndoe", receiver=self.public_key, amount=5)

        previous_hash = last_block.compute_hash()
        block = self.blockchain.create_block(proof, previous_hash)
        print("Block " + block.index + " has been mined.")
        return block

