class Solution:
    def minimumCost(self, s: str) -> int:
        strlen = len(s)
        mid = strlen // 2
        midval = s[mid]
        
        cost = 0
        
        
        inversions = 0
        for i in range(mid - 1, -1, -1):
            if s[i] == s[mid]:
                if inversions % 2 == 0:
                    continue
                else:
                    cost += i + 1
                    inversions += 1
                    print(i + 1)
            else:
                if inversions % 2 == 0:
                    cost += i + 1
                    inversions += 1
                else:
                    continue
        
        inversions = 0
        for i in range(mid + 1, strlen):
            if s[i] == s[mid]:
                if inversions % 2 == 0:
                    continue
                else:
                    cost += strlen - i
                    inversions += 1
            else:
                if inversions % 2 == 0:
                    cost += strlen - i
                    inversions += 1
                else:
                    continue
                    
        return cost
        

