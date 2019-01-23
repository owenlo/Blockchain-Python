'''Example blockchain implemented in Python.'''
import hashlib, block
import numpy as np
#import matplotlib.pyplot as plt #Include this import and remove comments on plot(...) function to enable real-time plotting of time taken to mine each block. Note that the code for plotting is quite buggy....

difficulty = 5 #Difficulty of mining operation. Using the example of 5 means that the first five hex values of a hash should be 0 to be considered the correct solution.

def main():
    #Instantiating a block requires (index, data, previous hash, difficulty)
    b = block.Block(str(0), 'This is my genesis block data', '0', difficulty)
    printResult(b)
    #plot(b.index, b.performance) 
    
    for i in range(1, 100): #We mine 100 blocks in this example code (including genesis).
        b = block.Block(str(i),'This is the blocks which follow genesis + i (i is just arbitrary data)' + str(i), b.hash , difficulty)                 
        printResult(b)
        #plot(b.index, b.performance) #Remove comment to enable real-time plotting of time taken to mine each block. Note that the code for plotting is quite buggy....

def printResult(block):
    #Print the results for each mined block. Nonce is the solution found. Only the final 6 hex values of previous hash is shown for brevity. The genesis block has a previous hash value of 0.
    print(f"Block {block.index} mined. Hash = {block.hash}. Nonce = {block.nonce}. Previous Hash = ...{block.prevhash[-6:]}") 
    

def plot(index, time):
    plt.scatter(index, time, linestyle='-', marker='o')
    plt.pause(0.05)
    
if __name__ == "__main__":
    main()
