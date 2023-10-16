def add(li):
    for i in li:
        yield i

li = [2,4,5,6,7,8]
a = add(li)
# print(a,id(a),list(a))
for i in list(a):
    print(i)
# print(next(a))