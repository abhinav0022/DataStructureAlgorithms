class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        #dynamic programing
        red = [costs[i][0] for i in range(len(costs))] #0
        blue = [costs[i][1] for i in range(len(costs))] #1
        green = [costs[i][2] for i in range(len(costs))] #2
        last = len(costs) - 1
        r, g, b = red[last], green[last], blue[last]

        for i in range(len(costs) - 2, -1, -1):
            tempr, tempb, tempg = r, b, g
            r = red[i] + min(tempb, tempg)
            b = blue[i] + min(tempg, tempr)
            g = green[i] + min(tempr, tempb)

        return min(r, g, b)        
        '''
        #memoization
        red = [costs[i][0] for i in range(len(costs))] #0
        blue = [costs[i][1] for i in range(len(costs))] #1
        green = [costs[i][2] for i in range(len(costs))] #2
        dp = {} #key is house index and color index



        def minPaintCost(i, color):
            if i >= len(costs):
                return 0
            if (i, color) in dp:
                return dp[(i, color)]
            res = -1
            if color == 0:
                res = red[i] + min((minPaintCost(i + 1, 1)), (minPaintCost(i + 1, 2)))
            if color == 1:
                res = blue[i] + min((minPaintCost(i + 1, 0)), (minPaintCost(i + 1, 2)))
            if color == 2:
                res = green[i] + min((minPaintCost(i + 1, 0)), (minPaintCost(i + 1, 1)))

            dp[(i, color)] = res
            
            return res
        
        return min(minPaintCost(0, 0), minPaintCost(0, 1), minPaintCost(0, 2))

        '''
        '''
        # pure recursive solution
        red = [costs[i][0] for i in range(len(costs))] #0
        blue = [costs[i][1] for i in range(len(costs))] #1
        green = [costs[i][2] for i in range(len(costs))] #2


        def minPaintCost(i, prevColor):
            if i >= len(costs):
                return 0
            
            if prevColor == "blue":
                res = min(red[i] + minPaintCost(i + 1, "red"), green[i] + minPaintCost(i + 1, "green"))
            if prevColor == "green":
                res = min(red[i] + minPaintCost(i + 1, "red"), blue[i] + minPaintCost(i + 1, "blue"))
            if prevColor == "red":
                res = min(blue[i] + minPaintCost(i + 1, "blue"), green[i] + minPaintCost(i + 1, "green"))
            
            return res
        
        return min(minPaintCost(0, "red"), minPaintCost(0, "blue"), minPaintCost(0, "green"))
        '''