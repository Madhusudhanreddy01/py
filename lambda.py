li  = [10,50,67,40,23,4,66,77]
maxi = (max(li))
indef = li.index(maxi)
print(maxi,indef)


max1 = 0
index = 0
for i in range(len(li)):
    if max1<i:
        max1 = li[i]
        index = i

print(max1,index)


# -----
li.sort()
print(li[-2])
