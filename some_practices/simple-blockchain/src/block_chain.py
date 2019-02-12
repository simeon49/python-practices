import time
from block import Block

block_chain = [Block.create_genesis_block()]

num_blocks_to_add = 10
for i in range(1, num_blocks_to_add + 1):
    block_chain.append(Block(block_chain[-1].hash, 'number {} of block'.format(i), int(time.time())))
