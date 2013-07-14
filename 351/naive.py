import time
start = time.time()
dic = {}
n = 1000
count =0
for height in range(2,n+1):
        leftovers = 0
        if height in dic:
                leftovers = height - dic[height]-1
        else:
                leftovers = height - 1
        for x in range(height, n+1, height):
                if x in dic:
                        dic[x] += leftovers
                else:
                        dic[x] = leftovers
        count +=height-leftovers-1
count +=n-1
count*=6
print(count)
print(time.time() - start)

