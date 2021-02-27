# https://practice.geeksforgeeks.org/problems/3b76f77c1b2107f809b1875aa9fe929ce320be97/1/?track=30-DOC-day-7&batchId=320#
from itertools import combinations

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

import os

path = "path to file"
df_list = []
for filename in os.listdir(path):
    if filename.endswith(".csv"): # This ensures that the code only read csv files
        filename_list = filename.split(".")
        # filename_list = filename.split(".") when split() is used on string, it turns it to list. Hence we have filename_list = ["file_name", "csv"] for each file name
        df_name = filename_list[0]
        df = spark.read.csv(path+filename, inferSchema=True, header=True) # filename here will reference the actual filname.csv before we splitted it
        df.name =df_name # after reading in each csv in the immediate above code, this line renames it to its own name. Hence df above is a temporary place holder for each dataframe
        df_list.append(df_name) # we are just appending the names of the dataframe here, nothing more
        exec(df_name + " = df")

# df_list

