'''
link: https://leetcode.com/problems/insert-delete-getrandom-o1/
Q380. Insert Delete GetRandom O(1)

Approach:
The key approach involves utilizing a set for efficient membership checks, insertions, and removals.
The getRandom method converts the set to a list for random access, enabling the selection of a random element in constant time.

⏰ TC: O(N): where N is total calls for Insert, Remove & Get-Random operations.
🚀 SC: O(1): at most set can have both 1 and 2, which is constant.
'''

class RandomizedSet:

    def __init__(self):
        self.set = set()  # Initialize an empty set.

    def insert(self, val: int) -> bool:
        # Insert value into the set. Return False if already exists.
        if val in self.set: return False  
        self.set.add(val)
        return True

    def remove(self, val: int) -> bool:
        # Remove value from the set. Return False if doesn't exist.
        if val not in self.set: return False  
        self.set.remove(val)
        return True

    def getRandom(self) -> int:
        # Return a random element from the set.
        return random.choice(list(self.set))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
