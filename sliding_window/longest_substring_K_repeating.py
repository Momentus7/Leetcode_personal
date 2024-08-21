class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        unique=len(set(s))
        n=len(s)
        res=0
        

        for curr_iter in range(1,unique+1):

            count=defaultdict(int)
            left=0

            for right in range(n):

                count[s[right]]+=1

                while len(count)>curr_iter:
                    count[s[left]]-=1

                    if count[s[left]]==0:
                        del count[s[left]]
                    
                    left+=1
                
                every_counts_greater_than_k=True

                for cnt in count.values():

                    if cnt<k:
                        every_counts_greater_than_k=False
                        break
                
                if every_counts_greater_than_k:

                    res=max(res,right-left+1)
        return res
                

        

        
        