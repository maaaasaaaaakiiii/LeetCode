class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        list_J = [s for s in J]
        for Stone in S:
            if Stone in list_J:
                count += 1

        return count