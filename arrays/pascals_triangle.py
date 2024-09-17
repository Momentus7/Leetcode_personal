class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res=[]

        for i in range(numRows):
            if i==0:
                prev=[1]
                res.append(prev)
            else:
                curr=[1]
                j=1
                while j <i:
                    curr.append(prev[j-1]+prev[j])
                    j+=1
                curr.append(1)
                res.append(curr)
                prev=curr
        return res
