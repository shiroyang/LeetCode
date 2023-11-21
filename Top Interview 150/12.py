import random
class RandomizedSet:

    def __init__(self):
        self.myset = set()

    def insert(self, val: int) -> bool:
        if val in self.myset:
            return False
        else:
            self.myset.add(val)
            return True
    def remove(self, val: int) -> bool:
        if val in self.myset:
            self.myset.discard(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        ls = list(self.myset)
        return random.choice(ls)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()