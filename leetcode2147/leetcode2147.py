class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = 0
        plants = 0
        ans = 1
        for c in corridor:
            if c == 'S':
                seats += 1
                if seats == 3:  
                    ans = ans * (plants + 1) % MOD
                    seats = 1    
                    plants = 0
            else:
                if seats == 2:   
                    plants += 1
        return ans if seats == 2 else 0
        
