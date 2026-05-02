import hashlib, json, time, secrets
from dataclasses import dataclass, asdict
from typing import List, Dict

# --- Wallets ---
class Wallet:
    def __init__(self):
        self.private_key = secrets.token_hex(32)
        self.address = hashlib.sha256(self.private_key.encode()).hexdigest()[:40]

# --- Transactions ---
@dataclass
class Transaction:
    sender: str
    receiver: str
    amount: float
    timestamp: float

# --- Blocks ---
@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[dict]
    previous_hash: str
    nonce: int = 0
    hash: str = ''

    def compute_hash(self):
        data = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'transactions': self.transactions,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()

# --- Blockchain ---
class SimpleCoin:
    difficulty = 3

    def __init__(self):
        self.chain: List[Block] = []
        self.pending: List[Transaction] = []
        self.balances: Dict[str, float] = {}
        self.create_genesis_block()

    def create_genesis_block(self):
        block = Block(0, time.time(), [], '0')
        block.hash = block.compute_hash()
        self.chain.append(block)

    def create_wallet(self):
        w = Wallet()
        self.balances[w.address] = 100.0
        return w

    def get_balance(self, address):
        return self.balances.get(address, 0.0)

    def add_transaction(self, sender, receiver, amount):
        if self.get_balance(sender) < amount:
            raise ValueError('Insufficient funds')
        tx = Transaction(sender, receiver, amount, time.time())
        self.pending.append(tx)
        return tx

    def mine_pending(self):
        if not self.pending:
            return None
        txs = [asdict(t) for t in self.pending]
        block = Block(len(self.chain), time.time(), txs, self.chain[-1].hash)
        while True:
            h = block.compute_hash()
            if h.startswith('0' * self.difficulty):
                block.hash = h
                break
            block.nonce += 1
        self.chain.append(block)
        for tx in self.pending:
            self.balances[tx.sender] -= tx.amount
            self.balances[tx.receiver] = self.get_balance(tx.receiver) + tx.amount
        self.pending = []
        return block

if __name__ == '__main__':
    coin = SimpleCoin()
    alice = coin.create_wallet()
    bob = coin.create_wallet()

    print('Alice:', alice.address, 'Balance:', coin.get_balance(alice.address))
    print('Bob  :', bob.address, 'Balance:', coin.get_balance(bob.address))

    coin.add_transaction(alice.address, bob.address, 25)
    mined = coin.mine_pending()
    print('Mined block:', mined.index, mined.hash)

    print('Alice Balance:', coin.get_balance(alice.address))
    print('Bob Balance  :', coin.get_balance(bob.address))
