import sys
import time
from struct import pack, unpack
import hashlib


class Block:

    def __init__(self, previous_block_hash, data, timestamp, throttle=1000000):
        self.previous_block_hash = previous_block_hash
        self.data = data
        self.timestamp = timestamp  # 开始产生区块的时间戳
        self.nonce = 0
        self.throttle = throttle    # 相当于比特币中的难度
        self.hash = ''
        self.pack()

    def pack(self):
        start = time.time()
        guess = 999999999999999999999
        payload = '{}{}{}'.format(self.previous_block_hash,
                                  self.data, self.previous_block_hash)
        target = 2**64 / self.throttle  # 8个字节的整数最大值 （2^64）除以难度（throttle ）
        nonce = 0
        while guess > target:
            nonce += 1
            inner_hash = hashlib.sha256(pack('>Q', nonce) + payload.encode('utf-8'))
            outer_hash = hashlib.sha256(inner_hash.digest())
            guess, = unpack('>Q', outer_hash.digest()[0:8])
        end = time.time()
        self.nonce = nonce
        self.hash = outer_hash.hexdigest()
        print('pack finished, time use: {}, nonce: {}, hash: {}'.format((end - start), self.nonce, self.hash))

    @staticmethod
    def create_genesis_block():
        return Block('0', 'this is genesis data.', int(time.time()))

if __name__ == '__main__':
    block = Block('0', 'this is genesis data.', int(time.time()))
    print(block.hash)
