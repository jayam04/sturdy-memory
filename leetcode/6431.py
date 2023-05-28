class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        if n == 1:
            return not derived[0]
        arr = [0 for i in range(n)]
        for i in range(n - 1):
            if derived[i]:
                arr[i + 1] = (arr[i] + 1) % 2
            else:
                arr[i + 1] = arr[i]
        if derived[-1]:
            if arr[0] == arr[-1]:
                return False
            return True
        else:
            if arr[0] == arr[-1]:
                return True
            return False
