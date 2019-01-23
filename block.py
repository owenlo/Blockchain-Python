'''Class which represents an individual block'''
import time, hashlib

class Block:

    def __init__(self, index, data, prevhash, difficulty):
        self._index = index
        self._data = data
        self._hash = None
        self._prevhash = prevhash
        self._timestamp = str(time.time())
        self._difficulty = difficulty
        self._nonce = None
        self._performance = None
        
        self.mine()
        
    def mine(self):
        '''Mining operation which is conducted when a new block is instantiated.'''
        nonce = 0
        
        start_time = time.perf_counter()
        result = hashlib.sha256((self._index + self._prevhash + self._timestamp + self._data + str(nonce)).encode()).hexdigest()
        
        while result.startswith(self._difficulty*'0') == False:
            nonce += 1
            result = hashlib.sha256((self._index + self._prevhash + self._timestamp + self._data + str(nonce)).encode()).hexdigest()
        stop_time = time.perf_counter()
    
        self._nonce = nonce
        self._hash = result
        self._performance = stop_time - start_time

        
    @property
    def data(self):
        '''Block data'''
        return self._data

    @property
    def index(self):
        '''Index of block'''
        return self._index

    @property
    def hash(self):
        '''Hash of block'''
        return self._hash

    @property
    def prevhash(self):
        '''Hash of previous block'''
        return self._prevhash
    
    @property
    def difficulty(self):
        '''Difficulty of mining operation'''
        return self._difficulty

    @property
    def timestamp(self):
        '''Timestamp when block was created'''
        return self._timestamp

    @property
    def nonce(self):
        '''Nonce when block was created'''
        return self._nonce

    @property
    def performance(self):
        '''Time taken to perform mining operation'''
        return self._performance
