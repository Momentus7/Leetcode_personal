        
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def func(ind,res):
            if len(digits)==ind:
                resl.append(res[:])
                return
            for i in d[digits[ind]]:
                func(ind + 1,res + i)
        
        resl=[]
        func(0,"")
        return resl