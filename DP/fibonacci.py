class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0#top-bottom approach
        mem=[-1 for i in range(n+1)]
        mem[0]=0
        mem[1]=1
        def func(n):
            if mem[n]!=-1:
                return mem[n]
            mem[n]= func(n-1)+func(n-2)
            return mem[n]
        return func(n)