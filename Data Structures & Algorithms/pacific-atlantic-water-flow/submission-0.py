class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:



        pac = set()
        atl = set()
        row = len(heights)
        col = len(heights[0])


        def dfs(r,c,visit,prev):

            if r < 0 or c < 0 or r == row or c == col or (r,c) in visit or heights[r][c] < prev : 

                return 

            visit.add((r,c))
            dfs(r -1,c,visit,heights[r][c])
            dfs(r,c -1 ,visit,heights[r][c])
            dfs(r + 1 ,c,visit,heights[r][c])
            dfs(r,c + 1 ,visit,heights[r][c])
            
        

        

        for i in range(col) :

            dfs(0,i,pac,heights[0][i]) 
            dfs(row-1,i,atl,heights[row-1][i])

        for j in range(row):

            dfs(j,0,pac,heights[j][0])
            dfs(j,col-1,atl,heights[j][col-1])
        

        res = []

        for r in range(row):

            for c in range(col ):

                if (r,c) in pac and (r,c) in atl :

                    res.append((r,c))


        return res 




