'''Example blockchain implemented in Python.'''
import hashlib, block
import numpy as np
import shelve

difficulty = 5 #Difficulty of mining operation. Using the example of 5 means that the first five hex values of a hash should be 0 to be considered the correct solution.

def main():
    
    b = loadState() #Load the last previous mined block if lastBlock.db file exists
    
    try:
        if b is None:
            #Instantiating a block requires (index, data, previous hash, difficulty)
            b = block.Block(str(0), 'This is my genesis block data', '0', difficulty)
            printResult(b)

        while(True):
            index = str(int(b.index) + 1)
            b = block.Block(index,'This is the blocks which follow genesis + i (i is just arbitrary data)' + index, b.hash , difficulty)                 
            printResult(b)

    except (KeyboardInterrupt, SystemExit):
        saveState(b)

def saveState(block):
    '''Try and save the state of the last mined block using the Python shelve module'''
    with shelve.open('lastBlock') as db:
        db['lastBlock'] = block

def loadState():
    '''Try and load the state of last mined block if file exists'''
    with shelve.open('lastBlock') as db:        
        block = db.get('lastBlock')
        if block is None:
            return None
        return block
                     
def printResult(block):
    #Print the results for each mined block. Nonce is the solution found. Only the final 6 hex values of previous hash is shown for brevity. The genesis block has a previous hash value of 0.
    print(f"Block {block.index} mined. Hash = {block.hash}. Nonce = {block.nonce}. Previous Hash = ...{block.prevhash[-6:]}") 
    
if __name__ == "__main__":
    main()
