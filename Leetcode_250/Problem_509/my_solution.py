class Solution:
    def fib(self, N: int) -> int:
        lastlast, last = 0,1
        for _ in range(N):
            lastlast, last = last, last+lastlast
        return lastlast 