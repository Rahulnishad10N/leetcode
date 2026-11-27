class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)

        prev1=1
        prev2=1

        for i in range(n-1,-1,-1):
            if s[i]=='0':
                curr=0
                prev1=prev2
                prev2=curr
                continue
            choice1=prev2
            choice2=0

            if i+1<n and int(s[i:i+2]) <=26:
                choice2=prev1

            curr= choice1+choice2 
            prev1=prev2
            prev2=curr   

        

        return prev2        
        