class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        n=len(players)
        m=len(trainers)
        players.sort()
        trainers.sort()
        i=0
        j=0
        ans=0
        while i<n and j<m:
            if players[i]<=trainers[j]:
                ans+=1
                i+=1
                j+=1
            else:
                j+=1

        return ans            
        