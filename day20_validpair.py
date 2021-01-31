# https://practice.geeksforgeeks.org/problems/3b76f77c1b2107f809b1875aa9fe929ce320be97/1/?track=30-DOC-day-7&batchId=320#


# Solution 1
 def ValidPair(self, a, n): 
    	c = [[k, v] for k,v in combinations(a, 2)]
        count = 0
        for item in c:
            if item[0] != item[-1] and (item[0] + item[-1])> 0:
                count +=1
            count += 0
        return count

# Solution 2
def ValidPair(self, a, n): 
    	c = [1 for (k,v) in combinations(a, 2) if k != v and k + v > 0]
        return sum(c)

