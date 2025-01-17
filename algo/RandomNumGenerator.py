# Implement congruential random number generator
from typing import List
import time
class SimpleRandom:
    def __init__(self, seed:int=None):
        if seed is None:
            seed = int(time.time())
        self.seed = seed
        self.multiplier = 166425
        self.increment = 1013904223
        self.n_steps = 2**32

    def next(self) -> float:
        self.seed = (self.multiplier * self.seed + self.increment) % self.n_steps
        return self.seed / self.n_steps

    def randint(self, low:int, high:int) -> float:
        if low > high:
            raise Exception("Low value greater than high not allowed")
        rand = self.next()
        return low + int(rand * (high-low + 1))      

    def uniform(self, low:float, high:float)-> float:
        if low > high:
            raise Exception("Low value greater than high not allowed")
        rand = self.next()
        return low + rand * (high - low)
    

    def choice(self, seq:List):
        if not seq:
            raise ValueError("Sequence cannot be empty")
        index = self.randint(0, len(seq) - 1)
        return seq[index]

import unittest

class Tests(unittest.TestCase):
    def test_rand_int(self):
        randg = SimpleRandom()
        for i in range(29):
            self.assertLess(0, randg.randint(1,100))    
            self.assertGreaterEqual(100, randg.randint(1,100))    
    
    def test_uniform(self):
        randg = SimpleRandom()
        for i in range(29):
            self.assertLess(0, randg.uniform(0,1.))    
            self.assertGreaterEqual(1, randg.uniform(0,1.))    
    
            
if __name__ == "__main__":
    unittest.main()

    


