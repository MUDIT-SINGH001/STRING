def longestPrefix(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            if(i!=len(s)-1):
                if(s[:i+1] == s[len(s)-i-1:]):
                   
                    if len(s[:i+1])>len(ans):
                        ans = ""
                        ans += s[:i+1]
        return ans
