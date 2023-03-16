d1 = {"key" : "value"}
d2 = {"key" : {"key1" : "value"}}
d3 = {"key":[{"key2":["this deep",["hello"]]}]}

print(d3["key"][0]["key2"][1][0])

g = [1,2,4,5,6,7,1,2,3,8,9,10]

for ind in range(0,len(g)):
    if g[ind] == 1 and g[ind+1] == 2 and g[ind+2] == 3:
        print("Found")

