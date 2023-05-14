class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        losers = [True for i in range(n)]
        last_turn = 0
        losers[0] = False
        i = 0
        while True:
            i += k
            last_turn = (last_turn + i) % n
            if losers[last_turn]:
                losers[last_turn] = False
            else:
                break
        final_losers = []
        for i in range(n):
            if losers[i]:
                final_losers.append(i + 1)
        return final_losers
